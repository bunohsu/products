import os #operating system

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f: #要記得加入編碼(encoding)，要不然會錯亂
		for line in f:
			if '商品,價格' in line:                #不想要顯示第一的商品,價格，所以使用continue功能跳過第一行
				continue 
			name, price = line.strip().split(',') #如果檔案內一行有多個項目，前面就要相對應幾個變數，另外要先strip在split
			products.append ([name, price])       #把變數丟到products清單內
	return products


#讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱:')
		if name == 'q':
			break
		price = input('請輸入商品價格:')
		price = int(price) #價格不是字串所以要轉成整數
		products.append([name, price]) 
	print(products)
	return products

	print(products[0])
	print(products[0][0])

#使用for loop篩選要的東西(印出購買紀錄)
def print_products(products):
	for p in products:
		print(p) #印出每個小清單
		print(p[0],'的價格是', p[1]) #因為是for loop會印出每個小清單的名稱&價格

#建立一個csv檔，並將清單存入(寫入檔案)
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f: #建立打開一個products.csv，並取代碼為f
		f.write('商品,價格\n') #建立標題，在csv裡逗號是下一格，加\n會變下一行
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n') #寫入f，並把字串加起來，這邊p[1]不是字串，所以要再轉成字串


def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #檢查檔案在不在
		print('yeah! 找到檔案了!')
		products = read_file(filename)
	else:
		print('找不到檔案.....')	
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()