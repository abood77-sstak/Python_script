from selenium import webdriver
import telebot
from time import sleep

def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1920, 1200")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    return driver

my_token = "6517080417:AAHQx2gxkQ5Sxs2GilTyCaOI4-jJZfIGaho"
chat_id =1085837500
bot = telebot.TeleBot(my_token)

driver= web_driver()
driver. maximize_window()
url ="https://www.google.com/"
driver.get(url)
sleep(5)
photo = driver.save_screenshot("screenshot.png")
with open("screenshot.png", "rb") as photo:
   bot.send_photo(chat_id, photo)

driver.quit()
