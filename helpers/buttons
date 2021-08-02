import asyncio
from helpers.database.access_db import db
from pyrogram.errors import FloodWait, MessageNotModified, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

"""async def OpenSettings(event: Message, user_id: int):
    try:
        await event.edit(
            text="Here You Can Set Your Settings:",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(f"Upload as Doc {'✅' if ((await db.get_upload_as_doc(user_id)) is True) else '❌'}",
                                          callback_data="triggerUploadMode")],
                    [InlineKeyboardButton("✏️ File Name Prefix ✏️", callback_data="triggerPrefix")],
                    [InlineKeyboardButton("🖼 Thumbnail 🖼", callback_data="triggerThumbnail")],
                    [InlineKeyboardButton("🏷 Caption 🏷", callback_data="triggerCaption")],
                    [InlineKeyboardButton("❎ Close ❎", callback_data="closeMeh")]
                ]
            )
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await OpenSettings(event, user_id)
    except MessageNotModified:
    """
import os
from helpers.translation import Translation
from configs import Config
from pyrogram import Client

Cortana = Client(
    session_name=Config.SESSION_NAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
  )

@Cortana.on_callback_query()
async def callback_handlers(event: Message, user_id: int):
    if message.data == "home":
        await event.edit(
            text=Translation.START_TEXT.format(message.from_user.mention),
            reply_markup=Translation.START_BUTTONS,
            disable_web_page_preview=True,
        )
    elif message.data == "help":
        await event.edit(
            text=Translation.HELP_TEXT.format(message.from_user.mention),
            reply_markup=Translation.HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "about":
        await event.edit(
            text=Translation.ABOUT_TEXT,
            reply_markup=Translation.ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "aboutdev":
        await event.edit(
            text=Translation.ABOUT_DEV_TEXT,
            reply_markup=Translation.ABOUT_DEV_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "info":
        await event.edit(
            text=Translation.INFO_TEXT.format(username=message.from_user.username, first_name=message.from_user.first_name, last_name=message.from_user.last_name, user_id=message.from_user.id, mention=message.from_user.mention),
            reply_markup=Translation.INFO_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "refreshme":
        if config.UPDATES_CHANNEL:
            invite_link = await client.create_chat_invite_link(int(config.UPDATES_CHANNEL))
            try:
                user = await client.get_chat_member(int(config.UPDATES_CHANNEL), message.message.chat.id)
                if user.status == "kicked":
                    await event.edit(
                        text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/leosupportx).",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await event.edit(
                    text="<b>Hey</b> {},\n\n<b>You still didn't join our Updates Channel ☹️ \nPlease Join and hit on the 'Refresh 🔄' Button</b>".format(message.from_user.mention),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Join Our Updates Channel 🗣", url=invite_link.invite_link)
                            ],
                            [
                                InlineKeyboardButton("Refresh 🔄", callback_data="refreshme")
                            ]
                        ]
                    ),
                    parse_mode="HTML"
                )
                return
            except Exception:
                await event.edit(
                    text="Something went Wrong. Contact my [Support Group](https://t.me/leosupportx).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        await event.edit(
            text=Translation.START_TEXT.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=Translation.START_BUTTONS,
        )
    else:
        await event.delete()
