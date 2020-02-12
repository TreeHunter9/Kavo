i = int(input())
if i == 1:
    print("Привет, мир!")

    ####################################################################

elif i == 2:
    a = None
    b = 1
    c = 1.1
    d = "1234"
    e = [1, 2, 3, 4]
    f = (True, False, 1)
    g = {1:"Артём", 2:"Стас"}
    i = {1, 2, 3, 4}
    print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(i), sep='\n')
    print(float(b), int(c), sep='\n')
    print(str(c), float(d), sep='\n')
    print(len(d), len(e), len(f), len(g), len(i))
    print(d[::3], e[::3], f[::2])
    print(d[1:3], e[1:3], f[1:2])
    #print(g[0]) # Исправить

    ########################################################################

elif i == 3:
    a = True
    b = False
    print(a,b)
    print(a and b, a or b, not a, not b, sep='\n')
    a = 2
    b = 4
    print(a == b, a != b, a > b, a < b, b >= a, b <= a)
    print(a + b, a - b, a * b, a / b, a**b, a % b, a // b)

    #########################################################################

elif i == 4:
    a = int(input())
    if a > 100 or a < -100:
        print("Число не входит в диапозон [-100; 100]")
    elif a < -50:
        print("Число меньше -50")
    elif a == -50:
        print("Число равно -50")
    elif a < 0 and a > -50:
        print("Число меньше 0, но больше -50")
    elif a > 0 and a < 50:
        print("Число больше 0, но меньше 50")
    elif a == 50:
        print("Число равно 50")
    elif a > 50:
        print("Число больше 50")
    else:
        print("Число равно 0")

    #####################################################################

elif i == 5:
    for a in range(0, 11):
        print(a)
    a = 0
    while a <= 10:
        print(a)
        a += 1
    print("Введите ФИО")
    n = str(input())
    for a in n:
        print(a, end="")
    print()
    l = ["Иванов АА", "Стас ГА"]
    for l_mini in l:
        print(l_mini)
    d = {"Артём":"13.12.10","Стас":"24.04.25"}
    for key, item in d.items():
        if int(item[3:5]) == 1 or int(item[3:5]) == 2 or int(item[3:5]) == 12 or int(item[3:5]) == 6 or int(item[3:5]) == 7 or int(item[3:5]) == 8:
            print(key)

    ####################################################################################

elif i == 6:
    def Hello():
        print("Привет, мир!")
    Hello()    
    def MyName(name):
        print(name)
    MyName("Артём")
    def Disc(a, b, c):
        D = b**2 - 4*a*c
        return D
    print(Disc(2,4,2))
    def User():
        print("Введите имя", end=" ")
        name = str(input())
        print("Введите свой возраст", end=" ")
        age = str(input())
        return name + " " + age
    print(User())
    def Alf(a):
        alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        return alf[a-1]
    print(Alf(2))

    ##########################################################################

elif i == 7:
    a = "Иванов Артём Игоревич"
    print(len(a))
    print(a + "123")
    print(a[7:12])
    print(a.upper())
    print(a.split(" "))

    #########################################################################

elif i == 8:
    l = [None, 1, 2.2, "абв", [1,2,3], (3, 2, 1), {1:"a", 2:"б"}]
    for a in l:
        print(type(a))
    l.pop()
    a = "Иванов Артём Игоревич"
    l2 = []
    for a_mini in a:
        l2.append(a_mini)
    b = ""
    for l2_mini in l2:
        b += l2_mini
    i = 0
    for a_mini in a:
        print(i, a_mini)
        i += 1
    print(l2.count("а"))

    ########################################################################

elif i == 9:
    i = 0
    l = [i*2 - 1 for i in range(1,51)]
    print(l)

    ##############################################################################

elif i == 10:
    a = int(input())
    b = int(input())
    try:
        c = a / b
    except:
        print("Вы поделили на 0")
    else:
        print(c)
