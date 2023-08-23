import datetime
import pytz
from YukkiMusic import app
import random
import asyncio
import requests
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery
from bs4 import BeautifulSoup
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from YukkiMusic.plugins.modules.blast import open_me_markup, surprise_markup, click_me_markup, close_me_markup
from typing import Union
from YukkiMusic.utils.database import get_client
from YukkiMusic.core.userbot import assistants


spam_chats = []

TAGMES = ["good morning", "good evening", "good night", "good afternoon"]
EMOJI = ["😊", "👋", "🌞", "🌙"]

COMMENTS = [
"saptiya nee - 1",
"yenna soru thina - 2",
"yennaku kodukama sapudura nee lam nalla irrupa - 3",
"sari nalla toongitu work parru  - 20",
"dei last bench kara toongatha da 😮‍💨 - 4 ",
"nalla saptu saptu toonguran pare 😬 - 5 ",
"ipo nee yelunthukula nu vei 🫣 - 8",
"Yun left side la parru un crush irrukanga - 9 ",
"sari toongu kanavula un crush varum 😝😅 - 10 ",
"nalla sapta pola inga varikum kekuthu yaepom 🙈😃 - 6 ",
"dei nalavaneee yelunthudu da - 7" ,
"sari sari toongunathu pothum velaiya parru - 11 ",
"innoruka polam variya sorru thinga - 12" ,
"sari oru tips solluren - toongama irruka - 13 ",
"pakathula work la un crush irruntha.. manager ku theriyama sight adey 🤧",
"sari sari parthathu pothum ipo parru nalla mandaila yerum 🫥 - 16",
"ninachen , yenna da kannu vera yengaiyo poguthu nu  😂 - 17",
"sari work pandra pasanga luku - meeting nu yulla poidunga 😃 - 18",
"AC la semaiya toongalam 🙈 - 19 ",
"Aaga inniku mudinzichi tipss hu ! Varaataahhhh 🏃‍♂️ - 21",
]

def get_random_news():    
    url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=8b7f36dbfcdc4d43bf0a9df50243072a"    
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'ok' and data['totalResults'] > 0:
        articles = data['articles']
        random_article = articles[random.randint(0, len(articles) - 1)]
        title = random_article['title']
        description = random_article['description']
        source = random_article['source']['name']
        url = random_article['url']
        
        news_info = f"Title: {title}\n\nURL: [Full article here!]({url})"
        return news_info
    else:
        return "Unable to fetch random news article.Better luck next time"

def get_random_quote():
    url = "https://quotes.toscrape.com/random"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    quote = soup.find("span", class_="text").text.strip()    
    return f"{quote}"

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    data = response.json()
    return f"{data['setup']}\n{data['punchline']}"

@app.on_message(filters.command(["tagu"], prefixes=["/", "#", "@", "!"]))
async def tagu_handler(client, message: Message):
    # Set the desired time zone
    tz = pytz.timezone('Asia/Kolkata')
    # Get the current time
    current_time = datetime.datetime.now(tz).time()
    # Determine the appropriate tag message based on the time of day
    if current_time >= datetime.time(4, 0) and current_time < datetime.time(10, 00):
        #msg = random.choice(TAGMES) + " " + EMOJI[2]  # Good morning
        msg = f"🌞 Good morning"
        markup = open_me_markup()
    elif current_time >= datetime.time(10, 00) and current_time < datetime.time(15, 30):
        #msg = random.choice(TAGMES) + " " + EMOJI[3]  # Good afternoon
        msg = f"😊 Good afternoon"
        markup = surprise_markup()
    elif current_time >= datetime.time(15, 30) and current_time < datetime.time(20, 00):
        #msg = random.choice(TAGMES) + " " + EMOJI[0]  # Good evening
        msg = f"👋 Good evening"
        markup = click_me_markup()
    else:
        #msg = random.choice(TAGMES) + " " + EMOJI[1]  # Good night
        msg = f"🌙 Good night"
        markup = close_me_markup()
    
    chat_id = message.chat.id
    if chat_id in spam_chats:
        await message.reply("Tagu command already oditu irukku paarunga!")
        return

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""

    async for usr in client.iter_chat_members(chat_id):
        if not chat_id in spam_chats:
            break

        if usr.user.is_bot:
            continue

        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id})"
        #usrtxt += f"{usr.user.mention}"

        if usrnum == 1:            
            tag_message = f"{msg}\n[{usr.user.first_name}](tg://user?id={usr.user.id})"
            for num in assistants:
                app = await get_client(num)
            await app.send_message(chat_id, tag_message, reply_markup=markup)
            
            
            # Generate a random sleep time between 10 and 30 seconds
            sleep_time = random.randint(0, 5)
            await asyncio.sleep(sleep_time)

            usrnum = 0
            usrtxt = ""

    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_callback_query(filters.regex("open_me"))
