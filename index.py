
from flask import Flask, request
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup

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

PORT = "8080"

TOKEN = os.getenv("TOKEN")
URL = "https://fz-ganeshmrxx.vercel.app"
bot = Bot(TOKEN)
msgid1 = ""
chatid1 = ""


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


"""
def welcome(update, context) -> None:
    update.message.reply_text(f"Hello *{update.message.from_user.first_name}* \n Welcome To Our Group.\n"
                              f"🔥 Search It 💯  Enjoy it  🍿")
    l = update.message.reply_text("👇 Type Movie Or Series Name 👇")



def find_movie(update, context):
    search_results = update.message.reply_text("🔥 Searching.... Pls Wait..💯")
    query = update.message.text
    chatid = update.message.chat.id
    movies_list = search_movies(query)
    tracemalloc.start()
    if movies_list:
        keyboards = []
        for movie in movies_list:
            keyboard = InlineKeyboardButton(movie["title"], callback_data=movie["id"])
            keyboards.append([keyboard])
        reply_markup = InlineKeyboardMarkup(keyboards)
        m = search_results.edit_text('Here I found - Pls Select One..!', reply_markup=reply_markup)   

    else:
         ok='ok'
       
        
    
    
def movie_result(update, context) -> None:
    query = update.callback_query
    msgid = query.message.message_id
    chatid = query.message.chat.id
    global chatid1
    chatid1 = chatid
    s = get_movie(query.data)
    response = requests.get(s["img"])
    img = BytesIO(response.content)
    m = query.message.reply_photo(photo=img, caption=f"🎥 {s['title']}")
    global msgid1
    msgid1 = m["message_id"]
    link = ""
    links = s["links"]
    keyboards = []
    request = InlineKeyboardButton("Join Our Official Channel", url="https://t.me/fzfilmyzilla")
    keyboards.append([request])
    for i in links:
        t = links[i] + "\n"
        urll = links[i]
        keyboard = InlineKeyboardButton(i, url=urll)
        keyboards.append([keyboard])
    reply_markup = InlineKeyboardMarkup(keyboards)
    k = query.message.reply_text('Click To Watch Online & Download', reply_markup=reply_markup)
    bot.delete_message(chat_id=chatid, message_id=msgid)
    #asyncio.create_task(dlt(chatid1, msgid))
    #loop = asyncio.get_event_loop()
    #task = loop.create_task(dlt(chatid1, msgid))
    #dlt(chatid1, msgid)

 
async def dlt(chid, midd): 
    
     await asyncio.sleep(20)
     bot.delete_message(chat_id=chid, message_id=midd)
"""   

def setup():
    app = Bot()
    app.run()
    update_queue = Queue()
    """
    dispatcher = Dispatcher(bot, update_queue, use_context=True)
    dispatcher.add_handler(CommandHandler('start', welcome))
    dispatcher.add_handler(MessageHandler(filters.text, find_movie))
    dispatcher.add_handler(CallbackQueryHandler(movie_result))
    """
    #return dispatcher

  
   

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/{}'.format(TOKEN), methods=['GET', 'POST'])
def respond():
    app = Bot()
    app.run()
    print("Hello World")
    #update = Update.de_json(request.get_json(force=True), bot)
    
    #setup().process_update(update)
    return 'ok'


@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}/{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"
