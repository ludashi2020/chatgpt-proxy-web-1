# chatgpt_proxy_website
Flask reverse proxy ChatGPT website chat.openai.com/chat.

[中文说明](https://github.com/cooolr/chatgpt_plus_proxy_website/blob/main/README_ZN.md)

## Prepare

You should first login to [ChatGPT Website](https://chat.openai.com/chat), find the cookies named `_puid` `__Secure-next-auth.session-token` `cf_clearance`, and copy their values.

**This project relies heavily on the exclusively for Plus `_puid` parameter. Without it, CloudFare cannot be bypassed.**

``` python
# Must and Required parameter.
_puid = ""

# session_token and cf_clearance
session_token = ""
cf_clearance = ""
```

~~Now you can use the chatgpt mailbox password to automatically log in to get session_token.~~

Now you can add password verification to your webpage, leave it blank for no verification.

``` python
# Password can be added if needed. example:  md5(('test@qq.com123456').encode()).hexdigest()
user_id = ""
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
