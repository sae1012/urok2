def task1():
    name = str(input("Введите ФИО: "))
    if name.count(" ") > 1:
        print(name[0:name.find(" ")] + " " + name[name.find(" ") + 1] + "." + " " + name[name.find(" ") + 1] + ".")
    else:
        print(name[0:name.find(" ")] + " " + name[name.find(" ") + 1] + ".")

def task2():
    num = int(input("Введите число: "))
    count = 0
    if 51 < num < 100:
        for ten in range(num // 10 + 1):
            for five in range((num - ten*10) // 5 + 1):
                for two in range(num - ten*10 - five * 5):
                    one = num -(ten * 10 + five * 5 + two * 2)
                    count += 1
                    print(ten, " ", five, " ", two, " ", one, " ")
    print(count)

def task5():
    print("Введите оценки: ")
    grades = list()
    a_count, b_count, c_count, f_count = 0
    for item in range(22):
        grades += input()
    for grade in grades:
        if grade == "5":
            a_count += 1
        if grade == "4":
            b_count += 1
        if grade == "3":
            c_count += 1
        if grade == "2":
            f_count += 1

    print("Пятёрки: ", a_count, "\n", "Четвёрки: ", b_count, "\n", "Тройки: ", c_count, "\n", "Двойки: ", f_count)

def task8():
    num = int(input("Введите число: "))
    if 1 <= num <= 1188 and num % 1 == 0:
        year = ""
        month = ""

        if (num // 12) % 10 == 1 or num // 12 == 1:
            year = "год"
        if 5 < (num // 12) % 10 < 20:
            year = "лет"
        if 1 < (num // 12) % 10 < 5:
            year = "года"

        if num % 12 == 1 or (num % 12) % 10 == 1:
            month = "месяц"
        if 5 < (num % 12) % 10 < 20:
            month = "месяца"
        if 1 < (num % 12) % 10 < 5:
            month = "месяцев"
        if (num % 12) % 10 == 0 or num % 12 == 0:
            month = "месяцев"
        print(num // 12, " ", year, num % 12, " ", month)

def task9():
    url = str(input("Введите URL: "))
    protocol = url[0:url.find("://")]
    if protocol == "https":
        security = "(защищённый)"
    else:
        security = "(незащищённый)"
    host = url[url.find("/") + 2:url.find("/", 8)]
    end_point = url[url.find("/", 8):url.find("?")]
    args = url[url.find("?") + 1:len(url)]
    args = args.replace("&", "; ")
    print("Протокол: ", protocol, " ", security, "\n", "Хост: ", host, "\n", "End point: ", end_point, "\n", "Args: ", args)

task9()