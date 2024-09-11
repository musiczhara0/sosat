# -*- coding: utf-8 -*-

from hikka import loader, utils
import aiohttp
import json
import random

@loader.tds
class TikTokModule(loader.Module):
    """TikTok Module"""
    strings = {"name": "TikTok"}

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "rapidapi_key",
                "a3b05d1879msh88bd3696e0fe7a6p128732jsnc894bc813ce8",
                "API ключ для доступа к RapidAPI"
            ),
        )

    @loader.command()
    async def randomtiktokcmd(self, message):
        """Команда для получения случайного видео из TikTok"""
        endpoint = "/index/Tiktok/getReplyListByCommentId?comment_id=7093219663211053829&cursor=0&count=10&video_id=7093219391759764782"
        response = await self.api_call(endpoint)

        if "error" in response:
            await utils.answer(message, f"Ошибка при получении данных: {response['error']}")
            return

        if not response.get("data"):
            await utils.answer(message, "Не удалось найти видео.")
            return

        video = random.choice(response["data"])
        video_url = video.get("video_url")

        if video_url:
            await utils.answer(message, f"Случайное видео из TikTok: {video_url}")
        else:
            await utils.answer(message, "Не удалось получить URL видео.")

    async def api_call(self, endpoint):
        """Метод для выполнения запроса к API"""
        url = f"https://tiktok-api15.p.rapidapi.com{endpoint}"
        headers = {
            'x-rapidapi-key': self.config["rapidapi_key"],
            'x-rapidapi-host': "tiktok-api15.p.rapidapi.com"
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    response.raise_for_status()
                    data = await response.json()
                    return data
        except aiohttp.ClientError as e:
            return {"error": str(e)}

__version__ = "1.0.0"
__author__ = "@musiczhara0"
