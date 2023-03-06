import logging
import logging.config

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)

from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import SESSION, API_ID, API_HASH, BOT_TOKEN, LOG_STR
from utils import temp
from typing import Union, Optional, AsyncGenerator
from pyrogram import types
from aiohttp import web
from plugins import web_server

from telethon import TelegramClient, events, Button
from decouple import config
import asyncio
import re
from telethon.tl.types import InputMediaPoll, Poll, PollAnswer
import random

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)



PORT = "8080"

class Bot(Client):

    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        b_users, b_chats = await db.get_banned()
        temp.BANNED_USERS = b_users
        temp.BANNED_CHATS = b_chats
        await super().start()
        await Media.ensure_indexes()
        me = await self.get_me()
        temp.ME = me.id
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        self.username = '@' + me.username
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()
        logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
        logging.info(LOG_STR)

    async def stop(self, *args):
        await super().stop()
        logging.info("Bot stopped. Bye.")
    
    async def iter_messages(
        self,
        chat_id: Union[int, str],
        limit: int,
        offset: int = 0,
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        """Iterate through a chat sequentially.
        This convenience method does the same as repeatedly calling :meth:`~pyrogram.Client.get_messages` in a loop, thus saving
        you from the hassle of setting up boilerplate code. It is useful for getting the whole chat messages with a
        single call.
        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).
                
            limit (``int``):
                Identifier of the last message to be returned.
                
            offset (``int``, *optional*):
                Identifier of the first message to be returned.
                Defaults to 0.
        Returns:
            ``Generator``: A generator yielding :obj:`~pyrogram.types.Message` objects.
        Example:
            .. code-block:: python
                for message in app.iter_messages("pyrogram", 1, 15000):
                    print(message.text)
        """
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(chat_id, list(range(current, current+new_diff+1)))
            for message in messages:
                yield message
                current += 1

# start the bot
logging.info("Starting...")
try:
    apiid = config("APP_ID", cast=int)
    apihash = config("API_HASH")
    bottoken = config("BOT_TOKEN")
    frm = config("FROM_CHANNEL", cast=lambda x: [int(_) for _ in x.split(" ")])
    tochnls = config("TO_CHANNEL", cast=lambda x: [int(_) for _ in x.split(" ")])
    rqstg = config("RequestG_1", cast=int)
    chan1 = config("Channel_1", cast=int)
    chan2 = config("Channel_2", cast=int)
    chan3 = config("Channel_3", cast=int)
    chanmoviebhandar = -1001850668602
    datgbot = TelegramClient("bot", apiid, apihash).start(bot_token=bottoken)
except:
    logging.error("Environment vars are missing! Kindly recheck.")
    logging.info("Bot is quiting...")
    exit()

"""
@datgbot.on(events.NewMessage(pattern="/start"))
async def _(event):
    await event.reply(
        f"Hi `{event.sender.first_name}`!\n\nI am a channel auto-post bot!! Read /help to know more!\n\nI can be used in only two channels (one user) at a time. Kindly deploy your own bot.\n\n[More bots](https://t.me/its_xditya)..",
        buttons=[
            Button.url("Repo", url="https://github.com/xditya/ChannelAutoForwarder"),
            Button.url("Dev", url="https://t.me/its_xditya"),
        ],
        link_preview=False,
    )
"""    
@datgbot.on(events.NewMessage(pattern="/helpp"))
async def helpp(event):
    await event.reply(
        "**Help**\n\nThis bot will send all new posts in one channel to the other channel. (without forwarded tag)!\nIt can be used only in two channels at a time, so kindly deploy your own bot from [here](https://github.com/xditya/ChannelAutoForwarder).\n\nAdd me to both the channels and make me an admin in both, and all new messages would be autoposted on the linked channel!!\n\nLiked the bot? Drop a ♥ to @xditya_Bot :)"
    )

@datgbot.on(events.NewMessage(incoming=True, chats=rqstg))
async def _(event):
    
    #await event.photo(photo="https://graph.org/file/0b96452b81925298b2ee2.jpg", caption=f"🔥 Requesting....💯\n**{event.text}**")
    a = await datgbot.send_file(rqstg, "https://graph.org/file/0b96452b81925298b2ee2.jpg", caption=f"🔥 Requesting....💯\n\nName: **{event.text}**💯", link_preview=False)
    await asyncio.sleep(5)
    await a.delete()
    a = await datgbot.send_file(rqstg, "https://graph.org/file/5836bb37d8445d90b8482.png", caption=f"🎥 **Request Accepted** 💯", link_preview=False)
    ss = "Please Wait Approx 24 hrs \n\nYour Requested Movie : 🎥 "
    sat = " 🍿\n\nWe will upload your movie asap\n\nहम आपकी मूवी को चैनल पर अपलोड करेंगे कृपया करके ज्वाइन हो जाओ\n\n👇Please Join For Request Delivery👇\n\n@FzFilmyZilla"
    tittle = f"{ss}**{event.text}**{sat}"
    k = await event.reply(tittle)
    await asyncio.sleep(30)
    await k.delete()
    await a.delete()
@datgbot.on(events.NewMessage(incoming=True, chats=frm))
async def _(event):
    
        try:
            if event.poll:
                return
            if event.photo:
                photo = event.media.photo
                idd = random.randint(0, 100_000)

                #a = await datgbot.send_file(chan1, photo, caption="Uploaded #MoviesBhandar 💯", link_preview=False)
                await datgbot.send_file(rqstg, photo, caption="Uploaded #MoviesBhandar 💯", link_preview=False)
                await datgbot.send_file(chan3, photo, caption="Uploaded #FzFilmyZilla 💯", link_preview=False)
                await datgbot.send_file(chanmoviebhandar, photo, caption="Uploaded #MoviesBhandar 💯", link_preview=False)
                await datgbot.send_message(chanmoviebhandar, file=InputMediaPoll(
                            poll=Poll(
                                id=idd,
                                question="Movie Rating Please?❌\nआपको यह कितनी पसंद है? ✔️",
                                answers=[PollAnswer('Good ( अच्छा ) 😘', b'1'), PollAnswer('Bad ( बुरा ) 😏', b'2')]
                                )
                            ))
                #await asyncio.sleep(300)
                #await a.delete()
                
            elif event.media:
                try:
                    if event.media.webpage:
                        ok ='ok'
                        #await datgbot.send_message(chan2, event.text, link_preview=False)
                        #await datgbot.send_message(chan1, event.text, link_preview=False)
                        
                except Exception:
                    media = event.media.document
                    filenames = event.text 
                    
                    s1 = re.sub('http://\S+|https://\S+', '', filenames)
                    remove_backk = lambda s: ' '.join(i for i in s.split() if '@' not in i)
                    remove_forwardd = lambda s: ' '.join(i for i in s.split() if '[' not in i)
                    newnamee =  remove_backk(remove_forwardd(s1))


                    text = f"#🎦 Requested / New Movie Uploaded\n\n#📽️: {newnamee}🍿\n\nSearch Again in Group To get \nThanks For Joining Our Clan \n 💢 @HindiJugard"
                    #a = await datgbot.send_file(chan1, media, caption=f"{newnamee}Uploaded By : @HindiJugard 💯", link_preview=False)
                    await datgbot.send_file(chan2, media, caption="Uploaded By : @FzFilmyZilla 💯", link_preview=False)
                    #await datgbot.send_file(chanmoviebhandar, media, caption="Uploaded By : @HindiJugard 💯", link_preview=False)
                    #await datgbot.send_message(chan3, text, link_preview=False)
                    if newnamee == "":
                        ol="ok"
                    else:
                        await datgbot.send_message(rqstg, text, link_preview=False)
                    
                    #await asyncio.sleep(300)
                    #await a.delete()
                finally:
                    #await datgbot.send_file(chan2, media, caption="Uploaded By : @FzFilmyZilla 💯", link_preview=False)
                    #await datgbot.send_file(chanmoviebhandar, media, caption="Uploaded By : @HindiJugard 💯", link_preview=False)
                    print("fail")
                    return
            else:
                ok = 'ok'
                
                #await datgbot.send_message(chan2, "@testing message Ignore", link_preview=False)
                #await datgbot.send_message(chan1, "@testing message Ignore", link_preview=False)
        except Exception as exc:
            logging.error(
                "TO_CHANNEL ID is wrong or I can't send messages there (make me admin).\nTraceback:\n%s",
                exc,
            )

                

logging.info("Bot has started.")
logging.info("Do visit ..")
datgbot.run_until_disconnected()

app = Bot()
app.run()
