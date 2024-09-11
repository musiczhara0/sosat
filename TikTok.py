# -*- coding: utf-8 -*-

from hikka import loader, utils
import http.client
import json

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

    async def api_call(self, endpoint):
        """Метод для выполнения запроса к API"""
        conn = http.client.HTTPSConnection("tiktok-api15.p.rapidapi.com")
        headers = {
            'x-rapidapi-key': self.config["rapidapi_key"],
            'x-rapidapi-host': "tiktok-api15.p.rapidapi.com"
        }

        try:
            conn.request("GET", endpoint, headers=headers)
            response = conn.getresponse()
            data = response.read()
            return json.loads(data.decode("utf-8"))
        except Exception as e:
            return {"error": str(e)}

    async def randomtiktokcmd(self, message):
        """Команда для получения случайного видео из TikTok"""
        endpoint = "/index/Tiktok/getReplyListByCommentId?comment_id=7093219663211053829&cursor=0&count=10&video_id=7093219391759764782"
        result = await self.api_call(endpoint)

        if "error" in result:
            await message.reply(f"Ошибка при получении данных: {result['error']}")
            return

        if not result.get("data"):
            await message.reply("Не удалось найти видео.")
            return

        video = random.choice(result["data"])
        video_url = video.get("video_url")

        if video_url:
            await message.reply(f"Случайное видео из TikTok: {video_url}")
        else:
            await message.reply("Не удалось получить URL видео.")

version = "1.0.0"
author = "@musiczhara0"
