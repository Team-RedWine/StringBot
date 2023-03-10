from config import MUST_JOIN

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://telegra.ph/file/f2632de43c3c94f4bf81d.jpg", caption=f"ยป ๐ฃ๐๐๐๐ฆ๐ ๐๐ข๐๐ก ๐ ๐ฌ [๐จ๐ฃ๐๐๐ง๐๐๐ฆ ๐๐๐๐ก๐ก๐๐]({link}) ๐ง๐ข ๐จ๐ฆ๐ ๐ง๐๐๐ฆ ๐๐ข๐ง.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("๐ธ ๐๐ข๐๐ก ๐จ๐ฃ๐๐๐ง๐๐ฆ ๐ธ", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {MUST_JOIN} !")
