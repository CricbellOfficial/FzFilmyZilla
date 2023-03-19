from apscheduler.schedulers.asyncio import AsyncIOScheduler

from pyrogram import filters, Client
from pyrogram.types import Message
import requests
from bs4 import BeautifulSoup

import re



#for link in soup.find_all('a'):
#	print(link.get('href'))

async def job():
   try:  
     group_id = -1001909929331
     url = 'https://www.youtube.com/results?search_query=cricket+shorts'
     reqs = requests.get(url)
     soup = BeautifulSoup(reqs.text, 'html.parser')
     target = "shorts/"
     d = f"{soup}"
     words = d.split()
     for w in words:
          if "shorts/" in w:
               #print(w)
               splited = w.split(",")
               #print(splited[2])
               splited = splited[2].split('"')
               #print(splited[7])
               newn = f"https://www.youtube.com{splited[7]}"
               #await Client.send_message(-1001909929331, newn)
               await Client.send_message(group_id, newn, disable_web_page_preview=True)
               print(newn)
               break
   except:
     await Client.send_message(group_id, "hiii", disable_web_page_preview=True)


scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds=30)

scheduler.start()
