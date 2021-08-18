import asyncio
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon import events
from userbot import catub
from . import mention
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _format

plugin_category = "extra"

@catub.cat_cmd(
    pattern="advlogo ([\s\S]*)",
    command=("advlogo", plugin_category),
    info={
        "header": "To Make Logo If Given Test",
        "description": "Note:You Must Join (@BotzHub) This Channel To Use This Plugin",
        "examples": [
            "{tr}advlogo <test>",
            "{tr}advlogo Avengers",
        ],
    },
)
async def kakashi(event):
    "To Make Advanced Logos Of Given Tests"
    chat = "@BHLogoBot"
    link = event.pattern_match.group(1)
    if "www.instagram.com" not in link:
        await conv.send_message(f"/gen {input_str or reply_message}")
        )
    else:
        catevent = await edit_or_reply(event, "**Downloading.....**")
    async with event.client.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            response = await conv.get_response()
            msg = await conv.send_message(/gen)
            image = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**Error:** `unblock` @BHLogoBot `and retry!`")
            return
        await catevent.delete()
        cat = await event.client.send_file(
            event.chat_id,
            image,
        )
    await event.client.delete_messages(
        conv.chat_id, [msg_start.id, response.id, msg.id, image.id, details.id]
    )
