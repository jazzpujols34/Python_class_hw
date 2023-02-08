# 4. 函數的練習-mersenne_prime
#
# 寫一函數is_mersenne_prime(n)用來判斷n是否為Mersenne質數。撰寫一程式找出前5個Mersenne質數。
#
# 提示：若質數滿足2^P-1=n (p為正整數)，則n為Mersenne Prime。
#
# 說明：當p=3時，2^3-1=7，故7為Mersenne Prime。

import math
def is_prime(n):
    if not int(math.log(n+1,2)) == math.log(n+1,2):
        return False
    else:
        pass
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5,int(n**0.5)+1,6):  # n 如果被 (6j-1) (6j+1)(此組數字包含所有質數、以及一些非質數) 整除 回傳False
        if n % i == 0 or n % (i+2) == 0:
            return False
    # 最後，以上條件都不符合的話，則為質數
    else:
        return True

print( is_prime(8191))

def get_nth_merssene_prime(n): # 我要找第n個梅森質數→塞入梅森質數的列表需要有n個元素
    x = 2  # 從 x = 2 開始檢測 是否為 梅森質數
    merssene_list = list()  # 創造一個 裝 梅森質數的串列 list
    while n > 0:
        if is_prime(x):
            merssene_list.append(x)   # 如果是 梅森質數， 將該數值塞入 list中
            n -= 1                  # 還需要找 n -1 個數字
            x += 1                  # x+1→ 繼續找下一個數字
        else:
            x += 1
    return merssene_list

print(get_nth_merssene_prime(5))

