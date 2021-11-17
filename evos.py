# TOKEN = 1920468384:AAFzSfKKliZd_y2tQxwvfN9kgdkzfyz-aG8
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, Location
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters, CallbackQueryHandler

location = Location
jami = []
summa = []


# Inlinelar
def inline_botn(user_id, user_name):
    return [
        [InlineKeyboardButton("Lavash🌯", callback_data=f"lavash_{user_id}_{user_name}"),
         InlineKeyboardButton("Shaurma🌮", callback_data=f"shaurma_{user_id}_{user_name}")],
        [InlineKeyboardButton("Burger🍔", callback_data=f"burger_{user_id}_{user_name}"),
         InlineKeyboardButton("Donar🌮", callback_data=f"danar_{user_id}_{user_name}")],
        [InlineKeyboardButton("Hot Dog🌭", callback_data=f"hotdog_{user_id}_{user_name}"),
         InlineKeyboardButton("Hoggi🥪", callback_data=f"haggi_{user_id}_{user_name}")],
        [InlineKeyboardButton("Free🍟", callback_data=f"fre_{user_id}_{user_name}"),
         InlineKeyboardButton("Ichimliklar🍷", callback_data=f"cola_{user_id}_{user_name}")],
        [InlineKeyboardButton("Jami buyurtmalar", callback_data=f"all_{user_id}_{user_name}")]
    ]


def keybord_btns(locationn):
    return ReplyKeyboardMarkup([
        [KeyboardButton("Manzilni yuborish 'геопозиция'")]
    ], resize_keyboard=True)


def location_x(update, context):
    loc = update.message.location
    if loc:
        update.message.reply_text("Manzilni yuborish 'геопозиция'",
                                  reply_markup=keybord_btns(location))


# OVQATLAR
mini = "Lavash🌯 mini 18000  so`m"
big = "Lavash🌯 big 22000  so`m"
oddiy = "Lavash🌯 oddiy 20000  so`m"
sirli = "Lavash🌯 sirli 22000  so`m"
tovuqli = "Shaurma🌮 tovuqli 16000  so`m"
goshti = "Shaurma🌮 go`shtli 18000  so`m"
bur_mini = "Burger🍔 mini 18000  so`m"
bur_oddiy = "Burger🍔 oddiy 20000  so`m"
bur_big = "Burger🍔 big 23000  so`m"
bur_sir = "Burger🍔 sirli 23000  so`m"
donar_mini = "Donar🌮 mini 18000  so`m"
donar_big = "Donar🌮 big 20000  so`m"
donar_big_s = "Donar🌮 big & sous  23000 so`m"
donar_mini_s = "Donar🌮 mini & sous  21000 so`m"
Xotdog_oddiy = "Hot Dog🌭 oddiy 8000  so`m"
Xotdog_karalevski = "Hot Dog🌭 karalevski  12000 so`m"
Xotdok_canadsky = "Hot Dog🌭 canadski  10000 so`m"
Xotdog_qazi = "Hot Dog🌭 Qazi  16000 so`m"
xaggi_mini = "Hoggi🥪 mini  17000 so`m"
xaggi_big = "Hoggi🥪 big  22000 so`m"
free = "Free🍟  8000 so`m"
cola15 = "CocaCola (1.5) 🥤  10000 so`m"
cola1 = "CocaCola (1) 🥤  8000 so`m"
cola05 = 'CocaCola (0.5) 🥤  6000 so`m'
cola_b = "CocaCola бутулка 🥤 3000 so`m"
fanta15 = "Fanta (1.5) 🍹  10000 so`m"
fanta1 = "Fanta (1) 🍹  8000 so`m"
fanta05 = 'Fanta (0.5) 🍹  6000 so`m'
fanta_b = "Fanta бутулка 🍹 3000 so`m"
Sok1 = "Sok (1) 🍷  9000 so`m"
Sok_s = "Sok stakan 🍷 3000 so`m"
cofe_d = "Coffee DARK ☕️ 4000 so`m"
cofe_m = "Coffee milk 🥛 3000 so`m"


