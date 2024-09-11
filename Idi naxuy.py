import requests
import os
import sys

version = (1, 0, 0)
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

    # Далее все остальные команды...
