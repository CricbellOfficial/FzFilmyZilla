from apscheduler.schedulers.asyncio import AsyncIOScheduler
import requests
from bs4 import BeautifulSoup
from pyrogram import filters, Client
from pyrogram.types import Message

async def job():
     youtube = BeautifulSoup(requests.get(f"https://www.youtube.com/results?search_query=cricket+shorts").text, "html.parser")
     ylink = youtube.find_all('a')['href']
     if ylink:
        for l in ylink:
            if "shorts/" in l:
                print(l)
                await Client.send_message("888849950", f"**𝙵𝙸𝙽𝙳𝙸𝙽𝙶 𝚈𝙾𝚄𝚁 𝚅𝙸𝙳𝙴𝙾**")
                break


scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds=10)

scheduler.start()
