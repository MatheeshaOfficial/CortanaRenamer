from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
Hello {} π
I'm Cortana Song Downloader Bot π±π°
You can rename any file with custom thumnails and custom captionπ
press /settings costomized me
If you want to know how to use me just
touch on " Help π "  Button π
"""    
    HELP_TEXT = """
Hello {}π
You should know following instructions to rename your files π
You can download song by,
π°Fist press βSetting button 
π©βπ§Then customized me π€
π° Then send me your file with me π
"""
    ABOUT_TEXT = """
π° **Bot :** [Cortana Renamer Bot](https://t.me/FileRename_CortanaBot)
π° **Developer :** [Master Chief](https://telegram.me/percy_jackson_4)
π° **Updates Channel :** [Cortana Updates π±π°](https://telegram.me/Cortana_Updates)
π° **Support Group :** [Cortana Support π±π°](https://telegram.me/CortanaBOTS)
π° **Language :** [Python3](https://python.org)
π° **Library :** [Pyrogram v1.2.0](https://pyrogram.org)
π° **Server :** [VPS](https://www.azure.com)
"""

    ABOUT_DEV_TEXT = """
Developer is a Super Noob π
You can find him in telegram as @percy_jackson_4
Developer's github account : [Github](https://github.com/PercyOfficial) π±π°
If you find any error on this bot please be kind to tell [Developer](https://t.me/percy_jackson_4) or in our [Support Group](https://telegram.me/CortanaBOTS) π
"""
    INFO_TEXT = """
Hey {mention},
Your details are here π
π° **First Name :** `{first_name}`
π° **Last Name  :** `{last_name}`
π° **Username   :** @{username}
π° **User Id    :** `{user_id}`
"""

    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('πDevoloper', url='https://t.me/percy_jackson_4'),
        InlineKeyboardButton('Rate us β', url='https://t.me/tlgrmcbot?start=FileRename_CortanaBot-review')
        ],[
        InlineKeyboardButton('Updates Channelπ£', url='https://telegram.me/Cortana_Updates'),
        InlineKeyboardButton('Support Group π₯', url='https://telegram.me/CortanaBOTS')
        ],[
        InlineKeyboardButton('Help π', callback_data='help')
        ],[
        InlineKeyboardButton('Settings β', callback_data='openSettings')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home π ', callback_data='home'),
        InlineKeyboardButton('About βοΈ', callback_data='about'),
        InlineKeyboardButton('User Info β', callback_data='info')
        ],[
        InlineKeyboardButton('Close β', callback_data='closeMeh')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home π ', callback_data='home'),
        InlineKeyboardButton('Help π', callback_data='help'),
        InlineKeyboardButton('About Dev π§βπ»', callback_data='masterchief')
        ],[
        InlineKeyboardButton('Close β', callback_data='closeMeh')
        ]]
    )
    INFO_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home π ', callback_data='home'),
        InlineKeyboardButton('About βοΈ', callback_data='about'),
        InlineKeyboardButton('Help π', callback_data='help')
        ],[
        InlineKeyboardButton('Close β', callback_data='closeMeh')
        ]]
    )
    ABOUT_DEV_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home π ', callback_data='home'),
        InlineKeyboardButton('Help π', callback_data='help'),
        InlineKeyboardButton('About βοΈ', callback_data='about')
        ],[
        InlineKeyboardButton('Close β', callback_data='closeMeh')
        ]]
    ) 
