import json



	
def json_load():

	try:
		with open("data_file.json", "r") as read_file:
			phonebook = json.load(read_file)
	except:
		phonebook = { 
		"дядя Ваня": { 'phones': [1231654,45646644],
		'birthday': '01.01.1960',
		'email': "[vanya@mail.ru](mailto:vanya@mail.ru)"
		}, 
		"дядя Вася": {'phones' : [12121244444]} }
	return phonebook

def сhange():
	name_to_сhange = input("Введите имя контакта: ")
	# if name_to_сhange in phonebook

phonebook = json_load()

while True:
	comend = input("Введите запрос: ")
	if comend == "/stop":
		break
	elif comend == "/help":
		print("Список команд")
	elif comend == "/show":
		print(phonebook)
	elif comend == "/сhange":
		сhange()
	else: print("Такой каманды нету изучите команды через запрос /help")
    
  
