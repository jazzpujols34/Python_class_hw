# 1.
# 選擇性敘述的練習 - season
# 輸入月份 1~12 月，判斷相對應的季節春、夏、秋、冬並印出。若不在此範圍則印出”輸入錯誤”。
# (備註︰春天是用 3、4和 5月，不是1、2和 3月)
try:
    m = int(input('請輸入月份(1月~12月): '))
except ValueError as err_name:
    print('輸入錯誤')
    # print(err_name)
else:
    if m <= 2 or m == 12:
        print('現在是冬季')
    elif 9 <= m <= 11:
        print('現在是秋季')
    elif 6 <= m <= 8:
        print('現在是夏季')
    elif 3 <= m <= 5:
        print('現在是春季')
    else:
        print('輸入錯誤')