async def on_open_me_button_click(client, etho: Union[types.Message, types.CallbackQuery]):
    print("Callback query received:", etho.message.text)
    chat_id = etho.message.chat.id
    user_name = etho.from_user.first_name
    message_text = etho.message.text    
    
    if user_name in etho.message.text:
        if "good morning" in etho.message.text.lower():
            print("Morning button clicked!")
            await etho.edit_message_text(text="Unga gift varuthu   ◉ ╾╤╦")
            await asyncio.sleep(0.5)
            await etho.edit_message_text(text="Unga gift varuthu ◉   ╾╤╦")
            await asyncio.sleep(0.5)   
            joke = get_random_joke()            
            await etho.edit_message_text(text=f"Kaalai vanakkam ley\n{etho.from_user.mention}!\nUngalukaana siripu vaithiyam itho 😁:\n┃\n╰➪ {joke}")

        else:
            await etho.edit_message_text(text=f"Hey {etho.from_user.mention}!\nMannichidunga.. yetho thavaru nadanthu vitathu 🔫 ")

        await etho.answer()

    else:
        await etho.answer("Un button ah mattum click pannu ve-nn-a")

@app.on_callback_query(filters.regex("surprise"))
async def on_open_me_button_click(client, etho: Union[types.Message, types.CallbackQuery]):
    print("Callback query received:", etho.message.text)
    chat_id = etho.message.chat.id
    user_name = etho.from_user.first_name
    message_text = etho.message.text    
    
    if user_name in etho.message.text:
        if "good afternoon" in etho.message.text.lower():
            print("Afternoon button clicked!")
            await etho.edit_message_text(text="waittt! Vanthuduchi 🙈   ◉ ╾╤╦")
            await asyncio.sleep(0.5)
            await etho.edit_message_text(text="waittt! Vanthuduchi 🙈 ◉   ╾╤╦")
            await asyncio.sleep(0.5)            
            comment = random.choice(COMMENTS)
            await etho.edit_message_text(text=f"Matinee show vanakkam\n{etho.from_user.mention}\n┃\n╰━➮ {comment}")

        else:
            await etho.edit_message_text(text=f"Hey {etho.from_user.mention}!\nMannichidunga.. yetho thavaru nadanthu vitathu 🔫 ")

        await etho.answer()

    else:
        await etho.answer("Un button ah mattum click pannu ve-nn-a")

@app.on_callback_query(filters.regex("click_me"))
async def on_open_me_button_click(client, etho: Union[types.Message, types.CallbackQuery]):
    print("Callback query received:", etho.message.text)
    chat_id = etho.message.chat.id
    user_name = etho.from_user.first_name
    message_text = etho.message.text    
    
    if user_name in etho.message.text:
        if "good evening" in etho.message.text.lower():
            print("Evening button clicked!")
            await etho.edit_message_text(text="Ithu theriyuma? 🤔   ◉ ╾╤╦")
            await asyncio.sleep(0.5)
            await etho.edit_message_text(text="Ithu theriyuma? 🤔 ◉   ╾╤╦")
            await asyncio.sleep(0.5)   
            random_news = get_random_news()
            await etho.edit_message_text(text=f"Maalai vanakkam\n{etho.from_user.mention}!\nUngaluku oru seithi :\n\n{random_news}")

        else:
            await etho.edit_message_text(text=f"Hey {etho.from_user.mention}!\nMannichidunga.. yetho thavaru nadanthu vitathu 🔫 ")

        await etho.answer()

    else:
        await etho.answer("Un button ah mattum click pannu ve-nn-a")

@app.on_callback_query(filters.regex("close_me"))
async def on_open_me_button_click(client, etho: Union[types.Message, types.CallbackQuery]):
    print("Callback query received:", etho.message.text)
    chat_id = etho.message.chat.id
    user_name = etho.from_user.first_name
    message_text = etho.message.text    
    
    if user_name in etho.message.text:
        if "good night" in etho.message.text.lower():
            print("Night button clicked!")
            await etho.edit_message_text(text="Last ah onnu ☺️   ◉ ╾╤╦")
            await asyncio.sleep(0.5)
            await etho.edit_message_text(text="Last ah onnu ☺️ ◉   ╾╤╦")
            await asyncio.sleep(0.5)              
            quote = get_random_quote()
            await etho.edit_message_text(text=f"Indha ley\n{etho.from_user.mention}!\nUnakku oru pazhamozhi :\n\n{quote}")

        else:
            await etho.edit_message_text(text=f"Hey {etho.from_user.mention}!\nMannichidunga.. yetho thavaru nadanthu vitathu 🔫 ")

        await etho.answer()

    else:
        await etho.answer("Un button ah mattum click pannu ve-nn-a")
    
