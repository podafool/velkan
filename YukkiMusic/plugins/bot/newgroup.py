from pyrogram import Client, filters
from pyrogram.types import Message
from config import LOG_GROUP_ID
from YukkiMusic import app


async def new_message(chat_id: int, message: str):
    await app.send_message(chat_id=chat_id, text=message)


@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Private Group"
        user = message.from_user.mention
        username = message.from_user.username
        title = message.chat.title
        chat_id = message.chat.id
        Insane = f"✨ **#New_Group** 😍\n\n🧡✨ **Chat ID :** {chat_id}\n✨💛 **Chat Title :** {title}\n💚✨ **User :** {user}\n✨💗 **Username :** @{username}\n💙✨ **User ID :** {message.from_user.id}\n✨💜 **Chat link :** {chatusername}"
        await new_message(LOG_GROUP_ID, Insane)
