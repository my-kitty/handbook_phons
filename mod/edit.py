import mod.Connect as connect
import mod.all_function as conact_strong

phonebook = connect.db()
print_dict = conact_strong.print_dict
mask_dataBase = connect.mask_dataBase

# /edit -name Иванов -ph +7(924) 345 19-95, +7(924) 345 19-96 -e dimedrol@gmail.com -b 30.04.1995
# /edit -name Иванов -ph +7(924) 345 19-96 -e dimedrol@gmail.com -b 30.04.1995



add_console = {
	"not_name": lambda x: f"""
	Контакта {x} в вашем контактном справочнеке не существует
	воспользуйтесть командой /show чтобы просмотреть список ваших контактов
	------------------------------------------
	""",
	"not_params":f"""
	Обязательные пораметры /edit [-name] [-ph] отсутствуют
	Воспользуйтес командой /edit help
	------------------------------------------
	""",
	"contact_exists": lambda x:f"""
	Контакт с {x[0]} {x[1]} уже существует!
	Придумайте пользвателя с другим {x[0]},
	Либо измените контакт командой /edit {x[2]}
	------------------------------------------""",

	"add_good": "\tКонтакт успешно изменён\n\t------------------------------------------\n"
}



def edit_connand(list_params = False):
	
	if list_params == False:
		return "Обычное добовление"
	
	contact_list = conact_strong.conact_strong(list_params)



	if not(contact_list["-name"] in [i for i in phonebook]):
		return add_console["not_name"](contact_list["-name"])
	
	list_unique = [i for i in mask_dataBase if mask_dataBase[i]["unique"]]
	nema = list_unique.pop(0)


	for i in phonebook:
		for j in phonebook[i]:

			if j in list_unique and mask_dataBase[j]["tupe"] == list and j !=contact_list[nema]:
				for z in contact_list[j]:
					if z in phonebook[i][j]:
						return add_console["contact_exists"]([mask_dataBase[j]["name"], z,i])

			if j in list_unique and mask_dataBase[j]["tupe"] == str and i !=contact_list[nema]:
				return add_console["contact_exists"]([mask_dataBase[j]["name"], phonebook[i][j],i])
			
	# neeeeeeeeeeeeeeeeeeeeeeeeeeeeee

	

	
	# return add_console["not_params"]
	return "Erreo ????"