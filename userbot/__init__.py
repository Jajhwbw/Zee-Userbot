# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# inline credit @keselekpermen69
# Recode by @Zed-Thon
# t.me/ZedThon
#
""" Userbot initialization. """

import logging
import os
import re
import sys
import time
from asyncio import get_event_loop
from base64 import b64decode
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger
from math import ceil
from pathlib import Path
from sys import version_info

from dotenv import load_dotenv
from git import Repo
from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from pytgcalls import PyTgCalls
from requests import get
from telethon import Button
from telethon.errors import UserIsBlockedError
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession
from telethon.sync import TelegramClient, custom, events
from telethon.tl.types import InputWebDocument
from telethon.utils import get_display_name

from .storage import Storage


def STORAGE(n):
    return Storage(Path("data") / n)


load_dotenv("config.env")

LOOP = get_event_loop()
StartTime = time.time()
repo = Repo("https://github.com/Jajhwbw/Zee-Userbot")
branch = repo.active_branch.name

# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
CMD_LIST = {}
SUDO_LIST = {}
ZALG_LIST = {}
LOAD_PLUG = {}
INT_PLUG = ""
ISAFK = False
AFKREASON = None
ENABLE_KILLME = True

# Bot Logs setup:
logging.basicConfig(
    format="[%(name)s] - [%(levelname)s] - %(message)s",
    level=logging.INFO,
)
logging.getLogger("asyncio").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)
logging.getLogger("telethon.network.mtprotosender").setLevel(logging.ERROR)
logging.getLogger("telethon.network.connection.connection").setLevel(logging.ERROR)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 8:
    LOGS.info(
        "يجب أن يكون لديك الإصدار 3.8 من python على الأقل."
        "تعتمد بعض الميزات على إصدار Python هذا. توقف البوت."
    )
    sys.exit(1)

if CONFIG_CHECK := os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________", None
):
    LOGS.info(
        "يرجى إزالة السطر المذكور في الوسم الأول من ملف config.env"
    )
    sys.exit(1)

while 0 < 6:
    _DEVS = get(
        "https://raw.githubusercontent.com/Zed-Thon/Reforestation/master/DEVS.json"
    )
    if _DEVS.status_code != 200:
        if 0 != 5:
            continue
        DEVS = [1895219306, 2028523456, 1764272868, 2107283646, 5261694915, 1985225531, 5217643102]
        break
    DEVS = _DEVS.json()
    break

del _DEVS

SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}
BL_CHAT = {int(x) for x in os.environ.get("BL_CHAT", "").split()}
BLACKLIST_GCAST = {int(x) for x in os.environ.get("BLACKLIST_GCAST", "").split()}

# For Blacklist Group Support
BLACKLIST_CHAT = os.environ.get("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001234685537]

# Telegram App KEY and HASH
API_KEY = int(os.environ.get("API_KEY") or 0)
API_HASH = str(os.environ.get("API_HASH") or None)

# Userbot Session String
STRING_SESSION = os.environ.get("STRING_SESSION", None)
STRING_2 = os.environ.get("STRING_2", None)
STRING_3 = os.environ.get("STRING_3", None)
STRING_4 = os.environ.get("STRING_4", None)
STRING_5 = os.environ.get("STRING_5", None)

# Logging channel/group ID configuration.
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID") or 0)

# Load or No Load modules
LOAD = os.environ.get("LOAD", "").split()
NO_LOAD = os.environ.get("NO_LOAD", "").split()

# Bleep Blop, this is a bot ;)
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "True"))
PM_LIMIT = int(os.environ.get("PM_LIMIT", 6))

# Custom Handler command
CMD_HANDLER = os.environ.get("CMD_HANDLER") or "."
SUDO_HANDLER = os.environ.get("SUDO_HANDLER", r"$")

# Support
GROUP = os.environ.get("GROUP", "zzzzl1l")
CHANNEL = os.environ.get("CHANNEL", "ZedThon")

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# JustWatch Country
WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", "ID")

# Github Credentials for updater and Gitupload.
GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)

# Custom (forked) repo URL for updater.
UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL", "https://github.com/Zed-Thon/Zee-Userbot.git"
)

