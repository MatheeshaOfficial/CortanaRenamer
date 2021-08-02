from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
Hello {} 👋
I'm Cortana Song Downloader Bot 🇱🇰
You can rename any file with custom thumnails and custom caption😊
press /settings costomized me
If you want to know how to use me just
touch on " Help 🆘 "  Button 😏
"""    
    HELP_TEXT = """
Hello {}👋
You should know following instructions to rename your files 😊
You can download song by,
🔰Fist press ⚙Setting button 
👩‍🔧Then customized me 🤗
🔰 Then send me your file with me 🙏
"""
    ABOUT_TEXT = """
🔰 **Bot :** [Cortana Renamer Bot](https://t.me/FileRename_CortanaBot)
🔰 **Developer :** [Master Chief](https://telegram.me/percy_jackson_4)
🔰 **Updates Channel :** [Cortana Updates 🇱🇰](https://telegram.me/Cortana_Updates)
🔰 **Support Group :** [Cortana Support 🇱🇰](https://telegram.me/CortanaBOTS)
🔰 **Language :** [Python3](https://python.org)
🔰 **Library :** [Pyrogram v1.2.0](https://pyrogram.org)
🔰 **Server :** [VPS](https://www.azure.com)
"""

    ABOUT_DEV_TEXT = """
Developer is a Super Noob 😅
You can find him in telegram as @percy_jackson_4
Developer's github account : [Github](https://github.com/PercyOfficial) 🇱🇰
If you find any error on this bot please be kind to tell [Developer](https://t.me/percy_jackson_4) or in our [Support Group](https://telegram.me/CortanaBOTS) 😊
"""
    INFO_TEXT = """
Hey {mention},
Your details are here 😊
🔰 **First Name :** `{first_name}`
🔰 **Last Name  :** `{last_name}`
🔰 **Username   :** @{username}
🔰 **User Id    :** `{user_id}`
"""

    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('😎Devoloper', url='https://t.me/percy_jackson_4'),
        InlineKeyboardButton('Rate us ★', url='https://t.me/tlgrmcbot?start=FileRename_CortanaBot-review')
        ],[
        InlineKeyboardButton('Updates Channel🗣', url='https://telegram.me/Cortana_Updates'),
        InlineKeyboardButton('Support Group 👥', url='https://telegram.me/CortanaBOTS')
        ],[
        InlineKeyboardButton('Help 🆘', callback_data='help')
        ],[
        InlineKeyboardButton('Settings ⚙', callback_data='openSettings')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home 🏠', callback_data='home'),
        InlineKeyboardButton('About ❗️', callback_data='about'),
        InlineKeyboardButton('User Info ❗', callback_data='info')
        ],[
        InlineKeyboardButton('Close ❎', callback_data='closeMeh')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home 🏠', callback_data='home'),
        InlineKeyboardButton('Help 🆘', callback_data='help'),
        InlineKeyboardButton('About Dev 🧑‍💻', callback_data='devabout')
        ],[
        InlineKeyboardButton('Close ❎', callback_data='closeMeh')
        ]]
    )
    INFO_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home 🏠', callback_data='home'),
        InlineKeyboardButton('About ❗️', callback_data='about'),
        InlineKeyboardButton('Help 🆘', callback_data='help')
        ],[
        InlineKeyboardButton('Close ❎', callback_data='closeMeh')
        ]]
    )
    ABOUT_DEV_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home 🏠', callback_data='home'),
        InlineKeyboardButton('Help 🆘', callback_data='help'),
        InlineKeyboardButton('About ❗️', callback_data='about')
        ],[
        InlineKeyboardButton('Close ❎', callback_data='closeMeh')
        ]]
    ) 
