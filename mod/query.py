import types

import mod.show as show
import mod.add as add

help = """

	Вы можете использовать следущие комманды:
	------------------------------------------

	/help -> Справочник по программе
	/stop -> Завершение рабоы программы
	/show -> Вывести базу номеров
	------------------------------------------
"""


comend = {
		"/stop": False,
		"/help": help,
		"/show": show.show,
		"/add": add.add_contact,
		"/edit": "Редактирывание",
		"save":"сохранить",
		"/сhange": "Запускать функцию"
	}

print(type(comend["/help"]))


def query_progect(input_humen):
	
	if(isinstance(comend[input_humen],types.FunctionType)): # ЕСЛИ функция
			return comend[input_humen]() 							# Выхываем эту функцию
	elif type(comend[input_humen]) == str:
		if input_humen in comend.keys():
			return comend[input_humen]
	

	
	
	return "Такой каманды нету изучите команды через запрос /help"