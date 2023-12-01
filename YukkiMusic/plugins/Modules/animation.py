from pyrogram import Client, filters
from pyrogram.errors import BadRequest
from pyrogram.types import Message

api_id = "your_api_id"
api_hash = "your_api_hash"
bot_token = "your_bot_token"

app = Client("my_bot", api_id, api_hash, bot_token=bot_token)

@app.on_message(filters.command("kill") & filters.user(user_id))
async def kill(client, message: Message):
    await message.reply("I love you too!")

@app.on_message(filters.command("love") & filters.user(user_id))
async def love(client, message: Message):
    # your love code here

@app.on_message(filters.command("hack") & filters.user(user_id))
async def hack(client, message: Message):
    # your hack code here

@app.on_message(filters.command("bombs") & filters.user(user_id))
async def bombs(client, message: Message):
    # your bombs code here
  
app.run()
