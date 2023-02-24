# chatgpt_plus_proxy_website
Flask反向代理ChatGPT网站，完美复刻chat.openai.com/chat ,已加入登录验证，原汁原味。

## 准备

你应该先登录[ChatGPT Website](https://chat.openai.com/chat)，找到名为`cf_clearance`、`__Secure-next-auth.session-token`、`_puid`的Cookies，复制它们的值。

其中`_puid`为Plus会员专属值，没它不行。

## 安装依赖

``` bash
pip install requests flask gevent
```

## 快速开始

1. 在`chatgpt.py`代码相应位置粘贴`cf_clearance`、`session_token`、`_puid`的值。

2. 运行程序
  ``` bash
  python3 chatgpt_proxy_website.py
  ```

3. 浏览器打开
  ``` plain Text
  http://127.0.0.1:8011/chat
  ```

## 登录认证

在代码页设置user_id即可开启登录认证，user_id为邮箱+密码的md5

``` python3
# 定义user_id 以test@qq.com 123456为例
user_id = md5(('test@qq.com123456').encode()).hexdigest()
```

## 注意事项

1. 只能用于Plus会员账号使用，免费账号没有_puid参数会有CF验证。
2. 目前登陆上的账号不需要翻墙也能正常使用。

## 效果图
![login](https://github.com/cooolr/chatgpt_plus_proxy_website/blob/main/login.png)
![chat](https://github.com/cooolr/chatgpt_plus_proxy_website/blob/main/chat.png)
