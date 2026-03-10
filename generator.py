#!/usr/bin/env python3
import random
import string
import time
import sys
import os
import hashlib
import base64
import uuid
import json
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
    print(f"{R}  Версия {W}:{P} 2.0{NC}")
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

# ── ГЕНЕРАЦИЯ ЛИЧНЫХ ДАННЫХ ───────────────────────────────────────
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

# ══════════════════════════════════════════════════════════════════
# ── ХАКЕРСКИЕ ФУНКЦИИ ─────────────────────────────────────────────
# ══════════════════════════════════════════════════════════════════

# ── ГЕНЕРАТОР ПАРОЛЕЙ ─────────────────────────────────────────────
def gen_password(length=16, use_special=True):
    chars = string.ascii_letters + string.digits
    if use_special:
        chars += "!@#$%^&*()-_=+[]{}|;:,.<>?"
    while True:
        pwd = ''.join(random.choices(chars, k=length))
        if (any(c.isupper() for c in pwd) and
            any(c.islower() for c in pwd) and
            any(c.isdigit() for c in pwd)):
            return pwd

def password_strength(pwd):
    score = 0
    if len(pwd) >= 12: score += 1
    if len(pwd) >= 16: score += 1
    if any(c.isupper() for c in pwd): score += 1
    if any(c.islower() for c in pwd): score += 1
    if any(c.isdigit() for c in pwd): score += 1
    if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?" for c in pwd): score += 1
    if score <= 2: return f"{R}СЛАБЫЙ{NC}"
    if score <= 4: return f"{Y}СРЕДНИЙ{NC}"
    return f"{G}СИЛЬНЫЙ{NC}"

def generate_passwords():
    loading("Генерация паролей")
    print()
    configs = [
        (8,  False, "Простой   "),
        (12, False, "Средний   "),
        (16, True,  "Сложный   "),
        (20, True,  "Максимум  "),
        (32, True,  "Параноик  "),
    ]
    print(f"{D}  ╔{'═'*58}╗{NC}")
    print(f"{D}  ║{R}  [ ГЕНЕРАТОР ПАРОЛЕЙ ]  {D}{' '*34}║{NC}")
    print(f"{D}  ╠{'═'*58}╣{NC}")
    for length, special, label in configs:
        pwd = gen_password(length, special)
        strength = password_strength(pwd)
        print(f"{D}  ║{NC}  {R}►{W} {label} {R}:{NC} {C}{pwd:<32}{NC} [{strength}]{D}  ║{NC}")
    print(f"{D}  ╚{'═'*58}╝{NC}\n")

# ── ГЕНЕРАТОР ХЕШЕЙ ───────────────────────────────────────────────
def generate_hashes():
    loading("Генерация хешей")
    print()
    word = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
    data = word.encode()
    hashes = {
        "MD5    ": hashlib.md5(data).hexdigest(),
        "SHA1   ": hashlib.sha1(data).hexdigest(),
        "SHA256 ": hashlib.sha256(data).hexdigest(),
        "SHA512 ": hashlib.sha512(data).hexdigest()[:52] + "...",
    }
    print(f"{D}  ╔{'═'*58}╗{NC}")
    print(f"{D}  ║{R}  [ ХЕШИ ДЛЯ: {W}{word}{R} ]  {D}{' '*(33-len(word))}║{NC}")
    print(f"{D}  ╠{'═'*58}╣{NC}")
    for algo, h in hashes.items():
        print(f"{D}  ║{NC}  {R}►{W} {algo} {R}:{P} {h:<43}{D}║{NC}")

    # Также покажем Base64
    b64 = base64.b64encode(data).decode()
    print(f"{D}  ║{NC}  {R}►{W} BASE64  {R}:{Y} {b64:<43}{D}║{NC}")
    print(f"{D}  ╚{'═'*58}╝{NC}\n")

# ── ГЕНЕРАТОР IP И MAC ────────────────────────────────────────────
def gen_ipv4():
    return f"{random.randint(1,254)}.{random.randint(0,254)}.{random.randint(0,254)}.{random.randint(1,254)}"

def gen_ipv6():
    groups = [f"{random.randint(0,65535):04x}" for _ in range(8)]
    return ":".join(groups)

def gen_mac():
    mac = [random.randint(0,255) for _ in range(6)]
    mac[0] = mac[0] & 0xFE  # unicast
    return ":".join(f"{b:02X}" for b in mac)

def gen_subnet():
    prefixes = [8, 16, 24]
    p = random.choice(prefixes)
    if p == 8:
        return f"{random.randint(10,10)}.0.0.0/{p}"
    elif p == 16:
        return f"172.{random.randint(16,31)}.0.0/{p}"
    else:
        return f"192.168.{random.randint(0,255)}.0/{p}"

