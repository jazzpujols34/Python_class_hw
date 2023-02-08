# 5. 迴圈敘述的練習 - interest
# 某人A以10 % 單利投資100000元，某人B則以5 % 複利投資100000元。
# 計算多少年後某人B的投資可以超過某人A，並將此時兩人錢數印出。(27年後)

# 提示：
# 單利公式：P(1 + r * n)
# 複利公式：P(1 + r) ^ n
# P：本金，r：利率，n：多少年
# (備註︰(1+r) ^ n表示(1 + r)的n次方)

# n = int(input('Invest year: '))
y = 1
a = 1 #啟動
while a == 1:
    A = 100000 * (1 + 0.1 * y)
    B = 100000 * (1.05) ** y
    print('第', y, '年。')
    print('A資產:', A)
    print('B資產:', B)
    if B<=A:
        y += 1
    elif B>A:
        print('第', y, '年，B會大於A')
        break
    else:
        print("pass")
        break








