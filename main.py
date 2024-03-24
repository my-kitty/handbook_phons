import mod.query as query

	




comend = "/help"
while True:
	if query.query_progect(comend) == False: break
	print(query.query_progect(comend))
	comend = input("	Введите комманду: ")

    

