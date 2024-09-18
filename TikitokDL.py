__version__ = (1, 0, 1)
# meta developer: @musiczhara0
# for more info: https://raw.githubusercontent.com/musiczhara0/sosat/main/TikitokDL.py
from tiktok_downloader import snaptik
import tempfile
import os

from .. import loader, utils


@loader.tds
class TikiTokDLMod(loader.Module):
    """Модуль для скачивания видео из Tik Tok"""

    strings = {
        "name": "TikitokDL",
        "args_no": "❌ Specify the TikTok video link",
        "download": "⬇️ Downloading video...",
        "done": "🎥 Here is your TikTok video",
        "error": "❌ Error downloading video: {str(e)}",
    }

    strings_ru = {
        "args_no": "❌‼️Ты не указал ссылку на видос‼️",
        "download": "⏳",
        "done": "🎥 Видос готов 📺",
        "error": "❌‼️Случилась ошибка при скачивании видео: {}",
    }

    async def tikicmd(self, message):
        """- Вставьте ссылку для скачивания видео"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("args_no"))
            return

        await utils.answer(message, self.strings("download"))

        try:
            get_video = snaptik(f"{args}")
            get_video_list = list(get_video)

            with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as temp_file:
                get_video_list[0].download(temp_file.name)
                temp_file_path = temp_file.name

            with open(temp_file_path, "rb") as video:
                await message.client.send_file(
                    message.to_id, video, caption=self.strings("done")
                )

            os.remove(temp_file_path)
            await message.delete()

        except Exception as e:
            await utils.answer(message, self.strings("error").format(e))
