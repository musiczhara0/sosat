__version__ = (1, 0, 0)
# meta developer: @musiczhara0

import aiohttp
import tempfile
import os

from .. import loader, utils

@loader.tds
class TikitokDLMod(loader.Module):
    """Модуль для скачивания видео из Tik Tok"""

    strings = {
        "name": "TikitokDL",
        "args_no": "❌ Specify the TikTok video link",
        "download": "⬇️ Downloading video...",
        "done": "🎥 Here is your TikTok video",
        "error": "❌ Error downloading video: {}",
    }

    strings_ru = {
        "args_no": "❌ Укажите ссылку на видео TikTok",
        "download": "⬇️ Загрузка видео...",
        "done": "🎥 Ваше видео с TikTok",
        "error": "❌ Ошибка при скачивании видео: {}",
    }

    async def tikicmd(self, message):
        """Скачивает видео с TikTok по ссылке"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("args_no"))
            return

        await utils.answer(message, self.strings("download"))

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://api.onlysq.ru/tiktok/v1?url={args}") as response:
                    response.raise_for_status()
                    video_data = await response.read()

                    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as temp_file:
                        temp_file.write(video_data)
                        temp_file_path = temp_file.name

                    with open(temp_file_path, "rb") as video:
                        await message.client.send_file(message.to_id, video, caption=self.strings("done"))

                    os.remove(temp_file_path)
                    await message.delete()

        except Exception as e:
            await utils.answer(message, self.strings("error").format(e))
