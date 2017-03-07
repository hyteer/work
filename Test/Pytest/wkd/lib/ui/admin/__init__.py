'''
Admin UI库
'''
from . import market
from . import terminal
from .common import Common

Market = market.Market
Terminal = terminal.Terminal

class Admin(object):

    def __init__(self,conf):
        self.common=Common(conf)
        self.market = market.Market(conf )
        self.terminal = terminal.Terminal(conf)

__all__ = [
    'Market',
    'Common',
    'Terminal'
]

