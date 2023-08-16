#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message

import random
import asyncio
import config
from config import BANNED_USERS
from strings import get_command
from YukkiMusic import YouTube, app
from YukkiMusic.core.call import Yukki
from YukkiMusic.misc import db
from YukkiMusic.utils.database import get_loop
from YukkiMusic.utils.decorators import AdminRightsCheck
from YukkiMusic.utils.inline.play import (stream_markup,
                                          telegram_markup)
from YukkiMusic.utils.stream.autoclear import auto_clean
from YukkiMusic.utils.thumbnails import gen_thumb

STICKERS = [
  "CAACAgQAAxkBAAEJ7AhkzQ7GZ7DrL3O4Q7eHVCAYz-N4nwACvQkAAnpcEVM6alQk5njq3y8E",
  "CAACAgQAAxkBAAEJ7ARkzQ60YZZ7t4ivO7K8VR0LQifh9gACFQwAAtUjEFPkKwhxHG8_Ky8E",
  "CAACAgQAAxkBAAEJ7B1kzRHZ8-XDcyZNUE7Qyc7lsdwFMQACjggAA1VQUdoUwOeQzZqmLwQ",
  "CAACAgQAAxkBAAEJ7AJkzQ6yOkDOwj9r01b7fljN_Boh9wAC6gsAAmwiEVOtWUCotxfPAy8E",
  "CAACAgQAAxkBAAEJ7AABZM0OsGD_J8puJTi9WkLqWQG-SAADuBEAAqbxcR57Dj3-S9mwaS8E",
  "CAACAgQAAxkBAAEJ6_5kzQ6u16es2S8IVUSSQrA9hi_vkwACnxEAAqbxcR57wYUDyflSIS8E",
  "CAACAgEAAxkBAAEJ6_xkzQ50xN3ytZjk5fTylx7DS2PDVgACNgEAAlEpDTkSG_gDZwABw6MvBA",
  "CAACAgEAAxkBAAEJ6_pkzQ5lhNGO3pF1awcVfWxfBC_lQwACGQEAAlEpDTkG9n5mFbHKpy8E",
  "CAACAgEAAxkBAAEJ6_hkzQ5jChDHyCPnrf-xuCQQtouztAACFQEAAlEpDTnRN1QlsQ8qLi8E",
  "CAACAgUAAxkBAAEJ6_ZkzQ3ldTCPnhslPTxQUoirypK47wACowYAAkME2FZILCjifFdIUC8E",
  "CAACAgQAAxkBAAEJ6_BkzQ2qVDgusETUthPZSJ0l4YyKyAACLwoAAgM8IFMao7hilxhkGi8E",
  "CAACAgEAAxkBAAEJ6-5kzQ2UPyvOoBhBh55zDwnpxy2S2QAC8wQAAlEpDTmH9fRvHZACii8E",
  "CAACAgQAAxkBAAEJ6-xkzQ1cU-Oxv0vMWC1Hy-uhlASEAwACpwoAAn-aOFAK54ox7NBRcC8E",
  "CAACAgQAAxkBAAEJ6-pkzQ0mL58wlqP6tTloYWOxYbwFgQACXgwAAghGuVOWomIaBycL7i8E",
  "CAACAgIAAxkBAAEJ66dkzPAnyyPwli7yRX1hpMMQb7PJTgACDQEAAladvQpG_UMdBUTXly8E",
  "CAACAgEAAxkBAAEJ66FkzPARmsJrT_FfgYn1A7BumF3CnwACuwADUSkNOR12rpeAPL_kLwQ",
  "CAACAgEAAxkBAAEJ655kzPANksJJTQXkWl1q1E729tegAgACuAADUSkNOeiAtZ8X-LsKLwQ",
  "CAACAgEAAxkBAAEJ65tkzPAH_xsIpOKY3y6pugABWnGYHdsAArMAA1EpDTkH2Th_5u9jEy8E",
  "CAACAgEAAxkBAAEJ65lkzO_5oUKK3Z5k8JTOjLW62Vr9gwACmgADUSkNOfUGBWVzkcCyLwQ",
  "CAACAgEAAxkBAAEJ65VkzO_yfQABWNWzp75LTIFwfN4PhFsAApMAA1EpDTkdCAmv9TYB9i8E",
  "CAACAgEAAxkBAAEJ65NkzO_qf0xu4BaRSEAEfKmVmYo9EAACjAADUSkNOaEz-mHfkE3aLwQ",
  "CAACAgQAAxkBAAEJ64ZkzO7Je62eg3T6QZNxgvNXMxQYzAACpRYAAqbxcR7qDYebQsdZoi8E",
  "CAACAgQAAxkBAAEJ6pVkzHkvmfmavL8AAZO8Chh1WOJn7WYAAmcNAAKYxTlQbCCYZOix0kQvBA",
  "CAACAgQAAxkBAAEJ6ptkzHoGfPr3wnuhsSowP3fin1iWhgACjggAAovV6FOaebAKJCO-5C8E",
]

