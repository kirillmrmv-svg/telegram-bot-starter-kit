Plaintext

📁 telegram-bot-starter-kit/

├── 📁 locales/

│   ├── 📄 en.json              # English UI strings

│   └── 📄 es.json              # Spanish UI strings

├── 📄 .env                     # Environment variables config template (BOT\_TOKEN, ADMIN\_IDS)

├── 📄 .gitignore               # Prevents committing .env, venv, and local DB to Git

├── 📄 config.py                # Centralized settings loader from .env (token, admins, paths)

├── 📄 database.py              # DB setup and basic queries (users, language, requests)

├── 📄 handlers.py              # Core command and button handlers

├── 📄 admin\_handlers.py        # Basic admin commands (/stats, /broadcast for ADMIN\_IDS)

├── 📄 keyboard.py              # Inline and Reply keyboards

├── 📄 locales.py               # JSON translation loader with fallback to English

├── 📄 scheduler.py             # Background tasks (e.g., daily reminder example)

├── 📄 main.py                  # Entry point, logging setup, bot and scheduler startup

├── 📄 requirements.txt         # Pinned Python dependencies

├── 📄 README.md                # Setup, run instructions, and adding new languages

├── 📄 README\_ES.md             # Setup, run instructions, and adding new languages

├── 📄 STRUCTURE.md             # Project directory tree and file responsibilities

└── 📄 AI\_interaction.md        # Guide on AI prompting, filling stubs, and testing steps





Want the complete starter kit with all modules and localization? You can purchase it on Gumroad here: \[Telegram Bot Starter Kit](https://mrmvkirill.gumroad.com/l/httpsmrmvkirillgumroadcomltelegram-bot-starter-kit)