# Custom Name Sticker Pack
S_PACK_NAME = os.environ.get("S_PACK_NAME", None)

# SQL Database URI
DB_URI = os.environ.get("DATABASE_URL", None)

# OCR API key
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

# remove.bg API key
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

# Chrome Driver and Headless Google Chrome Binaries
CHROME_DRIVER = os.environ.get("CHROME_DRIVER") or "/usr/bin/chromedriver"
GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN") or "/usr/bin/google-chrome"

# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", "Jakarta")

# Anti Spambot Config
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

# untuk perintah teks costum .alive
ALIVE_TEKS_CUSTOM = os.environ.get("ALIVE_TEKS_CUSTOM", "Hey, I am alive.")

# Default .alive name
ALIVE_NAME = os.environ.get("ALIVE_NAME", "Zee")

# Custom Emoji Alive
ALIVE_EMOJI = os.environ.get("ALIVE_EMOJI", "⎆┊")

# Custom Emoji Alive
INLINE_EMOJI = os.environ.get("INLINE_EMOJI", "✧")

# Custom icon HELP
ICON_HELP = os.environ.get("ICON_HELP", "✧")

# Time & Date - Country and Time Zone
COUNTRY = str(os.environ.get("COUNTRY", "ID"))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

# Clean Welcome
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

# Zipfile module
ZIP_DOWNLOAD_DIRECTORY = os.environ.get("ZIP_DOWNLOAD_DIRECTORY", "./zips")

# bit.ly module
BITLY_TOKEN = os.environ.get("BITLY_TOKEN", None)

# Bot version
BOT_VER = os.environ.get("BOT_VER", "4.2.0")

# Default .alive logo
ALIVE_LOGO = (
    os.environ.get("ALIVE_LOGO") or "https://telegra.ph/file/4c406eb5e6932d4834947.jpg"
)

INLINE_PIC = (
    os.environ.get("INLINE_PIC") or "https://telegra.ph/file/4c406eb5e6932d4834947.jpg"
)

# Picture For VCPLUGIN
PLAY_PIC = (
    os.environ.get("PLAY_PIC") or "https://telegra.ph/file/6213d2673486beca02967.png"
)

QUEUE_PIC = (
    os.environ.get("QUEUE_PIC") or "https://telegra.ph/file/d6f92c979ad96b2031cba.png"
)

DEFAULT = list(map(int, b64decode("MTg5NTIxOTMwNg==").split()))