# Commands
SKIP_COMMAND = get_command("SKIP_COMMAND")


@app.on_message(
    filters.command(SKIP_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def skip(cli, message: Message, _, chat_id):
    if not len(message.command) < 2:
        loop = await get_loop(chat_id)
        if loop != 0:
            return await message.reply_text(_["admin_12"])
        state = message.text.split(None, 1)[1].strip()
        if state.isnumeric():
            state = int(state)
            check = db.get(chat_id)
            if check:
                count = len(check)
                if count > 2:
                    count = int(count - 1)
                    if 1 <= state <= count:
                        for x in range(state):
                            popped = None
                            try:
                                popped = check.pop(0)
                            except:
                                return await message.reply_text(
                                    _["admin_16"]
                                )
                            if popped:
                                if (
                                    config.AUTO_DOWNLOADS_CLEAR
                                    == str(True)
                                ):
                                    await auto_clean(popped)
                            if not check:
                                try:                                    
                                    await message.reply_photo(
                                        photo="https://te.legra.ph/file/7801e08b59a0943cc9038.jpg",
                                        caption=_["admin_10"].format(
                                            message.from_user.mention
                                        )
                                    )
                                    await Yukki.stop_stream(chat_id)
                                    await asyncio.sleep(1)
                                    await message.reply_sticker("CAACAgQAAxkBAAEJ6npkzFsSvhmTyXqaEeCOYjbM_OW5ZgACmgoAAjaOOFE-q1peUos2-S8E")
                                except:
                                    return
                                break
                    else:
                        return await message.reply_text(
                            _["admin_15"].format(count)
                        )
                else:
                    return await message.reply_text(_["admin_14"])
            else:
                return await message.reply_text(_["queue_2"])
        else:
            return await message.reply_text(_["admin_13"])
    else:
        check = db.get(chat_id)
        popped = None
        try:
            popped = check.pop(0)
            if popped:
                if config.AUTO_DOWNLOADS_CLEAR == str(True):
                    await auto_clean(popped)
            if not check:                
                await message.reply_photo(
                    photo="https://te.legra.ph/file/7801e08b59a0943cc9038.jpg",
                    caption=_["admin_10"].format(message.from_user.mention)
                )
                await asyncio.sleep(1)
                await message.reply_sticker("CAACAgQAAxkBAAEJ6npkzFsSvhmTyXqaEeCOYjbM_OW5ZgACmgoAAjaOOFE-q1peUos2-S8E")
                try:
                    return await Yukki.stop_stream(chat_id)
                except:
                    return
        except:
            try:                
                await message.reply_photo(
                    photo="https://te.legra.ph/file/7801e08b59a0943cc9038.jpg",
                    caption=_["admin_10"].format(message.from_user.first_name)
                )
                await Yukki.stop_stream(chat_id)
                await asyncio.sleep(1)
                return await message.reply_sticker("CAACAgQAAxkBAAEJ6npkzFsSvhmTyXqaEeCOYjbM_OW5ZgACmgoAAjaOOFE-q1peUos2-S8E")
            except:
                return
    queued = check[0]["file"]
    title = (check[0]["title"]).title()
    user = check[0]["by"]
    streamtype = check[0]["streamtype"]
    videoid = check[0]["vidid"]
    status = True if str(streamtype) == "video" else None
    if "live_" in queued:
        n, link = await YouTube.video(videoid, True)
        if n == 0:
            return await message.reply_text(
                _["admin_11"].format(title)
            )
        try:
            await Yukki.skip_stream(chat_id, link, video=status)
        except Exception:
            return await message.reply_text(_["call_9"])
        button = telegram_markup(_, chat_id)
        img = await gen_thumb(videoid, chat_id)        
        run = await message.reply_photo(
            photo=img,
            caption=_["stream_1"].format(
                user,
                f"https://t.me/{app.username}?start=info_{videoid}",
            ),
            reply_markup=InlineKeyboardMarkup(button),
        )
        db[chat_id][0]["mystic"] = run
        db[chat_id][0]["markup"] = "tg"
        await asyncio.sleep(1)
        await message.reply_sticker("CAACAgEAAxkBAAEJ6pdkzHlCW4mw1JZrE-D4hPe4CWoZvgACFQMAAt5cIURnyX8sYRxXqi8E") #heart beat : queue la youtube live stream ku skip panna
    elif "vid_" in queued:
        mystic = await message.reply_text(
            _["call_10"], disable_web_page_preview=True
        )
        try:
            file_path, direct = await YouTube.download(
                videoid,
                mystic,
                videoid=True,
                video=status,
            )
        except:
            return await mystic.edit_text(_["call_9"])
        try:
            await Yukki.skip_stream(chat_id, file_path, video=status)
        except Exception:
            return await mystic.edit_text(_["call_9"])
        button = stream_markup(_, videoid, chat_id)
        img = await gen_thumb(videoid, chat_id)        
        run = await message.reply_photo(
            photo=img,
            caption=_["stream_1"].format(
                user,
                f"https://t.me/{app.username}?start=info_{videoid}",
            ),
            reply_markup=InlineKeyboardMarkup(button),
        )
        db[chat_id][0]["mystic"] = run
        db[chat_id][0]["markup"] = "stream"
        await message.reply_sticker(random.choice(STICKERS)) #Munnadi heart vechitu jumping : queue la video song ku skip pannum bothu
        await mystic.delete()
        
    elif "index_" in queued:
        try:
            await Yukki.skip_stream(chat_id, videoid, video=status)
        except Exception:
            return await message.reply_text(_["call_9"])
        button = telegram_markup(_, chat_id)
        await message.reply_sticker("CAACAgQAAxkBAAEJ6plkzHmxI62tjrxsXGCfFY7YmFGiLAACPgsAAsCwiFHs4-FX1TKh4S8E") #blowing heart : for m3u8 links (live streaming links)
        run = await message.reply_photo(
            photo=config.STREAM_IMG_URL,
            caption=_["stream_2"].format(user),
            reply_markup=InlineKeyboardMarkup(button),
        )
        db[chat_id][0]["mystic"] = run
        db[chat_id][0]["markup"] = "tg"
    else:
        try:
            await Yukki.skip_stream(chat_id, queued, video=status)
        except Exception:
            return await message.reply_text(_["call_9"])
        if videoid == "telegram":
            button = telegram_markup(_, chat_id)            
            run = await message.reply_photo(
                photo=config.TELEGRAM_AUDIO_URL
                if str(streamtype) == "audio"
                else config.TELEGRAM_VIDEO_URL,
                caption=_["stream_3"].format(
                    title, check[0]["dur"], user
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "tg"
            await asyncio.sleep(1)
            await message.reply_sticker(random.choice(STICKERS)) #Munnadi giving big heart : queue la telegram audio file tag panni /play pannirundha
        elif videoid == "soundcloud":
            button = telegram_markup(_, chat_id)
            run = await message.reply_photo(
                photo=config.SOUNCLOUD_IMG_URL
                if str(streamtype) == "audio"
                else config.TELEGRAM_VIDEO_URL,
                caption=_["stream_3"].format(
                    title, check[0]["dur"], user
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "tg"
        else:
            button = stream_markup(_, videoid, chat_id)
            img = await gen_thumb(videoid, chat_id)            
            run = await message.reply_photo(
                photo=img,
                caption=_["stream_1"].format(
                    user,
                    f"https://t.me/{app.username}?start=info_{videoid}",
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "stream"
            await asyncio.sleep(1)
            await message.reply_sticker(random.choice(STICKERS)) #Munnadi cute bunny girl : normal ah /play pannirundha
