from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from YukkiMusic import app

def blast_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=("Blast!"),
                    callback_data=f"blast",
                ),

            ]
        ]
    )
    return upl
