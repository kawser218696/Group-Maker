# generate_session.py
# Run locally to produce a string session that you will put into your server environment as SESSION.
# Usage: python generate_session.py
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os

api_id = int(os.environ.get("API_ID", "0"))
api_hash = os.environ.get("API_HASH", "")

if not api_id or not api_hash:
    print("Set API_ID and API_HASH as environment variables (from https://my.telegram.org).")
    exit(1)

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("If this opens, follow the prompts to login with your phone number and code.")
    string = client.session.save()
    print("\n--- Your string session (put this into SESSION env var on the server) ---\n")
    print(string)
    print("\n--- End ---\n")
