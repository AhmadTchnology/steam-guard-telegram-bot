import logging
import re
import subprocess
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
STEAMGUARD_PATH = os.getenv("STEAMGUARD_PATH")
MAFILES_DIR = os.getenv("MAFILES_DIR")


def username_exists(username: str) -> bool:
    """Check if a .maFile exists for the given username."""
    if not os.path.isdir(MAFILES_DIR):
        logger.error(f"maFiles directory not found: {MAFILES_DIR}")
        return False
    for filename in os.listdir(MAFILES_DIR):
        name, ext = os.path.splitext(filename)
        if ext.lower() == ".mafile" and name.lower() == username.lower():
            return True
    return False


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    welcome_message = (
        f"👋 Hey {user.first_name}! Welcome to the Steam Guard Bot 🔐\n\n"
        "Just send me your Steam username and I'll get your guard code for you! 🎮✨"
    )
    await update.message.reply_text(welcome_message)


async def handle_username(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the username message and execute the steamguard command."""
    username = update.message.text.strip()

    if not username:
        await update.message.reply_text("Please provide a valid username.")
        return

    if not username_exists(username):
        await update.message.reply_text(
            f"❌ No account found for username: {username}"
        )
        return

    processing_msg = await update.message.reply_text(
        f"Processing username: {username}..."
    )

    try:
        command = f'{STEAMGUARD_PATH} --username {username} code'
        logger.info(f"Executing command: {command}")

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30,
        )

        if result.returncode != 0:
            error_msg = f"Command failed with return code {result.returncode}"
            if result.stderr:
                error_msg += f": {result.stderr}"
            await processing_msg.edit_text(f"❌ Error: {error_msg}")
            return

        output = result.stdout
        logger.info(f"Command output: {output}")

        code_pattern = r'\b[A-Za-z0-9]{5}\b'
        matches = re.findall(code_pattern, output)

        if matches:
            steam_guard_code = matches[0]
            await processing_msg.edit_text(
                f"✅ Steam Guard code for {username}:\n\n`{steam_guard_code}`\n\n"
                f"It will Expire after 30 Seconds",
                parse_mode='Markdown',
            )
        else:
            await processing_msg.edit_text(
                f"⚠️ No 5-character alphanumeric code found in output.\n\n"
                f"Command output:\n```\n{output}\n```",
                parse_mode='Markdown',
            )

    except subprocess.TimeoutExpired:
        await processing_msg.edit_text("❌ Command timed out after 30 seconds.")
    except Exception as e:
        logger.error(f"Error executing command: {e}")
        await processing_msg.edit_text(f"❌ An error occurred: {str(e)}")


def main() -> None:
    """Start the bot."""
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_username)
    )

    logger.info("Starting Steam Guard Code Bot...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
