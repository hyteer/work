from ..actions import Action
from . import locators as LC


class Common(Action):

    def __init__(self,conf):
        Action.__init__(self,conf)

    def click(self, key, param=None):
        '''
        点击
        '''
        if param:
            # import pdbpdb.set_trace()
            self.G.click(self.conf.driver, LC.COMMON[key] % param)
        else:
            self.G.click(self.conf.driver, LC.COMMON[key])

    def input(self, key, value):
        '''
        输入
        '''
        self.G.input(self.conf.driver, xpath=LC.COMMON[key], value=value)

    def choose(self, key, index=None):
        '''
        选择
        '''
        self.G.choose(self.conf.driver, LC.COMMON[key], index)

    def get_value(self, key):
        '''
        获取元素value
        '''
        self.G.get_value(self.conf.driver, LC.COMMON[key])


    def get_text(self,key,param=None):
        '''
        获取文本
        '''
        if param:
            #import pdb pdb.set_trace()
            txt = self.G.get_text(self.conf.driver,LC.COMMON[key] % param)
            return txt
        else:
            txt = self.G.get_text(self.conf.driver, LC.COMMON[key])
            return txt






