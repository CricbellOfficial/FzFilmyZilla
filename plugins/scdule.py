import requests
from bs4 import BeautifulSoup
from info import SESSION, API_ID, API_HASH, BOT_TOKEN, LOG_STR
import re
from telethon import TelegramClient, events, Button

from telethon.tl.types import InputMediaPoll, Poll, PollAnswer
from telethon.sessions import StringSession


from schedule import every, repeat, run_pending
import time

@repeat(every(10).minutes)
async def job():
    print("I am a scheduled job")

while True:
    run_pending()
    time.sleep(1)
      
async def job():
     
     url = 'https://www.youtube.com/results?search_query=cricket+shorts'
     reqs = requests.get(url)
     soup = BeautifulSoup(reqs.text, 'html.parser')
     target = "shorts/"
     d = f"{soup}"
     words = d.split()
     try:
       for w in words:
          if "shorts/" in w:
               #print(w)
               splited = w.split(",")
               #print(splited[2])
               splited = splited[2].split('"')
               #print(splited[7])
               newn = f"https://www.youtube.com{splited[7]}"
               await BotzHubUser.send_message(group_id, newn)
               break
     except Exception as ap:
        #await BotzHubUser.send_message(group_id, newn)
        print("error")
    
