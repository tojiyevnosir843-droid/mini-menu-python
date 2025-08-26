def yigindi(a, b):
    return a + b

def katta_son(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Ikkalasi teng"

def kvadrat(x):
    return x ** 2

while True:
    print("\n--- Mini menyu ---")
    print("1. Yig'indi hisoblash")
    print("2. Katta sonni topish")
    print("3. Kvadrat hisoblash")
    print("4. Chiqish")

    tanlov = int(input("Tanlang: "))

    if tanlov == 1:
        a = int(input("1-sonni kiriting: "))
        b = int(input("2-sonni kiriting: "))
        print("Yig'indi:", yigindi(a, b))

    elif tanlov == 2:
        a = int(input("1-sonni kiriting: "))
        b = int(input("2-sonni kiriting: "))
        print("Katta son:", katta_son(a, b))

    elif tanlov == 3:
        x = int(input("Son kiriting: "))
        print("Kvadrati:", kvadrat(x))

    elif tanlov == 4:
        print("Dastur tugadi.")
        break

    else:
        print("Noto‘g‘ri tanlov!")
