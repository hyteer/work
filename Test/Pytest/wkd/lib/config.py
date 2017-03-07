# coding: utf-8
import os
from .utils import Utils
from . import ui
from . import api
from . import param
from . import combo
from . import url


ROOT_DIR = os.path.abspath(
    os.path.dirname(__file__)
)


class Config(object):
    '''
    基础配置
    '''

    CAPTCHA = '1111'
    PROXY = {'http' : 'http://127.0.0.1:8888'}
    URL = 'http://testwkd.snsshop.net/login/index'
    INIT_FLAG = 0
    ENV = 'default'
    SSID = None
    #COOKIE = None
    DEBUG = 'no'

    # 模块

    api = api
    API = api.API
    Api = api.Api
    ui = ui
    Ui = ui.Ui
    url = url
    Url = url.Url
    combo = combo
    Combo = combo.Combo
    Param = param.Param
    param = param

    LOADED_API = {}
    LOADED_MODULES = {}

    # 辅助功能函数
    Utils = Utils


    # 方法函数
    @staticmethod
    def get_flag():
        return Config.INIT_FLAG

    @staticmethod
    def set_flag(flag):
        Config.INIT_FLAG = flag

    @staticmethod
    def get_cookie():
        return {'PHPSESSID': Config.SSID}

    @property
    def cookie(self):
        return {'PHPSESSID': Config.SSID}

    @staticmethod
    def load_api_mod(*params):
        for mod in params:
            if mod in Config.API and mod not in Config.LOADED_API:
                api = Config.API[mod]
                Config.LOADED_API[mod] = api()

        return True


    HEADERS = {
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Upgrade-Insecure-Requests':'1',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'YT': 'for debug'
        }
    HEADERS_JSON = {
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Upgrade-Insecure-Requests':'1',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type':'application/json;charset=UTF-8',
        'YT': 'for debug'
    }


class AutoConfig(Config):
    '''
    微客多自动化测试环境配置(自动化测试专用)
    '''
    USERNAME = '20170108@qq.com'
    PASSWORD = '123456'
    USER_ID = '13764904'
    MEMBER_ID = '380'
    SHOP_ID = 98204
    TERMINAL_ID = 109828
    URL = 'http://testwkd.snsshop.net'
    URL_TERMINAL = 'http://testwkdshopadmin.snsshop.net'
    WX_URL = 'http://wkdianshang.testwkdwx.snsshop.net/wkdianshang'
    TITLE = u"微客多后台管理系统"

class TestConfig(Config):
    '''
    微客多测试环境配置(手工测试环境)
    '''
    USERNAME = 20170705
    PASSWORD = 123456
    USER_ID = '13764874'
    MEMBER_ID = '373'
    URL = 'http://testwkd.snsshop.net'
    URL_TERMINAL = 'http://testwkdshopadmin.snsshop.net'
    WX_URL = 'http://wkdianshang.testwkdwx.snsshop.net/wkdianshang'
    TITLE = u"微客多后台管理系统"

class BetaConfig(Config):
    USERNAME = 20151228
    PASSWORD = 123456
    USER_ID = '13764779'
    MEMBER_ID = '267'
    URL = 'http://betanewwsh.snsshop.net'
    TITLE = u"商户后台管理系统"


class DevConfig(Config):
    USER = 7638800811
    PASSWORD = 518000
    URL = 'http://335.newwsh.snsshop.net'

class CiConfig(Config):
    USER = 7638800811
    PASSWORD = 518000
    USER_ID = '137240011'
    URL = 'http://shanghutest.cxm'
    URL_TERMINAL = 'http://shopadmintest.cxm'
    URL_WEIXIN = 'http://scliveapp2015.weixintest.cxm/scliveapp2015'



def get_config(env):
    if env == "auto":
        return AutoConfig()
    elif env == "test":
        return TestConfig()
    elif env == "beta":
        return BetaConfig()
    elif env == "dev":
        return DevConfig()
    elif env == "ci":
        return CiConfig()
    else:
        print("Please input a legal env string,eg. 'test','wkd','auto','dev','ci'.")
        return None

# Report Utils
def count_testcase(items):
        case_count = {'Total':0,'YT':0,'BW':0,'XZ':0}
        for item in items:
            if hasattr(item.parent.obj,'AUTHOR') :
                case_count['Total'] += 1
                if item.parent.obj.AUTHOR == 'YT':
                    case_count['YT'] += 1
                elif item.parent.obj.AUTHOR == 'BW':
                    case_count['BW'] += 1
                elif item.parent.obj.AUTHOR == 'XZ':
                    case_count['XZ'] += 1
        return case_count

# Run filters
def run_author_only_filter(items,config):
    items2 = items.copy()
    author = config.getoption('author')
    items.clear()
    for item in items2:
        if hasattr(item.parent.obj,'AUTHOR'):
            if item.parent.obj.AUTHOR == author:
                items.append(item)


