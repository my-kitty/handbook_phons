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


# Словарь комманд и функций
comend = {
		"/stop": False,
		"/help": help,
		"/show": show.show,
		"/add": add.add_contact,
		"/edit": "Редактирывание",
		"/save":"сохранить",
		"/сhange": "Запускать функцию",
		"/test": "Используется для тестов",

		#Для выявления ошибок /error
		"/error" : "Тут ошибка",
		"/error_not_comend" : "Такой команды нету воспользуйтесь справочником команда /help",
		"/error_fotal_comand" : "FOTAL Ошибка: Команда не предусмотренна",
		"/error_none": "ZERO Ошибка: Команда нечего не возрощает"
	}



# Функция query_progect() анализирует комманды пользователя 
# и в зависимости от введёной команды возрощает функцию/строку
# из словаря любая вызываема функция должна возращать строку
def query_progect(input_humen):

	

	# Если команда болье чем из одного слова
	comend_strong = input_humen.split()
	if len(comend_strong) > 1: 
		if comend_strong[0] in comend.keys():
			return comend[comend_strong[0]](comend_strong)
	
	#Если команда существует
	if not(input_humen in comend.keys()): 
		return comend["/error_not_comend"]
		
	# ЕСЛИ функция
	if(isinstance(comend[input_humen], types.FunctionType)): 
			return comend[input_humen]()

	# Если стока
	if type(comend[input_humen]) == str: 
		return comend[input_humen]

	#Если bool
	if type(comend[input_humen]) == bool: 
		return comend[input_humen]

	if comend[input_humen] == None:
		return comend["/error_none"]

	return comend["/error_fotal_comand"]