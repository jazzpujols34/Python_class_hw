# 4. 迴圈的練習 - prime
# source: https://www.youtube.com/watch?v=V78XvTmYiKk&ab_channel=WrtTech
# 輸入一正整數，找出所有小於或等於的質數。
# 質數: 因數為1和其本身的數
first_num = int(input('Input a number: '))
end_num = int(input('Input another number: '))

for num in range(first_num, end_num+1):
    if num > 1: # all prime number is greater than 1

        for i in range(2, num): # check each number from range (2, num)
            if num%i == 0: # if num can be divided by any number(i) of the range, num would not be prime number.
                break # break out the loop to check another number

        else: # no number between 2 to num was divisible by num, num is prime number.
            print(num)