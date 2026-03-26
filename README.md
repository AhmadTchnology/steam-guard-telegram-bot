# 🔐 Steam Guard Telegram Bot

A Telegram bot that instantly retrieves your Steam Guard 2FA codes. Just send a username and get your code back in seconds.

## ✨ Features

- 🎮 Retrieve Steam Guard codes via Telegram
- ✅ Validates usernames against local `.maFile` accounts
- ⏱️ 30-second auto-expiry notification on codes
- 🔒 Secure — token and paths loaded from `.env`
- 🐳 Docker ready — deploy on any Linux server

## 📋 Prerequisites

- **Telegram Bot Token** — get one from [@BotFather](https://t.me/BotFather)
- **steamguard-cli** — [github.com/dyc3/steamguard-cli](https://github.com/dyc3/steamguard-cli)
- **maFiles** — your Steam account `.maFile` files

**For local (non-Docker) usage:** Python 3.7+

## 🚀 Quick Start (Local)

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
   STEAMGUARD_PATH=your_steamguard_path
   MAFILES_DIR=your_maFiles_directory_path
   ```

4. **Run the bot:**
   ```bash
   python steamguard_bot.py
   ```

## 🐳 Docker Deployment (Linux Server)

The easiest way to deploy on a Linux server. The Dockerfile automatically downloads `steamguard-cli`.

1. **Clone the repo on your server:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/steam-guard-telegram-bot.git
   cd steam-guard-telegram-bot
   ```

2. **Copy your `maFiles` into the project:**
   ```bash
   cp -r ~/.config/steamguard-cli/maFiles ./maFiles
   ```

3. **Create `.env`:**
   ```env
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   STEAMGUARD_PATH=/usr/local/bin/steamguard
   MAFILES_DIR=/app/maFiles
   ```

4. **Run with Docker Compose:**
   ```bash
   docker compose up -d --build
   ```

   **Or with plain Docker:**
   ```bash
   docker build -t steamguard-bot .
   docker run -d --name steamguard-bot --env-file .env -v ./maFiles:/app/maFiles:ro steamguard-bot
   ```

5. **Check logs:**
   ```bash
   docker compose logs -f
   ```

## 🗂️ Project Structure

```
├── steamguard_bot.py      # Main bot logic
├── Dockerfile             # Docker image definition
├── docker-compose.yml     # Docker Compose config
├── .env                   # Bot token + paths (not committed)
├── requirements.txt       # Python dependencies
├── maFiles/               # Your .maFile accounts (Docker volume)
└── README.md              # You are here
```

## ⚙️ Configuration

| Variable | Description | Windows | Linux / Docker |
|----------|-------------|---------|----------------|
| `TELEGRAM_BOT_TOKEN` | Bot token from BotFather | `123456:ABC...` | `123456:ABC...` |
| `STEAMGUARD_PATH` | Path to steamguard binary | `.\steamguard.exe` | `/usr/local/bin/steamguard` |
| `MAFILES_DIR` | Directory with `.maFile` accounts | `C:\Users\...\maFiles` | `/app/maFiles` |

## 🛡️ Security

- Bot token and paths are loaded from `.env` (never hardcoded)
- `.env` is excluded from version control via `.gitignore`
- No user data is stored or logged
- Subprocess execution is restricted to the steamguard command only
- Docker volume mounts maFiles as **read-only**

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Bot doesn't respond | Verify your bot token and internet connection |
| Command fails | Check steamguard path and permissions |
| No code extracted | Inspect command output format; adjust regex if needed |
| "No account found" | Ensure the username has a matching `.maFile` in `MAFILES_DIR` |
| Timeout | steamguard may be hanging — check manually |
| Docker container exits | Run `docker compose logs` to check errors |

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<p align="center">Made With ❤️ By AhmadTchnology</p>
