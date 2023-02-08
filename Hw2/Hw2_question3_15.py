# 3. 迴圏的練習 - armstrong
# source: https://www.programiz.com/python-programming/examples/armstrong-number
# Armstrong數: abcd... = an + bn + cn + dn + ...
#
# 找出所有三位數的Armstrong數，其各位數之立方和等於該數本身。
# Armstrong_num = a ** 3 + b ** 3 + c ** 3
# 說明：153 = 1 ^ 3 + 5 ^ 3 + 3 ^ 3，故153為Armstrong數。
# (2 ^ 3 表示 2 的 3 次方, 3 ^ 3 表示 3 的 3 次方)

# num = int(input('Input a number:'))
#
# sum = 0
#
# tmp = num
# while tmp > 0:
#     digit = tmp % 10
#     sum += digit ** 3
#     tmp //= 10
#
# if num == sum:
#     print(sum, 'is an Armstrong number.')
# else:
#     print(sum, 'is not an Armstrong number.')
