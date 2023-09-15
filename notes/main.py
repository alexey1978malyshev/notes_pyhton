# /*Задание
# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента.


import functions
import datetime

key_count = 0

def menu():

    note_dict = {}
    key_count = len(note_dict)
    print("Введите 0 ,если хотите выйти ")
    print("Введите 1 ,если хотите добавить заметку ")
    print("Введите 2 ,если хотите распечатать книгу заметок ")
    print("Введите 3 ,если хотите записать заметку в файл ")
    print("Введите 4 для поиска по названию ")
    print("Введите 5 для удаления ")
    print("Введите 6 для изменения записи ")

    while True:
        num = int(input("Выберите операцию: "))
        if num == 0:
            break
        if num == 1:
            note = functions.input_note()
            note_dict, key_count = functions.create(note_dict, note, key_count)
        if num == 2:
            functions.read_from_csv('test')
            #print(note_dict)
        if num == 3:
            file_name = input("Введите имя файла: ")
            functions.export_note_dict_to_csv(note_dict, file_name)
        if num == 4:
            search = input("Что ищем? \n")
            print(functions.search_note_by_name(note_dict, search))
        if num == 5:
            user_for_del = input("Какую запись удалим? \n")
            functions.delete_note_by_name(note_dict, user_for_del)
        if num == 6:
            note_for_up = input("Какую запись обновим?\n")
            functions.note_for_up(note_dict, user_for_up)


menu()

