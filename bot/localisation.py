#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AbirHasan2005 | @Technical-Jigar

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "<b>Hello, \n\nThis is a Telegram HEVC Video Compress Bot</b> \n\n<b>Please sent me any Telegram big file I Will compress a small file.</b> \n\n<b>/help for more details.</b> \n\n🏷 <b>Maintained By: @Amani_m_h_d</b>"
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "📥 Downloading ... 📥 \n"
    
    UPLOAD_START = "🚀 Uploading ... 🚀 \n"
    
    COMPRESS_START = "📀 Trying to compress ... 📀"
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "📥 Downloaded in {}\n\n📀 Compressed in {}\n\n📤 Uploaded in {}\n\n<b>By @Amani_m_h_d</b>"

    COMPRESS_PROGRESS = "⏳ ETA: {}\n🚀 Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = "✅ Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ Already one Process going on! ⚠️ \n\nCheck Live Status on Updates Channel."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "<b>Hi, I am HEVC Video Compressor Bot \n\n➥ Send me your telegram big video file \n➥ Reply the file - /compress And Persentage</b> \nEg: <code>/compress 50</code> \n➥ <b>Due to quality changing Bot will take too much time to compress. \n➥ So, Be patience & Send one video to compress in a day \n\n🏷 <b>Maintained By: @Amani_m_h_d</b>"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
