__version__ = (1, 0, 2)
# meta developer: @musiczhara0
# for more info: https://raw.githubusercontent.com/musiczhara0/sosat/refs/heads/main/memes.py
from .. import loader  # Импортируем необходимые модули
from telethon.tl.types import Message

@loader.tds
class memes(loader.Module):
    """Мемы и кружки"""
    
    strings = {
        "name": "Memes",
        "developer": "Разработчик: musiczhara0"
    }

    async def ёршикcmd(self, message: Message):
        """Иди бери ёршик чисти унитаз"""
        await self.send_voice(message, "https://telesco.pe/SosatXuyEtoXorosho/26")

    async def долбоёбcmd(self, message: Message):
        """Слыш ты пидорас, отсосёшь только ты"""
        await self.send_voice(message, "https://telesco.pe/SosatXuyEtoXorosho/27")

    async def боксcmd(self, message: Message):
        """Урок бокса"""
        await self.send_voice(message, "https://telesco.pe/SosatXuyEtoXorosho/28")

    async def бабушкаcmd(self, message: Message):
        """Что теплое в мёртвой бабушке ?"""
        await self.send_voice(message, "https://telesco.pe/SosatXuyEtoXorosho/29")

    async def взрослаяcmd(self, message: Message):
        """Забыла у тебя спросить"""
        await self.send_voice(message, "https://telesco.pe/SosatXuyEtoXorosho/30")

    async def нахуйcmd(self, message: Message):
        """Пошёл ты нахуй, я не буду плакать"""
        await self.send_voice(message, "https://telesco.pe/SosatXuyEtoXorosho/31")

    async def петардаcmd(self, message: Message):
        """Единственная петарда которая взорвёться в этом году"""
        await self.send_voice(message, "https://telesco.pe/SosatXuyEtoXorosho/32")

    async def скиньхуйcmd(self, message: Message):
        """Скинь хуй"""
        await self.send_voice(message, "https://telesco.pe/SosatXuyEtoXorosho/33")

     async def физкультcmd(self, message: Message):
        """Физкульт зарядка под ебейший бит"""
        await self.send_voice(message, "https://t.me/SosatXuyEtoXorosho/34")

     async def выхлопcmd(self, message: Message):
        """Я вообще делаю что хочу - ебейший выхлоп"""
        await self.send_voice(message, "https://t.me/SosatXuyEtoXorosho/34")

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
