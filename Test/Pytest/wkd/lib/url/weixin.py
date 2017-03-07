from .urls import WeixinUrl as Wx

wx_url = Wx()

class Weixin(object):

    def __init__(self,conf):
        self.BASE_URL = conf.WX_URL

    def order(self,key):
        return self.BASE_URL + wx_url.ORDER[key]




