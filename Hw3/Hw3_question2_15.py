# 2. 函數的練習-is_prime
# 寫一函數is_prime(n)用來判斷n是否為質數。

def is_prime(n):
    if n == 1:
        return 1
    else:
        for i in range(2, n):
            if n%i == 0:
                print(n, 'is not a prime number.')
                return
                break
        else:
            print(n, 'is a prime number.')
            return n
n = int(input("Please enter a number: "))
is_prime(n)


