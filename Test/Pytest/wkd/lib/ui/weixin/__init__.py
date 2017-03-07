'''
Weixin UI库
'''
from .actions import Action
from .product import Product
from .address import Address
from .cart import Cart
from . import locators as LOCATOR
from .common import Common
from .order import Order
from .userhome import UserHome
#from .combo import Combo


class Weixin(Action):

    def __init__(self,conf):
        Action.__init__(self,conf)
        self.product = Product(conf )
        self.order = Order(conf)
        self.cart = Cart(conf)
        self.address = Address(conf)
        self.common = Common(conf)
        self.userhome = UserHome(conf)
        #self.combo = Combo(conf)
        self.LOCATOR = LOCATOR

    def bottom_menu(self,key):
        '''
        底部主菜单
        '''
        self.G.click(self.conf.wxdriver,LOCATOR.BOTTOM_MENU[key])


__all__ = [
    'Action',
    'Product',
    'Order',
    'Address',
    'Cart',
    'LOCATOR',
    'Weixin',
    'UserHome',
    #'Combo'

]
