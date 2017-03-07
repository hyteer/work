import time


class Api(object):
    '''
    API操作功能组合
    '''

    def __init__(self,conf):
        self.conf = conf
        self.wx = conf.ui.Weixin(conf)
        self.WX_LC = self.wx.LOCATOR
        #self.ADMIN_LC = conf.admin.LOCATOR
        self.SHOP_PARAM = conf.param.Shop
        self.Utils = conf.Utils

    def add_a_second_kill_act(self):
        pass





