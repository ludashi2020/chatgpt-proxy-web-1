# chatgpt_proxy_website

Flask 反向代理 ChatGPT 网站 chat.openai.com/chat。

## 准备

您应该登录 [ChatGPT 网站](https://chat.openai.com/chat)，找到名为 `_puid` 的 cookie，然后复制值。

**该项目严重依赖于专用于 Plus 的 `_puid` 参数。 没有它，就无法绕过 CloudFlare。**

``` python
# Must and Required parameter.
_puid = ""
```

现在可以使用chatgpt邮箱密码自动登录了。
``` python
# Congratulations! Now you can log in with Chatgopt mailbox password.
email_address = ""
password = ""
```

如果您使用 Chrome 或 Microsoft 登录，您应该登录 [ChatGPT 网站](https://chat.openai.com/chat)，
找到名为 `__Secure-next-auth.session-token` `clearance` 的 cookie，以及 复制值。

``` python
# `session_token` and `cf_clearance`, get from cookies, if login by Chrome or Microsoft.
session_token = ""
cf_clearance = ""
```

现在您可以通过设置 `is_verify=True` 为您的网页添加密码验证，默认为不验证。

``` python
# Login Password can be set `is_verify = True` if needed.
is_verify = False

# 如果通过 Chrome 或 Microsoft 登录，必须重写 `user_id = md5((<your_email> + <your_password>).encode()).hexdigest()`
user_id = md5((email_address + password).encode()).hexdigest() if email_address and password else ""
```

如果您使用域名运行网站，则应将 listen_url 更改为域名。

``` python
# listen_url can be change if needed.
# if you change this, you should delete static resource.
listen_url = "http://127.0.0.1"
listen_port = 8011
```

## 安装依赖

``` bash
pip install -r requirements.txt
```

## 快速开始

``` bash
python3 chatgpt_proxy_website.py
```

浏览器打开链接：[http://127.0.0.1:8011/chat](http://127.0.0.1:8011/chat)

## 注意

1. 只能用于Plus会员账号，免费账号不带_puid参数会有CF验证。

## 效果图
![登录](https://github.com/cooolr/chatgpt_plus_proxy_website/blob/main/login.png)
![聊天](https://github.com/cooolr/chatgpt_plus_proxy_website/blob/main/chat.png)
