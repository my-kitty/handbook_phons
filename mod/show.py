import mod.Connect as connect

phonebook = connect.db()

"""

	Иванов 
	-------------------------
	+7 (924) 182 00-00
	ivanov@gmail.com
	24.03.2024
	-------------------------

	Дима одногруппник
	-------------------------
	+7 (924) 345 19-95
	dimedrol3004@gmail.com
	30.04.1995
	-------------------------

	Дядя Вася
	-------------------------
	+7(924)048-67-89
	+7(924)145-20-34
	-------------------------
"""



hr = "-------------------------"
def show():
	def if_show(params):
		string = ""
		
		if params in value.keys() and type(value[params]) == list:
			for i in value[params]:
				string += f"\t{i} \n"
			return string
		elif params in value.keys() and type(value[params]) == str:
			string += f"\t{value[params]} \n"
			return string
		# else: 
		# 	print(value)
		# 	return "False"
		return string
	

	string_connect = f"\n\tСписок ваших контактов:\n\t{hr}\n"
	for key, value in phonebook.items():
		string_connect += f"\n\t{key} \n\t{hr}\n"
		
		string_connect += if_show("-ph")
		string_connect += if_show("-e")
		string_connect += if_show("-b")
		

	return string_connect