from YukkiMusic import app
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions
from YukkiMusic.utils.database import get_client
from YukkiMusic.core.userbot import assistants


spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " **𝐕𝐚𝐧𝐚𝐤𝐚𝐦 𝐝𝐚 𝐦𝐚𝐩𝐥𝐚 𝐞𝐧𝐚 𝐩𝐚𝐧𝐫𝐚🖖** ",
           " **𝐞𝐧𝐚 𝐩𝐚𝐧𝐫𝐚 𝐬𝐚𝐩𝐭𝐢𝐲𝐚😀** ",
           " **𝐮𝐧𝐤𝐢𝐭𝐚 𝐥𝐚 𝐦𝐚𝐧𝐢𝐬𝐡𝐚𝐧 𝐩𝐞𝐬𝐮𝐯𝐚𝐧𝐚🤭** ",
           " **𝐍𝐞 𝐞𝐧𝐚 𝐚𝐯𝐥𝐨 𝐩𝐞𝐫𝐢𝐲𝐚 𝐚𝐚𝐥𝐚😏** ",
           " **𝐑𝐨𝐦𝐛𝐚 𝐩𝐚𝐧𝐚𝐭𝐡𝐚 𝐬𝐚𝐫𝐢𝐲𝐚😒** ",
           " **𝐍𝐚 𝐮𝐧 𝐦𝐞𝐥𝐚 𝐤𝐨𝐯𝐚𝐦𝐚 𝐢𝐫𝐮𝐤𝐚😌** ",
           " **𝐑𝐨𝐦𝐛𝐚 𝐩𝐚𝐧𝐚𝐭𝐡𝐚 𝐬𝐚𝐫𝐢𝐲𝐚😒** ",
           " **𝐧𝐚𝐥𝐥𝐚 𝐬𝐚𝐩𝐭𝐮 𝐬𝐚𝐩𝐭𝐮 𝐭𝐡𝐮𝐧𝐠𝐢𝐭𝐮 𝐢𝐫𝐮𝐤𝐚 𝐩𝐨𝐥𝐚😆** ",
           " **𝐞𝐩𝐚 𝐩𝐚𝐭𝐡𝐚𝐥𝐮 𝐮𝐫𝐮𝐭𝐢𝐭𝐞 𝐢𝐫𝐮 𝐯𝐞𝐫𝐚 𝐯𝐞𝐥𝐚𝐲𝐞 𝐢𝐥𝐚 𝐥𝐚🤦‍♂️** ",
           " **𝐧𝐚𝐥𝐥𝐚 𝐩𝐮𝐝𝐢𝐜𝐡𝐮 𝐯𝐚𝐜𝐡𝐚 𝐩𝐮𝐥𝐥𝐚𝐲𝐚𝐫 𝐦𝐚𝐭𝐡𝐢𝐫𝐢 𝐢𝐫𝐮𝐤𝐚 𝐞𝐩𝐝𝐢👀** ",
           " **𝐞𝐧𝐚𝐤𝐮 𝐞𝐧𝐚𝐦𝐨 𝐮𝐧 𝐦𝐞𝐥𝐚 𝐭𝐡𝐚 𝐬𝐚𝐧𝐭𝐡𝐞𝐠𝐚𝐦 𝐚𝐡 𝐢𝐫𝐮𝐤𝐮🤔** ",
           " **𝐢𝐫𝐮𝐧𝐭𝐡𝐚𝐥𝐮𝐦 𝐮𝐧𝐚𝐤𝐮 𝐢𝐯𝐥𝐨 𝐦𝐨𝐮𝐭𝐡 𝐟𝐚𝐭 𝐢𝐫𝐮𝐤𝐚 𝐤𝐮𝐝𝐚𝐭𝐡𝐮❌** ",
           " **𝐧𝐞 𝐥𝐨𝐨𝐬𝐚 𝐢𝐥𝐚 𝐥𝐨𝐨𝐬𝐮 𝐦𝐚𝐭𝐡𝐢𝐫𝐢 𝐧𝐚𝐝𝐢𝐤𝐮𝐫𝐢𝐲𝐚😂** ",
           " **𝐈 𝐭𝐡𝐢𝐧𝐤 𝐢 𝐡𝐚𝐯𝐞 𝐚 𝐥𝐢𝐭𝐭𝐥𝐞 𝐜𝐫𝐮𝐬𝐡 𝐨𝐧 𝐲𝐨𝐮 🙈** ",
           " **𝐊𝐨𝐥𝐚𝐧𝐭𝐡𝐚 𝐩𝐨𝐢 𝐩𝐚𝐚𝐥 𝐤𝐮𝐝𝐢𝐜𝐡𝐢𝐭𝐮 𝐭𝐡𝐮𝐧𝐠𝐮 𝐩𝐨 🤣** ",
           " **𝐍𝐞 𝐮𝐫𝐮𝐭𝐮 𝐮𝐧 𝐧𝐚𝐥𝐥𝐚 𝐦𝐚𝐧𝐚𝐬𝐮𝐤𝐮 𝐧𝐞𝐞𝐭𝐡𝐚 𝐣𝐞𝐢𝐩𝐚🎲** ",
           " **𝐮𝐧𝐚𝐤𝐮 𝐞𝐧 𝐦𝐞𝐥𝐚 𝐩𝐚𝐬𝐚𝐦𝐞 𝐢𝐥𝐚🤧** ",
           " **𝐍𝐚 𝐮𝐧𝐚𝐤𝐮 𝐟𝐫𝐢𝐞𝐧𝐝 𝐚𝐡 𝐤𝐞𝐝𝐚𝐢𝐤𝐚 𝐧𝐞 𝐤𝐮𝐝𝐮𝐭𝐡𝐮 𝐯𝐚𝐜𝐡𝐢𝐫𝐮𝐤𝐚𝐧𝐮🥱** ",
           " **𝐞𝐧𝐤𝐮𝐝𝐚 𝐩𝐞𝐬𝐚 𝐦𝐚𝐭𝐢𝐲𝐚😞** ",
           " **𝐞𝐧𝐚 𝐬𝐞𝐞𝐧𝐝𝐢 𝐩𝐚𝐤𝐚𝐭𝐡𝐚 😈** ",
           " **𝐧𝐞 𝐞𝐧𝐚 𝐩𝐮𝐥𝐢𝐲𝐚 😄** ",
           " **𝐄𝐧 𝐞𝐞𝐞𝐞 𝐧𝐮 𝐩𝐚𝐥𝐥𝐚 𝐩𝐚𝐥𝐥𝐚 𝐤𝐚𝐭𝐮𝐫𝐚💦** ",
           " **𝐒𝐮𝐦𝐚𝐯𝐞 𝐢𝐫𝐮𝐤𝐚 𝐦𝐚𝐭𝐢𝐲𝐚 🙄** ",
           " **𝐀𝐚𝐦𝐚 𝐲𝐚𝐫 𝐧𝐞🤔** ",
           " **𝐲𝐨𝐮 𝐛𝐮𝐟𝐟𝐚𝐥𝐨 🐃** ",
           " **𝐩𝐚𝐞😏** ",
           " **𝐮𝐧𝐤𝐮𝐝𝐚 𝐧𝐚 𝐝𝐨𝐨 🤞** ",
           " **𝐮𝐧𝐚 𝐓𝐡𝐢𝐫𝐮𝐭𝐡𝐚𝐯𝐞 𝐦𝐮𝐝𝐢𝐲𝐚𝐭𝐡𝐮 🤦‍♂️💦** ",
           " **𝐧𝐚𝐦𝐦𝐚 𝐫𝐞𝐧𝐝𝐮 𝐩𝐞𝐫𝐮𝐦 𝐠𝐨𝐨𝐝 𝐜𝐨𝐮𝐩𝐥𝐞𝐬 🙈🙊** ",
           " **𝐢𝐭𝐡𝐮 𝐨𝐫𝐮 𝐩𝐚𝐢𝐭𝐡𝐢𝐲𝐚𝐦 🤦‍♂️** ",
           " **ai naughty 😆** ",
           " **thungitiya 🙄** ",
           " **amma kita soliruva 😒** ",
           " **sumave iruka matiya 🤧** ",
           " **aala vidu saami🙏** ",
           " **ada kiruku paya bulla🤪** ",
           " **en owner kita solata 📞** ",
           " **ne commited thana 😞** ",
           " **sarah hert broken 💔** ",
           " **una vita yaru iruka enkau 😥** ",
           " **telegram la tha unaku saavu 🤣** ",
           " **na nalla padunana ☺️** ",
           " **ithuku tha oorukula oru aal in all azhagurani venu solrathu 🙈** ",
           " **aiyo keela vilinthuta ambulance kupdu ga🚑 ** ",
           " **nuts podatha 😒** ",
           " **daily pallu valaka theva brush uh neetha en crush uh 🙊** ",
           " **ungaluku kaal valikalaya neenga en head la odite irukinga👀** ",
           " **po po poi un aalu kuda chat panu po🤞** ",
           " **un kanu ena gun mathiri shoot panuthu🔫** ",
           " **road la iruku pallam neetha en chellam🙊** ",
           " **en kolusin satham un uthadil tharum mutham💋** ",
           " **aalum mandaium paaru💦** ",
           " **rasa rasa una vachiruka nenjula✨😆** ",
           " **uthu pakatha mama vekama iruku 🙈** ",
           " **ambulance ku call panunga unga kanu ena koluthu🙊** ",
           " **boom boom maadu un vaya knjm moodu🗣️** ",
           " **pata pagaliley panguni veililey enai parthu sirikum nila🌙** ",
           " **yara namburathuney therila das anna😌** ",
           " **Do you have any map a way to enter into your heart i just lost 👉👈** ",
           " **azhagiya laila athu enoda styla😝** ",
           " **nane oru kolantha 🥺** ",
           " **ena pathu solu en kanna pathu solu👀** ",
           " **poya po 👋** ",
           " **avlothana apdiye  4 vartha mudincha oru cup coffee ☕** ",
           " **ivlo gunda iruka🤭😂** ",
           " **congratulations kilambungal👋** ",
           " **avasara patutiyae kumaru🥱** ",
           " **singam single ah tha iruku 👨‍👦** ",
           " **ithu namma list laye ilaye 🤣** ",
           " **ena ranga niyama ithu🤨** ",
           " **helo police station please arrest this beauty always killing me😚** ",
           " **enathayavathu olaritu iru 🤣** ",
           " **ada mala Korangu🐒** ",
           " **cringe uh cringe uh 💦** ",
           " **shaving pana karadi mathiri oru munji🐻** ",
           " **ithoda 1254avathu urutu🎲** ",
           " **chapu chapu nu aranjiduva🤨** ",
           " **onu solrathuku ila🤞** ",
           " **hey epudraaa😱** ",
           " **solita la kelambu 😴** ",
           " **aii avlotha unaku mariyatha 😌** ",
           " **paaarah😝** ",
           " **ne puli ila mookula vara sali💦** ", 
           " **time illa😌😴** ",
           " **ena ena solra parunga 😂** ",
           " **Sarah pavom 🥺** ",
           " **love you by sarah👉👈** ",
         ]

@app.on_message(filters.command(["tagme"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == "private":
        return await message.reply("This command can be used in groups and channels!")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in ("administrator", "creator"):
            is_admin = True
    if not is_admin:
        return await message.reply("**ᴏɴʟʏ ᴀᴅᴍɪɴ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ!**")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall hello 👈** ᴛʀʏ ᴛʜɪs ɴᴇxᴛ ᴛɪᴍᴇ ғᴏʀ ᴛᴀɢɢɪɴɢ...*")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall hii 👈 **ᴛʀʏ ᴛʜɪs ᴏʀ ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ...**")
    else:
        return await message.reply("/tagall hii 👈 **ᴛʀʏ ᴛʜɪs ᴏʀ ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ...**")

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                for num in assistants:
                      app = await get_client(num)
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await app.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["cancel", "stop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("**ɴᴏ ᴀᴄᴛɪᴠᴇ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss ɪs sᴛᴀʀᴛᴇᴅ ʙʏ ᴍᴇ...**")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in ("administrator", "creator"):
            is_admin = True
    if not is_admin:
        return await message.reply("**ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs. ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ...**")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("**ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss sᴛᴏᴘᴘᴇᴅ**")
