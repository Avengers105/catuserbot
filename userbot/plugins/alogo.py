from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import catub

from ..core.managers import edit_or_reply

plugin_category = "extra"


@catub.cat_cmd(
    pattern="alogo ([\s\S]*)",
    command=("alogo", plugin_category),
    info={
        "header": "To get Logos",
        "description": "To get logo",
        "usage": "{tr}alogo <codename>",
        "examples": "{tr}alogo Avengers",
    },
)
async def _(event):
    "To get logos"
    link = event.pattern_match.group(1)
    get = "alogo"
    catevent = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@BHLogoBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await catbot.client.send_message(chat, reply_message)
            respond = await response
        except YouBlockedUserError:
            return await catevent.edit("```Unblock @BHLogoBot plox```")
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)
