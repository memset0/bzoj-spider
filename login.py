import requests

# 配置登陆地址
# > 理论上可以登录一切 Hust OJ
url = 'https://www.lydsy.com/JudgeOnline/login.php'

# 输入账号密码
# > 测试用户: UserName: testuser, Password: 123456
# > 以上账号密码仅供测试， memset0 跪求您不要盗号 qwq...
print('Please input your user name: ', end = '')
username = input()
print('and the password: ', end = '')
password = input()
print('OK, your user name is "{username}" and the password is "{password}".'.format(username = username, password = password))

# 尝试登陆并保存 Cookie
try:
    data = { 'user_id': username, 'password': password }
    request = requests.Session()
    # ↓ 伪造 Header ，否则很想了解一下 TMD 为什么总是 404
    request.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3395.99 Safari/537.36'})
    ret = request.post(url, data = data)
    # ↓ 判断是否成功登录
    if ('history.go(-2);' in ret.text):
        # ↓ 利用人类智慧获取 cookie
        cookie = str(ret.cookies)[37:-22]
        with open('cookie.txt', 'w+') as file:
            file.write(cookie)
            file.close()
        print('Successfully got your cookie.')
        print('Here it is:', cookie)
    else:
        print('Your user name or password is wrong.')
except:
    print('An error has been taken place, please try again.')
