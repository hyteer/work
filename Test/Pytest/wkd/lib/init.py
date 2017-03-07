# coding: utf-8
# Filename: init.py
'''
初始化模块配置
'''
#import Cookie
# Python3
import http.cookies
import json

import requests

from .config import Config
from .param.utils import Utils
from .api.generic import Generic as g
utils = Utils()

def api_login(conf):
    '''
    登录微商户API
    Returns:cookies
    '''
    baseurl = conf.URL
    headers = conf.HEADERS
    captcha = conf.CAPTCHA
    username = conf.USERNAME
    password = conf.PASSWORD

    r = requests.get(baseurl, headers=headers)
    cookie = http.cookies.SimpleCookie(r.headers['Set-Cookie'])
    sessionid = cookie['PHPSESSID'].value
    # Login
    print("--- API Login ---")
    url = baseurl+"/login/login-ajax"
    postdata = {'captcha': captcha, 'username': username, 'password': password}
    cookies = {'PHPSESSID': sessionid}

    r = requests.post(url, data=postdata,headers=headers,cookies=cookies)
    data = json.loads(r.text)
    errcode = data['errcode']
    print("errcode:", data['errcode'])
    assert errcode == '0'
    Config.SSID = sessionid
    Config.COOKIE = {'PHPSESSID': sessionid}

    if conf.DEBUG == 'yes':
        str = u"-------------【调试】------------"
        print(utils.utf8_filter(str))
        #print "Cookies:",r.cookies
        #print "Raw:",r.raw
        print("cookies:", cookies)
        print("SessionID:", sessionid)
        print("Config::SSID:%s" % conf.SSID)
        print("Headers:",r.headers)
        print("headers:",r.headers)
        #length = len(r.text)
        #print "Response:", r.text[1:length]
        #print("r.content char:",chardet.detect(r.content))
        print("r.text:", utils.utf8_filter(r.text))

    return cookies

def wx_api_login(conf):
    '''
    登录微信前端API
    Returns:session
    '''
    baseurl = conf.WX_URL
    url = baseurl + "/oauth/testing?id=" + conf.USER_ID
    print("Weixin User_ID:",conf.USER_ID)
    print("URL:",url)
    headers = conf.HEADERS
    # Login
    print("--- Weixin API Login ---")
    r = requests.get(url,headers=headers)
    cookie = http.cookies.SimpleCookie(r.headers['Set-Cookie'])
    sessionid = cookie['PHPSESSID'].value
    cookies = {'PHPSESSID': sessionid}
    Config.WX_COOKIE = cookies

    #s = requests.Session()
    #s.get(baseurl)
    #s.get(url)
    #Config.WX_SS = s


    return cookies
