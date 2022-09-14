from pyrogram import filters

from .. import Calls, bot, chat_id
from ..functions import admin_check


@bot.on_message(filters.command("vpause") & filters.chat(chat_id))
async def pause(client, message):  
    admins = await admin_check(client, message)   
    await Calls.set_pause(True)
    


@bot.on_message(filters.command("vresume") & filters.chat(chat_id))
async def resume(client, message):   
    admins = await admin_check(client, message)   
    await Calls.set_pause(False)
    
