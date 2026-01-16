from telegram import Bot
import os
import time

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

while True:
    bot.send_message(chat_id=CHAT_ID, text="🤖 Bot online com sucesso!")
    time.sleep(3600)
