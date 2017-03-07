# coding: utf-8
'''
API库通用功能函数
'''

import json
import requests


class Generic(object):

    @staticmethod
    def post_requests(conf,url,data=None,id=None,page=False,header='json',terminal=False):
        '''
        通用Post请求函数封装
        :param conf:
        :param url:
        :param data:
        :param id:
        :param page:
        :param header:
        :return:content
        '''
        print("\n--- API: " + url + " ---")
        if terminal:
            url = conf.URL_TERMINAL + url
        else:
            url = conf.URL+ url
        cookie = conf.cookie
        if header == 'json':
            headers = conf.HEADERS_JSON
            if data != None:
                data = json.dumps(data)
        else:
            headers = conf.HEADERS
        if id != None:
            data = {"id":id}
            data = json.dumps(data)
        if page != False:
            data = {"_page_size":15,"_page":1}
            data = json.dumps(data)
#         print "headers:",headers
        r = requests.post(url,data,headers=headers,cookies=cookie)
        content = json.loads(r.text)
        errcode = content['errcode']
        print("resp:",r.text)
        assert errcode == 0
        #print "errcode is:%s" % errcode
        return content

    @staticmethod
    def wx_post_requests(conf,url,data=None,id=None,page=False,header='json'):
        '''
        微信前端通用Post请求函数封装
        :param conf:
        :param url:
        :param data:
        :param id:
        :param page:
        :param header:
        :return:content
        '''
        print("\n--- WeixinAPI: " + url + " ---")
        url = conf.WX_URL+ url
        cookie = conf.WX_COOKIE
        if header == 'json':
            headers = conf.HEADERS_JSON
            if data != None:
                data = json.dumps(data)
        else:
            headers = conf.HEADERS
        if id != None:
            data = {"id":id}
            data = json.dumps(data)
        if page != False:
            data = {"_page_size":15,"_page":1}
            data = json.dumps(data)
        r = requests.post(url,data,headers=headers,cookies=cookie)
        content = json.loads(r.text)
        errcode = content['errcode']
        assert errcode == 0
        print("resp:",r.text)
        #print "errcode is:%s" % errcode
        return content
