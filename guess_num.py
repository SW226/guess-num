import random
start = input('請輸入隨機數字起始值: ')
start = int(start)
end = input('請輸入隨機數字結尾值: ')
end = int(end)
r = random.randint(start,end)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('請猜數字 ')
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