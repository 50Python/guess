import random

password = random.randint(1, 100)
times = 0

while True:
	check = input('猜猜看現在數字是多少: ')
	check = int(check)
	times = times + 1
	print('到目前已經猜了', times  , '次')
	if check < password:
		print('猜得比答案小')
		print('提示:' , password) #測試用
		#print('到目前已經猜了',  , '次')
	elif check > password:
		print('猜得比答案大')	
		print('提示:' , password) #測試用
	elif check == password:
		print('答對了')
		break
