# 3.
# 選擇性敘述的練習 - electricity
#
# 輸入何種用電和度數，計算出需繳之電費。
# 電力公司使用累計方式來計算電費，分工業用電及家庭用電。
#
# 家庭用電
# 工業用電
#
# 120度(含)以下
# 1.63 元
# 0.5元
#
# 121~330(含)度
# 2.38 元
# 0.5元
#
# 330度以上
# 3.52元
# 0.5元


elec_type = input('請輸入為何種用電(A. 家庭用電 B. 工業用電)?')
bill = 0

if elec_type == 'A':
    typeA = float(input('請輸入用電量: '))

    if typeA <= 120:
        bill = typeA * 1.63
    elif 330 >= typeA > 120:
        bill = 120 * 1.63 + (typeA-120) * 2.38
    if typeA > 330:
        bill = 120 * 1.63 + (330 -121) * 2.38 + (typeA-330) * 3.52
elif elec_type == 'B':
    typeB = float(input('請輸入用電量: '))
    bill = typeB * 0.5
else:
    print('請確認是何種用電型態。')

if bill != 0:
    print('您需繳電費 ', bill, '元。')
else:
    print('您無須繳費。')