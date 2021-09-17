documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

def people_name():
    doc_number = input("Введите номер дркумента: ")
    for request in documents:
        if doc_number == request["number"]:
            print(f'По вашему запросу {doc_number}  найден: {request["name"]}')
            return request["name"]

def search_shelf():
    doc_number = input("Введите номер документа: ")
    for key,value in directories.items():
        if doc_number in value:
            print(f'По вашему запросу {doc_number} документ лежит на : {key} полке')
            doc = 1
            break
        else:
            doc = 0
    if doc == 0:
        print(f"Документа с номером {doc_number} нет на полках")

def add_people():
    type_doc = input("Введите тип документа: ")
    number = input("Введите номер документа: ")
    name = input("Введите имя владельца: ")
    shelf = input("На какйю полку поставить документ: ")
    new_doc = {"type":type_doc, "number":number, "name":name}
    if shelf in directories:
        documents.append(new_doc)
        directories[shelf].append(number)
        # print(directories, "\n", documents)
        print(f"Документ {type_doc} с номером:{number} принадлежащий {name} добавлен на {shelf} полку")
        return True
    else:
        return False
    # if flag is False:
    #     print("Такой полки нет")

def all_docs():
    for str_value in documents:
        for key, value in str_value.items():
            print(value, end=" ")
        print()

def del_doc():
    num_shelf = 0
    doc_number = input("Введите номер документа который хотите удалить: ")
    for request in documents:
        if doc_number == request["number"]:
            documents.remove(request)
            for key, value in directories.items():
                if doc_number in value:
                    num_shelf = key
                    directories[key].remove(doc_number)
            print(f"Документ №{doc_number} удален с полки {num_shelf}")
            return doc_number
    print("Такого документа нет")
    return False


def replace_doc():
    flag = False
    doc_number = input("Введите номер документа для перемещения: ")
    for request in documents:
        if doc_number == request["number"]:
            flag = True
            break
    if not flag:
        print("Такого документа нет")
        return
    num_shelf = input("Введите номер полки, на которую хотите переместить документ: ")
    if num_shelf not in directories.keys():
         print("Такой полки нет")
         return
    for key, value in directories.items():
        if doc_number in value and num_shelf != key:
            directories[key].remove(doc_number)
            directories[num_shelf].append(doc_number)
            print(f"Документ № {doc_number} перемещен на {num_shelf} полку")
            return
    print(f"Документ № {doc_number} уже находится на полке № {num_shelf}")


def add_shelf():
    num_shelf = input("Введите номер полки: ")
    if num_shelf in directories.keys():
        print ("Такая полка уже есть")
        return False
    directories[num_shelf] = []
    print(f"Полка с №{num_shelf} добавлена")
    return num_shelf


def main():
    while True:
        print()
        print("=" * 40)
        choice = int(input("Выберите пунк меню: "))
        if choice == 1:
            people_name()
        elif choice == 2:
            search_shelf()
        elif choice == 3:
            all_docs()
        elif choice == 4:
            add_people()
        elif choice == 5:
            del_doc()
        elif choice == 6:
            replace_doc()
        elif choice == 7:
            add_shelf()
        elif choice == 8:
            break

print("""               МЕНЮ
        1 - Поиск имени по номеру документа.
        2 - Номер полки по номеру документа.
        3 - Вывод всех документов.
        4 - Добавить документы.
        5 - Удалить документ
        6 - Переместить документ
        7 - Добавить полку
        8 - Выход.
      """)
if __name__ == '__main__':
    main()