import os
def tozalash():
    os.system("clear")

tozalash()

file = open("nomi.txt")
qator1 = file.readline()
qator2 = file.readline()

qator1 = qator1[:-1]       # qatorni tozalab olish
qator2 = qator2.strip()    # qatorni tozalab olish

login = qator1.split("=")[-1]
parol = qator2.split("=")[-1]

input_login = input("Enter your login: ").lower().strip()
input_password = input("Enter your password: ").strip()

while input_login != login or input_password != parol:
    tozalash()
    print("Iltimos qayta urinib ko'ring!\n")
    input_login = input("Enter your login: ").lower().strip()
    input_password = input("Enter your password: ").strip()

tozalash()
print("Tabriklaymiz siz tizimga kirdingiz!")
ha_yoq = input("Account ni o'zgartirishni hohlaysizmi? [h/y]").strip()
input_options = ["h", "ha", "yoq, y"]
while ha_yoq not in input_options:
    print("Siz noto'g'ri tugmani bostingiz, iltimoz ko'rsatilgan yugmalardan birini kiriting: ")







