# 1. 迴圏的練習 - factor
# 輸入一正整數，求其所有的因數。
# 說明：36的因數為1, 2, 3, 4, 6, 9, 12, 18, 36


num = int(input('Please insert a number: '))
for i in range(1, num+1):
    if (num % i) == 0:
        print(i)