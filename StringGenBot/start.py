from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""𝗛𝗘𝗬 {msg.from_user.mention},

𝗜 𝗮𝗺 𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗦𝘁𝗿𝗶𝗻𝗴 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗼𝗿 𝗯𝗼𝘁 𝗳𝗼𝗿 𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺 & 𝗧𝗲𝗹𝗲𝘁𝗵𝗼𝗻.


𝗠𝗔𝗗𝗘 𝗕𝗬: [𝗦𝗔𝗡𝗚𝗥𝗔𝗠](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🌸 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗘 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 🌸", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("🌸 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 🌸", url="https://t.me/WorldChattingFriendsWCF"),
                    InlineKeyboardButton("🌸 𝗨𝗣𝗗𝗔𝗧𝗘𝗦 🌸", url="https://t.me/WCFnetwork")
                ],
                [
                    InlineKeyboardButton("🌸 𝗢𝗪𝗡𝗘𝗥 🌸", url="https://t.me/Kalakar_Sangram")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )
