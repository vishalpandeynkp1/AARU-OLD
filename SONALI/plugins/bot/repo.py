from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI import app
from config import BOT_USERNAME
from SONALI.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
✰ 𝗪ᴇʟᴄᴏᴍᴇ ᴛᴏ 𝗧ᴇᴀᴍ 𝗡ᴏʙɪᴛᴀ 𝗥ᴇᴘᴏs ✰
 
✰ 𝗥ᴇᴘᴏ ᴛᴏ 𝗡ʜɪ 𝗠ɪʟᴇɢᴀ 𝗬ʜᴀ
 
✰ 𝗣ᴀʜʟᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ 𝗥ᴇᴘᴏ 𝗢ᴡɴᴇʀ ᴋᴏ 

✰ || @ll_NOBITA_BOT_DEVLOPER_ll ||
 
✰ 𝗥ᴜɴ 24x7 𝗟ᴀɢ 𝗙ʀᴇᴇ 𝗪ɪᴛʜᴏᴜᴛ 𝗦ᴛᴏᴘ
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔ᴅᴅ ᴍᴇ 𝗠ᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛ᴇʟᴘ", url="https://t.me/THE_VIP_BOY_OP"),
          InlineKeyboardButton("𝗡ᴏʙɪᴛᴀ", url="https://t.me/ll_NOBITA_BOT_DEVLOPER_ll"),
          ],
               [
                InlineKeyboardButton("𝗧ᴇᴀᴍ 𝗡ᴏʙɪᴛᴀ 𝗕ᴏᴛs", url=f"https://t.me/NOBITA_ALL_BOT"),
],
[
InlineKeyboardButton("𝗠ᴀɪɴ 𝗕ᴏᴛ", url=f"https://t.me/AARU_MUSIC_XBOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/of7wlb.webp",
        caption=start_txt,
        reply_markup=reply_markup
    )
