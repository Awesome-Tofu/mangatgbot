import logging
import os
import time
from pyrogram import filters
from pyrogram import Client
import pyromod.listen




FORMAT = "[BOT]: %(message)s"

logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('logs.txt'),
                                                    logging.StreamHandler()], format=FORMAT)

StartTime = time.time()

prefix = [".","!","?","*","$","#","/"]

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time


api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("TOKEN")



bot = Client("bot", 
       api_id=api_id, 
       api_hash=api_hash,
       bot_token=bot_token,
       plugins=dict(root="Manga"), )


@bot.on_message(filters.command("ping", prefix))
async def ping(_, message):
    start_time = time.time()
    await message.reply_text("`Getting Server Ping...`")
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 3)
    uptime = get_readable_time((time.time() - StartTime))
    await message.reply_text(f"**ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ**\n⋙ 🔔 **Ping**: {ping_time}\n⋙ ⬆️ **Uptime**: {uptime}")
  
