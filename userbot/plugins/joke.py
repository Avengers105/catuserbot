import os
import random

import requests

from userbot import catub

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

plugin_category = "fun"

async def random_joke():
    pgno = random.randint(1, 100)
    jokeurl = f"https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
    results = await extract_joke(jokeurl)
    return random.choice(results)


@catub.cat_cmd(
    pattern="joke(?:\s|$)([\s\S]*)",
    command=("joke", plugin_category),
    info={
        "header": "Just For Fun.",
        "description": "CMD For Get Jokes",
        "usage": "{tr}joke",
    },
)
async def joke(event):
    "Just For Fun"
    await edit_or_reply(event, "`Processing...`",)
    await event.delete()
 else:
     try:
         response = await random_joke
     except Exception:
         return await edit_delete(event, "`Sorry Zero results found`", 5)
     await edit_or_reply(event, response, parse_mode=parse_pre)



