# coding: utf-8
'''
辅助功能函数
'''
import sys
import random,string


class Utils(object):

    def utf8_filter(self,str):
        '''
        UTF8终端打印编码过滤
        :param str:
        :return:
        '''
        if sys.stdout.encoding == 'cp936':
            #sys.stdout = UnicodeStreamFilter(sys.stdout)
            return str
        elif sys.stdout.encoding == 'UTF-8':
            return str.encode('utf-8')
        else:
            return str.encode('utf-8')

    def float_compare(self,x,y,flag="yes"):
        '''
        浮点数比较
        :param x:
        :param y:
        :param flag: 可选参数：'yes'/'no',默认为'yes',即为正向比较，'no'为反向比较
        :return:True
        '''
        print("x:%s,y:%s" % (x,y))
        if flag == "yes":
            assert float(x) == float(y)
            return True
        else:
            assert float(x) != float(y)
            return True

    def floa_not_equalst(self,x,y):
        '''
        浮点数反向比较，即不等于
        :param x:
        :param y:
        :return: True
        '''
        print("x:%s,y:%s" % (x,y))
        assert float(x) != float(y)
        return True

    @staticmethod
    def rand_num(digit=6,sample=None):
        if sample is None:
            sample = ['0','1','2','3','4','5','6','7','8','9']
        randNameX = "".join(random.sample(sample, digit))
        return randNameX

    @staticmethod
    def rand_mobile():
        '''
        随机电话
        '''
        second_num = "".join(random.sample(['3','5','8'], 1))
        suffix_num = "".join(random.sample(['0','1','2','3','4','5','6','7','8','9'], 9))
        phone_num = '1' + second_num + suffix_num
        return phone_num

    @staticmethod
    def rand_str():
        randstr = "".join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))
        return randstr

    @staticmethod
    def rand_cn_str(digit=5):
        randstr = "".join(random.sample(['一','二','三','四','五','六','七','八','九','十','明','达','科','抚','天','在','工','不','金','木','水','火','土','气','雷','电'], digit))
        return randstr

    @staticmethod
    def rand_name():
        name_len = random.randrange(2,3)
        given_name = "".join(random.sample(['李','周','马','王','张','邓','肖','魏','赵','胡','罗'], 1))
        first_name = "".join(random.sample(['辉','明','三','星','柳','六','晴','香','晶','静','伟','达','科','抚','天','敏','工','清','金','木','水','德','土','气','慧','华'], name_len))
        full_name = given_name + first_name
        return full_name
