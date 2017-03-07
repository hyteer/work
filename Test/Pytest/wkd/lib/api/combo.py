

class Combo(object):
    '''
    API操作功能组合
    '''


    def __init__(self,conf):
        self.conf = conf
        self.SHOP_PARAM = conf.param.Shop
        self.Utils = conf.Utils

    def do(self,key):
        dict = {
            '添加一个商品': self.add_a_product,
            '添加一个秒杀活动':self.add_a_secondkill_act,
        }
        return dict[key]

    def add_a_product(self,onsale=True,param=None):
        '''
        添加一个商品,默认上线并采用默认商品参数，也可指定参数和是否上线
        '''
        pd = self.conf.api.Shop(self.conf)
        if param is None:
            param = self.SHOP_PARAM(self.conf).product_add()
        resp = pd.product_add(param)
        product_id = resp['errmsg']['product']['id']
        print("ProductID:",product_id)
        if onsale:
            payload = {"ids":[product_id]}
            pd.product_on_sale(payload)
        return product_id

    def add_a_secondkill_act(self,onsale=True,param=None):

        pass