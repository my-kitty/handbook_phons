phonebook = {
	"Иванов": {
	"-ph": ["+7 (924) 182 00-00"],
	"-e": "ivanov@gmail.com",
	"-b": "24.03.2024",},

	"Дима одногруппник": {
	"-ph": ["+7(924) 345 19-95"],
	"-e": "dimedrol3004@gmail.com",
	"-b": "30.04.1995",},

	"Дядя Вася": {
	"-ph" : ["+7(924)048-67-89", "+7(924)145-20-34"] }
	}


mask_dataBase = {
	"-name" : {
		"name":"именем",
		"tupe": str,
		"length" : 50,
		"mandatory" : True,
		"unique":True
	},

	"-ph" : {
		"name":"телефоном",
		"tupe": list,
		"length" : 5,
		"mandatory" : True,
		"unique":True
	},

	"-e" : {
		"name":"email",
		"tupe": str,
		"length" : 50,
		"mandatory" : False,
		"unique":True
	},

	"-b" : {
		"name":"дата рождения",
		"tupe": str,
		"length" : 10,
		"mandatory" : False,
		"unique":False
	},

}

def db(): return phonebook
def db_mask(): return mask_dataBase