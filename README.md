# chatgpt-proxy-web
Flask reverse proxy ChatGPT website chat.openai.com/chat.

[中文](https://github.com/cooolr/chatgpt-proxy-web/blob/main/README_ZH.md) | [English](https://github.com/cooolr/chatgpt-proxy-web/blob/main/README.md)

## Prepare

You should log in to the [ChatGPT website](https://chat.openai.com/chat), find the cookie named `_puid`, and then copy its value.

**This project heavily relies on the Plus-exclusive _puid parameter. Without it, CloudFlare cannot be bypassed.**

Modify `config.py` to set the configuration.
``` python
# If you change this property, the `resource` directory needs to be manually deleted.
listen_url = "http://127.0.0.1"
listen_port = 8011

# Enable account and password authentication for the webpage.
is_verify = False

# Proxy configuration, either HTTP or SOCKS5.
proxies = {"https": ""}

# Plus-exclusive cookie parameters. If you don't have them, ask a friend to share theirs.
puid = ""

'''
1. If using email login, only the `email_address` and `password` require.
2. If not email login, only the `session_token` require.
3. If not email login and also enable is_verify, the `user` needs to be rewritten.
   user = md5(('your_email' + 'your_password').encode()).hexdigest()
'''

password_list = [
    {"email_address": "", "password": "", "session_token": None, "user": None},
]
```

## Install dependencies

``` bash
pip install -r requirements.txt
```

## Quick start

``` bash
python3 main.py
```

browser open link: [http://127.0.0.1:8011/chat](http://127.0.0.1:8011/chat)

**If you need to access using a domain name, you can refer to my configuration.**

`config.py`
``` python
listen_url = "https://cooolr.online"
listen_port = 8011
```

`nginx.conf`
```plain text
server {
    location / {
        proxy_pass http://127.0.0.1:8011;
    }
}
```



## Note

1. It can only be used for Plus member accounts, free accounts without _puid parameters will have CF verification.
2. auto login `auth.py`, thank you [https://github.com/acheong08/OpenAIAuth](https://github.com/acheong08/OpenAIAuth).

## Renderings
![login](https://github.com/cooolr/chatgpt_plus_proxy_website/blob/main/static_files/login.png)
![chat](https://github.com/cooolr/chatgpt_plus_proxy_website/blob/main/static_files/chat.png)
