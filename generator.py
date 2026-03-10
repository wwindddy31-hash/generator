#!/usr/bin/env python3
import random
import string
import time
import sys
import os
from datetime import datetime, timedelta

# ── ЦВЕТА ─────────────────────────────────────────────────────────
R  = '\033[1;31m'
P  = '\033[1;35m'
C  = '\033[1;36m'
W  = '\033[1;37m'
Y  = '\033[1;33m'
G  = '\033[1;32m'
D  = '\033[2;31m'
NC = '\033[0m'

# ── ТРАНСЛИТЕРАЦИЯ ────────────────────────────────────────────────
TRANS_TABLE = {
    'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e',
    'ж':'zh','з':'z','и':'i','й':'y','к':'k','л':'l','м':'m',
    'н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u',
    'ф':'f','х':'h','ц':'ts','ч':'ch','ш':'sh','щ':'sh','ъ':'',
    'ы':'y','ь':'','э':'e','ю':'yu','я':'ya'
}

def translit(text):
    return ''.join(TRANS_TABLE.get(c, c) for c in text.lower())

# ── БАННЕР ────────────────────────────────────────────────────────
def banner():
    os.system("clear")
    print(f"""
{R}  ██████╗ ███████╗███╗   ██╗{P}███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗{NC}
{R}  ██╔════╝ ██╔════╝████╗  ██║{P}██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗{NC}
{R}  ██║  ███╗█████╗  ██╔██╗ ██║{P}█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝{NC}
{R}  ██║   ██║██╔══╝  ██║╚██╗██║{P}██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗{NC}
{R}  ╚██████╔╝███████╗██║ ╚████║{P}███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║{NC}
{R}   ╚═════╝ ╚══════╝╚═╝  ╚═══╝{P}╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝{NC}
""")
    print(f"{D}  {'─'*65}{NC}")
    print(f"{P}  {'[ ГЕНЕРАТОР ТЕСТОВЫХ ДАННЫХ ]':^65}{NC}")
    print(f"{D}  {'─'*65}{NC}")
    print(f"{R}  Версия {W}:{P} 1.0{NC}")
    print(f"{D}  {'─'*65}{NC}\n")

# ── АНИМАЦИЯ ─────────────────────────────────────────────────────
def loading(text="Загрузка"):
    chars = ["⣾","⣽","⣻","⢿","⡿","⣟","⣯","⣷"]
    for i in range(16):
        sys.stdout.write(f"\r{R}  {chars[i % len(chars)]} {P}{text}...{NC}")
        sys.stdout.flush()
        time.sleep(0.07)
    print(f"\r{G}  ✓ {W}{text} завершена{NC}     ")

# ── ДАННЫЕ ────────────────────────────────────────────────────────
FIRST_M  = ["Александр","Дмитрий","Максим","Иван","Артём","Михаил","Никита","Алексей","Андрей","Сергей","Кирилл","Роман","Егор","Владимир","Павел"]
FIRST_F  = ["Анастасия","Мария","Анна","Виктория","Екатерина","Наталья","Ольга","Дарья","Юлия","Алина","Татьяна","Полина","Валерия","Ксения","Елена"]
LAST_M   = ["Иванов","Смирнов","Кузнецов","Попов","Васильев","Петров","Соколов","Михайлов","Новиков","Фёдоров","Морозов","Волков","Алексеев","Лебедев","Семёнов"]
LAST_F   = ["Иванова","Смирнова","Кузнецова","Попова","Васильева","Петрова","Соколова","Михайлова","Новикова","Фёдорова","Морозова","Волкова","Алексеева","Лебедева","Семёнова"]
MID_M    = ["Александрович","Дмитриевич","Иванович","Сергеевич","Андреевич","Михайлович","Алексеевич","Николаевич"]
MID_F    = ["Александровна","Дмитриевна","Ивановна","Сергеевна","Андреевна","Михайловна","Алексеевна","Николаевна"]
CITIES   = ["Москва","Санкт-Петербург","Новосибирск","Екатеринбург","Казань","Нижний Новгород","Челябинск","Самара","Омск","Ростов-на-Дону","Уфа","Красноярск","Воронеж"]
STREETS  = ["Ленина","Мира","Советская","Гагарина","Пушкина","Садовая","Молодёжная","Центральная","Школьная","Лесная","Набережная","Строителей","Победы","Кирова"]
DOMAINS  = ["gmail.com","mail.ru","yandex.ru","yahoo.com","outlook.com","rambler.ru","bk.ru","inbox.ru"]
NICK_PRE = ["cool","dark","light","super","mega","ultra","pro","best","fast","star","fire","ice","neo","void","ghost"]
NICK_SUF = ["boy","girl","man","pro","777","666","123","xd","lol","epic","gg","vip","top","king","hack"]

