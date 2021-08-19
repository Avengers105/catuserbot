# this plugin is created by @MineisZarox and @Peterparker6
import os
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
    pattern="(dlogo|ilogo)(?:\s|$)([\s\S]*)",
    command=("advlogo", plugin_category),
    info={
        "header": "To make Advanced logo of given text.",
        "options": {
            "dlogo": "To Make Logos Of Given Text as Document(PNG) Format",
            "ilogo": "To Make Logos Of Given Text As Image Format.",
        },
        "usage": [
            "{tr}dlogo",
            "{tr}ilogo",
            "{tr}dlogo Venom",
            "{tr}ilogo Venom",
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
    tr = os.environ.get("COMMAND_HAND_LER")
    if cmd == "dlogo" :
        async with event.client.conversation(chat) as conv:
            try:
                try:
                    await event.client(ImportChatInviteRequest('RvT1YQvgl_8D9Hbd'))
                except UserAlreadyParticipantError:
                    await asyncio.sleep(0.00000069420)
                await conv.send_message(f"/gen {input_str or reply_message}")
                await event.delete()
                message = await conv.get_response(1)
                await event.client.send_message(event.chat_id, message)
                Peter = await conv.get_response(1)
                Mine = input_str or reply_message
                Zarox = str(Peter.file.ext)
                Parker = Mine + Zarox
                file = await event.client.download_media(Peter, Parker)
            except YouBlockedUserError:
                return await edit_or_reply(event,f"{tr}unblock @BHLogoBot and then try",)
            await event.client.send_file(event.chat_id,  file, force_document=True, caption=f"➥ Genrated by :- {mention}")

    if cmd == "ilogo" :
        async with event.client.conversation(chat) as conv:
            try:
                try:
                    await event.client(ImportChatInviteRequest('RvT1YQvgl_8D9Hbd'))
                except UserAlreadyParticipantError:
                    await asyncio.sleep(0.00000069420)
                await conv.send_message(f"/gen {input_str or reply_message}")
                await event.delete()
                message = await conv.get_response(1)
                await event.client.send_message(event.chat_id, message)
                Peter = await conv.get_response(1)
                Mine = input_str or reply_message
                Zarox = str(Peter.file.ext)
                Parker = Mine + Zarox
                file = await event.client.download_media(Peter, Parker)
            except YouBlockedUserError:
                await edit_or_reply(event,f"{tr}unblock @BHLogoBot and then try","Please Unblock @BHLogoBot and Try",)
            await event.client.send_file(event.chat_id,  file, force_document=False, caption=f"➥ Genrated by :- {mention}")
            if os.path.exists(file):    os.remove(file)
