i = 3
password = 'a123456'
while i > 0:
    i -= 1
    pwd = input('請輸入密碼:')
    if pwd == password:
        print('登入成功!')
        break
    else:
        print('密碼錯誤!')
        if i > 0:
            print('還有',i,'次機會',sep = '')
        else:    
            print('你沒機會了QQ')