# chatgpt_proxy_website

Flask 反向代理 ChatGPT 网站 chat.openai.com/chat

## 准备

您应该先登录[ChatGPT Website](https://chat.openai.com/chat)，找到名为`_puid` `__Secure-next-auth.session-token` `cf_clearance`的cookie，并复制它们的值。

**本项目严重依赖Plus会员专属 `_puid` 参数。 没有它，就无法绕过 CloudFare。**

``` python
# Must and Required parameter.
_puid = ""

# session_token and cf_clearance
session_token = ""
cf_clearance = ""
```

~~现在可以使用chatgpt邮箱密码自动登录获取session_token。~~(还不稳定）

现在您可以在您的网页中添加密码验证，留空表示不验证。

``` python
# Password can be added if needed. example:  md5(('test@qq.com123456').encode()).hexdigest()
user_id = ""
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

## 注意事项 

1. 只能用于Plus会员账号，免费账号不带_puid参数会有CF验证。

2、当前登录的账号无需翻墙即可正常使用。 在中国。

## 效果图
![登录](https://github.com/cooolr/chatgpt_plus_proxy_website/blob/main/login.png)

![聊天](https://github.com/cooolr/chatgpt_plus_proxy_website/blob/main/chat.png)
