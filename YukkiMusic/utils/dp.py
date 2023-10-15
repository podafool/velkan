import aiohttp
import aiofiles
from YukkiMusic import app


async for aiohttp.ClientSession() as session:
    async with session.get(thumbnail) as resp:
        if resp.status == 200:
            f = await aiofiles.open(f"cache/thumb{videoid}.png", mode="wb")
            await f.write(await resp.read())
            await f.close()

try:
    wxyz = await app.get_profile_photos(user_id)
    wxy = await app.download_media(wxyz[0]['file_id'], file_name=f'{user_id}.jpg')
except:
    hehe = await app.get_profile_photos(app.id)
    wxy = await app.download_media(hehe[0]['file_id'], file_name=f'{app.id}.jpg')
xy = Image.open(wxy)
a = Image.new('L', [640, 640], 0)
b = ImageDraw.Draw(a)
b.pieslice([(0, 0), (640,640)], 0, 360, fill = 255, outline = "white")                
c = np.array(xy)
d = np.array(a)
e = np.dstack((c, d))
f = Image.fromarray(e)
dps = f.resize((245, 245))

