import asyncio
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message
import time
import re
from bot import Bot
from config import ADMINS, LOG_ID
import requests as ree
from bs4 import BeautifulSoup

#@Bot.on_message(filters.private & filters.command(["start"]))
#async def start_command(client: Client, message: Message):
    #await client.send_message(chat_id = message.chat.id, text = "I am alive 💥")

list1 =[1]
list2=[1]
d=dict()
@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command(["get"]))
async def newepisode(client: Client, message: Message):
    while True:
        print("Searching..??")
        #kannada serials link
        url = ('https://www.zee5.com/tv-shows/collections/before-tv-episodes-zee-kannada/0-8-670')
        response = ree.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the HTML element that contains information about the latest episode
        episode_element = soup.find_all("a", class_="noSelect content", href=True)
                
        for i in episode_element:
            u = "https://www.zee5.com"+str(i['href'])
            r = ree.get(u)
            s = BeautifulSoup(r.content, 'html.parser')
            # Find the HTML element that contains information about the latest episode
            episode_no = s.find("div", class_="metaInfo lineHeightClass")
            episode = str(episode_no.find("p"))
            ep=str(re.findall("E\s\d+",episode)[0])
            d[ep]=u
            list2.append(ep)
        
        #here we check the episode is new or not
        s3=set(list2).difference(set(list1))
        new_list = list(s3)
        for i in new_list:
            list1.append(i)
            a=str(i)
            a = None
            a = await client.send_message(chat_id = 5963138883, text = f"https://www.zee5.com{b}")
            d = await client.send_message(chat_id = 1284476297, text = f"https://www.zee5.com{b}")
            if a and d:
                print('Msg sent successfully to both..!')
            elif a:
                print('Msg sent successfully to Monstar..!')
            elif d:
                print('Msg sent successfully to Nandan..!')
            else:
                print('Msg not sent successfully..!')
            time.sleep(5)
            
        #here we delete the old episode link(premium free)
        duplicate=set(list1).difference(set(list2))
        duplicate_ep=list(duplicate)
        for j in duplicate_ep:
                list1.remove(j)
        time.sleep(20)
        continue
