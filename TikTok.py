
from hikka import loader, utils
import requests
import random

@loader.tds
class TikTokModule(loader.Module):
    """TikTok Module"""
    strings = {"name": "TikTok"}

    def init(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "rapidapi_key",
                "a3b05d1879msh88bd3696e0fe7a6p128732jsnc894bc813ce8",
                lambda: "API ключ для доступа к RapidAPI"
            ),
        )

    async def api_call(self, method, endpoint, headers=None, params=None):
        """Метод для выполнения запроса к API"""
        url = f"https://tiktok-apis.p.rapidapi.com/{endpoint}"
        if headers is None:
            headers = {
                "X-RapidAPI-Key": self.config["rapidapi_key"],
                "X-RapidAPI-Host": "tiktok-apis.p.rapidapi.com"
            }

        try:
            response = requests.request(method, url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    async def randomtiktokcmd(self, message):
        """Команда для получения случайного видео из TikTok"""
        result = await self.api_call("GET", "trending")

        if "error" in result:
            await message.reply(f"Ошибка: {result['error']}")
            return

        if not result.get("videos"):
            await message.reply("Не удалось найти видео.")
            return

        video = random.choice(result["videos"])
        video_url = video.get("video_url")

        if video_url:
            await message.reply(f"Случайное видео из TikTok: {video_url}")
        else:
            await message.reply("Не удалось получить URL видео.")

