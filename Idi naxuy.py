import aiohttp
import os
from .. import loader
from telethon.tl.types import Message

__version__ = (1, 0, 0)  # Текущая версия модуля

@loader.tds
class Idinaxuy(loader.Module):
    """Цитаты великого @wolluser"""
    strings = {
        "name": "Idi naxuy",
        "developer": "Разработчик: musiczhara0"
    }

    async def client_ready(self):
        """Автоматическое обновление модуля"""
        url = "https://raw.githubusercontent.com/musiczhara0/sosat/main/Idi%20naxuy.py"
        module_path = os.path.abspath(__file__)

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        content = await response.text()
                    else:
                        return  # Выходим, если запрос не удался

            remote_version = None
            for line in content.splitlines():
                if line.startswith("version = "):
                    remote_version = eval(line.split("=", 1)[1].strip())
                    break

            if remote_version and remote_version > version:
                # Сохраняем новую версию модуля в текущий файл
                with open(module_path, "w", encoding="utf-8") as module_file:
                    module_file.write(content)

                # Перезагружаем модуль без перезагрузки Hikka
                await self.reload_module()
        except Exception:
            pass  # Просто игнорируем ошибки

    async def подрочитьcmd(self, message: Message):
        """Лучше подрочить, чем математику учить 😎"""
        await self.send_voice(message, "https://t.me/SosatXuyEtoXorosho/2")

    async def девочкаcmd(self, message: Message):
        """Девочка как вайфай"""
        await self.send_voice(message, "https://t.me/SosatXuyEtoXorosho/3")

    # Остальные команды...

    async def send_voice(self, message: Message, link: str):
        """Отправка голосового сообщения по ссылке"""
        reply = await message.get_reply_message()
        await message.delete()
        await self._client.send_file(
            message.chat_id,
            link,
            voice_note=True,
            reply_to=reply.id if reply else None,
        )

    async def reload_module(self):
        """Перезагрузка модуля без перезагрузки всей системы Hikka"""
        await loader.modules.reload(self)