def Lavash_botn(user_id, user_name):
    return [
        [InlineKeyboardButton("Mini 🌯", callback_data=f"mini_{user_id}_{user_name}"),
         InlineKeyboardButton("Big 🌯", callback_data=f"big_{user_id}_{user_name}")],
        [InlineKeyboardButton("Sirli 🧀", callback_data=f"sirli_{user_id}_{user_name}"),
         InlineKeyboardButton("Oddiy 🌯", callback_data=f"oddiy_{user_id}_{user_name}")],
        [InlineKeyboardButton("Orqaga ⬅️", callback_data=f"back1_{user_id}_{user_name}")]
    ]


def shaur_botn(user_id, user_name):
    return [
        [InlineKeyboardButton("Tovuqli 🍗", callback_data=f"tovuq_{user_id}_{user_name}"),
         InlineKeyboardButton("Goshtli 🥩", callback_data=f"gosht_{user_id}_{user_name}")],
        [InlineKeyboardButton("Orqaga ⬅️", callback_data=f"back1_{user_id}_{user_name}")]
    ]


def burger_botn(user_id, user_name):
    return [
        [InlineKeyboardButton("Mini 🍔", callback_data=f"minni_{user_id}_{user_name}"),
         InlineKeyboardButton("Big 🍔", callback_data=f"bigg_{user_id}_{user_name}")],
        [InlineKeyboardButton("CHesse Burger 🧀", callback_data=f"ssirli_{user_id}_{user_name}"),
         InlineKeyboardButton("Oddiy 🍔", callback_data=f"odddiy_{user_id}_{user_name}")],
        [InlineKeyboardButton("Orqaga ⬅️", callback_data=f"back1_{user_id}_{user_name}")]
    ]


def Donar_botn(user_id, user_name):
    return [
        [InlineKeyboardButton("Mini 🌮", callback_data=f"kichik_{user_id}_{user_name}"),
         InlineKeyboardButton("Big 🌮", callback_data=f"katta_{user_id}_{user_name}")],
        [InlineKeyboardButton("Mini & Sous", callback_data=f"msous_{user_id}_{user_name}"),
         InlineKeyboardButton("Big & Sous", callback_data=f"bsous_{user_id}_{user_name}")],
        [InlineKeyboardButton("Orqaga ⬅️", callback_data=f"back1_{user_id}_{user_name}")]
    ]


def Hot_botn(user_id, user_name):
    return [
        [InlineKeyboardButton("Oddiy 🌭", callback_data=f"oddiy_{user_id}_{user_name}"),
         InlineKeyboardButton("Canadski 🌭", callback_data=f"canada_{user_id}_{user_name}")],
        [InlineKeyboardButton("Karalevski 🌭", callback_data=f"karalev_{user_id}_{user_name}"),
         InlineKeyboardButton("Qazili 🌭", callback_data=f"qazi_{user_id}_{user_name}")],
        [InlineKeyboardButton("Orqaga ⬅️", callback_data=f"back1_{user_id}_{user_name}")]
    ]


def Hoggi_botn(user_id, user_name):
    return [
        [InlineKeyboardButton("Mini 🥪", callback_data=f"minyi_{user_id}_{user_name}"),
         InlineKeyboardButton("Big 🥪", callback_data=f"bigi_{user_id}_{user_name}")],
        [InlineKeyboardButton("Orqaga ⬅️", callback_data=f"back1_{user_id}_{user_name}")]
    ]


def Free_botn(user_id, user_name):
    return [
        [InlineKeyboardButton("Free 🍟", callback_data=f"freee_{user_id}_{user_name}")],
        [InlineKeyboardButton("Orqaga ⬅️", callback_data=f"back1_{user_id}_{user_name}")]
    ]


