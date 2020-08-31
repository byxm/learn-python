'''
python建议每一个文件模块顶部都有一个简短的说明程序
'''


account = 'simone'
password = '123456'

print('please input account')
user_account = input()

print('please input password')
user_password = input()

if account == user_account and password == user_password:
    print('success')
else:
    print('fail')






