import mod.Connect as connect

# /add -name Дмитрий Алёхин -ph +7(924) 345 19-95, +7(924) 345 19-96 -e dimedrol@gmail.com -b 30.04.1995
# /add -name Дмитрий Алёхин -ph +7(924) 345 19-96 -e dimedrol@gmail.com -b 30.04.1995

phonebook = connect.db()
mask_is_base = connect.db_mask()

add_status = {
	"status" : "\tКоманда /add разработана на 30%\n",
	"help" : """
	Команда /add добовляек новый контакт, Полная запись комманды:
	/add -nema [Имя*] -ph [Телефон*] -e [email] -b [день рождения]
	* обязательные пораметы комманды.
	------------------------------------------
	""",
}


add_console = {
	"not_params":f"""
	Обязательные пораметры /add [-name] [-ph] отсутствуют
	Воспользуйтес командой /add help
	------------------------------------------
	""",
	"contact_exists": lambda x:f"""
	Контакт с {x[0]} {x[1]} уже существует!
	Придумайте пользвателя с другим {x[0]},
	Либо измените уже имеющеся контакта командой /edit {x[2]}
	------------------------------------------""",

	"add_good": "\tКонтакт успешно добавлен\n\t------------------------------------------\n"
}




def add_conact_strong(list_params):
	# list_params это введёная строка(Команда) в види list

	mandatory_params = [i for i in mask_is_base if mask_is_base[i]["mandatory"] == True] # mandatory_params Возращает обязательные пораметры Например ["-name", "-ph"]
	name_params = [i for i in mask_is_base] # Список имён пораметров Например ['-name', '-ph', '-e', '-b']
	
	name_params_type_in_list = [i for i in mask_is_base if mask_is_base[i]["tupe"] == list ] # Имя параметра

	if set(mandatory_params).issubset(list_params):

		list_params.remove(list_params[0]) # Удаляет первый элемент из списка
		contact_list = {kay:"" for kay in name_params} # Формирует contact_list Например: { "-name":"", "-ph":"", "-e":"", 	"-b":"" }
		connect_params = False

		for i in list_params:
			if i in contact_list: connect_params = i; continue
			contact_list[connect_params] += i + " "
			
		for i in contact_list: contact_list[i] = contact_list[i].strip() # Уберает все пробел в начале и конце строки

		for i in name_params_type_in_list: # если пораметр list сделать contact_list list
			contact_list[i] = contact_list[i].split(",")
			contact_list[i] = [j.strip() for j in contact_list[i]]

		return contact_list
	

	else: False
	

def print_dict(t):
	print("\n{")
	for key, value in t.items():
		print("{0}: {1}".format(key,value))
	print("}\n")

def error_add_params(contact_list):
	unique_params = [kay for kay in contact_list if mask_is_base[kay]["unique"]]
	# print(unique_params)

	# print_dict(mask_is_base)
	# print_dict(phonebook)
	# print_dict(contact_list)

	for kay in phonebook:
		if contact_list[unique_params[0]] == kay: 
			return mask_is_base[unique_params[0]]["name"],kay,kay
		
		for i in phonebook[kay]:
			if i in unique_params and type(phonebook[kay][i]) == str:
				if phonebook[kay][i] == contact_list[i]:
					return mask_is_base[i]["name"],contact_list[i],contact_list[unique_params[0]]

			if i in unique_params and type(phonebook[kay][i]) == list:
				for j in phonebook[kay][i]:
					if j in contact_list[i]:
						return mask_is_base[i]["name"],', '.join(contact_list[i]),contact_list[unique_params[0]]

	return False





# Главная функция 
def add_contact(list_params = False):
	
	if list_params == False:
		nema = input("Введите имя нового контакта: ")
		phons = input(f"Ведите номер {nema}: ")
		phonebook[nema] = {"phones":[phons]}
		return "Добавил"
	
	if list_params[1] in add_status: # Я уже забы лчто делает =) 
		return add_status[list_params[1]]
	
	
	contact_list = add_conact_strong(list_params) # Преобразованый список	
	contact_exists = error_add_params(contact_list)

	if contact_exists != False: 
		return add_console["contact_exists"](contact_exists)

	

	# Добовление в БД новый контакт
	if not(contact_exists) and contact_list != False:

		name = contact_list["-name"]
		del contact_list["-name"]
		phonebook[name] = {key : value for key, value in contact_list.items()}
			

		return add_console["add_good"]
	return add_console["not_params"]
	
	

