# -*- coding: utf-8 -*-
'''
First Author：cooolr
Second Author：chatgpt
Date：2023-02-22
'''

import os
import requests
from hashlib import md5
from urllib.parse import unquote
from flask import Flask, request, redirect, send_file, Response, stream_with_context, make_response
from werkzeug.routing import BaseConverter

# Use gevent to speed up if needed.
'''
from gevent.pywsgi import WSGIServer
from gevent import monkey
monkey.patch_all()
'''

# Proxy can be set if needed.
proxies = {"https": ""}

# Must and Required parameter.
_puid = ""

# session_token and cf_clearance, get rtom cookies.
session_token = ""
cf_clearance = ""

# listen_url can be change if needed.
# if you change this, you should delete static resource.
listen_url = "http://127.0.0.1:8011"

# Password can be added if needed. example:  md5(('test@qq.com123456').encode()).hexdigest()
user_id = ""

# Login and get cookie_dict
cookie_dict = {
    "_puid":_puid, 
    "__Secure-next-auth.session-token":session_token,
    "cf_clearance": cf_clearance
}
cookie = '; '.join([f'{k}={v}' for k,v in cookie_dict.items()])

headers = {
    'authority': 'chat.openai.com',
    'accept': 'text/event-stream',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'cookie': cookie,
    'dnt': '1',
    'origin': 'https://chat.openai.com',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

# set accessToken
def get_authorization():
    """get accessToken"""
    url = "https://chat.openai.com/api/auth/session"
    r = requests.get(url, headers=headers, cookies=cookie_dict, proxies=proxies)
    print(r.json()['user']['email'], 'get accesstoken successful.')
    authorization = r.json()["accessToken"]
    return "Bearer "+authorization

headers["authorization"] = get_authorization(headers, cookie_dict)

app = Flask(__name__)

# custom regex converter
class RegexConverter(BaseConverter):
    def __init__(self, map, *args):
        self.map = map
        self.regex = args[0]

# register regex converter
app.url_map.converters['regex'] = RegexConverter

# if change http://127.0.0.1:8011, should be delete.
resource_dir = './resource'
os.makedirs(resource_dir, exist_ok=True)

# define the login request page
with open('login.html', 'r', encoding='utf-8') as f:
    login_html = f.read()
with open('login_failed.html', 'r', encoding='utf-8') as f:
    login_failed_html = f.read()

# login authentication
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.cookies.get("accessToken")  == user_id:
        return redirect('/chat',302)
    if request.method =='GET':
        return login_html
    username = request.form['username']
    password = request.form['password']
    # user_id加密过程
    uid = md5((username+password).encode()).hexdigest()
    if uid == user_id:
        resp = make_response(redirect('/chat',302))
        resp.set_cookie("accessToken", uid, max_age=604800)
        return resp
    else:
        return login_failed_html

# handles all HTTP request methods
@app.route('/<path:uri>', methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD', 'TRACE', 'CONNECT', 'PATCH'])
def index(uri):
    # authentication cookie
    if user_id and request.cookies.get("accessToken") != user_id:
        return redirect("/", 302)
    # signout
    if 'auth/signout' in uri:
        resp = make_response('{"url":"/"}'.encode())
        resp.delete_cookie("accessToken")
        return resp
    param = '&'.join([f'{i}={j}' for i,j in request.args.items()])
    url = f"https://chat.openai.com/{uri}?{param}" if param else f"https://chat.openai.com/{uri}"
    # If the request is a static resource, otherwise get it from the remote
    if any(x in url for x in ('.jpg', '.png', '.ico', '.woff', '.otf', '.css', '.js')):
        ext = url.split('.')[-1]
        filename = md5(url.encode('utf-8')).hexdigest()
        filepath = os.path.join(resource_dir, f'{filename}.{ext}')
        if os.path.isfile(filepath):
            return send_file(filepath)
        else:
            r = requests.get(url, headers=headers, cookies=cookie_dict, data=request.data, proxies=proxies)
            if '.js' in url or '.css' in url:
                content = r.content.replace(b'https://chat.openai.com', listen_url.encode())
            else:
                content = r.content
            with open(filepath, 'wb') as f:
                f.write(content)
            return send_file(filepath)
    # cache page html
    elif '/backend' not in url and '/cdn-cgi' not in url and '.' not in url:
        filename = md5(url.encode('utf-8')).hexdigest()
        filepath = os.path.join(resource_dir, f'{filename}')
        if os.path.isfile(filepath):
            return send_file(filepath)
        else:
            r = requests.get(url, headers=headers, cookies=cookie_dict, data=request.data, proxies=proxies)
            content = r.content.replace(b'https://chat.openai.com', listen_url.encode())
            with open(filepath, 'wb') as f:
                f.write(content)
            return send_file(filepath)
    # stream request
    elif 'conversation' in url:
        # If a live conversation is requested, the response is streamed
        r = requests.request(request.method, url, headers=headers, cookies=cookie_dict, data=request.data, proxies=proxies, stream=True)
        response = Response(stream_with_context(r.iter_content(chunk_size=1024)))
        response.headers['content-type'] = r.headers.get('content-type')
        return response
    # backend api request
    else:
        headers['cookie'] = '; '.join([f'{k}={v}' for k,v in cookie_dict.items()])
        r = requests.request(request.method, url, headers=headers, cookies=cookie_dict, data=request.data, proxies=proxies)
        cookie_dict.update(r.cookies)
        return r.content.replace(b'https://chat.openai.com', listen_url.encode())

if __name__ == "__main__":
    host = '0.0.0.0' if '127.0.0.1' not in listen_url else '127.0.0.1'
    port = int(listen_url.split(':')[-1]) if ':' in listen_url.split('//')[1] else 80
    app.run(host=host, port=port, threaded=True)
    # WSGIServer((host, port), app).serve_forever()
    # open in browser: http://127.0.0.1:8011/chat
