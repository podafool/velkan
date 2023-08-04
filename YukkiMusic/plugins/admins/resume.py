#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, RESUME_IMG_URL
from strings import get_command
from YukkiMusic import app
from YukkiMusic.core.call import Yukki
from YukkiMusic.utils.database import is_music_playing, music_on
from YukkiMusic.utils.decorators import AdminRightsCheck

# Commands
RESUME_COMMAND = get_command("RESUME_COMMAND")


@app.on_message(
    filters.command(RESUME_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if await is_music_playing(chat_id):
        await message.reply_sticker("CAACAgQAAxkBAAEJ6oJkzF3wQKdCyGC3d5ShVAn9R56VwwACpQoAAgXwqFAIT7lt7WkHqy8E")
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    await Yukki.resume_stream(chat_id)
    awaut message.reply_sticker("CAACAgQAAxkBAAEJ6oBkzF1vz0A67_2_fNIAATlbvZrwWZgAAr8RAAKm8XEerbGHklFUk2svBA") #rose kudukkurathu
    await message.reply_photo(
        photo=RESUME_IMG_URL,
        caption=_["admin_4"].format(message.from_user.mention)
    )
