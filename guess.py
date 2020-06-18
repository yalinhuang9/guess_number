import random
x = random.randint(1,100)
while True:
	y = input ('猜猜看～請輸入你心裡的數字：')
	y = int(y)
	if y == x:
		print('終於答對了！')
		break
	else:
		if y > x:
			print('比答案大')
		elif y < x:
			print('比答案小')	
