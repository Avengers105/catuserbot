import os
import random
from bs4 import BeautifulSoup
import requests

from userbot import catub

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

plugin_category = "fun"

async def extract_jokeContainer(url):
    results = []
    request = requests.get(url).text
    soup = BeautifulSoup(request, "html.parser")
    for jokeContainer in soup.find_all("div", class_="jokeContainer"):
        response = jokeContainer.find("div", {"class": "jokeText"}).text
        results.append(response.replace("\n", " ").strip())
    return results

async def random_jokeContainer():
    pgno = random.randint(1, 100)
    jokeContainerurl = f"https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
    results = await extract_jokeContainer(jokeContainerurl)
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
async def random_jokeContainer(event):
    "Just For Fun"
    try:
        response = await random_jokeContainer()
    except Exception:
        return await edit_delete(event, "`Sorry Zero results found`", 5)
    await edit_or_reply(event, response, parse_mode=parse_pre)



