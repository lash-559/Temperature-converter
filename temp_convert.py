temp = input('請問您要查詢的是攝氏還是華氏？')
if temp == '攝氏' :
    c = input('請輸入攝氏溫度： ')
    c = float(c)
    f = c * 9 / 5 + 32
    print('華氏溫度為', f)

if temp == '華氏' :
	f = input('請輸入華氏溫度： ')
	f = float(f)
	c = (f - 32) * 5 / 9
	print('攝氏溫度為', c)
