from .market import Market
from .member import Member
from .weixin import Weixin
from .myvkd import MyVkd
from .shop import Shop
from .terminal import Terminal
from .combo import Combo

API = {
        'member':Member,
        'weixin':Weixin,
        'shop':Shop,
        'market':Market,
        'myvkd':MyVkd,
        'terminal':Terminal,
    }

__all__ = [
    'Market',
    'Member',
    'Weixin',
    'MyVkd',
    'Shop',
    'Terminal',
    'API',
    'Api',
    'Combo'
]

class Api(object):
    def __init__(self,conf):
        self.conf = conf
        self.market = Market(conf)
        self.member = Member(conf)
        self.weixin = Weixin(conf)
        self.shop = Shop(conf)
        self.terminal = Terminal(conf)
        self.myvkd = MyVkd(conf)
        self.combo = Combo(conf)

