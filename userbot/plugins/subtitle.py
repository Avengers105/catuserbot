import requests
from bs4 import BeautifulSoup as bs
from uuid import uuid4

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InlineQueryResultDocument
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
from telegram.ext import CallbackContext
)


BASE_URL = "https://isubtitles.org"

def search_sub(query):
    r = requests.get(f"{BASE_URL}/search?kwd={query}").text
    soup = bs(r, "lxml")
    list_search = soup.find_all("div", class_="row")
    index = []
    title = []
    keywords = []

    second_soup = bs(str(list_search), 'lxml')
    headings = second_soup.find_all("h3")

    third_soup = bs(str(headings), "lxml")
    search_links = third_soup.find_all("a")

    i = 0

    for a in search_links:
        i += 1
        index.append(i)
        title.append(a.text)
        key = a.get("href").split("/")
        keywords.append(key[1])

    return index, title, keywords


def get_lang(keyword):
    url = f"{BASE_URL}/{keyword}"
    request = requests.get(url).text
    fourth_soup = bs(request, "lxml")
    filesoup = fourth_soup.find_all("table")
    fifth_soup = bs(str(filesoup), "lxml")
    table_soup = fifth_soup.find_all("a")
    language = []
    index = []
    link = []
    i = 0
    for b in table_soup:
        if b["href"].startswith("/download/"):
            i += 1
            h = b.get("href").split("/")
            buttoname = h[3]
            if buttoname not in language:
                index.append(i)
                language.append(buttoname)
                link.append(f"{BASE_URL}{b.get('href')}")
    return index, language, link


@catub.cat_cmd(
    pattern="subtitle(?:\s|$)([\s\S]*)",
    command=("subtitle", plugin_category),
    info={
        "header": "Get Subtitles of Give Movies",
        "description": "Subtitles Finder",
        "usage": "{tr}subtitle",
    },
)
async def subtitle(event):
    "Get Subtitles of Given Movies"
    input_str = event.pattern_match.group(1)
   def searching(update: Update, context: CallbackContext):
    if update.message.via_bot != None:
        return

    search_message = context.bot.send_message(chat_id=update.effective_chat.id, text="Searching your subtitle file")
    sub_name = update.effective_message.text
    full_index, title, keyword = search_sub(sub_name)
    inline_keyboard = []
    if len(full_index) == 0:
        context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=search_message.message_id, text="No results found")
        return
    
    index = full_index[:15]
    for i in index:
        subtitle = title[i-1]
        key = keyword[i-1]
        inline_keyboard.append([InlineKeyboardButton(subtitle, callback_data=f"{key}")])

    reply_markup = InlineKeyboardMarkup(inline_keyboard)
    context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=search_message.message_id, text=f"Got the following results for your query *{sub_name}*. Select the preffered type from the below options", parse_mode="Markdown", reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    query.answer()
    sub = query.data
    index, language, link = get_lang(sub)

    if len(index) == 0:
        query.edit_message_text(text="Something went wrong")
        return

    inline_keyboard = []
    for i in range(len(index)):
        button_name = language[i-1]
        button_data = link[i-1]
        inline_keyboard.append([InlineKeyboardButton(f"{button_name.upper()}", switch_inline_query_current_chat=f"{button_data}")])

    reply_markup = InlineKeyboardMarkup(inline_keyboard)
    query.edit_message_text(text="Select your language", reply_markup=reply_markup)

def inlinequery(update, context):
    query = update.inline_query.query
    inline = [
        [
            InlineKeyboardButton("Our Group", url="https://telegram.dog/Keralasbots"),
            InlineKeyboardButton("Our Channel", url="https://telegram.dog/Keralabotsnews")
        ]
    ]
    results = [
        InlineQueryResultDocument(
            id=uuid4(),
            document_url=query,
            title="Get the File",
            mime_type="application/zip",
            reply_markup=InlineKeyboardMarkup(inline),
            caption="©️ @GetSubtitles_bot\n\nUse @UnzipTGBot for unzipping this zip file or download the file and unzip manually"
        )
    ]
    update.inline_query.answer(results)
