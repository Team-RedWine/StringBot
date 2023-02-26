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
                    photo="https://telegra.ph/file/f2632de43c3c94f4bf81d.jpg", caption=f"» 𝗣𝗟𝗘𝗔𝗦𝗘 𝗝𝗢𝗜𝗡 𝗠𝗬 [𝗨𝗣𝗗𝗔𝗧𝗘𝗗𝗦 𝗖𝗛𝗔𝗡𝗡𝗘𝗟]({link}) 𝗧𝗢 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🌸 𝗝𝗢𝗜𝗡 𝗨𝗣𝗗𝗔𝗧𝗘𝗦 🌸", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {MUST_JOIN} !")