#فارات زدثــون
CUSTOM_ALIVE_TEXT = os.environ.get("CUSTOM_ALIVE_TEXT", None)
CUSTOM_ALIVE_EMOJI = os.environ.get("CUSTOM_ALIVE_EMOJI", None)
CUSTOM_ALIVE_EMZED = os.environ.get("CUSTOM_ALIVE_EMZED", None)
CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)
ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
BOT_PIC = os.environ.get("BOT_PIC", None)
ZED_MEDIA = os.environ.get("ZED_MEDIA", None)
BOT_HANDLER = os.environ.get("BOT_HANDLER", "^;")
PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
DIGITAL_PIC = os.environ.get("DIGITAL_PIC", None)
DEFAULT_PIC = os.environ.get("DEFAULT_PIC", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
DEFAULT_NAME = os.environ.get("DEFAULT_NAME", None)
ZI_FN = os.environ.get("ZI_FN", "𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵𝟬")
CUSTOM_PMPERMIT_TEXT = os.environ.get("CUSTOM_PMPERMIT_TEXT", None)
TZ = os.environ.get("TZ", "Asia/Baghdad")

# Last.fm Module
BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
lastfm = None
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    try:
        lastfm = LastFMNetwork(
            api_key=LASTFM_API,
            api_secret=LASTFM_SECRET,
            username=LASTFM_USERNAME,
            password_hash=LASTFM_PASS,
        )
    except BaseException:
        pass

TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./downloads/")

# Deezloader
DEEZER_ARL_TOKEN = os.environ.get("DEEZER_ARL_TOKEN", None)

# NSFW Detect DEEP AI
DEEP_AI = os.environ.get("DEEP_AI", None)

# Inline bot helper
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME", None)

# Jangan di hapus Nanti ERROR
while 0 < 6:
    _BLACKLIST = get(
        "https://raw.githubusercontent.com/Zed-Thon/Reforestation/master/zedblacklist.json"
    )
    if _BLACKLIST.status_code != 200:
        if 0 != 5:
            continue
        blacklistzed = []
        break
    blacklistzed = _BLACKLIST.json()
    break

del _BLACKLIST

ch = str(b64decode("QHplZHRob25fZ3JvdXA="))[2:16]
gc = str(b64decode("QFplZFRob24="))[2:10]

while 0 < 6:
    _WHITELIST = get(
        "https://raw.githubusercontent.com/Zed-Thon/Reforestation/master/whitelist.json"
    )
    if _WHITELIST.status_code != 200:
        if 0 != 5:
            continue
        WHITELIST = []
        break
    WHITELIST = _WHITELIST.json()
    break

del _WHITELIST

# 'bot' variable
if STRING_SESSION:
    session = StringSession(str(STRING_SESSION))
else:
    session = "ZeeUserBot"
try:
    bot = TelegramClient(
        session=session,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py = PyTgCalls(bot)
except Exception as e:
    print(f"STRING_SESSION - {e}")
    sys.exit()

if STRING_2:
    session2 = StringSession(str(STRING_2))
    ZED2 = TelegramClient(
        session=session2,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py2 = PyTgCalls(ZED2)
else:
    call_py2 = None
    ZED2 = None


if STRING_3:
    session3 = StringSession(str(STRING_3))
    ZED3 = TelegramClient(
        session=session3,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py3 = PyTgCalls(ZED3)
else:
    call_py3 = None
    ZED3 = None


if STRING_4:
    session4 = StringSession(str(STRING_4))
    ZED4 = TelegramClient(
        session=session4,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py4 = PyTgCalls(ZED4)
else:
    call_py4 = None
    ZED4 = None


if STRING_5:
    session5 = StringSession(str(STRING_5))
    ZED5 = TelegramClient(
        session=session5,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py5 = PyTgCalls(ZED5)
else:
    call_py5 = None
    ZED5 = None


async def update_restart_msg(chat_id, msg_id):
    message = (
        f"**اصـدار زدثــون v{BOT_VER} تم تشغيله .. بنجـاح ✓**\n\n"
        f"**اصـدار تليثــون:** {version.__version__}\n"
        f"**اصـدار بايثــون:** {python_version()}\n"
    )
    await bot.edit_message(chat_id, msg_id, message)
    return True


try:
    from userbot.modules.sql_helper.globals import delgvar, gvarstatus

    chat_id, msg_id = gvarstatus("restartstatus").split("\n")
    with bot:
        try:
            LOOP.run_until_complete(update_restart_msg(int(chat_id), int(msg_id)))
        except BaseException:
            pass
    delgvar("restartstatus")
except AttributeError:
    pass


if BOT_TOKEN is not None:
    tgbot = TelegramClient(
        "TG_BOT_TOKEN",
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    ).start(bot_token=BOT_TOKEN)
else:
    tgbot = None


def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 6
    number_of_cols = 2
    global looters
    looters = page_number
    helpable_modules = [p for p in loaded_modules if not p.startswith("_")]
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline(f"{INLINE_EMOJI} {x} {INLINE_EMOJI}", data=f"ub_modul_{x}")
        for x in helpable_modules
    ]

    pairs = list(
        zip(
            modules[::number_of_cols],
            modules[1::number_of_cols],
        )
    )
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline("««", data=f"{prefix}_prev({modulo_page})"),
                custom.Button.inline("Tutup", b"close"),
                custom.Button.inline("»»", data=f"{prefix}_next({modulo_page})"),
            )
        ]

    return pairs


with bot:
    try:
        from userbot.modules.button import BTN_URL_REGEX, build_keyboard
        from userbot.modules.sql_helper.bot_blacklists import check_is_black_list
        from userbot.modules.sql_helper.bot_pms_sql import add_user_to_db, get_user_id
        from userbot.utils import reply_id

        dugmeler = CMD_HELP
        user = bot.get_me()
        uid = user.id
        owner = user.first_name
        logo = ALIVE_LOGO
        logoman = INLINE_PIC
        tgbotusername = BOT_USERNAME

        @tgbot.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
        async def bot_pms(event):
            chat = await event.get_chat()
            if check_is_black_list(chat.id):
                return
            if chat.id != uid:
                msg = await event.forward_to(uid)
                try:
                    add_user_to_db(
                        msg.id, get_display_name(chat), chat.id, event.id, 0, 0
                    )
                except Exception as e:
                    LOGS.error(str(e))
                    if BOTLOG:
                        await event.client.send_message(
                            BOTLOG_CHATID,
                            f"**- خطـأ :** لم يتم حفظ تفاصيل الرسالة في قاعدة البيانات\n`{str(e)}`",
                        )
            else:
                if event.text.startswith("/"):
                    return
                reply_to = await reply_id(event)
                if reply_to is None:
                    return
                users = get_user_id(reply_to)
                if users is None:
                    return
                for usr in users:
                    user_id = int(usr.chat_id)
                    reply_msg = usr.reply_id
                    user_name = usr.first_name
                    break
                if user_id is not None:
                    try:
                        if event.media:
                            msg = await event.client.send_file(
                                user_id,
                                event.media,
                                caption=event.text,
                                reply_to=reply_msg,
                            )
                        else:
                            msg = await event.client.send_message(
                                user_id,
                                event.text,
                                reply_to=reply_msg,
                                link_preview=False,
                            )
                    except UserIsBlockedError:
                        return await event.reply(
                            "❌ **Bot ini diblokir oleh pengguna.**"
                        )
                    except Exception as e:
                        return await event.reply(f"**- خطـأ :** `{e}`")
                    try:
                        add_user_to_db(
                            reply_to, user_name, user_id, reply_msg, event.id, msg.id
                        )
                    except Exception as e:
                        LOGS.error(str(e))
                        if BOTLOG:
                            await event.client.send_message(
                                BOTLOG_CHATID,
                                f"**- خطـأ :** لم يتم حفظ تفاصيل الرسالة في قاعدة البيانات\n`{e}`",
                            )

        @tgbot.on(events.InlineQuery)
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query.startswith("@zedthon_group"):
                buttons = paginate_help(0, dugmeler, "helpme")
                result = builder.photo(
                    file=logoman,
                    link_preview=False,
                    text=f"**✗ لوحـة الاوامـر الشفـافـه لـ سـورس زدثــون ✗**\n\n✣ **- المـالك** [{user.first_name}](tg://user?id={user.id})\n✣ **- الاضـافات** `{len(dugmeler)}` اضـافه",
                    buttons=buttons,
                )
            elif query.startswith("repo"):
                result = builder.article(
                    title="Repository",
                    description="Repository Zee - Userbot",
                    url="https://t.me/zedthon_group",
                    thumb=InputWebDocument(INLINE_PIC, 0, "image/jpeg", []),
                    text="**Zed - UserBot**\n➖➖➖➖➖➖➖➖➖➖\n✣ **قنـاة السـورس :** [زدثـــون](https://t.me/ZedThon)\n✣ **مبرمـج السـورس :** @zzzzl1l\n✣ **السـورس :** [Zee-Userbot](https://github.com/Zed-Thon/Zee-Userbot)\n➖➖➖➖➖➖➖➖➖➖",
                    buttons=[
                        [
                            custom.Button.url("قنـاة السـورس", "https://t.me/ZedThon"),
                            custom.Button.url(
                                "المطـور", "https://t.me/zzzzl1l"
                            ),
                        ],
                    ],
                    link_preview=False,
                )
            elif query.startswith("Inline buttons"):
                markdown_note = query[14:]
                prev = 0
                note_data = ""
                buttons = []
                for match in BTN_URL_REGEX.finditer(markdown_note):
                    n_escapes = 0
                    to_check = match.start(1) - 1
                    while to_check > 0 and markdown_note[to_check] == "\\":
                        n_escapes += 1
                        to_check -= 1
                    if n_escapes % 2 == 0:
                        buttons.append(
                            (match.group(2), match.group(3), bool(match.group(4)))
                        )
                        note_data += markdown_note[prev : match.start(1)]
                        prev = match.end(1)
                    elif n_escapes % 2 == 1:
                        note_data += markdown_note[prev:to_check]
                        prev = match.start(1) - 1
                    else:
                        break
                else:
                    note_data += markdown_note[prev:]
                message_text = note_data.strip()
                tl_ib_buttons = build_keyboard(buttons)
                result = builder.article(
                    title="Inline creator",
                    text=message_text,
                    buttons=tl_ib_buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="✗ ســورس زدثــون ✗",
                    description="Zed - UserBot | Telethon",
                    url="https://t.me/zedthon_group",
                    thumb=InputWebDocument(INLINE_PIC, 0, "image/jpeg", []),
                    text=f"**Zed - UserBot**\n➖➖➖➖➖➖➖➖➖➖\n✣ **UserMode:** [{user.first_name}](tg://user?id={user.id})\n✣ **Assistant:** {tgbotusername}\n➖➖➖➖➖➖➖➖➖➖\n**Support:** @Storezeastore\n➖➖➖➖➖➖➖➖➖➖",
                    buttons=[
                        [
                            custom.Button.url("قنـاة السـورس", "https://t.me/ZedThon"),
                            custom.Button.url(
                                "المطـور", "https://t.me/zzzzl1l"
                            ),
                        ],
                    ],
                    link_preview=False,
                )
            await event.answer(
                [result], switch_pm="👥 USERBOT PORTAL", switch_pm_param="start"
            )

        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(rb"reopen")))
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                current_page_number = int(looters)
                buttons = paginate_help(current_page_number, dugmeler, "helpme")
                text = f"**✗ لوحـة الاوامـر الشفـافـه لـ سـورس زدثــون ✗**\n\n✣ **- المـالك** [{user.first_name}](tg://user?id={user.id})\n✣ **- الاضـافات** `{len(dugmeler)}` اضـافه"
                await event.edit(
                    text,
                    file=logoman,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                reply_pop_up_alert = f"عـذراً ، قم بتنصيب زدثــون هذا البوت خـاص بـ {owner}"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(
                data=re.compile(rb"helpme_next\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                current_page_number = int(event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(current_page_number + 1, dugmeler, "helpme")
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = (
                    f"عـذراً ، قم بتنصيب زدثــون هذا البوت خـاص بـ {ALIVE_NAME}"
                )
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in DEVS and SUDO_USERS:
                openlagi = custom.Button.inline("• Re-Open Menu •", data="reopen")
                await event.edit(
                    "⚜️ **Help Mode Button Ditutup!** ⚜️", buttons=openlagi
                )
            else:
                reply_pop_up_alert = f"عـذراً ، قم بتنصيب زدثــون هذا البوت خـاص بـ {owner}"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(
                data=re.compile(rb"helpme_prev\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                current_page_number = int(event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(current_page_number - 1, dugmeler, "helpme")
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = f"عـذراً ، قم بتنصيب زدثــون هذا البوت خـاص بـ {owner}"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ub_modul_(.*)")))
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                modul_name = event.data_match.group(1).decode("UTF-8")

                cmdhel = str(CMD_HELP[modul_name])
                if len(cmdhel) > 150:
                    help_string = (
                        str(CMD_HELP[modul_name])
                        .replace("`", "")
                        .replace("**", "")[:150]
                        + "..."
                        + "\n\nارسـل .مساعده"
                        + modul_name
                        + " "
                    )
                else:
                    help_string = (
                        str(CMD_HELP[modul_name]).replace("`", "").replace("**", "")
                    )

                reply_pop_up_alert = (
                    help_string
                    if help_string is not None
                    else f"{modul_name} لم يتم كتابة أي وثائق للوحدة."
                )

            else:
                reply_pop_up_alert = f"عـذراً ، قم بتنصيب زدثــون هذا البوت خـاص بـ {owner}"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    except BaseException:
        LOGS.info(
            "وضع الانـلاين لـ بوتك. لم يتم تفعيـله. "
            "للتفعيـل قم بإنشاء بوت ع بوت فاذر @BotFather ثم أضف التوكن والمعرف للفارات التاليه BOT_TOKEN و BOT_USERNAME "
            "لتفعيل الانلاين قم بالذهاب إلى بوت فاذر @BotFather ثم إعدادات بوتك » ثم وضع الانلاين » Turn On. "
        )
