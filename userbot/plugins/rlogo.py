# this plugin is created by @MineisZarox and @Peterparker6

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
    pattern="(rlogo?(?:\s|$)([\s\S]*)",
    command=("(d)(i)logo", plugin_category),
    info={
        "header": "To make logo of given text.",
        "flag": {
            "d": "To make logo of given text document format",
            "i": "To make logo of given text incompressed image format",
        },
        "usage": [
            "{tr}dlogo <text>",
            "{tr}ilogo <text>",
        ],
        "examples":[ 
            "{tr}dlogo Mine",
            "{tr}ilogo Mine",
        ],
    },
)
async def _(event):
    "To make logo of given text."
    cmd = event.pattern_match.group(1).lower()
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not input_str and not reply_message:
        await edit_delete(
            event,
            "Please give some text or reply to any message",
        )

    chat = "@BHLogoBot"
    if cmd == "d" :
        async with event.client.conversation(chat) as conv:
            try:
                try:
                    await event.client(ImportChatInviteRequest('AAAAAFZPuYvdW1A8mrT8Pg'))
                except UserAlreadyParticipantError:
                    await asyncio.sleep(0.00000069420)
                await event.delete()
                await conv.send_message(f"/gen {input_str or reply_message}")
                message = await conv.get_response(1)
                await event.client.send_message(event.chat_id, message)
                x = await conv.get_response(1)
                y = input_str or reply_message
                z = str(x.file.ext)
                a = y + z
                f = await event.client.download_media(x, a)
                await event.client.send_file(event.chat_id,  file=f, force_document=True, caption=f"➥ Genrated by :- {mention}")
                await event.delete()
            except YouBlockedUserError:
                await edit_delete("unblock @BHLogoBot and then try") 

    if cmd == "i" :
        async with event.client.conversation(chat) as conv:
            try:
                try:
                    await event.client(ImportChatInviteRequest('AAAAAFZPuYvdW1A8mrT8Pg'))
                except UserAlreadyParticipantError:
                    await asyncio.sleep(0.00000069420)
                await event.delete()
                await conv.send_message(f"/gen {input_str or reply_message}")
                message = await conv.get_response(1)
                await event.client.send_message(event.chat_id, message)
                x = await conv.get_response(1)
                y = input_str or reply_message
                z = str(x.file.ext)
                a = y + z
                f = await event.client.download_media(x, a)
                await event.client.send_file(event.chat_id,  file=f, force_document=False, caption=f"➥ Genrated by :- {mention}")
                await event.delete()
            except YouBlockedUserError:
                await edit_delete("unblock @BHLogoBot and then try")
