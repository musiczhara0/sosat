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
                        print("Ошибка при загрузке обновления: ", response.status)
                        return

            remote_version = None
            for line in content.splitlines():
                if line.startswith("version = "):
                    remote_version = eval(line.split("=", 1)[1].strip())
                    break

            if remote_version and remote_version > version:
                print(f"Обновление доступно: текущая версия {version}, удаленная версия {remote_version}")

                # Сохраняем новую версию модуля в текущий файл
                with open(module_path, "w", encoding="utf-8") as module_file:
                    module_file.write(content)

                # Важно: Модуль будет обновлен только после перезагрузки Hikka. Перезагрузка модуля здесь не осуществляется.
        except Exception as e:
            print(f"Ошибка при обновлении модуля: {e}")

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

    async def send_voice(self, message: Message, link: str):
        """Общий метод для отправки голосового сообщения по ссылке"""
        reply = await message.get_reply_message()
        await message.delete()
        await self._client.send_file(
            message.chat_id,
            link,
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