def Ichimlik_botn(user_id, user_name):
    return [
        [InlineKeyboardButton("Cola 1,5 🥤", callback_data=f"1,5_{user_id}_{user_name}"),
         InlineKeyboardButton("Cola 1 🥤", callback_data=f"1_{user_id}_{user_name}")],
        [InlineKeyboardButton("cola 0,5 🥤", callback_data=f"0,5_{user_id}_{user_name}"),
         InlineKeyboardButton("cola бутулка 🥤", callback_data=f"butulka_{user_id}_{user_name}")],
        [InlineKeyboardButton("Fanta 1,5 🍹", callback_data=f"f1,5_{user_id}_{user_name}"),
         InlineKeyboardButton("Fanta 1 🍹", callback_data=f"f1_{user_id}_{user_name}")],
        [InlineKeyboardButton("Fanta 0,5 🍹", callback_data=f"f0,5_{user_id}_{user_name}"),
         InlineKeyboardButton("Fanta бутулка 🍹", callback_data=f"fbutulka_{user_id}_{user_name}")],
        [InlineKeyboardButton("Sok 1 🍷", callback_data=f"1L_{user_id}_{user_name}"),
         InlineKeyboardButton("Sok Stakan 🍷", callback_data=f"soks_{user_id}_{user_name}")],
        [InlineKeyboardButton("Coffee DARK ☕️", callback_data=f"DARK_{user_id}_{user_name}"),
         InlineKeyboardButton("Coffee milk 🥛", callback_data=f"milk_{user_id}_{user_name}")],
        [InlineKeyboardButton("Orqaga ⬅️", callback_data=f"back1_{user_id}_{user_name}")]
    ]


def start(update, context):
    user = update.message.from_user
    print(user.username)
    jami.clear()
    summa.clear()
    update.message.reply_text(f"""Assalomu alaykum {user.first_name}
EVOS rasmiy✅ botiga hush kelibsiz
Buyurtma 🍽 berish uchun tanlang ⬇️""",
                              reply_markup=InlineKeyboardMarkup(inline_botn(user.id, user.username)))


