import mod.Connect as connect

import mod.show as show

phonebook = connect.db()

add_status = {
	"status" : "\tКоманда /add разработана на 30%\n",
	"help" : """
	Команда /add добовляек новый контакт, Полная запись комманды:
	/add -nema [Имя*] -ph [Телефон*] -e [email] -b [день рождения]
	* обязательные пораметы комманды.
	------------------------------------------
	""",
}

# /add -nema Дмитрий Алёхин -ph +7(924) 345 19-95 -e dimedrol@gmail.com -b 30.04.1995
add_params = {
	"-nema": "Имя контакта",
	"-ph": "phones",
	"-e": "email",
	"-b":"birthday"
}

add_console = {
	"not_params":f"""
	Обязательные пораметры /add [-nema] [-ph] отсутствуют
	Воспользуйтес командой /add help
	------------------------------------------
	""",
	"add_good": "Контакт успешно добавлен"
}

def add_conact_strong(list_params):
	if "-nema" and "-ph" in list_params:

		list_params.remove("/add")
		contact_list = {
			"-nema":"",
			"-ph":"",
			"-e":"",
			"-b":"",
		}
		connect_params = False
		for i in list_params:
			if i == "-nema": connect_params = "-nema"; continue
			elif i == "-ph": connect_params = "-ph"; continue
			elif i == "-e": connect_params = "-e"; continue
			elif i == "-b": connect_params = "-b"; continue
			

			if connect_params == "-nema": contact_list["-nema"] += i + " "
			elif connect_params == "-ph": contact_list["-ph"] += i + " "
			elif connect_params == "-e": contact_list["-e"] += i + " "
			elif connect_params == "-b": contact_list["-b"] += i + " "
		
		contact_list["-ph"] = contact_list["-ph"].split(",")
		contact_list["-ph"] = [j.strip() for j in contact_list["-ph"]]
		
		return contact_list
	else: False
	




def add_contact(list_params = False):
	
	if list_params == False:
		nema = input("Введите имя нового контакта: ")
		phons = input(f"Ведите номер {nema}: ")
		phonebook[nema] = {"phones":[phons]}
		return "Добавил"
	
	if list_params[1] in add_status:
		return add_status[list_params[1]]
	
	contact_list = add_conact_strong(list_params)

	if contact_list != False:
		phonebook[contact_list["-nema"]] = {
			"phones" : contact_list["-ph"],
			"email" : contact_list["-e"],
			"birthday" : contact_list["-b"],
			}
		return add_console["add_good"]
	else:
		return add_console["not_params"]
	
	

