import asyncio
from pyrogram import filters
from pyrogram import Client as client
from pyrogram.types import Message as message
import time
from bot import Bot
from config import ADMINS, METHOD_MESSAGE
import requests as ree
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from bs4 import BeautifulSoup

link1=[1]
listlink=[1]

LINK_REPLY_MARKUP = InlineKeyboardMarkup(
    [
            InlineKeyboardButton(
                "New Episodes", callback_data="newepisode"
            ),
            InlineKeyboardButton(
                "Stop Searching", callback_data="stopsearch"
            ),
    ]
)
@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command(["link"]))
async def date(bot, message):
    method_name = CallbackQuery.data.split("#")[1]
    REPLY_MARKUP = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Back", callback_data="LINK_REPLY_MARKUP")]]
        )
    s = METHOD_MESSAGE.format(method=method_name)
    return await CallbackQuery.message.edit(s, reply_markup=LINK_REPLY_MARKUP)
        
    await query.message.edit(
            "Method changed successfully",
            reply_markup=REPLY_MARKUP,
        )

@Bot.on_callback_query(filters.regex('newepisode'))
async def newepisode(client: Client, message: Message):
    while True:
        print("Searching..??")
                #kannada serials link
        url = ('https://www.zee5.com/tv-shows/collections/before-tv-episodes-zee-kannada/0-8-670')
        
        response = ree.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
                # Find the HTML element that contains information about the latest episode
        episode_element = soup.find_all("a", class_="noSelect content", href=True)
                
        for l in episode_element:
                if l['href'] not in listlink:
                    listlink.append(l['href'])
                        
                #here we check the episode is new or not
        new_link = set(listlink).difference(set(link1))
        newlist=list(new_link)
        for i in newlist:
                link1.append(i)
                b=str(i)
                a = None
                a = await client.send_message(message.chat.id, f"https://www.zee5.com{b}")
                if a:
                    print('Msg sent successfully..!')
                else:
                    print('Msg not sent successfully..!')
                    # print(f"https://www.zee5.com{b}\n\n")
                time.sleep(3)
            
                #here we delete the old episode link(premium free)
        duplicatelinks = set(link1).difference(set(listlink))
        duplicatelist=list(duplicatelinks)
        for j in duplicatelist:
                link1.remove(j)
        time.sleep(10)
        #await notify(client,message)
        continue
    
@Bot.on_callback_query(filters.regex('stopsearch'))
async def stopsearch():
    pass
        
# @Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
# async def batch(client: Client, message: Message):
#         await client.send_message(chat_id=message.chat.id, text=f"<b>{}</b>")
