'''
admin market UI库
'''
from ..actions import Action
from ..actions import Action
from . import locators as LOCATOR
from .favoure_activity import FavoureActivity
from .offline_activity import OfflineActivity
from .promot_activity import PromotActivity
from .sales_activity import SalesActivity
from .common import Common


class Market(Action):


    def __init__(self,conf):
        Action.__init__(self,conf)
        self.offline_activity=OfflineActivity(conf)
        self.sales_activity= SalesActivity(conf )
        self.favoure_activity = FavoureActivity(conf)
        self.promot_activity = PromotActivity(conf)
        self.common = Common(conf)
        self.LOCATOR = LOCATOR


__all__ = [
    'Market',
    'Common',
    #'Terminal',
]


