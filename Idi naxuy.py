__version__ = (1, 0, 2)
# meta developer: @musiczhara0
# for more info: https://github.com/musiczhara0/sosat/blob/main/Idi%20naxuy.py
from .. import loader  # Импортируем необходимые модули
from telethon.tl.types import Message

@loader.tds
class идинахуй(loader.Module):
    """Цытаты великого @wolluser и не только"""
    
    strings = {
        "name": "Иди нахуй",
        "developer": "Разработчик: musiczhara0"
    }

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

    async def циганкаcmd(self, message: Message):
        """Однажды ко мне подошла циганка чтобы погадать, но она не угадала что я ей дам по ебалу"""
        await self.send_voice(message, "https://t.me/SosatXuyEtoXorosho/21")

    async def тревогаcmd(self, message: Message):
        """Тревога тревога женщина в чате"""
        await self.send_voice(message, "https://t.me/SosatXuyEtoXorosho/22")
    
    async def send_voice(self, message: Message, link: str):
        """Общий метод для отправки голосового сообщения по ссылке"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            link,
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
