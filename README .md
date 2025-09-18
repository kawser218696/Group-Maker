# Telegram Supergroup "User-like" Creator (Telethon)

Overview
- This project demonstrates creating a Telegram supergroup (megagroup) and sending messages using a user account (userbot) so messages appear like a regular member.
- This uses Telethon (Telegram client API) and requires a real Telegram account and the API_ID / API_HASH from https://my.telegram.org.

Warning and legal notes
- Using a user account as a userbot can violate Telegram’s Terms of Service and may result in bans. Use responsibly and at your own risk.
- If you prefer a fully-compliant bot approach, use the Bot API (but the message will show as the bot).

Local setup (generate SESSION)
1. Get API_ID and API_HASH from https://my.telegram.org
2. On your local machine:
   - Set environment variables:
     - API_ID
     - API_HASH
   - Run: `python generate_session.py`
   - Complete the login flow (phone + code). The script prints a string session.
3. Copy the printed string session to your server environment as `SESSION`.

Deploy to Railway / Heroku
- Add environment variables: API_ID, API_HASH, SESSION
- Use the provided Procfile. The worker will run `python bot.py`.
- Start a worker dyno (Heroku) or deploy to Railway (long-running process).

Why not AWS Lambda or GitHub Actions?
- AWS Lambda and GitHub Actions are not good for persistent connections because Telethon requires a long-lived client/socket connection. You could make short-lived calls, but userbot needs to stay connected to receive events and keep the session active.
- Use Railway, Heroku, a small VPS, or Cloud Run (with proper concurrency) for a reliable long-running process.

What's next
- If you want, I can:
  - Convert this to a Pyrogram version.
  - Add commands for automated group creation with dynamic user invites.
  - Add a safer Bot-API-only version that creates groups but posts as a bot (ToS-friendly).
  - Provide step-by-step Railway / Heroku deployment commands.
