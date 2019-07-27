#記帳程式專案 二維清單(就是清單中還有一個清單，一個清單裡面有2個東西(名字+價格))
products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
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