def gen_name():
    g = random.choice(["m","f"])
    if g == "m":
        return f"{random.choice(LAST_M)} {random.choice(FIRST_M)} {random.choice(MID_M)}", "♂"
    return f"{random.choice(LAST_F)} {random.choice(FIRST_F)} {random.choice(MID_F)}", "♀"

def gen_email(name):
    base = translit(name.split()[1])
    return f"{base}{random.randint(1,999)}@{random.choice(DOMAINS)}"

def gen_phone():
    ops = ["900","901","902","903","905","906","908","909","910",
           "911","912","913","914","915","916","917","918","919","920",
           "921","922","923","924","925","926","927","928","929","930",
           "950","951","952","953","960","961","962","963","964","965",
           "985","986","987","988","989","999"]
    op = random.choice(ops)
    n  = "".join([str(random.randint(0,9)) for _ in range(7)])
    return f"+7 ({op}) {n[:3]}-{n[3:5]}-{n[5:7]}"

def gen_address():
    return f"г. {random.choice(CITIES)}, ул. {random.choice(STREETS)}, д. {random.randint(1,150)}, кв. {random.randint(1,200)}"

def gen_birthday():
    start = datetime(1970,1,1)
    bd    = start + timedelta(days=random.randint(0,(datetime(2005,12,31)-start).days))
    return bd.strftime("%d.%m.%Y")

def gen_nickname():
    s = random.randint(1,4)
    if s == 1: return f"{random.choice(NICK_PRE)}_{random.choice(NICK_SUF)}"
    if s == 2: return "".join(random.choices(string.ascii_lowercase, k=random.randint(4,8))) + str(random.randint(10,9999))
    if s == 3: return random.choice(NICK_PRE) + str(random.randint(100,9999))
    return "".join(random.choices(string.ascii_lowercase, k=random.randint(5,10)))

# ── ГЕНЕРАЦИЯ ─────────────────────────────────────────────────────
def generate(count):
    loading("Генерация данных")
    print()
    for i in range(count):
        name, gender = gen_name()
        email = gen_email(name)
        print(f"{D}  ╔{'═'*50}╗{NC}")
        print(f"{D}  ║{R}  [ ЗАПИСЬ #{str(i+1).zfill(2)} ] {gender}  {D}{' '*(36-len(str(i+1)))}║{NC}")
        print(f"{D}  ╠{'═'*50}╣{NC}")
        print(f"{D}  ║{NC}  {R}►{W} Имя        {R}:{P} {name:<35}{D}║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} Email      {R}:{P} {email:<35}{D}║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} Телефон    {R}:{P} {gen_phone():<35}{D}║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} Адрес      {R}:{C} {gen_address():<35}{D}║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} Дата рожд  {R}:{Y} {gen_birthday():<35}{D}║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} Никнейм    {R}:{G} {gen_nickname():<35}{D}║{NC}")
        print(f"{D}  ╚{'═'*50}╝{NC}\n")
        time.sleep(0.1)

# ── МЕНЮ ─────────────────────────────────────────────────────────
def menu():
    banner()
    print(f"{D}  {'─'*40}{NC}")
    print(f"  {R}[{W}01{R}]{NC} {P}►{W} Сгенерировать 1 запись")
    print(f"  {R}[{W}02{R}]{NC} {P}►{W} Сгенерировать 5 записей")
    print(f"  {R}[{W}03{R}]{NC} {P}►{W} Сгенерировать 10 записей")
    print(f"  {R}[{W}04{R}]{NC} {P}►{W} Своё количество")
    print(f"  {R}[{W}00{R}]{NC} {P}►{W} Выход")
    print(f"{D}  {'─'*40}{NC}")
    print(f"\n  {R}anubis{P}@{R}generator{W} ~# {NC}", end="")

def main():
    while True:
        menu()
        try:
            choice = input().strip()
        except KeyboardInterrupt:
            print(f"\n\n  {R}[{W}!{R}]{P} Выход...{NC}\n")
            sys.exit(0)

        if choice == "00":
            print(f"\n  {R}[{W}!{R}]{P} Выход...{NC}\n")
            sys.exit(0)
        elif choice == "01":
            print()
            generate(1)
        elif choice == "02":
            print()
            generate(5)
        elif choice == "03":
            print()
            generate(10)
        elif choice == "04":
            print(f"\n  {R}[{W}?{R}]{P} Введите количество (1-50): {W}", end="")
            try:
                n = int(input().strip())
                n = max(1, min(n, 50))
                print()
                generate(n)
            except (ValueError, KeyboardInterrupt):
                print(f"\n  {R}[{W}!{R}]{P} Неверный ввод{NC}")
        else:
            print(f"\n  {R}[{W}!{R}]{P} Неверный выбор{NC}")

        print(f"\n  {R}[{W}↵{R}]{P} Нажмите Enter...{NC}", end="")
        try:
            input()
        except KeyboardInterrupt:
            sys.exit(0)

if __name__ == "__main__":
    main()
