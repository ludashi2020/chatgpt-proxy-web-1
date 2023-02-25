# chatgpt_plus_proxy_website
Flask reverse proxy ChatGPT website chat.openai.com/chat.

## Prepare

You should first login to [ChatGPT Website](https://chat.openai.com/chat), find the cookies named `_puid`, and copy their values.

**This project relies heavily on the `_puid` parameter. Without it, CloudFare cannot be bypassed.**

``` python
# Must and Required parameter.
_puid = ""
```

Now you can use the chatgpt mailbox password to automatically log in to get session_token.

``` python3
# ChatGPT account password login without session_token if needed.
email_address = ""
password = ""
```

If you login with Google or Microsoft, you can only get another `__Secure-next-auth.session-token` parameter.

``` python
# session_token login without chatgpt account if needed.
session_token = ""
```

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
