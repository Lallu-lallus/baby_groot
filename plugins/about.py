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

@Client.on_message(filters.private & filters.incoming & filters.command("about"))
await client.send_message(
            text=presets.ABOUT_TXT.format(query.from_user.mention),
            chat_id=query.message.chat.id,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ɢʀᴏᴜᴘ", url="https://t.me/Ls_Bots")
                    ],
                    [
                        InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/LSBOTZ_UPDATE"),
                        InlineKeyboardButton("ʜᴇʟᴘ", url="https://t.me/EDIT_REPO")
                    ],
                    [
                        InlineKeyboardButton("Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ", url="https://t.me/Ls_filesendbot?startgroup=true")
                    ]
                ]
            )
           
        )
        
