import asyncio
from pyrogram import filters, enums 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from Manga import bot
from Manga import prefix
from pyrogram.types import Message

START_TEXT = """ HEY {mention} , I Am powerful Manga Scrapper Do /help To Know My abilities
"""
buttons = 


@bot.on_message(filters.command("start", prefix) | filters.private)
async def start(_, message):
    user_id = int(message.from_user.id)
    mention = message.from_user.mention

HELP_TEXT = """
Help Menu Of Bot /help
"""

HELP_BUTTON = [[
        InlineKeyboardButton('🙂 About', callback_data='about')
        ],[
        InlineKeyboardButton('😴 Home', callback_data='home')]]


@bot.on_callback_query(filters.regex("home"))
async def help(_, query: CallbackQuery):
    await query.message.edit_caption(START_TEXT,
                                    reply_markup=InlineKeyboardMarkup(buttons),)

@bot.on_callback_query(filters.regex("help_back"))
async def help(_, query: CallbackQuery):
    await query.message.edit_caption(HELP_TEXT,
                                    reply_markup=InlineKeyboardMarkup(HELP_BUTTON),)

@bot.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
           query = query.message
           await query.delete()

BUTTON = [[InlineKeyboardButton("Back", callback_data="help_back"),
            InlineKeyboardButton("Close", callback_data='close'),]]


# Incomplete wait for update
