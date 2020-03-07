import random
r = random.randint(1,100)
b = 0
while True:
	x = input("請輸入一個1~100的隨機整數: ")
	x = int(x)
	if x == r :
		print('恭喜猜對了!')
		b = b + 1
		print('總共猜了', b,'次')
		break
	elif x > r :
		print('錯了,比', x,'再小一點')
		b = b + 1
	elif x < r :
		print('不對喔，要比', x, '再大一點')
		b = b + 1