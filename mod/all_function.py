import mod.Connect as connect
mask_is_base = connect.db_mask()

def conact_strong(list_params):
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