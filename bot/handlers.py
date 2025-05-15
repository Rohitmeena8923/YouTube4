from pyrogram.types import Message
from bot.youtube_search import search_youtube
from bot.downloader import download_and_upload

async def handle_start(client, message: Message):
    await message.reply_text("Send a YouTube video title to search and download.")

async def handle_search(client, message: Message):
    query = message.text
    results = search_youtube(query)
    if not results:
        return await message.reply("No results found.")

    for video in results[:5]:  # Send top 5 with buttons
        await download_and_upload(client, message.chat.id, video["url"])