# 2. 迴圏的練習 - perfect_number
# source: https://www.tutorialgateway.org/python-program-to-find-perfect-number/
# 一個數字若等於其所有因數的總和，則此數為perfect number。
# 找出100以內所有的完美數。
#
# 說明：6 的因數為1, 2, 3，6 = 1 + 2 + 3，故6為完美數。

# Set a range between 2 numbers
min = int(input('Please input a minimum number: '))
max = int(input('Please input a minimum number: '))


for Number in range(min, max - 1):
    sum = 0 # Initialize sum
    for n in range(1, Number - 1):
        if (Number % n) == 0:
            sum += n
    if (sum == Number):
        print('{} is a perfect number.'.format(Number))


# 輸入任1數找perfect number
# num = int(input('Please input a number: '))
# sum = 0
#
# for i in range(1, num):
#     if (num % i) == 0:
#         sum += i
# if (sum == num):
#     print('{} is a perfect number.'.format(num))
# else:
#     print('{} is not a perfect number.'.format(num))