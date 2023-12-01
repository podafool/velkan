import time
import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode
from aiogram.utils import executor

API_TOKEN = '6348947600:AAGyd84Hjn1Kqu296-mUbx9oJdd6VLJVB3s'
AFK_MESSAGE = 'I am AFK, please excuse me!'
WAIT_TIME = 5 # minutes

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Variable to keep track of last activity time
last_activity_time = time.time()


# Handler to handle incoming messages
@dp.message_handler()
async def handle_message(message: types.Message):
    global last_activity_time
    last_activity_time = time.time()
    await bot.send_message(message.chat.id, 'I am not AFK anymore.')


# Handler to handle bot going offline
@dp.chosen_inline_handler()
async def handle_chosen_inline(inline_query: types.ChosenInlineResult):
    global last_activity_time
    last_activity_time = time.time()


async def check_afk():
    global last_activity_time
    while True:
        await asyncio.sleep(60) # Check every minute
        current_time = time.time()
        if current_time - last_activity_time > WAIT_TIME * 60:
            await bot.send_message(message.chat.id, f'{AFK_MESSAGE} I was last active {WAIT_TIME} minutes ago.')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(check_afk())
    executor.start_polling(dp, loop=loop)