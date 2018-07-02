#Данная программа создана для генерации фейковой базы данных объемом в 500 человек, каждый из которых имеет 15 параметров
#Программа будет иметь два вида доступа: администратор и пользователь. Их функции будут расписаны в самой программе
MENU_ADMIN =  (
    """
    0 - Выход
    1 - Генерация базы данных
    2 - Удаление элеметов
    3 - Редактирование
    4 - Чтение
    5 - Добавить новоего участника
    """
    )
MENU_USER = (
    """
    0 - Выход
    1 - Чтение
    2 - Редактирование
"""
    )
print ("""
                База данных Arisha
-------------------------------------------------------
Вы пытаетесь войти в базу данных клиентов. Пожалуйста подтвердите Ваш статус!
""")
#ввод пароля
password = str(input("Введите пароль: "))
if password == "admin":
    print("\nВы вошли как администратор. Добро пожаловать!")
    choice = None
    while choice != "0":
        choice2 = None
        print(MENU_ADMIN)
        choice = input("Ваш выбор: ")
        print()
        #выход из базы
        if choice == "0":
            print("\nВы вышли из базы")
        elif choice == "4":
            doc = open(r"C:\Users\Ариша\Desktop\Рабочий стол\Политех\DLP-light\test.txt", "r")
            data = doc.read()
            print(data)
        elif choice == "5":
            doc = open(r"C:\Users\Ариша\Desktop\Рабочий стол\Политех\DLP-light\test.txt", "w")
            doc.write("New file!")
            doc.close()
elif password  == "user":
    print("\nВы вошли как пользователь. Добро пожаловать!")
    choice = None
    while choice != "0":
        choice2 = None
        print(MENU_USER)
        choice = input("Ваш выбор: ")
        print()
        #выход из базы
        if choice == "0":
            print("\nВы вышли из базы")
        elif choice == "1":
            doc = open(r"C:\Users\Ариша\Desktop\Рабочий стол\Политех\DLP-light\test.txt", "r")
            data = doc.read()
            print(data)
else:
    print("\nСтатус не подтвержден. Вам необходимо снова войти в базу для подтверждения")
   

        
    

