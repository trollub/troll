# meta developer: @cybertrolling
import random
from asyncio import sleep
import os
from .. import loader, utils
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import Message


class volnaMod(loader.Module):
    '''Модуль сделаный легендой: @@cybertrolling'''
    strings = {
    "name":  "[🇷🇺]psychokill[🇷🇺]",
    "loading": "<b>𐋏ᥲчᥙнᥲю ᥲннᥙᴦᥙ᧘яцᥙю ɯᥲ᧘ᥲʙ...</b>",
    "not_chat": "<b>Ты нᥱ нᥲчᥙнᥲᥱɯь ᥲннᥙᴦᥙ᧘яцᥙю нᥱ ʙ чᥲᴛᥱ😡</b>",} # name loader () \n
    
    
    async def client_ready(self, client, db) -> None:
        
        self.db = db
        self.client = client
        
        
    async def volnahelpcmd(self, message):
        """ᥰ᧐κᥲᤋᥲᴛь ᥲнᥙⲙᥲцᥙю"""
        args = utils.get_args_raw(message)
        await message.edit("P")
        await message.edit("Ps")
        await message.edit("Psy")
        await message.edit("Psyc")
        await message.edit("Psуcho")
        await message.edit("Psychoki")
        await message.edit("Psychokil")
        await message.edit("Psychokill")
        await message.edit("<emoji document_id=5398017006165305287>🇷🇺</emoji>")
        await message.edit("<emoji document_id=5398017006165305287>🇷🇺</emoji><emoji document_id=5398017006165305287>🇷🇺</emoji>")
        await message.edit("<emoji document_id=5398017006165305287>🇷🇺</emoji><emoji document_id=5398017006165305287>🇷🇺</emoji><emoji document_id=5398017006165305287>🇷🇺</emoji>")
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        message = await utils.answer(message, self.strings("loading"))
        try:
            user_id = (
                (
                    (
                        await self._client.get_entity(
                            args if not args.isdigit() else int(args)
                        )
                    ).id
                )
                if args
                else reply.sender_id
            )
        except Exception:
            user_id = self._tg_id
            
            user = await self._client(GetFullUserRequest(user_id))

            user_ent = user.users[0]

            photo = await self._client.download_profile_photo(user_ent.id, bytes)
            user_info = (
            "<b><emoji document_id=5398017006165305287>🇷🇺</emoji><emoji document_id=5398017006165305287>🇷🇺</emoji><emoji document_id=5398017006165305287>🇷🇺</emoji>Psychokill Help<emoji document_id=5398017006165305287>🇷🇺</emoji><emoji document_id=5398017006165305287>🇷🇺</emoji><emoji document_id=5398017006165305287>🇷🇺</emoji>:</b>\n\n"
            "<b><emoji document_id=5398017006165305287>🇷🇺</emoji>.Psychokills - ᥴᥱκунды + ɯᥲᥰκᥲ: ᤋᥲᥰуᥴᴛᥙᴛь ⲙ᧐ду᧘ь ᥰ᧐ 1 ɯᥲδ᧘᧐ну<emoji document_id=5780466925997919731>💀</emoji></b>\n\n"
            f"<b>Username:</b>@{user_ent.username or '☠️'}\n"
            f"<b>First name:</b> {user_ent.first_name or '🚫'}\n"
            f"<b>ID:</b> <code>{user_ent.id}</code>\n"
            )

        if photo:
            await self._client.send_file(
                message.peer_id,
                photo,
                caption=user_info,
                link_preview=False,
                reply_to=reply.id if reply else None,
            )
            if message.out:
                await message.delete()
        else:
            await utils.answer(
                message,
                user_info,
                reply_to=reply.id if reply else None,
                link_preview=False,
            )

    async def Psychokillscmd(self, message):
        '''секунды в отписке сообщений + шаблон'''
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>𐌑᧐ду᧘ь psychokill help ᤋᥲκ᧐нчᥙ᧘ᥲ ᥲннᥙᴦᥙ᧘яцᥙю ɯᥲ᧘ᥲʙ<emoji document_id=5780466925997919731>💀</emoji>!</b>")
            return
        await utils.answer(
        message,
        "<b>𐌑᧐ду᧘ь psychokill help нᥲчᥲ᧘ᥲ ᥲᥰᥱ᧘ᥙᴦᥙ᧘яцᥙю ɯᥲ᧘ᥲʙ<emoji document_id=5780466925997919731>💀</emoji>!\n\n"
        "Կᴛ᧐δы ʙыκ᧘ючᥙᴛь ⲙ᧐ду᧘ь psychokill help ᥰρ᧐ᥰᥙɯᥙ ʙ κ᧐нɸᥱρᥱнцᥙᥙ,᧘ᥴ ᥰρ᧐ᥰᥙɯᥙ<emoji document_id=5780466925997919731>💀</emoji> <code>.psychokill</code></b>",
        )
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message()
        shabl = [
"[<emoji document_id=5780466925997919731>💀</emoji>]туловище твоей блядоматери своим хуем вскрыл непосредственно [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]ты сранимешный подхуйный астматический сын хуйни ни на что не способный [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]своему кавалеро-психокилловскому богу ебырю ты прям сейчас делаешь недоростоящий минет [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]гляди к утру не стухни манямироидная дочь свиноблядины ракавальная [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]черепушку твоей мамаши блядины вскрыл ковшом от трактора по классике жанра как таковой [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]ты тупейший никому неизвестный сын потаскушьей мордахенции крайне страшной [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>] непременно своим половым етуном ебал весь твой род чуркотских осетинцев бездарных [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]гляди тут не утухни что свойственно для тебе подобных говнотроллей слабейших [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]хуэм своим уродую ебальце твоей мамаши блядины максимально страшной мдам [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]не падай духом насадка ебучая пока мой хуэц окончательно не упал тебе в пиздлище продавив его до ядра земли где расщепило на субатомные частицы твою мамашу блядину [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]ты слабый сын шлюхи поебал тебе тушку [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]ты слабейший что свет повидал сын бляди [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]пиздец ну ты и сынуля бляди слабый конечно [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]туловище твоей блядоматери своим хуем вскрыл непосредственно [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]ты чо афганская полурванка даже никнейма как такового не имеешь потому что естесна последствием данного станет шлейф кринжэвости что будет за тобой тянуться мдам [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]ты манька ебливая [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>] уроженец саратова гляди здесь не потухни к утру [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]чеченский ты беженец сделал тебе хуэм дырку в черепе и использовал ее как насадку  [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]вырвал тебе кадык и насадил насвой хуй а всецело трахею использовал непосредственно в качестве как таковой пепельницы для своего хуя мдам колхозанец ебливый [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]туловище твоей блядоматери своим хуем вскрыл непосредственно [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]я из себя представляю разве что того кто тебе нахуй тушку вскроет остриём ковша тракторного [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]не задирай нос говнотроллина манямешная[<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]копрофагу ебаному непосредственно в данной конференции скальп снимем с его головушки максимально скудоумной что в себя таки и внушила что мой хуй сможет уравнять по силе мдам [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]тупейший сын бляди лови хуяру мою национал монархическую[<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]во славу России тебе тут  поебал мамашу шлюху не сдохни главное сыняра африканской бездушной швабры [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]ты подноготная грязь созданная для ублажения моего хуя и не более  [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]сжирай мои испражнения насадка [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]какое тебе такое осилить ты чо там в край ебанулась со своей шизофренией дочурка блядины[<emoji document_id=5398017006165305287>🇷🇺</emoji>]", 
"[<emoji document_id=5780466925997919731>💀</emoji>]ты сын двух ослепших глухонемых умалишённых куртизанок казачьих  [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]ты никому неизвестный сын шлюхотени бездарный [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]ты не более чем манямирочная членодырка слабейшая что вообще встречалась мне за все мое времяпрепровождение в текстописании [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]ты сошка ебанная терпящая закрой ебальник свой покуда я тебе окончательно кожаный покров не стянул с рыльца [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]копросрачерок ебучий бегом утух по одному моему желанию эу [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]ты слабейший рабпидорас [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]поюзал тебя как никому неизвестную дочь шлюхи что требуется только в качестве насадки [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]маньке ебанной оторвем на всеобщее обозрение копытца  мдам[<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]стянул  свой хуец непременно в ебальце твоей мамаши блядины ну а чо ты ещё хотела рабыня то ебливая [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]усраинский терпильный свинопас мне кажется ты не до конца понял мои слова отписанные в твою сторону например о том что я априори сильнее тебя на любом аспекте в троллинге или же о том что я без лишних разбирательств буду исключительно что делать так это ебарировать твою тушку астматическую нахуйную ебливая ты каракатица сука никому неизвестная) [<emoji document_id=5398017006165305287>🇷🇺</emoji>]",
"[<emoji document_id=5780466925997919731>💀</emoji>]прекращай как бы максимально крупномасштабное терпение моего полового етуна который тебе ебальце терзает сука нахуйная ты сошка ни к чему стоящему априори неприспособленная которая не будет более чем насадкой для моего члена который тебе ебаловину и пиздлище просто напросто изорвет в субатомные частички сальных мясных ошметков ну что в общем-то характерно для усраинских вертлявых тушек [<emoji document_id=5398017006165305287>🇷🇺</emoji>]" ]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(sh+(random.choice(shabl)))
            await sleep(time)