def generate_network():
    loading("Генерация сетевых данных")
    print()
    print(f"{D}  ╔{'═'*58}╗{NC}")
    print(f"{D}  ║{R}  [ СЕТЕВЫЕ ИДЕНТИФИКАТОРЫ ]  {D}{' '*29}║{NC}")
    print(f"{D}  ╠{'═'*58}╣{NC}")
    for i in range(1, 6):
        ipv4   = gen_ipv4()
        ipv6   = gen_ipv6()
        mac    = gen_mac()
        subnet = gen_subnet()
        port   = random.choice([22, 80, 443, 3306, 5432, 6379, 8080, 8443, 27017])
        print(f"{D}  ║{R}  ─── Хост #{i} ─────────────────────────────────────{D}║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} IPv4    {R}:{G} {ipv4:<43}{D}║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} IPv6    {R}:{C} {ipv6[:43]:<43}{D}║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} MAC     {R}:{Y} {mac:<43}{D}║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} Subnet  {R}:{P} {subnet:<43}{D}║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} Port    {R}:{R} {str(port):<43}{D}║{NC}")
    print(f"{D}  ╚{'═'*58}╝{NC}\n")

# ── ГЕНЕРАТОР UUID / ТОКЕНОВ ──────────────────────────────────────
def gen_api_key(prefix="sk"):
    body = ''.join(random.choices(string.ascii_letters + string.digits, k=40))
    return f"{prefix}-{body}"

def gen_jwt_mock():
    header  = base64.urlsafe_b64encode(json.dumps({"alg":"HS256","typ":"JWT"}).encode()).decode().rstrip("=")
    payload = base64.urlsafe_b64encode(json.dumps({
        "sub": str(uuid.uuid4()),
        "iat": int(time.time()),
        "exp": int(time.time()) + 3600,
        "role": random.choice(["admin","user","moderator"])
    }).encode()).decode().rstrip("=")
    sig = ''.join(random.choices(string.ascii_letters + string.digits + "-_", k=43))
    return f"{header}.{payload}.{sig}"

def generate_tokens():
    loading("Генерация токенов и UUID")
    print()
    print(f"{D}  ╔{'═'*65}╗{NC}")
    print(f"{D}  ║{R}  [ ТОКЕНЫ / UUID / API КЛЮЧИ ]  {D}{' '*32}║{NC}")
    print(f"{D}  ╠{'═'*65}╣{NC}")
    for i in range(1, 4):
        u4    = str(uuid.uuid4())
        u1    = str(uuid.uuid1())
        api1  = gen_api_key("sk")
        api2  = gen_api_key("pk")
        token = ''.join(random.choices(string.ascii_letters + string.digits, k=64))
        jwt   = gen_jwt_mock()
        print(f"{D}  ║{R}  ─── Набор #{i} {'─'*52}{D}║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} UUID v4  {R}:{P} {u4}{D}  ║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} UUID v1  {R}:{C} {u1}{D}  ║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} API sk   {R}:{G} {api1:<55}{D}║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} API pk   {R}:{G} {api2:<55}{D}║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} Token    {R}:{Y} {token[:55]:<55}{D}║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} JWT      {R}:{R} {jwt[:55]}...{D}║{NC}")
    print(f"{D}  ╚{'═'*65}╝{NC}\n")

