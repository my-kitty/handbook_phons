import mod.Connect as connect

import mod.show as show

phonebook = connect.db()
 
def add_contact():
	nema = input("Введите имя нового контакта: ")
	phons = input(f"Ведите номер {nema}: ")
	phonebook[nema] = {"phones":[phons]}
	return "Добавил"