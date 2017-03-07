from . import weixin
from . import admin

Weixin = weixin.Weixin
Admin = admin.Admin

class Ui(object):

    def __init__(self,conf):
        self.weixin = weixin.Weixin(conf)
        self.admin=admin.Admin(conf)

__all__ = [
    'Weixin',
    'Admin'
]