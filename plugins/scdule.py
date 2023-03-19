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
               print(newn)
               break

     await Client.send_message("888849950", f"**𝙵𝙸𝙽𝙳𝙸𝙽𝙶 𝚈𝙾𝚄𝚁 𝚅𝙸𝙳𝙴𝙾**")
   except:
     print("error fail")


scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds=30)

scheduler.start()
