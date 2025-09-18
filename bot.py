# bot.py
# Telethon userbot that can create a supergroup and send a message as a user account.
# Requires environment variables: API_ID, API_HASH, SESSION (string session)
import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = int(os.environ.get("API_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")
SESSION = os.environ.get("SESSION", None)  # Should be a Telethon StringSession

if not API_ID or not API_HASH:
    raise SystemExit("Missing API_ID / API_HASH environment variables. Get them from https://my.telegram.org")

if not SESSION:
    raise SystemExit("Missing SESSION environment variable. Generate one locally with generate_session.py")

client = TelegramClient(StringSession(SESSION), API_ID, API_HASH, loop=asyncio.get_event_loop())

async def create_supergroup_and_send(title: str, users=None, initial_message: str = None):
    # Create a channel as a supergroup (megagroup=True)
    # Telethon create_channel => channel, and use megagroup=True to create a supergroup
    print(f"Creating supergroup '{title}'...")

    result = await client(functions.channels.CreateChannelRequest(
        title=title,
        about="Created by userbot",
        megagroup=True
    ))
    chat = result.chats[0]
    print(f"Created chat id={chat.id} ({chat.title})")

    # Optionally invite users (users should be user IDs or usernames accessible to your account)
    if users:
        try:
            await client.invite_to_channel(chat, users)
            print(f"Invited users: {users}")
        except Exception as e:
            print(f"Invite failed: {e}")

    # send an initial message
    if initial_message:
        await client.send_message(chat, initial_message)
        print("Sent initial message.")

async def main():
    await client.start()
    print("Client started as", (await client.get_me()).stringify())
    # Example: create a supergroup and send a first message
    await create_supergroup_and_send("My SuperGroup from Userbot", users=None, initial_message="Hello from my user account!")
    # Keep the client running to respond to events or to be used later
    @client.on(events.NewMessage(pattern="/whoami"))
    async def handler(event):
        me = await client.get_me()
        await event.reply(f"I am {me.first_name} ({me.id})")

    print("Userbot is running. Listening for events...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    import sys
    # Run the asyncio main
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stopping...")
