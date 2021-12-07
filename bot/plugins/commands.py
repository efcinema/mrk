#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG & @yaduvind

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = f"{file_name} \n \n♻️കൂടുതൽ സിനിമകൾക്കും മറ്റു വിവരങ്ങൾക്കുമായി ഞങ്ങളുടെ ഗ്രൂപ്പിൽ ജോയിൻ ചെയ്യൂ♻️
━━━━━━━━━━━━━━━━
🎗️ʝσιи 🎗️ ѕнαяє🎗️ ѕυρρσят🎗️

👥 Group : @efcinema 
📢Channel📢:https://t.me/joinchat/9NVz9tJLa3E0OWVl
🗂️Series channel🗂️:https://t.me/joinchat/TV5ijQpEgxxiNTJl",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '🎖️Our Group🎖️', url="https://t.me/Mo_Tech_YT"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('👨‍💼 𝙼𝚊𝚜𝚝𝚎𝚛', url='https://t.me/yaduvind'),
        InlineKeyboardButton('𝙷𝚎𝚕𝚙 🤔', callback_data="help")
    ],[
        InlineKeyboardButton('🌟OUR GROUP🌟', url='https://t.me/efmovieschannel')
    ],[
        InlineKeyboardButton('🗣️ 𝙰𝚗𝚢 𝙳𝚘𝚞𝚋𝚝', url='https://t.me/efcinema'),
        InlineKeyboardButton('My Dev', url='https://t.me/yaduvind')
    ],[
        InlineKeyboardButton('💥 Hi 💥', url='https://t.me/efcinema')
   ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('🏠 𝙷𝚘𝚖𝚎', callback_data='start'),
        InlineKeyboardButton('𝙰𝚋𝚘𝚞𝚝 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('🔐 𝙲𝚕𝚘𝚜𝚎 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('👤 @yaduvind 👤', url='https://t.me/yaduvind')
    ],[
        InlineKeyboardButton('👤 @𝙰𝚕𝚋𝚎𝚛𝚝𝙴𝚒𝚗𝚜𝚝𝚎𝚒𝚗𝚃𝙶 👤', url='https://t.me/AlbertEinstein_TG')
    ],[
        InlineKeyboardButton('🏠 𝙷𝚘𝚖𝚎', callback_data='start'),
        InlineKeyboardButton('𝙲𝚕𝚘𝚜𝚎 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
