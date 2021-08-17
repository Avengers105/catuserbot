from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import catub

from ..core.managers import edit_or_reply

plugin_category = "extra"


@catub.cat_cmd(
    pattern="gen ([\s\S]*)",
    command=("gen", plugin_category),
    info={
        "header": "This Will Give Beautiful Logos",
        "description": "This Will Give Beautiful Logos With the Help of @BHLogoBot",
        "usage": "{tr}gen <name>",
        "examples": "{tr}gen Avengers",
    },
)
async def _(event):
    "This Will Give Beautiful Logos"
    link = event.pattern_match.group(1)
    gen = "gen"
    catevent = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@BHLogoBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1532727866)
            )
            await conv.send_message(f"/{gen} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await catevent.edit("```Unblock @BHLogoBot plox```")
        else:
            await catevent.delete()
            await event.client.sent_file(event.chat_id, respond.message.media)
