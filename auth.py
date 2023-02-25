# -*- coding: utf-8 -*-

import time
import requests
from urllib.parse import quote

proxies = {}

headers = {
    'authority': 'chat.openai.com',
    'cookie': '',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

cookies = {}

session = requests.Session()

def get_csrf_token(_puid):
    cookies["_puid"] = _puid
    url = "https://chat.openai.com/api/auth/csrf"
    headers["cookie"] = '; '.join([f'{k}={v}' for k,v in cookies.items()])
    r = session.get(url, headers=headers, cookies=cookies, proxies=proxies)
    cookies.update(r.cookies)
    cookies.update(session.cookies)
    csrf_token = r.json()["csrfToken"]
    return csrf_token

def get_authrize_url(csrf_token):
    url = "https://chat.openai.com/api/auth/signin/auth0?prompt=login"
    payload=f'callbackUrl=%2Fchat&csrfToken={csrf_token}&json=true'
    cookie = '; '.join([f'{k}={v}' for k,v in cookies.items()])
    headers = {
        'authority': 'chat.openai.com',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    r = session.post(url, headers=headers, data=payload, cookies=cookies, proxies=proxies)
    cookies.update(r.cookies)
    cookies.update(session.cookies)
    return r.json()["url"]

def get_identifier_url(authrize_url):
    headers["cookie"] = '; '.join([f'{k}={v}' for k,v in cookies.items()])
    r = session.get(authrize_url, headers=headers, cookies=cookies, proxies=proxies)
    cookies.update(r.cookies)
    cookies.update(session.cookies)
    auth0_compat = session.cookies.get("auth0_compat")
    return r.url

def get_password_url(identifier_url, email_address):
    state = identifier_url.split("state=")[1]
    url = f"https://auth0.openai.com/u/login/identifier?state={state}"

    payload = f'state={state}&username={quote(email_address)}&js-available=true&webauthn-available=true&is-brave=false&webauthn-platform-available=false&action=default'
    cookie = '; '.join([f'{k}={v}' for k,v in cookies.items()])
    headers = {
      'authority': 'auth0.openai.com',
      'content-type': 'application/x-www-form-urlencoded',
      'cookie': cookie,
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    r =session.post(url, headers=headers, data=payload, cookies=cookies, proxies=proxies)
    cookies.update(r.cookies)
    cookies.update(session.cookies)
    return r.url

def get_resume_state(password_url, email_address, password):
    state = password_url.split("state=")[1]

    payload = f'state={state}&username={quote(email_address)}&password={quote(password)}&action=default'
    cookie = '; '.join([f'{k}={v}' for k,v in cookies.items()])
    headers = {
      'authority': 'auth0.openai.com',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
      'cache-control': 'no-cache',
      'content-type': 'application/x-www-form-urlencoded',
      'cookie': cookie,
      'dnt': '1',
      'origin': 'https://auth0.openai.com',
      'pragma': 'no-cache',
      'referer': f'https://auth0.openai.com/u/login/password?state={state}',
      'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    r = session.post(password_url, headers=headers, data=payload, cookies=cookies,proxies=proxies)
    cookies.update(r.cookies)
    cookies.update(session.cookies)

def get_cookies(_puid, email_address, password):
    get_login_cookie(_puid)
    time.sleep(1)
    csrf_token = get_csrf_token()
    time.sleep(1)
    authrize_url = get_authrize_url(csrf_token)
    time.sleep(1)
    identifier_url = get_identifier_url(authrize_url)
    time.sleep(1)
    password_url = get_password_url(identifier_url, email_address)
    time.sleep(1)
    get_resume_state(password_url, email_address, password)
    return cookies


if __name__ == "__main__":
    print(get_cookies("user-xxxxxxxxxx", "test@proton.me", "123456"))