# ── ГЕНЕРАТОР КАРТ (ТЕСТОВЫЕ НОМЕРА LUHN) ─────────────────────────
def luhn_checksum(number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    total = sum(odd_digits)
    for d in even_digits:
        total += sum(digits_of(d * 2))
    return total % 10

def gen_card_number(prefix):
    number = prefix + [random.randint(0,9) for _ in range(15 - len(prefix))]
    check  = (10 - luhn_checksum(int(''.join(map(str, number)) + '0'))) % 10
    number.append(check)
    n = ''.join(map(str, number))
    return f"{n[:4]} {n[4:8]} {n[8:12]} {n[12:]}"

def gen_cvv():
    return str(random.randint(100, 999))

def gen_card_expiry():
    now = datetime.now()
    m   = random.randint(1, 12)
    y   = now.year + random.randint(1, 5)
    return f"{m:02d}/{str(y)[2:]}"

def generate_cards():
    loading("Генерация тестовых карт")
    print()
    cards = [
        ("VISA",       [4]),
        ("MasterCard", [5, random.randint(1,5)]),
        ("MIR",        [2, 2]),
        ("VISA",       [4]),
        ("MasterCard", [5, random.randint(1,5)]),
    ]
    print(f"{D}  ╔{'═'*58}╗{NC}")
    print(f"{D}  ║{R}  [ ТЕСТОВЫЕ НОМЕРА КАРТ (LUHN) ]  {D}{' '*23}║{NC}")
    print(f"{D}  ║{Y}  ⚠  Только для тестирования платёжных форм!  {D}       ║{NC}")
    print(f"{D}  ╠{'═'*58}╣{NC}")
    for label, prefix in cards:
        num    = gen_card_number(prefix)
        expiry = gen_card_expiry()
        cvv    = gen_cvv()
        holder, _ = gen_name()
        holder_t  = translit(holder).upper()[:26]
        print(f"{D}  ║{R}  ► {W}{label:<12}{R}:{NC}")
        print(f"{D}  ║{NC}    {C}Номер  {R}: {P}{num:<35}{D}  ║{NC}")
        print(f"{D}  ║{NC}    {C}Срок   {R}: {Y}{expiry:<35}{D}  ║{NC}")
        print(f"{D}  ║{NC}    {C}CVV    {R}: {R}{cvv:<35}{D}  ║{NC}")
        print(f"{D}  ║{NC}    {C}Имя    {R}: {G}{holder_t:<35}{D}  ║{NC}")
        print(f"{D}  ║{'─'*58}║{NC}")
    print(f"{D}  ╚{'═'*58}╝{NC}\n")

# ── ГЕНЕРАТОР ДАННЫХ ДЛЯ РЕГИСТРАЦИИ ─────────────────────────────
def generate_reg_data():
    loading("Генерация данных для регистрации")
    print()
    print(f"{D}  ╔{'═'*58}╗{NC}")
    print(f"{D}  ║{R}  [ ДАННЫЕ ДЛЯ РЕГИСТРАЦИИ ]  {D}{' '*29}║{NC}")
    print(f"{D}  ╠{'═'*58}╣{NC}")
    for i in range(1, 4):
        name, gender = gen_name()
        email  = gen_email(name)
        nick   = gen_nickname()
        pwd    = gen_password(14, True)
        bd     = gen_birthday()
        phone  = gen_phone()
        sec_q  = random.choice([
            "Имя первого питомца",
            "Девичья фамилия матери",
            "Любимый город детства",
            "Кличка вашей собаки",
        ])
        sec_a  = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5,9)))
        print(f"{D}  ║{R}  ─── Аккаунт #{i} {'─'*41}{D}║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} Логин    {R}:{G} {nick:<43}{D}║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} Email    {R}:{P} {email:<43}{D}║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} Пароль   {R}:{C} {pwd:<43}{D}║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} Имя      {R}:{W} {name:<43}{D}║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} Дата рожд{R}:{Y} {bd:<43}{D}║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} Телефон  {R}:{P} {phone:<43}{D}║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} Вопрос   {R}:{D} {sec_q:<43}{NC}{D}║{NC}")
        print(f"{D}  ║{NC}  {R}►{W} Ответ    {R}:{R} {sec_a:<43}{D}║{NC}")
    print(f"{D}  ╚{'═'*58}╝{NC}\n")

# ══════════════════════════════════════════════════════════════════
# ── МЕНЮ ─────────────────────────────────────────────────────────
# ══════════════════════════════════════════════════════════════════
def menu():
    banner()
    print(f"{D}  {'─'*50}{NC}")
    print(f"  {R}[{W}01{R}]{NC} {P}►{W} Сгенерировать 1 запись")
    print(f"  {R}[{W}02{R}]{NC} {P}►{W} Сгенерировать 5 записей")
    print(f"  {R}[{W}03{R}]{NC} {P}►{W} Сгенерировать 10 записей")
    print(f"  {R}[{W}04{R}]{NC} {P}►{W} Своё количество")
    print(f"{D}  {'─'*50}{NC}")
    print(f"  {R}[{W}05{R}]{NC} {P}►{W} Генератор паролей")
    print(f"  {R}[{W}06{R}]{NC} {P}►{W} Генератор хешей (MD5/SHA/BASE64)")
    print(f"  {R}[{W}07{R}]{NC} {P}►{W} Генератор сетевых данных (IP/MAC)")
    print(f"  {R}[{W}08{R}]{NC} {P}►{W} Генератор токенов (UUID/JWT/API)")
    print(f"  {R}[{W}09{R}]{NC} {P}►{W} Генератор тестовых карт (LUHN)")
    print(f"  {R}[{W}10{R}]{NC} {P}►{W} Генератор данных для регистрации")
    print(f"{D}  {'─'*50}{NC}")
    print(f"  {R}[{W}00{R}]{NC} {P}►{W} Выход")
    print(f"{D}  {'─'*50}{NC}")
    print(f"\n  {R}root{P}@{R}generator{W} ~# {NC}", end="")

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
        elif choice == "05":
            print()
            generate_passwords()
        elif choice == "06":
            print()
            generate_hashes()
        elif choice == "07":
            print()
            generate_network()
        elif choice == "08":
            print()
            generate_tokens()
        elif choice == "09":
            print()
            generate_cards()
        elif choice == "10":
            print()
            generate_reg_data()
        else:
            print(f"\n  {R}[{W}!{R}]{P} Неверный выбор{NC}")

        print(f"\n  {R}[{W}↵{R}]{P} Нажмите Enter...{NC}", end="")
        try:
            input()
        except KeyboardInterrupt:
            sys.exit(0)

if __name__ == "__main__":
    main()
