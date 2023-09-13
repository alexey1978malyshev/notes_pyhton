
from os.path import join, abspath, dirname
import pandas as pd
from functions_notes import functions


key_count = 0
phone_dict = {1: ['Иванов', 'Иван', '+7(900)95686596', 'дуралей'],
              2: ['Петров', 'Петр', '+7(253)565685475', 'умник'],
              3: ['Соколов', 'Илья', '+7/655/656565848777', 'жадина']}


def input_users() -> list:
    user_input = []
    user_input.append(input("Введите имя пользователя: "))
    user_input.append(input("Введите фамилию пользователя: "))
    user_input.append(input("Введите телефон пользователя: "))
    user_input.append(input("Введите описание пользователя: "))

    return user_input


# print(input_users())

def create(phone_dict_loc: dict, user: list, idc: int) -> dict:
    idc += 1
    phone_dict_loc[idc] = user
    return phone_dict_loc, idc


def menu():
    phone_dict = {1: ['Иванов', 'Иван', '+7(900)95686596', 'дуралей'],
                  2: ['Петров', 'Петр', '+7(253)565685475', 'умник'],
                  3: ['Соколов', 'Илья', '+7/655/656565848777', 'жадина'],
                  4: ['Савельев', 'Илья', '+7*585*5455/65852', 'странный']}
    key_count = len(phone_dict)
    print("Введите 0 ,если хотите выйти ")
    print("Введите 1 ,если хотите добавить абонента ")
    print("Введите 2 ,если хотите распечатать справочник ")
    print("Введите 3 ,если хотите записать данные в файл ")
    print("Введите 4 для поиска ")
    print("Введите 5 для удаления ")
    print("Введите 6 для изменения записи ")

    while True:
        num = int(input("Выберите операцию: "))
        if num == 0:
            break
        if num == 1:
            user = input_users()
            phone_dict, key_count = create(phone_dict, user, key_count)
        if num == 2:
            print(phone_dict)
        if num == 3:
            file_name = input("Введите имя файла: ")
            export_phone_dict(phone_dict, file_name)
        if num == 4:
            search = input("Кого ищем? \n")
            print(search_user(phone_dict, search))
        if num == 5:
            user_for_del = input("Кого удалим? \n")
            delete_user(phone_dict, user_for_del)
        if num == 6:
            user_for_up = input("Чью запись перекошмарим???\n")
            update_user(phone_dict, user_for_up)


def export_phone_dict(phone_dict: dict, file_name: str):
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, file_name + '.txt')
    with open(full_name, mode='w', encoding='utf-8') as file:
        for key, val in phone_dict.items():
            file.write(f"{key},{val[0]},{val[1]},{val[2]},{val[3]}\n")


def export_phone_dict_to_csv(phone_dict: dict, file_name: str):
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, file_name + '.csv')
    df = pd.DataFrame(phone_dict)
    df.to_csv(full_name, index=False, header=True)

def import_from_csv(file_name):
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, file_name + '.csv')
    df = pd.read_csv(full_name, index_col=False)
    print(df)
def search_user(phone_dict: dict, searchstr: str) -> int:
    for key, val in phone_dict.items():
        if val[0].startswith(searchstr):
            return key


def delete_user(phone_dict: dict, delete_user: str):
    for key, val in phone_dict.items():
        if val[0].startswith(delete_user):
            del phone_dict[key]
            break


def update_user(phone_dict: dict, up_user: str):
    for key, val in phone_dict.items():
        if val[0].startswith(up_user):
            val.clear()
            val.append(input("Введите фамилию"))
            val.append(input("Введите Имя"))
            val.append(input("Введите тф"))
            val.append(input("Введите описание"))


#
# print(phone_dict)
# print(search_user(phone_dict,'д'))
#menu()
# export_phone_dict(phone_dict, "phones")
#export_phone_dict_to_csv(phone_dict, "phones11")
#import_from_csv("phones11")
# print(update_user(phone_dict, 'Пе'))
# print(phone_dict)












