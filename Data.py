# Credits: @hskdashing
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/hskdashing & t.me/hskdashing

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ How to use this boat
 ├ /start - start Bot
 ├ /about - about this bot
 ├ /help - help this Bot 
 ├ /ping - to check live bots
 └ /uptime - to see status 
 
 ❏ Commands for BOT Admin
 ├ /logs - to view bot logs
 ├ /setvar - to set var with command dibotted
 ├ /delvar - delvar-to delete a var with a bot command
 ├ /getvar - to view one of the VARs with the command dibotted
 ├ /users - to view bot User Statistics
 ├ /batch - batch-to link more than one file
 ├ /speedtest - to test the speed of the bot server
 └ /broadcast - to send a broadcast message to the bot user

👨‍💻 Develoved by </b><a href='https://t.me/@Zblivebot/101'>@Zblivebot</a>
"""

    close = [
        [InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ", callback_data="about"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    ABOUT = """
<b>Tentang Bot ini:

@{} adalah Bot Telegram untuk menyimpan Postingan atau File yang dapat Diakses melalui Link Khusus.

 • Creator: @{}
 • Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>
 • Source Code: <a href='lun</a>

👨‍💻 Develoved by </b><a href='https://t.me/@Zblivebot/101'>@Zblivebot</a>
"""
