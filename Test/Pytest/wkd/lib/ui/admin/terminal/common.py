# -*- coding: utf-8 -*- 

from ..actions import Action
from . import locators as LC


class Common(Action):

    def __init__(self,conf):
        Action.__init__(self,conf)
        
        
    def select_time(self):
        self.select_frame(LC.COMMON['时间选择框'])
        