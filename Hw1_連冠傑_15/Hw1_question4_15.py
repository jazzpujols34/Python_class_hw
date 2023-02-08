# 4.
# 選擇性敘述的練習 - refund
#
# 輸入在某商店購物應付金額與實付金額。
# 實付金額小於應付金額，則印出”金額不足”。
# 實付金額等於應付金額，則印出”不必找錢”。
# 實付金額大於應付金額，則輸出找回金額最少的鈔票數和錢幣數。
# 假設幣值只有1000, 500, 100元紙鈔和50, 10, 5, 1元硬幣。
# 說明：若買了132元的商品，付1000元，應找868元，找回一張500元，三張100元，一個50元硬幣，一個10元硬幣，一個5元硬幣和三個1元硬幣。



def to_change(change):
    m_1000 = int(change / 1000)
    change = change - (m_1000 * 1000)
    m_500 = int(change / 500)
    change = change - (m_500 * 500)
    m_100 = int(change / 100)
    change = change - (m_100 * 100)
    m_50 = int(change / 50)
    change = change - (m_50 * 50)
    m_10 = int(change / 10)
    change = change - (m_10 * 10)
    m_5 = int(change / 5)
    change = change - (m_5 * 5)
    m_1 = change
    print('應找回{}張1000元，{}張500元，{}張100元，{}個50元硬幣，{}個10元硬幣，{}個5元硬幣和{}個1元硬幣。'
          .format(m_1000, m_500, m_100, m_50, m_10, m_5,m_1))
try:
    price = int(input('應付金額: '))
    pay_amount = int(input('實付金額: '))
    if price > pay_amount:
        print('金額不足')
    elif price == pay_amount:
        print('不必找錢')

    else:
        change = pay_amount - price
        print('買了', price, '元的商品，', '付', pay_amount, '元', '應找', change, '元。')
        to_change(change)

except ValueError as err:
    print(err)
    print('請輸入數字。')






# if change > 1000:
#     a = change / 1000
#     if (change - a*1000) > 500:
#         b = (change - a*1000) / 500
#         if (change - a*1000 - b*500) > 100:
#             c = (change - a*1000 - b*500) / 100
#             if (change - a*1000 - b*500 - c*100)>50:
#                 d = (change - a*1000 - b*500 - c*100) / 50
#                 if (change - a*1000 - b*500 - c*100 - d*50)>10:
#                     e = (change - a*1000 - b*500 - c*100 - d*50) / 10
#                     if (change - a * 1000 - b * 500 - c * 100 - d * 50 - e*10) > 5:
#                         f = (change - a * 1000 - b * 500 - c * 100 - d * 50 - e*10) / 5
#                         if (change - a * 1000 - b * 500 - c * 100 - d * 50 - e * 10 - f*5) > 1:
#                             g = (change - a * 1000 - b * 500 - c * 100 - d * 50 - e * 10 - f*5) / 1