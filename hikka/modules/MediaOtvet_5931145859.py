import random
from asyncio import sleep
import os
from .. import loader, utils, version
from telethon.tl.functions.users import GetFullUserRequest
import time 
import logging
import re
from ..inline.types import InlineCall
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.types import Message
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest, GetFullChatRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins, UserStatusOnline
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError)
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest
from datetime import datetime
from math import sqrt
import requests
import git
from .. import loader, utils
from asyncio import sleep as s

lesenka1 = ('сынуля ты дряхлой тифозницы вообще в ступор ебанулся или че',
            'сынуля шлюхи ты почему во сне язык высовываешь и что то лижешь я не пойму')
lesenka2 = " ублюдок ебанный я твою мать тут убью нахуй"
lesenka3 = 'украинский ты свинорылый сын хуйни которой я ебалище оторву нахуй я те щас ебалище тут обоссу сын шлюхи'
lesenka4 = " да закрой ебалище уже свое ничего не стоющее хуесос ебанный"
lesenka5 = " я те мать ебал говнакусок ебучий"
lesenka6 = " закрой ебалище свое ты кривозубый сынуля шлюхенции ебучей"
lesenka7 = " ты че пешкарь ебанный в себя поверил или че"
lesenka8 = " я твою мать тут ровным счетом убью жирный ублюдок ты"
lesenka9 = " эу ты жалкий сынуля паскудницы пешкарной начинай мне членяру своим языком полировать ты хуесос ебанный"
lesenka10 = " ты можешь свое ебалище около моего члена не открывать как по привычке пес ты ебанный"
lesenka11 = " псина ебанная ты тут в живых не уйдешь пойми это ебучий ты в жопу гомосек"
lesenka12 = " ты че сынчела шлюхи тут ебу дал или че ты куда поперся на член мой пешкарь ебанный"
lesenka13 = " ты можешь хоть на секунду свое кривое украинское свиное ебалище прикрыть во славу россии слабак ебаный, ты умрешь нахуй от этого богоподобного автоответчика, украинский сын жирного сердобольного куртизанского еблана"
lesenka14 = " я же тебя убью тут нахуй слабость ебанная ты чё там вообще попутал или че слабак ебучий просто напросто пешкарный хуеплет который будет изо дня в день по ебалу получать харчки со стороны #sindze, а именно твоего ебыря, сынуля шлюхи ты черный"
lesenka15 = " я твою мать тут хуем зарежу нахуй сын украинского гомосексуального сына шлюхи "
lesenka16 = " я ж тя пешкаря ебанного щас тут буду по всей выебанной рашкой украины таскать хуем за волосы слабак ты ебанный"
lesenka17 = " че ты там мне под член кудахчешь слабак ебучий"
lesenka18 = " вникай своей тупой головой в то что я твою мать убью нахуй сынуля шалавы ебанной"
lesenka19 = " ну и че ты Украинский спермоглот, заглоти член великой РФ и помри стоя на коленях блядина ты жирная нахуй"
lesenka20 = " ахаххаха ты че там пиздоболишь тупой идиот нахуй "
lesenka21 = " ты тут в живых не останешься слабак ебанный, я те мать тут выебу сынуля шлюхи ты тупоеблой"
lesenka22 = " ты че там укроп ебанный я вашего президента, если его так назвать можно, стриптизера ебанного засадил на член как и твою умолишенную мать и те двоя танцевали на нем как на танцполе сын шлюхи ты тупой сука "
lesenka23 = " аэаээа ебать ты че там противопоставить что то собираешься? я же тебя тут убью без сомнений пес ты ебанный"
lesenka24 = " ты будешь мою сперму пить под предлогом того что это сок и даже зная что это сперма ты продолжал делать вид что думаешь что это сок чтобы не показать свое идиотское исключительно тупое состояние дабы я тя не опозорил перед всеми, ну увы я заметил как усердно ты сосал мне мой член, хуесос ты ебаный"
lesenka25 = " так че ты еблан тупой куда мой член в засос пустил"
lesenka26 = " ты че пегас ебанный, на мой член полетишь как голодные псы на мясо твоей обнаженной моим членом матери шлюховатой собаки, просто напросто украинской шлюхи"
lesenka27 = " хуесос любящий свою разгромленную Россией родину украину у которой президент стриптизер ебанный, ты там вообще мороженное с моим членом перепутал или че, иначе я не пойму почему ты мой член так усердно лижешь"
lesenka28 = " я твою мать тут запросто убью нахуй и че ты сделаешь сосунок ты ублюдский"
lesenka29 = " ты в живых не останешься тут поверь мне слабый ты сынишка шлюхи получавший уже пизды по сто раз ты че там в рыданье пустился уже слабый ты сын падали гнилозубой"
lesenka30 = " ты заживо будешь членом моим похоронен слабак ебаный "
lesenka31 = " пегас ебанный ты че там ускакал на чьем то члене, ты че прям так мя боишься"
lesenka32 = " твой побег от члена моего те не поможет долбоеб ебанный"
lesenka33 = " я те мать ебарировал сынишка ты шлюхи которой я вспорол живот а дальше вытащил все кишки и внутренности считая ее матку и скормил отцу, вникай в это тупорылое ты обьебанное ты создание не видящее мир а лишь член надвигающийся прямо в ебало те"
lesenka34 = " ты че как краб так крепко за член мой схватился ебанат ты ебучий"
lesenka35 = " я те рот же щас обоссу хуеглот ебанный"
lesenka36 = " ты че там пешкарь ебанный в себя поверил, иначе я не пойму почему ты так стремительно надвигаешься на мой член"
lesenka37 = " ты нахуя харчки летящие те в твое украинское ебалище терпишь как свинья ебучая я не понял"
lesenka38 = " я твою матерь тут хуем ща обработаю ты меня понял или нет псина ты ебанная"
lesenka39 = " ходячая ты насадка для хуя ты че там вообще попутал я же тебе мать ебал "
lesenka40 = " сердобольник я тут тебе щас твои зубы повырываю нахуй черт ты ебанный"
lesenka41 = " ты че там жирдяй ебанный поднимайся и начинай мне член сосать пес ты ебанный"
lesenka42 = " я ж тя тут хуем убью нахуй "
lesenka43 = " облеплю тя жирными хуями псина ебанная"
lesenka44 = " ты че попутал сынуля путаны ебучей на кого лезешь "
lesenka45 = " я - твой ебарь, выебу тебя без сомнений даже о жалости укроотсос ты ебучий"
lesenka46 = " подохни стоя на члене моем слабак ебанный ну же"
lesenka47 = " посмей только на член мне.харкнуть я тя им же заставлю мне его сосать ебливый ты сынуля куртизанки ебнутой на голову "
lesenka48 = " ты че мне отпора не даешь слабоватый ты хуеплет, мать те ебал запомни пёс "
lesenka49 = " я те разрешаю сдохнуть на коленях держа мой член у себя во рту слышишь меня"
lesenka_all = [lesenka1, lesenka2, lesenka3, lesenka4, lesenka5, lesenka6, lesenka7, lesenka8, lesenka9, lesenka10, lesenka11, lesenka12, lesenka13, lesenka14, lesenka15, lesenka16, lesenka17, lesenka18, lesenka19, lesenka20, lesenka21, lesenka22, lesenka23, lesenka24, lesenka25, lesenka26, lesenka27, lesenka28, lesenka29, lesenka30, lesenka31, lesenka32, lesenka33, lesenka34, lesenka35, lesenka36, lesenka37, lesenka38, lesenka39, lesenka40, lesenka41, lesenka49]
media = ""


