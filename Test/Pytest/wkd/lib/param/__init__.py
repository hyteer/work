from .market import Market
from .member import Member
from .shop import Shop
from .weixin import Weixin
from .terminal import Terminal

PARAM = {

}

__all__ = [
    'Market',
    'Member',
    'Shop',
    'Weixin',
    'Terminal',
    'Param'
]

class Param(object):
    def __init__(self,conf):
        self.conf = conf
        self.market = Market(conf)
        self.member = Member(conf)
        self.weixin = Weixin(conf)
        self.shop = Shop(conf)
        self.terminal = Terminal(conf)

