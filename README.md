# 🔐 Steam Guard Telegram Bot

A Telegram bot that instantly retrieves your Steam Guard 2FA codes. Just send a username and get your code back in seconds.

## ✨ Features

- 🎮 Retrieve Steam Guard codes via Telegram
- ✅ Validates usernames against local `.maFile` accounts
- ⏱️ 30-second auto-expiry notification on codes
- 🔒 Secure — token and paths loaded from `.env`

## 📋 Prerequisites

- **Python** 3.7+
- **steamguard.exe** — [steamguard-cli](https://github.com/dyc3/steamguard-cli) installed and configured with accounts
- **Telegram Bot Token** — get one from [@BotFather](https://t.me/BotFather)

## 🚀 Quick Start

1. **Clone the repo:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/steam-guard-telegram-bot.git
   cd steam-guard-telegram-bot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure `.env`:**
   ```env
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   STEAMGUARD_PATH=your_steamguard.exe_path
   MAFILES_DIR=your_maFiles_directory_path
   ```

4. **Run the bot:**
   ```bash
   python steamguard_bot.py
   ```

## 🗂️ Project Structure

```
├── steamguard_bot.py    # Main bot logic
├── steamguard.exe       # Steam Guard CLI executable
├── .env                 # Bot token + paths (not committed)
├── requirements.txt     # Python dependencies
└── README.md            # You are here
```

## ⚙️ Configuration

| Variable | Description | Example |
|----------|-------------|---------|
| `TELEGRAM_BOT_TOKEN` | Your Telegram bot token | `123456:ABC-DEF...` |
| `STEAMGUARD_PATH` | Path to `steamguard.exe` | `.\steamguard.exe` |
| `MAFILES_DIR` | Directory containing `.maFile` accounts | `C:\Users\...\maFiles` |

## 🛡️ Security

- Bot token and paths are loaded from `.env` (never hardcoded)
- `.env` is excluded from version control via `.gitignore`
- No user data is stored or logged
- Subprocess execution is restricted to the steamguard command only

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Bot doesn't respond | Verify your bot token and internet connection |
| Command fails | Check `steamguard.exe` path and permissions |
| No code extracted | Inspect command output format; adjust regex if needed |
| "No account found" | Ensure the username has a matching `.maFile` in `MAFILES_DIR` |
| Timeout | steamguard.exe may be hanging — check manually |

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<p align="center">Made With ❤️ By AhmadTchnology</p>