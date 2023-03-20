import requests
from bs4 import BeautifulSoup
from info import SESSION, API_ID, API_HASH, BOT_TOKEN, LOG_STR
import re

import time

      
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
               
               break
     except Exception as ap:
        #await BotzHubUser.send_message(group_id, newn)
        print("error")
    
