from .check import Check

class Combo(object):

    def __init__(self,conf):
        self.conf = conf
        self.check = Check(conf)


__all__ = [
    'Check',
    'Combo'

]