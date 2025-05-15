import os
from pytube import YouTube

async def download_and_upload(client, chat_id, url):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    file_path = stream.download()

    await client.send_video(chat_id, video=file_path, caption=yt.title)
    os.remove(file_path)