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


await client.send_photo(
            photo=random.choice(vid),
            caption=presete.ABOUT_TXT.format(query.from_user.mention),
            chat_id=query.message.chat.id,
            reply_markup=reply_markup,
