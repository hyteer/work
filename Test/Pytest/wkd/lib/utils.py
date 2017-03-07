# coding: utf-8
'''
常用辅助函数
'''
import time,random



class Utils(object):

    def __init__(self,conf):
        self.conf = conf

    @staticmethod
    def scroll_to(driver,xpath):
        '''
        滚动到指定元素
        '''
        js = """var evaluator = new XPathEvaluator();var result = evaluator.evaluate('""" + xpath + """', document.documentElement, null,XPathResult.ORDERED_NODE_ITERATOR_TYPE, null); var node = result.iterateNext();node.scrollIntoView();"""
        driver.execute_script(js)
        time.sleep(1)

    @staticmethod
    def trav_val(d,key):
      global tempval
      for k,v in d.items():
        if type(v) == dict:
          Utils.trav_val(v,key)
        elif k == key:
          tempval = v
          break
      return tempval

    @staticmethod
    def get_trav_val(d,key):
        tempval = None
        x = Utils.trav_val(d,key)
        tempval = None
        return x
    @staticmethod
    def rand_num(digit=6,sample=None):
        if sample is None:
            sample = ['0','1','2','3','4','5','6','7','8','9']
        num = ''.join(random.sample(sample,8))
        return num

    @staticmethod
    def rand_mobile():
        '''
        随机电话
        '''
        second_num = ''.join(random.sample(['3','5','8'], 1))
        suffix_num = ''.join(random.sample(['0','1','2','3','4','5','6','7','8','9'], 9))
        phone_num = '1' + second_num + suffix_num
        return phone_num

    @staticmethod
    def rand_str():
        randstr = ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))
        return randstr

    @staticmethod
    def rand_cn_str(digit=5):
        randstr = ''.join(random.sample(['一','二','三','四','五','六','七','八','九','十','明','达','科','抚','天','在','工','不','金','木','水','火','土','气','雷','电'], digit))
        return randstr

    @staticmethod
    def rand_name():
        name_len = random.randrange(2,3)
        given_name = ''.join(random.sample(['李','周','马','王','张','邓','肖','魏','赵','胡','罗','钟','韩','刘'], 1))
        first_name = ''.join(random.sample(['辉','明','三','星','柳','六','晴','香','晶','静','伟','达','科','抚','天','敏','工','清','金','木','华','德','可','气','慧','华','喜'], name_len))
        full_name = given_name + first_name
        return full_name




