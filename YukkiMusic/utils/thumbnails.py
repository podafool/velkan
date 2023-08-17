import os
import re
import textwrap
import random
import asyncio

import aiofiles
import aiohttp
import numpy as np

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
import PIL
from youtubesearchpython.__future__ import VideosSearch

from config import YOUTUBE_IMG_URL, MUSIC_BOT_NAME
from YukkiMusic import app

BACKGROUND = [
    "https://telegra.ph/file/66969e848effd83d95c87.jpg",
    "https://telegra.ph/file/9f3b78e7c34b39b2d7bb4.jpg",
]

def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))    
    return newImage


def add_corners(im):
    bigsize = (im.size[0] * 5, im.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    size = [(0,100), bigsize]
    ImageDraw.Draw(mask).rectangle(size, fill=255)
    mask = mask.resize(im.size, Image.LANCZOS)
    mask = ImageChops.darker(mask, im.split()[-1])
    im.putalpha(mask)


#@asyncio.coroutine
async def gen_thumb(videoid, user_id):
    if os.path.isfile(f"cache/{videoid}_{user_id}.png"):
        return f"cache/{videoid}_{user_id}.png"
    url = f"https://www.youtube.com/watch?v={videoid}"
    #event_loop = asyncio.get_event_loop()
    try:
        results = VideosSearch(url, limit=1)
        #results = asyncio.coroutine(VideosSearch(url, limit=1))
        #for result in (await results.next())["result"]:        
        #async for result in event_loop.run_until_complete(VideosSearch(url, limit=1)):
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                views = result["viewCount"]["short"]
            except:
                views = "Unknown Views"
            try:
                channel = result["channel"]["name"]
            except:
                channel = "Unknown Channel"
                
        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/thumb{videoid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        try:
            wxyz = await app.get_chat_photos(user_id)
            wxy = await app.download_media(wxyz[0]['file_id'], file_name=f'{user_id}.jpg')
        except:
            hehe = await app.get_chat_photos(app.id)
            wxy = await app.download_media(hehe[0]['file_id'], file_name=f'{app.id}.jpg')
        xy = Image.open(wxy)
        a = Image.new('L', [640, 640], 0)
        b = ImageDraw.Draw(a)
        b.pieslice([(0, 0), (640,640)], 0, 360, fill = 255, outline = "white")                
        c = np.array(xy)
        d = np.array(a)
        e = np.dstack((c, d))
        f = Image.fromarray(e)
        x = f.resize((245, 245))        
        
        youtube = Image.open(f"cache/thumb{videoid}.png")        
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        #background = image2.filter(filter=ImageFilter.BoxBlur(30))
        enhancer = ImageEnhance.Brightness(image2)
        background = enhancer.enhance(1)

        bg = Image.open(f"assets/rose2.png")
        #bg = random.choice(BACKGROUND)
        image3 = changeImageSize(1280, 720, bg)
        image5 = image3.convert("RGBA")
        Image.alpha_composite(background, image5).save(f"cache/temp{videoid}.png")

        Xcenter = youtube.width / 2
        Ycenter = youtube.height / 2
        x1 = Xcenter - 640
        y1 = Ycenter - 725
        x2 = Xcenter + 640
        y2 = Ycenter + 555
        logo = youtube.crop((x1, y1, x2, y2))
        logo.thumbnail((342, 342), Image.LANCZOS)
        logo.save(f"cache/chop{videoid}.png")
        if not os.path.isfile(f"cache/cropped{videoid}.png"):
            im = Image.open(f"cache/chop{videoid}.png").convert("RGBA")
            add_corners(im)
            im.save(f"cache/cropped{videoid}.png")

        crop_img = Image.open(f"cache/cropped{videoid}.png")
        logo = crop_img.convert("RGBA")
        logo.thumbnail((400, 400), Image.LANCZOS)
        #logo = ImageOps.expand(logo, border=10, fill="orange")
        background = Image.open(f"cache/temp{videoid}.png")
        background.paste(logo, (110, 265), mask=logo)
        background.paste(x, (947, 118), mask=x)        

        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("assets/Hungline.ttf", 45)
        font2 = ImageFont.truetype("assets/Hawaii.otf", 150)
        arial = ImageFont.truetype("assets/font2.ttf", 30)
        name_font = ImageFont.truetype("assets/font2.ttf", 30)
        para = textwrap.wrap(title, width=32)
        j = 0
        draw.text(
            (950, 650), 
            f"with {MUSIC_BOT_NAME}", 
            fill="black",
            stroke_width=1,
            stroke_fill="yellow", 
            font=name_font
        )
        draw.text(
            (640, 370),
            "Enjoyie",
            fill="white",
            stroke_width=2,
            stroke_fill="black",
            font=font2,
        )
        draw.text(
            (895, 445),
            "the",
            fill="white",
            stroke_width=2,
            stroke_fill="black",
            font=font2,
        )
        draw.text(
            (1015, 475),
            "song!",
            fill="white",
            stroke_width=2,
            stroke_fill="black",
            font=font2,
        )
        for line in para:
            if j == 1:
                j += 1
                draw.text(
                    (100, 75),
                    f"{line}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="blue",
                    font=font,
                )
            if j == 0:
                j += 1
                draw.text(
                    (150, 115),
                    f"{line}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="blue",
                    font=font,
                )
        
        try:
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass
        background.save(f"cache/{videoid}_{user_id}.png")
        return f"cache/{videoid}_{user_id}.png"
    except Exception as e:
        print(e)
        return (YOUTUBE_IMG_URL)
