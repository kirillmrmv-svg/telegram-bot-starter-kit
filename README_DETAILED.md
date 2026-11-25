Español: see README\_ES.md.



English (README.md)

Telegram Bot Starter Kit (Aiogram + SQLite + Multi-Language)

A modular starter template for building Telegram bots in Python with multi-language support, a Terms of Service and Privacy Policy acceptance screen, a local SQLite database, a background scheduler, and basic admin commands.

The project is designed as a clean foundation: you don't need to build architecture, navigation, user storage, or localization from scratch — just plug in your own copy, buttons, and business logic.

Detailed file and architecture notes are provided separately in STRUCTURE.md (double-check the filename spelling when creating it).

Important! If you plan to customize or extend the bot's logic with an AI assistant, check out a few tips from the bot's creators in AI\_interaction.md.

Use Cases for This Template

This starter kit works well for a wide range of projects that benefit from clean structure, localization, and fast setup:

•	Business card bots, catalogs, and directories (services, courses, FAQs, product cards with menu navigation);

•	Consultation, inquiry, and lead-generation bots (collecting requests, basic user qualification, recording consent to data processing);

•	Communities, private clubs, and media projects (member onboarding, broadcasts via /broadcast, scheduled reminders);

•	MVPs and client builds (whenever you need a clear modular skeleton that is easy to extend).

What's Included

•	Start screen and language selection — welcome screen and language choice saved to the database.

•	Terms \& Privacy acceptance screen — view Terms of Service and Privacy Policy text, accept terms with status saved to the database, or return to language selection.

•	Main menu and navigation — clean in-chat message updates, help section, and language switching.

•	JSON localization — strings live in separate locale files (en and es by default) with safe UTF-8 / UTF-8 with BOM reading.

•	SQLite database — stores users, selected language, and terms acceptance status without requiring an external database server to start.

•	Scheduler (scheduler.py) — example recurring background task.

•	Admin commands (admin\_handlers.py) — view basic stats (/stats) and broadcast messages to users (/broadcast).

Quick Start and Running the Bot

Step 1. Configure the .env file

Open .env in any text editor (such as VS Code, Notepad++, or Notepad) and add your details:

•	Bot token — get it from @BotFather in Telegram and paste it into BOT\_TOKEN=....

•	Your Telegram ID — check your numeric ID (for example, via @userinfobot or @getidsbot) and paste it into ADMIN\_IDS=123456789.

Save the .env file. Do not share it or publish it publicly.

Step 2. Create a virtual environment, install dependencies, and run

Open a terminal (command prompt) inside the folder containing the bot files (main.py, requirements.txt, .env), and run the commands for your operating system.

Windows (PowerShell / CMD)

PowerShell

python -m venv venv

.\\venv\\Scripts\\activate

pip install -r requirements.txt

python main.py

macOS

Bash

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python3 main.py

Linux (Ubuntu / Debian, etc.)

Bash

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python3 main.py

Note: If creating the virtual environment on Linux fails with an ensurepip or venv error, install the environment package for your Python version (for example, sudo apt update \&\& sudo apt install -y python3-venv), then run the venv command again.

Once started, the terminal will show logs for database initialization, the scheduler, and polling startup — your bot is ready to test in Telegram with /start.

How to Add a New Language

1\.	Create a new JSON file in locales/, for example locales/de.json or locales/fr.json (the language code in the filename should match the language identifier you use).

2\.	Copy locales/en.json into the new file and translate all string values into the target language while keeping all keys unchanged.

3\.	Validate JSON syntax and encoding — escape quotes inside strings as \\", write line breaks as \\n, and do not leave a trailing comma after the last key in the object.

4\.	Wire the new language into the bot flow and keyboards (keyboard.py, handlers.py, and/or default settings in config.py) by adding a selection button and handling the new language code.

5\.	Restart the bot so the files in locales/ are reloaded.

Tips Before Going to Production

•	Replace placeholder texts with your own bot description, Terms of Service, and Privacy Policy in locales/en.json and locales/es.json.

•	Check scheduler timing (scheduler.py) — if a schedule is based on UTC, account for the offset from your local time zone.

•	For 24/7 operation on a VPS, run the bot under a process manager (such as systemd on Linux) so it restarts automatically after reboots or crashes.



Want the complete starter kit with all modules and localization? You can purchase it on Gumroad here: \[Telegram Bot Starter Kit](https://mrmvkirill.gumroad.com/l/httpsmrmvkirillgumroadcomltelegram-bot-starter-kit)

