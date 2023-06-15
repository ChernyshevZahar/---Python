# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
# для изменения и удаления данных



def newcontact(filename):
    with open(filename,"a") as file:
        file.write("\n"  + input("Имя очество город номер:"))

def readcontact(filename):
    arrcont =[]
    with open(filename,"r" , encoding="utf-8") as file:
        for line in file:
            surname,name,city,numbers = line.strip().split(",")
            contact = {
                "surname":surname,
                "name":name,
                "city":city,
                "numbers":numbers, 
            }
            arrcont.append(contact)
    return arrcont

def update_contact(filename):
    name = input("Введите имя или фамилию контакта, который хотите изменить: ")
    contacts = readcontact(filename)
    found = False
    for contact in contacts:
        if name in contact["name"] or name in contact["surname"]:
            found = True
            print("Контакт найден:")
            print(contact)
            new_numbers = input("Введите новый номер телефона: ")
            contact["numbers"] = new_numbers
            break
    if not found:
        print("Контакт не найден.")
    else:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("\n".join([f"{contact['surname']},{contact['name']},{contact['city']},{contact['numbers']}" for contact in contacts]))  

def delete_contact(filename):
    name = input("Введите имя или фамилию контакта, которого хотите удалить: ")
    contacts = readcontact(filename)
    found = False
    new_contacts = []
    for contact in contacts:
        if name not in contact["name"] and name not in contact["surname"]:
            new_contacts.append(contact)
        else:
            found = True
    if not found:
        print("Контакт не найден.")
    else:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("\n".join([f"{contact['surname']},{contact['name']},{contact['city']},{contact['numbers']}" for contact in new_contacts]))
                
        print("Контакт удален.")


Path_num = "numbers.txt"
war = int(input(f"Что вы хотите? \n1- Увидеть \n2-добавить \n3-изменить \n4-удалить\n"))

if war==1:
    print(readcontact(Path_num))
elif war==2:
    newcontact(Path_num)
elif war==3:
    update_contact(Path_num)
elif war==4:
    delete_contact(Path_num)
else:
    print("Нет такой команнды")