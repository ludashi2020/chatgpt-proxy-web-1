# chatgpt_proxy_website
Flask reverse proxy ChatGPT website chat.openai.com/chat.

[中文说明](https://github.com/cooolr/chatgpt_plus_proxy_website/blob/main/README_ZN.md)

## Prepare

You should login to [ChatGPT Website](https://chat.openai.com/chat), find the cookies named `_puid`, and copy value.

**This project relies heavily on the exclusively for Plus `_puid` parameter. Without it, CloudFlare cannot be bypassed.**

``` python
# Must and Required parameter.
_puid = ""
```

Now you can use the chatgpt mailbox password to automatically log in.
``` python
# Congratulations! Now you can log in with Chatgopt mailbox password.
email_address = ""
password = ""
```

If you login by Chrome or Microsoft, You should login to [ChatGPT Website](https://chat.openai.com/chat), find the cookies named `__Secure-next-auth.session-token` `clearance`, and copy value. 

``` python
# `session_token` and `cf_clearance`, get from cookies, if login by Chrome or Microsoft.
session_token = ""
cf_clearance = ""
```

Now you can add password verification to your webpage with set `is_verify=True`, default for no verification.

``` python
# Login Password can be set `is_verify = True` if needed.
is_verify = False

# if login by Chrome or Microsoft, must be rewrite `user_id = md5((<your_email> + <your_password>).encode()).hexdigest()`
user_id = md5((email_address + password).encode()).hexdigest() if email_address and password else ""
```

If you run website with domain, you should change listen_url to domain.
``` python
# listen_url can be change if needed.
# if you change this, you should delete static resource.
listen_url = "http://127.0.0.1"
listen_port = 8011
```

## Install dependencies

``` bash
pip install -r requirements.txt
```

## Quick start

``` bash
python3 chatgpt_proxy_website.py
```

browser open link: [http://127.0.0.1:8011/chat](http://127.0.0.1:8011/chat)

## Note

1. It can only be used for Plus member accounts, free accounts without _puid parameters will have CF verification.
2. The account currently logged in can be used normally without overpassing the wall. In China。

## Renderings
![login](https://github.com/cooolr/chatgpt_plus_proxy_website/blob/main/login.png)
![chat](https://github.com/cooolr/chatgpt_plus_proxy_website/blob/main/chat.png)
