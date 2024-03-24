
import mod.show as show

help = """

	Вы можете использовать следущие комманды:
	------------------------------------------

	/help -> Справочник по программе
	/stop -> Завершение рабоы программы
	/show -> Вывести базу номеров
	------------------------------------------
"""





def query_progect(input_humen):
	comend = {
		"/stop": False,
		"/help": help,
		"/show": show.show(),
		"/сhange": "Запускать функцию"
	}
	
	#  Тут есть лагическая ошибка в in ???
	#  show.show() вызывается сама по себе при проходе input_humen in comend.keys()
	if input_humen in comend.keys():
		return comend[input_humen]
	
	return "Такой каманды нету изучите команды через запрос /help"