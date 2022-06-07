import re
import os
import time
import random
from bot import Bot
from presets import Presets
from base64 import b64decode
from helper.file_size import get_size
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.private & filters.text)
async def bot_pm(client: Bot, message: Message):
    if message.text == "/about":
        await client.send_message(
            chat_id=message.chat.id,
            caption=Presets.ABOUT_TEXT.format(message.from_user.first_name),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ɢʀᴏᴜᴘ", url="https://t.me/Ls_Bots")
                    ],
                    [
                        InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/LSBOTZ_UPDATE"),
                        InlineKeyboardButton("ᴄʀᴇᴀᴛᴏʀ", url="https://t.me/lallu_tg")
                    ],
                    [
                        InlineKeyboardButton("Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ", url="https://t.me/Ls_filesendbot?startgroup=true")
                    ]
                ]
            )
           
        )
