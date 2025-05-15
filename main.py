from pyrogram import Client, filters
from bot.handlers import handle_start, handle_search

app = Client("yt_bot", config_file="bot/config.ini")

@app.on_message(filters.command("start"))
async def start(client, message):
    await handle_start(client, message)

@app.on_message(filters.text & ~filters.command("start"))
async def search(client, message):
    await handle_search(client, message)

app.run()