# 2.
# 選擇性敘述的練習 - salary
#
# 輸入便利商店工讀生的工作時數並計算其薪資。
# 60 小時以內，時薪160元。
# 61~80小時，以時薪1.25倍計算。
# 81小時以上，以時薪1.5倍計算。

# 說明：薪資以累計方式計算。若工時為90小時，
# 則薪資為60 * 160 + 20 * 160 * 1.25 + 10 * 160 * 1.5元。
# hour * 160 + (hour - 60 ) * 160 * 1.25 + (hour - 80) * 160 * 1.5

hour =float(input('請輸入工時: '))
total = 0

if 60 >= hour:
    total = hour * 160
elif 80 > hour >= 61:
    total = 60 * 160 + (hour - 60 ) * 160 * 1.25
else:
    total = 60 * 160 + (80 - 60 ) * 160 * 1.25 + (hour - 80) * 160 * 1.5


print('您的薪資為:', total, '元。')

