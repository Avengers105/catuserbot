import os

import requests

import jokeapi

from userbot import catub

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

plugin_category = "fun"


@catub.cat_cmd(
    pattern="joke(?:\s|$)([\s\S]*)",
    command=("joke", plugin_category),
    info={
        "header": "Just For Fun.",
        "description": "CMD For Get Jokes",
        "usage": "{tr}joke",
    },
)
async def jokeapi(event):
    "Just For Fun"
    input_str = event.pattern_match.group(1)
    jokeapi = jokeapi(source="https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit")


