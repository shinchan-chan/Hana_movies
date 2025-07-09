#Recoded by @Its_Oreki_Hotarou

import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "24371796"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8121c78f4b8b31e88cc2623d1277338d")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002857493189"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1683225887"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://adamopytbusiness1:uSswEjo4ZHMGDU8Z@cluster0.gqgmk.mongodb.net/?retryWrites=true&w=majority&appName=KimaChanBot")
DB_NAME = os.environ.get("DATABASE_NAME", "KimaChanBot")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1002445904065"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1002557169359"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#pics
START_PIC = os.environ.get("START_PIC", "https://envs.sh/Me9.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/Mes.jpg")

#text
HELP_TXT = "<blockquote><b>Hi Dude!\n\nTo use this bot you just have to join both channels that's it..\nWatch Tutorial to open Link - <a href=https://t.me/+KPJ5glEICD40Njc1>Clickhere</a></b></blockquote>"
ABOUT_TXT = "<blockquote><b><i>» ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/DoraShin_hlo>➳≛⃝ Gojo</a>\n» ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/HellFire_Academy>𝐇ᴇʟʟғɪʀᴇ 𝐀ᴄᴀᴅᴇᴍʏ</a>\n» ᴏɴɢᴏɪɴɢ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Ongoing_HellFire_Academy>𝐎ɴɢᴏɪɴɢ 𝐇ᴇʟʟғɪʀᴇ 𝐀ᴄᴀᴅᴇᴍʏ</a>\n» sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ : <a href=https://t.me/HellFire_Academy_Chat>𝐇ᴇʟʟғɪʀᴇ 𝐆ᴄ</a>\n» ᴏᴡɴᴇʀ : <a href=https://t.me/DoraShin_hlo>➳≛⃝ Gojo</i></b></blockquote>"
#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜɪ ᴛʜᴇʀᴇ... {first}! 💥\n\nɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ...!\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ....!\n\nᴘᴏᴡᴇʀᴇᴅ ʙʏ : <a href=https://t.me/@HellFire_Network>HellFire Network</a></b>")
try:
    ADMINS=[6521688979]
    for x in (os.environ.get("ADMINS", "5195665501 6521688979").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}!⚡\n\n🫧ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ʙᴏᴛʜ ᴏꜰ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ...!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

#Short Url or Api
SHORT_URL = os.environ.get("SHORTNER_URL", "arolinks.com")
SHORT_API = os.environ.get("SHORTNER_API", "401e6f6a477d6438175e361c558ab6cf1282e064")

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ - @DoraShin_hlo"

AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "43200"))
DEL_MSG = "<b>This File is deleting automatically in {time}. Forward in your Saved Messages..!</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(1418213560)

LOG_FILE_NAME = "filesharingbot.txt"

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

#Bhen ke lavdo Credit hataya na ma choddunga wahi aakr salo use karo bas 
