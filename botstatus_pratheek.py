from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

app = Client(
    name = "botstatus_pratheek",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_string = os.environ["SESSION_STRING"]
)
TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]
async def main_pratheek():
    async with app:
            while True:
                print("Checking...")
                GET_CHANNEL_OR_GROUP = await app.get_chat(int(CHANNEL_OR_GROUP_ID))
                CHANNEL_OR_GROUP_NAME = GET_CHANNEL_OR_GROUP.title
                CHANNEL_OR_GROUP_TYPE = GET_CHANNEL_OR_GROUP.type
                xxx_pratheek = f"📊 𝙇𝙄𝙑𝙀 𝘽𝙊𝙏 𝙎𝙏𝘼𝙏𝙐𝙎\n\n**💬 {CHANNEL_OR_GROUP_TYPE}**: {CHANNEL_OR_GROUP_NAME}"
                for bot in BOT_LIST:
                    try:
                        yyy_pratheek = await app.send_message(bot, "/start")
                        aaa = yyy_pratheek.id
                        await asyncio.sleep(10)
                        zzz_pratheek = app.get_chat_history(bot, limit = 1)
                        async for ccc in zzz_pratheek:
                            bbb = ccc.id
                        if aaa == bbb:
                            xxx_pratheek += f"\n\n🤖 **BOT**: @{bot}\n🔴 **STATUS**: down ❌"
                            async for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"🚨 **Beep! Beep!! @{bot} is down** ❌")
                                except Exception:
                                    pass
                            await app.read_chat_history(bot)
                        else:
                            xxx_pratheek += f"\n\n🤖 **BOT**: @{bot}\n🟢 **STATUS**: alive ✅"
                            await app.read_chat_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                xxx_pratheek += f"\n\n✔️ Last checked on: {last_update} ({TIME_ZONE})\n\n<i>♻️ Updates every 45min - [Powered by Bot Status Checker](https://github.com/PratheekXD/Bot_Status_Checker)</i>"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_pratheek)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(6300)
                        
app.run(main_pratheek())
