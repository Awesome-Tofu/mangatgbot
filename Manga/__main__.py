from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Manga import bot

markup = InlineKeyboardMarkup([
    [InlineKeyboardButton("OWNER", url="https://t.me/just_a_bio"),
     InlineKeyboardButton("SUPPORT", url="https://t.me/just_a_bio")]
])

caption = "Bot Awake 🌟"
photo = "https://telegra.ph/file/dc59c2b7bdfc7132895f1.jpg"

if __name__ == "__main__":
    waifu.run()
    with waifu:
        waifu.send_photo(chat_id=-1001692098754, photo=photo, caption=caption, reply_markup=markup)
