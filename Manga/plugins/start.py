import asyncio
from pyrogram import filters, enums 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from Manga import bot
from Manga import prefix

@bot.on_message(filters.command("start", prefix) | filters.private)
async def start(_, message):
    user_id = int(message.from_user.id)
    mention = message.from_user.mention

markup = InlineKeyboardMarkup([
    [InlineKeyboardButton("OWNER", url="https://t.me/just_a_bio"),
     InlineKeyboardButton("SUPPORT", url="https://t.me/just_a_bio")]
])

caption = "Bot Awake 🌟"
photo = "https://telegra.ph/file/dc59c2b7bdfc7132895f1.jpg"
