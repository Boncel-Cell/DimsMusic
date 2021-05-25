from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Haii, My Name is  {bn} \n\n Saya Bot Music Group, Yang dapat Memutar Lagu di Voice Chat Group Dengan cara yang Mudah
Saya Memiliki Banyak Fitur Praktis Seperti :\n **┏━━━━━━━━━━━━━━
┣• Memutar Musik.
┣• Mendownload Lagu.
┣• Mencari Lagu Yang ingin di Putar atau di Download.
┗━━━━━━━━━━━━━━** \n **❃ Managed With ☕️ By : @dims_whydi** \n **━━━━━━━━━━━━━━━** \n\n **Asisten harus ada di grup Anda untuk memutar musik di obrolan suara grup Anda.** \n\ **untuk mengetahui perintah saya tekan /help**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "OWNER⚡️", url="https://t.me/dims_whydi"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "JOIN GROUP⚡️", url="https://t.me/CARI_DOI_INDONESIA"
                    ),
                    InlineKeyboardButton(
                        "JOIN CHANNEL⚡️", url="https://t.me/GOLDEN_QUOTES_INDONESIA"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Tambahkan Ke Group⚡️", url="https://t.me/@MusicDimsBot?startgroup=true"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
