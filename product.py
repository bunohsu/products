#檢查檔案在不在
import os #operating system
if os.path.isfile('products.csv'):
	print('yeah! 找到檔案了!')
	#可以把讀取檔案10~18行丟進來第5行，但是要記的縮排，因為要在if內才是一個group
else:
	print('找不到檔案.....')


#讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f: #要記得加入編碼(encoding)，要不然會錯亂
	for line in f:
		if '商品,價格' in line:                #不想要顯示第一的商品,價格，所以使用continue功能跳過第一行
			continue 
		name, price = line.strip().split(',') #如果檔案內一行有多個項目，前面就要相對應幾個變數，另外要先strip在split
		products.append ([name, price])       #把變數丟到products清單內
print(products)


#記帳程式專案 二維清單(就是清單中還有一個清單，一個清單裡面有2個東西(名字+價格))
products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price) #價格不是字串所以要轉成整數
	p = [] # 也可以寫成 p = [name, price] 這樣8.9.10只要變一行就可以了
	p.append(name)  #建立一個P清單，分別append name&price進去，然後再把P丟到最外面的products清單
	p.append(price)
	products.append(p) #也可以寫成 products.append([name, prcie])這樣8.9.10都不用寫了
print(products)

print(products[0])
print(products[0][0])

#使用for loop篩選要的東西
for p in products:
	print(p) #印出每個小清單
	print(p[0],'的價格是', p[1]) #因為是for loop會印出每個小清單的名稱&價格

#建立一個csv檔，並將清單存入
with open('products.csv', 'w', encoding='utf-8') as f: #建立打開一個products.csv，並取代碼為f
	f.write('商品,價格\n') #建立標題，在csv裡逗號是下一格，加\n會變下一行
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') #寫入f，並把字串加起來，這邊p[1]不是字串，所以要再轉成字串
