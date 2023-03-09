# -*- coding: utf-8 -*-

# 如果更改了此属性，需要手动删除资源目录 [If you change this property, the `resource` directory needs to be manually deleted.]
listen_url = "http://127.0.0.1"
listen_port = 8011

# 开启页面的账号密码认证 [Enable account and password authentication for the webpage.]
is_verify = False

# 代理配置，http或socks5都可以 [Proxy configuration, either HTTP or SOCKS5.]
proxies = {"https": ""}

# Plus专属Cookie参数，如果没有，找朋友蹭一个 [Plus-exclusive cookie parameters. If you don't have them, ask a friend to share theirs.]
_puid = ""

'''
1. 如果使用邮箱密码登录，则只需要填写email_address和password这两个参数 [If using email login, only the `email_address` and `password` require.]
2. 如果使用Chrome或Microsoft登录，则只需要填写session_token这一个参数 [If not email login, only the `session_token` require.]
3. 如果使用Chrome或Microsoft登录，并且同时开启了账号密码认证，则需要重写user参数 [If not email login and also enable is_verify, the `user` needs to be rewritten.]
   user = md5(('your_email' + 'your_password').encode()).hexdigest()
'''

password_list = [
    {"email_address": "", "password": "", "session_token": None, "user": None},
]
