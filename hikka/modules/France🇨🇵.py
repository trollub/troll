import random
from asyncio import sleep
import os
from .. import loader, utils


@loader.owner
def register(cb):
    cb(francemod())


class francemod(loader.Module):
    strings = {"name": "France🇨🇵"} # name loader ()

    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client

    async def slxcmd(self, message):
        '''Интервал в секундах + шапка''' 
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "Франция прекратила разъебку🇨🇵 ")
            return
        await utils.answer(
            message,
            "<b>Франция начинает разъебку🇨🇵 \n\n"
            "что бы его выключить напиши <code>.lsx</code></b>"
        )
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message()
        shabl = ["ну ты понимаешь что  если  у твоей матери получилось избежать лобового столкновения с моей залупы то у тебя не сможет это получиться и ты чиста мне на хуй прыгнешь 🇫🇷",
" у тя мать как шалава грязная сосет чо за хуйня раньше лучше было🇫🇷",
"починил твоей матери еë влагалище🇫🇷",
"ну бля ты мне неровня тут  сынуля дегенерата🇫🇷",
"ты тут чисто мой хуй смешишь своим видом🇫🇷",
"устроил полку для твоей мамки 🇫🇷",
"понятие весы для твоей матери не доступно🇫🇷",
"вспорол твоей матери живот🇫🇷",
"всаси как кабан🇫🇷",
"переменал твою мать  к себе в дом и начал  хуярить  эту дуру без устали🇫🇷",
"у тебя в доме мой хуй в рамке лежит а вы любуйтесь 🇫🇷","ну выебали тебя же🇫🇷",
"ну сын шлюхи на саси🇫🇷",
"саси май пинос сын твари🇫🇷",
"поломаем тебя тут🇫🇷",
"ты сын шлюхи слабохарактерной🇫🇷",
"ты понимаешь что твоя мать дура мой хуй как увеличитель для губ узает🇫🇷",
"отсоси слабак ебаный🇫🇷",
"твоей матерью как марионеткой пользуюсь🇫🇷",
"поломаю  тебя🇫🇷",
"у тебя мать шлюха дикая🇫🇷",
"мой член любишь как минеральный🇫🇷",
"атрафировал мать твою сын шлюхи🇫🇷",
"сосешь как бешеный🇫🇷",
"убил тя хуем🇫🇷",
"свернул нос твоей мамке🇫🇷",
"у тебя мать жируха ебаная🇫🇷",
"на хуй🇫🇷",
"держи хуй🇫🇷",
"я твою мамашу как таракана пришиб ногой🇫🇷",
"пасаси🇫🇷",
"Даже Пифагор создал теорему на счет твоей матери если твоя мать нам не пососет с ней по любому что нибудь случиться и теперь она этого боиться и отсасывает нам каждый день и все с ней хорошо и все рады вобщем🇫🇷",
"ты вкурсе что я твою пизду когда ебу)крики васе тиши и тиши)оказываеться ее и заряжать надо🇫🇷", 
"на пит стопе твою мать ебал когда она прыгала в тачке к чужим мужикам они расчитывали на что то но потом поняли что сосёт она только мне🇫🇷",
"ты понимешь что мой хуй как заштёпангый флаг ебал твою мамшку в говне🇫🇷", 
"Не как не пойму твоя мать притворяеться или она на деле шлюхадумаю что ей не стоит присутствовать в нашей жизни но сосет она великолепна только из за этого мы не сожгли ее на ксотре как ведьму🇫🇷",
"пидор абоссаный), вот зачем ты на свою мать нассал, когда мы ее встретили) я понимаю что у тебя рефлексы собаки, но твоя мать же не дерево) даже не бревно) в постели она хороша)🇫🇷",
"у тебя мать когда  за пивом бежит все думают что это трактор🇫🇷",
"тераризирую мать твою🇫🇷",
"все французы мамашу твою ебут🇫🇷",
"ускоглазую мамань твою убью🇫🇷",
"я своим хуем маму твою парабатил🇫🇷",
"всаси 🇫🇷",
"паразил твою мать одной тенью🇫🇷",
"почему мамаша твоя шлюха? 🇫🇷",
"порезал маму твою🇫🇷",
"мамзель раскрутил твою🇫🇷",
"ты лох ебаный🇫🇷",
"напором убей себя🇫🇷",
"хуй бери🇫🇷",
"когда твоя мать надевает жёлтую футболку все думают что она такси🇫🇷",
"ты прикинь чо будет если тебя на улице после моего хуя увидят🇫🇷",
"я же твоей маме кости все вырву🇫🇷",
"твою маму как пса на поводу держу🇫🇷",
"у тебя мать от моего хуя загорелась🇫🇷",
"танцую брейк на могиле твоей отца а после ебу твою кучерявую мать🇫🇷",
"ты тут сосешь же🇫🇷",
"сосешь как циливизованый🇫🇷",
"страстно сосешь 🇫🇷",
"без предела сосешь🇫🇷",
"потусторонне сосешь🇫🇷",
"бессильно сосешь🇫🇷",
"как обрыган сосешь🇫🇷",
"как недоарденталиц сосешь🇫🇷",
"я покорил сердце твоей матери своим хуем🇫🇷",
"я мамашу твою насилую🇫🇷",
"прекрасно сосешь 🇫🇷",
"с усилением сосешь 🇫🇷",
"под стоны сосешь 🇫🇷",
"как камень об твою бошку я суну хуй твоей маме 🇫🇷",
"расстоптал твою мамашу а она и не против 🇫🇷",
"без эмоций сосешь 🇫🇷",
"я же тя убью 🇫🇷",
"всем сосешь 🇫🇷",
"твоя соседка пыталась сделать покушение на мои яйца, но твою, мамань их отбила🇫🇷",
"я тебя хуем на работу пульну🇫🇷",
"под звук океана сосешь 🇫🇷",
"на берегу реки сосешь 🇫🇷",
"я твоей матерью как колонией зеков управляю🇫🇷",
"мне соси кирпич 🇫🇷",
" со всеми словами мамушу ебу🇫🇷",
"твою бабку поимел🇫🇷",
"как из астрала сосешь мне 🇫🇷",
"паразит ебаный убью тебя🇫🇷",
"побей себя моей залупой🇫🇷",
"слыш саси🇫🇷",
"не придуривайся все знают что ты хуй один отсосешь и поперхнешься моей залупой🇫🇷",
"все учёный приняли факт того что твоя мать самое больше существо на свете🇫🇷",
"трансфигурировал твою мать 🇫🇷",
"ты телка смазливая🇫🇷",
"вытирай слезы   и готовься получать по ебалу🇫🇷",
"ну сломал же тя🇫🇷",
"давай соси сын шлюхи",
"ты шлюхи сын дешевой🇫🇷",
"на мой член губы сложи🇫🇷",
"мамашу те ебем🇫🇷",
"запомни что у тебя клеймо пидараса🇫🇷",
"мы твою прабабушку ебали🇫🇷",
"я твой рот переодически как трусы юзаю🇫🇷",
"хуйца на🇫🇷",
"губка ебаная я твою мать в другую страну отправил🇫🇷",
"поразил тя членом-корреспондентом 🇫🇷",
" когда твоя мать прыгает все думают что это землетрясение🇫🇷",
"ты же внатуре отсосник ебаный🇫🇷",
"ты сдесь терпила ни на что не годная🇫🇷",
"лови мой хуй🇫🇷",
"у тебя мать кривая дура мой хуй нюхать начала 🇫🇷",
"у тебя мать шмаль немытая мне хуй полирует а я ей ноги ломаю 🇫🇷",
"мамаша твоя думала что она безнаказанная будет а я ей с двух ног в матку залетел и выходил тебя очкарика ебаного🇫🇷",
"хуй возьми🇫🇷",
"под эффектом ебу твою мать🇫🇷",
"всоси хуй как насос🇫🇷",
"поебу мать те🇫🇷",
"неосязаемо сосешь 🇫🇷",
"на крыше сосешь 🇫🇷",
"как покойник сосешь 🇫🇷",
"ты понимаешь что мы когда устраивали ванные процедуры твоя мама первая лезла ко мне в ванну а я ей голову об угол бил🇫🇷",
"ты че внатуре удумал тягаться с лучшим, или че я тебе телке кривоносой буду ебальник вытрахивать🇫🇷",
"у тя клан хуйня🇫🇷",
" ты шаблоной бляди сын ну ка к моему хую примкнул🇫🇷",
"слабак ты ебаный у тебя цель на всю жизнь это мое внимание получить🇫🇷",
"вытрахиваю тебя сына шлюхи🇫🇷",
"сосешь тут без дела🇫🇷",
"малоумный упырь я же тебя тут разобью напросто🇫🇷",
"в конце концов твоя мать мертва 🇫🇷",
"поимел тебя ичо🇫🇷",
"ты же выродок своё древо семейное портишь🇫🇷",
"твою мать на хим заводе трахал 🇫🇷",
"гасим тя чурку🇫🇷",
" на выходных вместо кино твою мать на кладбище вожу🇫🇷",
"ты же терпила даже ниче не скажешь мне🇫🇷",
"телка соси🇫🇷",
"проводил твою мать до общаги🇫🇷",
"в харю лови🇫🇷",
"твоя мечта мне хуй дрочить 🇫🇷",
"жирное ебало твое ебал🇫🇷",
"всневзашел на живот твоей матери🇫🇷",
"я твоей матери своей спермой желудок расплавил🇫🇷",
"вспорол живот теюе и твоей мамаша🇫🇷",
"сестру твою трахал🇫🇷",
"поимел тебя а ты ток за🇫🇷",
"откинулся на 5 сек ару ты ньюфажище, сидишь в чате из  себя героя на каблуках строишь, а на самом деле ты сын шлюхи тупой🇫🇷",
"чиста мамаху твою ебу🇫🇷",
"да я тваю маму не уважаю ичо 🇫🇷",
"кристалически сосешь 🇫🇷",
"ну на саси 🇫🇷",
" мой хуй как соска для твоеы мамы 🇫🇷",
" я же твоей матери клитор распорошил сынуля шлюхи поебаной 🇫🇷",
"все тебя в рот ебут 🇫🇷",
"у всех твоя мать на цепи🇫🇷",
"рейванул в твою мать 🇫🇷",
"я же тебя и все что ты любишь унижтожу🇫🇷",
"рассаси членяру🇫🇷",
"у меня залупа под твой рот идеально входит 🇫🇷",
"как проекция сосешь мне🇫🇷",
"ну ты загнаный в угол хуесос🇫🇷",
"на всаси🇫🇷",
"ебу тя во всех позах и времени🇫🇷",
"поимел тя как пса🇫🇷",
"угомонил тя хуем 🇫🇷",
"не расслабляйся ты сынок ляври ебаной ты тут мой хуй дегустировать будешь🇫🇷",
"убил тя пенисом и спрятался🇫🇷",
"твоей матерью в футбол играл🇫🇷",
"юзаю твою мать как дешевый презик🇫🇷",
"ну ты сын шлюхи соси🇫🇷",
"шаблонизированая хуйня падай на колени предомной я же тя внатуре изничтожу 🇫🇷",
" я твоей матери в щеки сувал🇫🇷",
"ну паипал  тебя знатно🇫🇷",
"вся деревня твоя вместо сигар волосы твоей матери скуривала🇫🇷",
"тебя зарежем🇫🇷",
"бараздил пизду твоей матери, кстати там внатуре глубоко))))🇫🇷",
"хуяку наверни🇫🇷",
"ты псина слабая🇫🇷",
"че там сосешь🇫🇷",
"чо у меня в ногах забыл ты сынуля шлюхи🇫🇷",
"не раскисай тут пидарас🇫🇷",
"смотри не потухни пока сосешь🇫🇷",
"самовнушай себе слова в обратном порядке, произнося их, держа в руках зеркало, направленное в твою сторону в твоем облике, самопровкацией ты отца пидораса накажи, подтверди словом ниже, что сосал мне, мой отец до и после этого дня в своем облике тебя в рот ебал, ты глаголишь проекцию лжи с хуем во рту, проснись и абстрагируйся дефом лживым🇫🇷",
"резко Саси🇫🇷",
"умеренно Саси🇫🇷",
"по немного соси🇫🇷",
"по левому соси🇫🇷",
"по правде ты Саси🇫🇷",
"папу убей а я уже матерью займусь твоей🇫🇷",
"ну все ты Саси🇫🇷",
"заткни свой ебальнмк моей залупоы в ритме вальса🇫🇷",
"на Саси тварь знаменитой дуры🇫🇷",
"ты же слабак отсосешь тут🇫🇷",
"на изях мать те убил🇫🇷",
"ну на Саси пока даю🇫🇷",
"остановил время и избил твою мать что бы она сразу падать на мой хуй начала🇫🇷",
"ты же дурь двуличная сосешь мне тут🇫🇷",
"жопу лижи🇫🇷",
"сынок бляди ты задроченой🇫🇷",
"я же тя тут вкачаю пидарса ебаного🇫🇷",
"ты тут не надейся на мою милость я тебе просто мать зарежу 🇫🇷",
"с минигана твою мать обстрелял🇫🇷",
"твоя мать мне еще в детстве хуй сосала🇫🇷",
"псина безрылая поимею тебя прямо на месте🇫🇷",
"тебя чисто тут будем пинать беглеца ебаного🇫🇷", ]
        self.db.set(self.strings["name"], "state", True)
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(sh+(random.choice(shabl)))
            await sleep(time)