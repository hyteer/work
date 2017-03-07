from ..actions import Action
from . import locators as LOCATOR
from .common import Common
from .terminal_manage import TerminalManage
from .push_strategy_manage import PushStrategyManage


class Terminal(Action):
    def __init__(self,conf):
        self.common = Common(conf)
        self.terminal_manage = TerminalManage(conf)
        self.push_strategy_manage = PushStrategyManage(conf)