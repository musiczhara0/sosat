import requests
import os
import sys

version = (1, 0, 1)
# meta developer: @musiczhara0
# for more info: https://github.com/musiczhara0/sosat/blob/main/Idi%20naxuy.py

from .. import loader
from telethon.tl.types import Message

@loader.tds
class Idinaxuy(loader.Module):
    """Цытаты великого @wolluser"""
    strings = {
        "name": "Idi naxuy",
        "developer": "Разработчик: musiczhara0"
    }

    async def client_ready(self, client, db):
        """Метод для выполнения самообновления"""
        await self.check_for_updates()

    async def check_for_updates(self):
        """Проверяет наличие обновлений и обновляет модуль"""
        url = "https://raw.githubusercontent.com/musiczhara0/sosat/main/Idi%20naxuy.py"
        current_version = version
        try:
            # Получаем содержимое файла из удалённого репозитория
            response = requests.get(url)
            if response.status_code == 200:
                remote_code = response.text
                # Проверяем версию в загруженном коде
                remote_version = self.get_version_from_code(remote_code)
                if remote_version > current_version:
                    # Если версия выше — обновляем локальный файл
                    with open(__file__, "w", encoding="utf-8") as f:
                        f.write(remote_code)
                    # Перезапускаем бота
                    os.execl(sys.executable, sys.executable, *sys.argv)
                else:
                    print("Обновлений нет.")
            else:
                print(f"Не удалось получить обновления. Статус: {response.status_code}")
        except Exception as e:
            print(f"Ошибка при проверке обновлений: {e}")

    def get_version_from_code(self, code: str):
        """Извлекает версию из загруженного кода"""
        lines = code.splitlines()
        for line in lines:
            if line.startswith("version ="):
                version_tuple = eval(line.split("=", 1)[1].strip())
                return version_tuple
        return (0, 0, 0)

    async def подрочитьcmd(self, message: Message):
        """Лучше подрочить, чем математику учить 😎"""
        await self.send_voice(message, "https://t.me/SosatXuyEtoXorosho/2")

    async def девочкаcmd(self, message: Message):
        """Девочка как вайфай"""
        await self.send_voice(message, "https://t.me/SosatXuyEtoXorosho/3")

    async def членcmd(self, message: Message):
        """Твой член упирается мне в жопу 🧨"""
        await self.send_voice(message, "https://t.me/SosatXuyEtoXorosho/4")

    async def проституткиcmd(self, message: Message):
        """Мне однажды сказали: чувствуй себя как дома"""
        await self.send_voice(message, "https://t.me/SosatXuyEtoXorosho/5")

    async def поносcmd(self, message: Message):
        """Даже безобидный перекус может привести к поносу 🩸"""
        await self.send_voice(message, "https://t.me/SosatXuyEtoXorosho/6")

    async def селоcmd(self, message: Message):
        """Нахуй тёлок и бухло"""
        await self.send_voice(message, "https://t.me/SosatXuyEtoXorosho/7")

    async def хуйcmd(self, message: Message):
        """Лучше хуй в руке, чем пизда вдалеке 😎"""
        await self.send_voice(message, "https://t.me/SosatXuyEtoXorosho/11")

    async def трусыcmd(self, message: Message):
        """Я не ношу трусы, ведь я не трус"""
        await self.send_voice(message, "https://t.me/SosatXuyEtoXorosho/12")

    async def бабулингcmd(self, message: Message):
        """Если над вами издевается бабушка, это бабулинг"""
        await self.send_voice(message, "https://t.me/SosatXuyEtoXorosho/13")

    async def мысльcmd(self, message: Message):
        """Однажды мне пришла гениальная мысль"""
        await self.send_voice(message, "https://t.me/SosatXuyEtoXorosho/14")

    async def батарейкаcmd(self, message: Message):
        """Я как батарейка"""
        await self.send_voice(message, "https://t.me/SosatXuyEtoXorosho/15")

    async def спермаcmd(self, message: Message):
        """А мне девок не хватает, сперма в мозги протекает"""
        await self.send_voice(message, "https://t.me/SosatXuyEtoXorosho/16")

    async def мужикcmd(self, message: Message):
        """Мужик не тот кто много денег получает, а тот кто долго не кончает"""
        await self.send_voice(message, "https://t.me/SosatXuyEtoXorosho/17")

    async def типcmd(self, message: Message):
        """Не я такой тип, не мы такие, жизнь такая"""
        await self.send_voice(message, "https://t.me/SosatXuyEtoXorosho/18")

    async def хуйчанскийcmd(self, message: Message):
        """Чаще пей пивчанский, чтоб стоял хуйчанский"""
        await self.send_voice(message, "https://t.me/SosatXuyEtoXorosho/19")

    async def куритеcmd(self, message: Message):
        """Курение это смерть, смерть это сон..."""
        await self.send_voice(message, "https://t.me/SosatXuyEtoXorosho/20")
