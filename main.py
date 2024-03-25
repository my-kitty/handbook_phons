import mod.query as query

	




comend = "/help"
while True:
	funtipn_commend = query.query_progect(comend)
	if funtipn_commend == False: break
	print(funtipn_commend)
	comend = input("	Введите комманду: ")

    

