from apscheduler.schedulers.asyncio import AsyncIOScheduler
import requests
from bs4 import BeautifulSoup
from pyrogram import StopTransmission
from pyrogram import filters as Filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from ..config import Config
from ..utubebot import UtubeBot

async def job():
     youtube = BeautifulSoup(requests.get(f"https://www.youtube.com/results?search_query=cricket+shorts").text, "html.parser")
     ylink = youtube.find_all('a')['href']
     if ylink:
        for l in ylink:
            if "shorts/" in l:
                print(l)
                await client.send_message(message.chat.id, f"**𝙵𝙸𝙽𝙳𝙸𝙽𝙶 𝚈𝙾𝚄𝚁 𝚅𝙸𝙳𝙴𝙾** `{urlissed}`")
                break


scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds=10)

scheduler.start()
