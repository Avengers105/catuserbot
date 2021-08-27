import asyncio
import base64
import os
import random
import re
import shutil
import time
import urllib
from datetime import datetime

import requests
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.errors import FloodWaitError
from telethon.tl import functions
from urlextract import URLExtract

from ..Config import Config
from ..helpers.utils import _format
from ..sql_helper.global_list import (
    add_to_list,
    get_collection_list,
    is_in_list,
    rm_from_list,
)
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import (
    AUTONAME,
    BOTLOG,
    BOTLOG_CHATID,
    DEFAULT_BIO,
    _catutils,
    catub,
    edit_delete,
    logging,
)

plugin_category = "tools"

autopic_path = os.path.join(os.getcwd(), "userbot", "original_pic.png")
digitalpic_path = os.path.join(os.getcwd(), "userbot", "digital_pic.png")
autophoto_path = os.path.join(os.getcwd(), "userbot", "photo_pfp.png")

COLLECTION_STRINGS = {
    "ironmanpfp_strings": [
        "avengers-hd-4k-wallpaper",
        "awesome-ironman-wallpapers",
        "ironman-arkham-knight-4k-wallpaper",
        "ironman-hd-wallpapers-1080p",
        "the-joker-hd-wallpaper",
        "dark-knight-joker-wallpaper",
    ],
}

@catub.cat_cmd(
    pattern="ironmanpfp$",
    command=("ironmanpfp", plugin_category),
    info={
        "header": "Changes profile pic with random IronMan pics every 1 minute",
        "description": "Changes your profile pic every 1 minute with random IronMan pics.\
        If you like to change the time then set CHANGE_TIME var in Heroku with time(in seconds) between each change of profilepic.",
        "note": "To stop this do '.end ironmanpfp'",
        "usage": "{tr}ironmanpfp",
    },
)
async def _(event):
    "To set random ironman profile pics"
    if gvarstatus("autopfp_strings") is not None:
        pfp_string = gvarstatus("autopfp_strings")[:-8]
        return await edit_delete(event, f"`{pfp_string} is already running.`")
    addgvar("autopfp_strings", "ironmanpfp_strings")
    await event.edit("`Starting thor Profile Pic.`")
    await autopfp_start()