@loader.tds
class MediaOtvet(loader.Module):
    '''lesenka'''
    strings = {
        "name": "<b>MediaOtvet</b>",
        "loading": "<b>MesdiaLoading...</b>",
        "not_chat": "<b>Eblan, ti ne v chate</b>",
    }

    async def client_ready(self, client, db):
        self.db = db
        self.client = client
        
    async def client_ready(self, client, db):
        self.db = db
        self.users = self.db.get("les", "users", [])
        self.phrases = self.db.get("les", "phrases", [])

    def add_user(self, user_id: int):
        self.users.append(user_id)
        self.db.set("les", "users", self.users)

    def remove_user(self, user_id: int):
        self.users.remove(user_id)
        self.db.set("les", "users", self.users)

    async def rautomsgphcmd(self, message):
        """ʙᴋᴧючиᴛь ʍᴏдуᴧь ᴄ ᴏᴛʙᴇᴛᴀʍи ⟨𝗋𝖾𝗉𝗅𝗒⟩"""

        reply = await message.get_reply_message()

        if reply is not None:
            if reply.from_id is not None:
                await utils.answer(
                    message=message,
                    response="<b>on</b>"
                )

                self.add_user(reply.from_id)

            else:
                await utils.answer(
                    message=message,
                    response="<b>модуль не работает на анонимных администраторах или каналах</b>"
                )

        else:
            await utils.answer(
                message=message,
                response="<b><code>Нужᥱн ρᥱᥰ᧘ᥲᥔ д᧘я ρᥲδ᧐ᴛы.</code>"
            )

    async def roffcmd(self, message):
        """ ᴨᴏᴧнᴀя ᴏᴄᴛᴀнᴏʙᴋᴀ ʍᴏдуᴧя ᴄ ᴏᴛʙᴇᴛᴀʍи"""

        self.users = []
        self.db.set("les", "users", self.users)

        await utils.answer(
            message=message,
            response="<b>off</b>"
        )

    async def выклответылсcmd(self, message):
        """ ᴏᴄᴛᴀнᴏʙᴋᴀ ʍᴏдуᴧя ᴄ ᴏᴛʙᴇᴛᴀʍи нᴀ ʙыбᴩᴀнный ᴀᴋᴋᴀунᴛ  ⟨𝗋𝖾𝗉𝗅𝗒⟩"""

        reply = await message.get_reply_message()

        if reply is not None:
            await utils.answer(
                message=message,
                response="<b></b>"
            )

            try:
                self.remove_user(reply.from_id)
            except:
                await utils.answer(
                    message=message,
                    response="<b>off</b>"
                )

        else:
            await utils.answer(
                message=message,
                response="<b><code>pls reaply</code>"
            )

    async def watcher(self, message):
        if getattr(message, "from_id", None) in self.users:
            await message.reply(random.choice(lesenka_all), file=media)
            
    async def dlrphhcmd(self, message):
        reply = await message.get_reply_message()
        file = reply if reply and reply else False
        await utils.answer(message, "<b>скачиваю...</b>")
        await s(3)
        global media
        media = file
        await utils.answer(message, "<b>фото принято!</b>")