def inline_handlerlar(update, context):
    # data = update.callback_query.data
    query = update.callback_query
    print(query.data)
    data = query.data.split("_")
    # pullar

    # lavash
    if data[0] == "lavash":
        print("user_id", data[1])
        print("user", data[2])
        query.message.edit_text('taomlardan birini tanlang',
                                reply_markup=InlineKeyboardMarkup(Lavash_botn(data[1], data[2])))
    if data[0] == "shaurma":
        print("user_id", data[1])
        print("user", data[2])
        query.message.edit_text("taomlardan birini tanlang",
                                reply_markup=InlineKeyboardMarkup(shaur_botn(data[1], data[2])))

    if data[0] == "burger":
        print("user_id", data[1])
        print("user", data[2])
        query.message.edit_text('taomlardan birini tanlang',
                                reply_markup=InlineKeyboardMarkup(burger_botn(data[1], data[2])))
    if data[0] == "danar":
        print("user_id", data[1])
        print("user", data[2])
        query.message.edit_text("taomlardan birini tanlang",
                                reply_markup=InlineKeyboardMarkup(Donar_botn(data[1], data[2])))

    if data[0] == "hotdog":
        print("user_id", data[1])
        print("user", data[2])
        query.message.edit_text('taomlardan birini tanlang',
                                reply_markup=InlineKeyboardMarkup(Hot_botn(data[1], data[2])))
    if data[0] == "haggi":
        print("user_id", data[1])
        print("user", data[2])
        query.message.edit_text("taomlardan birini tanlang",
                                reply_markup=InlineKeyboardMarkup(Hoggi_botn(data[1], data[2])))

    if data[0] == "fre":
        print("user_id", data[1])
        print("user", data[2])
        query.message.edit_text('taomlardan birini tanlang',
                                reply_markup=InlineKeyboardMarkup(Free_botn(data[1], data[2])))
    if data[0] == "cola":
        print("user_id", data[1])
        print("user", data[2])
        query.message.edit_text("taomlardan birini tanlang",
                                reply_markup=InlineKeyboardMarkup(Ichimlik_botn(data[1], data[2])))
    # AAAAAAAAAA
    if data[0] == "mini":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(mini)
        query.message.edit_text(f"{mini}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "big":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(big)
        query.message.edit_text(f"{big}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "oddiy":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(oddiy)
        query.message.edit_text(f"{oddiy}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "sirli":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(sirli)
        query.message.edit_text(f"{sirli}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))
    # shurma
    if data[0] == "tovuq":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(tovuqli)
        query.message.edit_text(f"{tovuqli}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "gosht":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(goshti)
        query.message.edit_text(f"{goshti}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))
    # burger
    if data[0] == "minni":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(bur_mini)
        query.message.edit_text(f"{bur_mini}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "bigg":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(bur_big)
        query.message.edit_text(f"{bur_big}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "ssirli":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(bur_sir)
        query.message.edit_text(f"{bur_sir}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "odddiy":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(bur_oddiy)
        query.message.edit_text(f"{bur_oddiy}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))
    # donar
    if data[0] == "kichik":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(donar_mini)
        query.message.edit_text(f"{donar_mini}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "katta":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(donar_big)
        query.message.edit_text(f"{donar_big}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "msous":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(donar_mini_s)
        query.message.edit_text(f"{donar_mini_s}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "bsous":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(donar_big_s)
        query.message.edit_text(f"{donar_big_s}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))
    # hotdog
    if data[0] == "oddiy":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(Xotdog_oddiy)
        query.message.edit_text(f"{Xotdog_oddiy}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "karalev":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(Xotdog_karalevski)
        query.message.edit_text(f"{Xotdog_karalevski}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "canada":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(Xotdok_canadsky)
        query.message.edit_text(f"{Xotdok_canadsky}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "qazi":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(Xotdog_qazi)
        query.message.edit_text(f"{Xotdog_qazi}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))
    # xaggi
    if data[0] == "minyi":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(xaggi_mini)
        query.message.edit_text(f"{xaggi_mini}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "bigi":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(xaggi_big)
        query.message.edit_text(f"{xaggi_big}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))
    # free
    if data[0] == "freee":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(free)
        query.message.edit_text(f"{free}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    # ichimliklar
    if data[0] == "1,5":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(cola15)
        query.message.edit_text(f"{cola15}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "1":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(cola1)
        query.message.edit_text(f"{cola1}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "0,5":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(cola05)
        query.message.edit_text(f"{cola05}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "butulka":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(cola_b)
        query.message.edit_text(f"{cola_b}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "f1,5":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(fanta15)
        query.message.edit_text(f"{fanta15}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "f1":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(fanta1)
        query.message.edit_text(f"{fanta1}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "f0,5":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(fanta05)
        query.message.edit_text(f"{fanta05}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "fbutulka":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(fanta_b)
        query.message.edit_text(f"{fanta_b}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "1L":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(Sok1)
        query.message.edit_text(f"{Sok1}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "soks":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(Sok_s)
        query.message.edit_text(f"{Sok_s}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "DARK":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(cofe_d)
        query.message.edit_text(f"{cofe_d}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "milk":
        print("user_id", data[1])
        print("user", data[2])
        jami.append(cofe_m)
        query.message.edit_text(f"{cofe_m}\n Yana biror narsa harid qiling ",
                                reply_markup=InlineKeyboardMarkup(inline_botn(data[1], data[2])))

    if data[0] == "all":
        print(jami)
        for i in jami:
            c = i.split()
            for j in c:
                if j.isdigit():
                    summa.append(int(j))
        s = ""
        for i in jami:
            s = f"{s}\n{i}"
        query.message.edit_text(f"Jami berilgan buyurtmalar\n{s}\n \n{sum(summa)} so`m")

    elif data[0] == "back1":
        query.message.edit_text(
            f"taomlardan birini tanlang",
            reply_markup=InlineKeyboardMarkup(inline_botn(user_id=data[1], user_name=data[2])))


def main():
    Token = "1920468384:AAFzSfKKliZd_y2tQxwvfN9kgdkzfyz-aG8"
    updater = Updater(Token)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(inline_handlerlar))
    updater.dispatcher.add_handler(MessageHandler(Filters.location, location_x))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
