
import os
from telethon import TelegramClient, events

API_ID = os.environ["api_id"]
API_HASH = os.environ["api_hash"]
BOT_TOKEM = os.environ["token_bot"]


client = TelegramClient ("mbot", API_ID, API_HASH)
client.start(bot_token=BOT_TOKEM)
@client.on(events.NewMessage)
async def handler (event):
        await event.reply(event.raw_text)

client.start()
client.run_until_disconnected()


