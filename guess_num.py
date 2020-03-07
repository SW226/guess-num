import random
r = random.randint(1,100)
count = 0
while True:
	count += 1 # count = count + 1
	num = input("請輸入一個1~100的隨機整數: ")
	num = int(num)
	if num == r :
		print('恭喜猜對了!')
		print('總共猜了', count,'次')
		break
	elif num > r:
		print('錯了,比', num,'再小一點')
	elif num < r:
		print('不對喔，要比', num,'再大一點')
	print('這是你猜的第', count,'次')