# 5.迴圏的練習 - password
# 出現”請輸入密碼”的提示，使用者有最多三次輸入的機會。
# 若輸入正確，則印出”密碼輸入正確，歡迎使用本系統！”。
# 若輸入不正確，再次出現”請輸入密碼”的提示。
# 若三次輸入不正確，則印出”密碼輸入超過三次！”，並結束程式的執行。

times = 0

while True:
    pwd = 1234
    login = int(input('請輸入密碼: '))

    times += 1
    if times < 3:
        if login == pwd:
            print('密碼輸入正確，歡迎使用本系統!')
            break
        else:
            print('請再次輸入密碼。')

    else:
        print('密碼輸入超過三次！')
        break
