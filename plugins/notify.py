import asyncio
from pyrogram import filters
from pyrogram import Client as client
from pyrogram.types import Message as message

from bot import Bot
from config import ADMINS
import requests as ree
from bs4 import BeautifulSoup

link1=[1]
listlink=[1]
@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('notify'))
# async def notify(client: Client, message: Message):
#     noti()

while True:
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
            await client.send_message(message.chat.id, f"https://www.zee5.com{b}")
            # print(f"https://www.zee5.com{b}\n\n")
            await asyncio.sleep(3)
            
        #here we delete the old episode link(premium free)
        duplicatelinks = set(link1).difference(set(listlink))
        duplicatelist=list(duplicatelinks)
        for j in duplicatelist:
            link1.remove(j)
        await asyncio.sleep(10)
        # notify(client,message)
        # break
