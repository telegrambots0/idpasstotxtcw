import requests
import json
import subprocess
from pyrogram.types.messages_and_media import message
import helper
from pyromod import listen
from pyrogram.types import Message
import tgcrypto
import pyrogram
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
import time
from pyrogram.types import User, Message
from p_bar import progress_bar
from subprocess import getstatusoutput
import logging
import os
import sys
import re
import cloudscraper
from bs4 import BeautifulSoup

load_dotenv()
os.makedirs("./downloads", exist_ok=True)

bot = Client(
    "CW",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

logger = logging.getLogger()
# thumb = os.environ.get("THUMB")
# if thumb.startswith("http://") or thumb.startswith("https://"):
#     getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
#     thumb = "thumb.jpg"

@bot.on_message(filters.command(["start"]))
async def start(bot, update):
       await update.reply_text("Hi i am **ℂ𝕒𝕣𝕖𝕖𝕣𝕨𝕚𝕝𝕝 𝔻𝕠𝕨𝕟𝕝𝕠𝕒𝕕𝕖𝕣**.\n\n"
                              "**NOW:-** "
                                       
                              "Press **/login** to continue..\n\n"
                                     
                              "Hello im txt file downloader\nPress /pyro to download links listed in a txt file in the format **Name:link**\n\n"
                              "Bot made by **『 🅰🅸🆁 🅿🅷🅴🅾🅽🅸🆇™ 』**")
        

ACCOUNT_ID = "6206459123001"
BCOV_POLICY = "BCpkADawqM1474MvKwYlMRZNBPoqkJY-UWm7zE1U769d5r5kqTjG0v8L-THXuVZtdIQJpfMPB37L_VJQxTKeNeLO2Eac_yMywEgyV9GjFDQ2LTiT4FEiHhKAUvdbx9ku6fGnQKSMB8J5uIDd"
bc_url = (
    f"https://edge.api.brightcove.com/playback/v1/accounts/{ACCOUNT_ID}/videos"
)
bc_hdr = {"BCOV-POLICY": BCOV_POLICY}

@bot.on_message(filters.command(["login"]))
async def account_login(bot: Client, m: Message):
    input1 = await app.ask(message.chat.id, text="**Send ID & Password in this manner otherwise bot will not respond.\n\nSend like this:-  ID*Password\n\n OR Send Your Token**")
        login_url = "https://elearn.crwilladmin.com/api/v3/login-other"
        raw_text = input1.text
        if "*" in raw_text:
            headers = {
                "Host": "elearn.crwilladmin.com",
                "origintype": "web",
                "accept": "application/json",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.9.1"
            }

            email, password = raw_text.split("*")
            data = {
                "deviceType": "web",
                "password": password,
                "deviceModel": "chrome",
                "deviceVersion": "Chrome+119",
                "email": email
            }

            response = requests.post(login_url, headers=headers, json=data)
            response.raise_for_status()  # Raise an error if the request was unsuccessful
            token = response.json()["data"]["token"]
            await message.reply_text(f"**Login Successful**\n\n`{token}`")
        else:
            token = raw_text
    except Exception as e:
        await message.reply_text(f"An error occurred during login: {e}")
        return

    headers = {
        "Host": "elearn.crwilladmin.com",
        "origintype": "web",
        "usertype": "2",
        "token": token,
        "accept-encoding": "gzip",
        "user-agent": "okhttp/3.9.1"
    }

    await input1.delete(True)
    batch_url = "https://elearn.crwilladmin.com/api/v3/my-batch"
    response = requests.get(batch_url, headers=headers)
    data = response.json()
    topicid = data["data"]["batchData"]

    FFF = "**BATCH-ID     -     BATCH NAME**\n\n"
    for data in topicid:
        FFF += f"`{data['id']}`     -    **{data['batchName']}**\n\n"

    await message.reply_text(f"**HERE IS YOUR BATCH**\n\n{FFF}")
    input2 = await app.ask(message.chat.id, text="**Now send the Batch ID to Download**")
    raw_text2 = input2.text
    topic_url = "https://elearn.crwilladmin.com/api/v3/batch-topic/" + raw_text2 + "?type=class"
    response = requests.get(topic_url, headers=headers)
    topic_data = response.json()
    batch_data = topic_data['data']['batch_topic']
    name = topic_data["data"]["batch_detail"]["name"]

    BBB = "**TOPIC-ID - TOPIC**\n\n"
    id_num = ""
    for data in batch_data:
        topic_id = data["id"]
        topic_name = data["topicName"]
        id_num += f"{topic_id}&"
        BBB += f"`{topic_id}` -  **{topic_name}** \n\n"

    await message.reply_text(f"**Batches details of {name}**\n\n{BBB}")
    input3 = await app.ask(message.chat.id, text=f"Now send the **Topic IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n`{id_num}`")
    raw_text3 = input3.text
    
    editable3= await m.reply_text("**Now send the Resolution**")
    input4 = message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text
    
    editable7= await m.reply_text("**Enter the Title : **")
    input7 = message = await bot.listen(editable.chat.id)
    raw_te = input7.text

    editable4= await m.reply_text("Now send the **Thumb url** Eg : ```https://telegra.ph/file/d9e24878bd4aba05049a1.jpg```\n\nor Send **no**")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    
    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"
    
#     editable9= await m.reply_text(f"Now send the **Topic Names**\n\nSend like this **1&2&3&4** and so on\nor copy paste or edit **below names according to you in Order of ids you entered above** :\n\n**Enter this to download full batch :-**\n```{vp}```")
    
#     input9 = message = await bot.listen(editable.chat.id)
#     raw_text9 = input9.text
  
    try:
        xv = raw_text3.split('&')
        for y in range(0,len(xv)):
            t =xv[y]
        
#              xvv = raw_text9.split('&')
#              for z in range(0,len(xvv)):
#                  p =xvv[z]
        
        
            #gettting all json with diffrent topic id https://elearn.crwilladmin.com/api/v1/comp/batch-detail/881?redirectBy=mybatch&topicId=2324&token=d76fce74c161a264cf66b972fd0bc820992fe57
            scraper = cloudscraper.create_scraper()
            html4 = scraper.get("https://elearn.crwilladmin.com/api/v1/comp/batch-detail/"+raw_text2+"?redirectBy=mybatch&topicId="+t+"&token="+token).content
            ff = json.loads(html4)
            #vc =ff.json()["data"]["class_list"]["batchDescription"]
            mm = ff["data"]["class_list"]["batchName"]   
            vv =ff["data"]["class_list"]["classes"]
            vv.reverse()
            #clan =f"**{vc}**\n\nNo of links found in topic-id {raw_text3} are **{len(vv)}**"
            #await m.reply_text(clan)
            count = 1
            try:
                for data in vv:
                    vidid = (data["id"])
                    lessonName = (data["lessonName"]).replace("/", "_")
                    
                    bcvid = (data["lessonUrl"][0]["link"])
                     #lessonName = re.sub('\|', '_', cf)

                    if bcvid.startswith("62"):
                        try:
                            scraper = cloudscraper.create_scraper()
                            html6 = scraper.get(f"{bc_url}/{bcvid}", headers=bc_hdr).content
                            video = json.loads(html6)
                            video_source = video["sources"][5]
                            video_url = video_source["src"]
                            #print(video_url)
                            scraper = cloudscraper.create_scraper()
                            html5 = scraper.get("https://elearn.crwilladmin.com/api/v1/livestreamToken?type=brightcove&vid="+vidid+"&token="+token).content
                            surl = json.loads(html5)
                            stoken = surl["data"]["token"]
                            #print(stoken)
                            
                            link = video_url+"&bcov_auth="+stoken
                            #print(link)
                        except Exception as e:
                            print(str(e))
                            
                    elif bcvid.startswith("63"):
                        try:
                            scraper = cloudscraper.create_scraper()
                            html7 = scraper.get(f"{bc_url}/{bcvid}", headers=bc_hdr).content
                            video1 = json.loads(html7)
                            video_source1 = video1["sources"][5]
                            video_url1 = video_source1["src"]
                            #print(video_url)
                            scraper = cloudscraper.create_scraper()
                            html8 = scraper.get("https://elearn.crwilladmin.com/api/v1/livestreamToken?type=brightcove&vid="+vidid+"&token="+token).content
                            surl1 = json.loads(html8)
                            stoken1 = surl1["data"]["token"]
                            #print(stoken)
                            
                            link = video_url1+"&bcov_auth="+stoken1
                            #print(link)
                        except Exception as e:
                            print(str(e))
                    else:
                        link="https://www.youtube.com/embed/"+bcvid
                        
                    #raw_text4 = 480

                    cc = f"**{count}) Title :** {lessonName}\n\n**Quality :** {raw_text4}\n**Batch :** {mm}\n**𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗱 𝗕𝘆 :** {raw_te}\n**𝗕𝗼𝘁 𝗢𝘄𝗻𝗲𝗿 : 🅢🅐🅚🅢🅗🅐🅜™"
                    Show = f"**Downloading:-**\n**Title -** ```{lessonName}\n\nQuality - {raw_text4}```\n\n**Url :-** ```{link}```"
                    prog = await m.reply_text(Show)

                    if "youtu" in link:
                        if raw_text4 in ["144", "240", "480"]:
                            ytf = f'bestvideo[height<={raw_text4}][ext=mp4]+bestaudio[ext=m4a]'
                        elif raw_text4 == "360":
                            ytf = 18
                        elif raw_text4 == "720":
                            ytf = 22
                        else:
                            ytf = 18
                    else:
                        ytf=f"bestvideo[height<={raw_text4}]"
                        
                    if ytf == f'bestvideo[height<={raw_text4}][ext=mp4]+bestaudio[ext=m4a]':
                        cmd = f'yt-dlp -o "{lessonName}.mp4" -f "{ytf}" "{link}"'
                    else:
                        cmd = f'yt-dlp -o "{lessonName}.mp4" -f "{ytf}+bestaudio" "{link}"'


                    #cmd = f'yt-dlp -o "{lessonName}.mp4" -f "{ytf}+bestaudio" "{link}"'
                    try:
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
                        os.system(download_cmd)
                        

                        filename = f"{lessonName}.mp4"
                        #await prog.delete (True)
#                         reply = await m.reply_text("Uploading Video")
                        subprocess.run(f'ffmpeg -i "{filename}" -ss 00:00:19 -y -vframes 1 "{filename}.jpg"', shell=True)
    
                        thumbnail = f"{filename}.jpg"
                        await prog.delete (True)
                        reply = await m.reply_text("Uploading Video")         

                        try:
                            if thumb == "no":
                                thumbnail = f"{filename}.jpg"
                            else:
                                thumbnail = thumb
                        except Exception as e:
                            await m.reply_text(str(e))

                        dur = int(helper.duration(filename))
#                         await prog.delete (True)
                        start_time = time.time()
                        await m.reply_video(f"{lessonName}.mp4",caption=cc, supports_streaming=True,height=720,width=1280,thumb=thumbnail,duration=dur, progress=progress_bar,progress_args=(reply,start_time))
                        count+=1
                        os.remove(f"{lessonName}.mp4")   
                        os.remove(f"{filename}.jpg")
                        await reply.delete (True)
                    except Exception as e:
                        await m.reply_text(f"**Video downloading failed ❌**\n{str(e)}\n**Name** - {lessonName}\n**Link** - `{link}`")
                        continue
            except Exception as e:
                await m.reply_text(str(e))
            
    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("Done")
    
    try:
        notex = await m.reply_text("Do you want download notes ?\n\nSend **y** or **n**")
        input5:message = await bot.listen (editable.chat.id)
        raw_text5 = input5.text
        if raw_text5 == 'y':
            scraper = cloudscraper.create_scraper()
            html7 = scraper.get("https://elearn.crwilladmin.com/api/v1/comp/batch-notes/"+raw_text2+"?topicid="+raw_text2+"&token="+token).content
            pdfD=json.loads(html7)
            k=pdfD["data"]["notesDetails"]
            bb = len(pdfD["data"]["notesDetails"])
            ss = f"Total PDFs Found in Batch id **{raw_text2}** is - **{bb}** "
            await m.reply_text(ss)
            k.reverse()
            count1 = 1
            try:
                
                for data in k:
                    name=(data["docTitle"])
                    s=(data["docUrl"]) 
                    xi =(data["publishedAt"])
                 
                    
                    ww = f"**{count1}) File Name :- **{name}\n**Date : **{xi}\n{bn}"
                    show2 = f'**Downloading :-**\n\n**Link :** ```{s}```'
                    prog2 = await m.reply_text(show2)
                    cmd2=f'yt-dlp -o "{name}.pdf" "{s}"'
                    try:
                        download_cmd2 = f"{cmd2} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
                        os.system(download_cmd2)
                        await m.reply_document(f'{name}.pdf', caption=ww)

                        count1+=1
                        await prog2.delete (True)
                        os.remove(f'{name}.pdf')
                        time.sleep(2)
                        
                    except Exception as e:
                        await m.reply_text(f"**PDF downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{s}`")
                        continue
            except Exception as e:
                await m.reply_text(str(e))
            #await m.reply_text("Done")
    except Exception as e:
        print(str(e))
    await m.reply_text("Done")
    
@bot.on_message(filters.command(["cancel"]))
async def cancel(_, m):
    editable = await m.reply_text("Canceling All process Plz wait")
    global cancel
    cancel = True
    await editable.edit("cancled")
    return
@bot.on_message(filters.command("restart"))
async def restart_handler(_, m):
    await m.reply_text("Restarted!", True)
    os.execl(sys.executable, sys.executable, *sys.argv)
bot.run()
