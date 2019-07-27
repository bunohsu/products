#記帳程式專案 二維清單(就是清單中還有一個清單，一個清單裡面有2個東西(名字+價格))
products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	p = []
	p.append(name)  #建立一個P清單，分別append name&price進去，然後再把P丟到最外面的products清單
	p.append(price)
	products.append(p)
print(products)

print(products[0])
print(products[0][0])
