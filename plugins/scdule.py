from apscheduler.schedulers.asyncio import AsyncIOScheduler

import requests
from bs4 import BeautifulSoup
from info import SESSION, API_ID, API_HASH, BOT_TOKEN, LOG_STR
import re
from telethon import TelegramClient, events, Button

from telethon.tl.types import InputMediaPoll, Poll, PollAnswer
from telethon.sessions import StringSession


apiid = API_ID
apihash = API_HASH
bottoken = BOT_TOKEN
ss = "1BVtsOLgBuyDLMoZOURUGEg81gV5njgorTVbwoEAuJV4w0SCGIH4zeyU5rTGIRTdqXmCH7iASI7g7WybmbKqLdrQs1jADUDxgrI2dy5t5X7Te3O8mu7zLkqyW7ui2pSLnk1xYpGRBm9Fs6lbGyCugpioMREpby3xQxPngJzo8loqiCqFDft_s95GTNr4GlroaY6DjbgH_i_LPPjon92HG94ZvoiUz9ky8Ate6TkWUNkFRrqdzt1lauIbZ1enUF-26LP-u-4VJfzZPNYp2ttyo22T-1YyIbfdrCac3kL4c-gbjDRFq-3gsYd8EIjtv4ZXVYAFn1hTtgcf_JrfkPsvp1Uz_Zrm6A98="
     
BotzHubUser = TelegramClient(StringSession(ss), apiid, API_HASH)
BotzHubUser.start()
     
group_id = -1001909929331
BotzHubUser.send_message(group_id, "hii")
      
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
    


scheduler = AsyncIOScheduler()
#scheduler.add_job(job, "interval", seconds=30)

#scheduler.start()
