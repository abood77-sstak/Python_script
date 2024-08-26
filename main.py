
import os
from telethon import TelegramClient, events

API_ID = os.environ["API_ID"]
API_HASH = os.environ["API_HASH"]
BOT_TOKEM = os.environ["BOT_TOKEN"]


client = TelegramClient ("bot", API_ID, API_HASH)
client.start(bot_token=BOT_TOKEM)
@client.on(events.NewMessage)
async def handler (event):
        await event.reply(event.raw_text)

client.start()
client.run_until_disconnected()