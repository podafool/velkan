#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from YukkiMusic.utils.formatters import time_to_seconds


def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 10:
        bar = "👨‍🦰❤️ ▃ ▃ ▃ ▃ ▃ ▃ ▃ ▃ ▃ 👩‍🦰"
    elif 10 < anon < 20:
        bar = " ▃ 👨‍🦰❤️ ▃ ▃ ▃ ▃ ▃ ▃ ▃ ▃ 👩‍🦰"
    elif 20 <= anon < 30:
        bar = " ▃ ▃ 👨‍🦰❤️ ▃ ▃ ▃ ▃ ▃ ▃ ▃ 👩‍🦰"
    elif 30 <= anon < 40:
        bar = " ▃ ▃ ▃ 👨‍🦰❤️ ▃ ▃ ▃ ▃ ▃ ▃ 👩‍🦰"
    elif 40 <= anon < 50:
        bar = " ▃ ▃ ▃ ▃ 👨‍🦰❤️ ▃ ▃ ▃ ▃ ▃ 👩‍🦰"
    elif 50 <= anon < 60:
        bar = " ▃ ▃ ▃ ▃ ▃ 👨‍🦰❤️ ▃ ▃ ▃ ▃ 👩‍🦰"
    elif 60 <= anon < 70:
        bar = "▃ ▃ ▃ ▃ ▃ ▃ 👨‍🦰❤️ ▃ ▃ ▃ 👩‍🦰"
    elif 70 <= anon < 80:
        bar = "▃ ▃ ▃ ▃ ▃ ▃ ▃ 👨‍🦰❤️ ▃ ▃ 👩‍🦰"
    elif 80 <= anon < 95:
        bar = "▃ ▃ ▃ ▃ ▃ ▃ ▃ ▃ 👨‍🦰❤️ ▃ 👩‍🦰"
    else:
        bar = "▃ ▃ ▃ ▃ ▃ ▃ ▃ ▃ ▃ ▃ ▃ 👩‍❤️‍👨"
    not_dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data="close",
            ),
        ]
    ]
    dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_2"].format(played, dur),
                callback_data="GetTimer",
            ),
            InlineKeyboardButton(
                text=f"{played}  {bar}  {dur}",
                callback_data="GetTimer",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data="close",
            ),
        ],
    ]
    upl = InlineKeyboardMarkup(
        not_dur if DURATION == "Unknown" else dur
    )
    return upl


def queue_back_markup(_, CPLAY):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"queue_back_timer {CPLAY}",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
