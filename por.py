# -*- coding: utf-8 -*-

from hikka import loader, utils
import aiohttp
from bs4 import BeautifulSoup
import random

@loader.tds
class PhotoScraperModule(loader.Module):
    """Модуль для получения случайного изображения с сайта"""
    strings = {"name": "PhotoScraper"}

    @loader.command()
    async def randomphotocmd(self, message):
        """Получить случайное фото с сайта"""
        url = "https://pornpen.ai/search"  # URL сайта для парсинга
        photos = await self.get_photos(url)

        if not photos:
            await utils.answer(message, "Не удалось найти изображения.")
            return

        random_photo = random.choice(photos)
        await utils.answer(message, f"Случайное фото: {random_photo}")

    async def get_photos(self, url):
        """Метод для получения ссылок на изображения с сайта"""
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    response.raise_for_status()
                    html = await response.text()

            soup = BeautifulSoup(html, "html.parser")
            # Извлекаем все изображения
            images = soup.find_all("img")  # Возможно, нужно уточнить теги
            photos = [img["src"] for img in images if img.get("src")]

            return photos
        except Exception as e:
            return None

version = "1.0.0"
author = "@musiczhara0"
