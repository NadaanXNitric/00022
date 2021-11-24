from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAADBQADRQIAAhHHQFSfHJ-IR0eN6gI")
    await message.reply_text(
        f"""**- 𝐇𝐞𝐲 𝐀𝐦 {bn} 💛🐬,

- 𝐈 𝐂𝐚𝐧 𝐏𝐥𝐚𝐲 𝐌𝐮𝐬𝐢𝐜 𝐈𝐧 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩'𝐬 𝐕𝐨𝐢𝐜𝐞 𝐂𝐚𝐥𝐥. 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 [𝐍 𝐢 𝐭 𝐫 𝐢 𝐜 𓆩👅𓆪](https://t.me/official_nitric) ❣️🤞.

𝐀𝐝𝐝 𝐌𝐞 𝐈𝐧 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝 𝐏𝐥𝐚𝐲 𝐌𝐮𝐬𝐢𝐜 𝐅𝐫𝐞𝐞𝐥𝐲 💕**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                         "🌸 𝐎𝐰𝐧𝐞𝐫 ", url="https://t.me/official_nitric")
                  ],[
                    InlineKeyboardButton(
                        "💡 𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url="https://t.me/sanki_bots_support"
                    ),
                    InlineKeyboardButton(
                        "📌 𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url="https://t.me/crowrace"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ 𝐀𝐝𝐝 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ➕", url="https://t.me/NovoMusicRobot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""** 𝐍𝐨𝐯𝐨 𝐌𝐮𝐬𝐢𝐜 𝐏𝐥𝐚𝐲𝐞𝐫 𝐈𝐬 𝐎𝐧𝐥𝐢𝐧𝐞 ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 𝐌𝐚𝐧𝐚𝐠𝐞𝐫", url="https://t.me/official_nitric")
                ]
            ]
        )
   )

