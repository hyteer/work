from . import weixin
#from . import admin

Weixin = weixin.Weixin


class Url(object):

    def __init__(self,conf):
        self.weixin = weixin.Weixin(conf)

__all__ = [
    'Weixin',
    'Url'
]