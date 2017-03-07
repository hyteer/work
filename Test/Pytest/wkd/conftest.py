# coding: utf-8
import sys,os
Path=os.path.abspath(__file__)
BASE_DIR=os.path.dirname(Path)
sys.path.append(BASE_DIR)
print("BASE_DIR:%s" % BASE_DIR)

import pytest
import lib.init as init
from lib.api.member import Member
from lib.common import Common
from lib.config import Config
from lib.config import get_config
from lib.config import count_testcase,run_author_only_filter
from lib.param.utils import Utils
from lib.ui import Ui
from lib.api import Api
from lib.param import Param
GFLAG = False
ss = 123


def pytest_addoption(parser):
    '''
    获取环境变量
    :param parser:
    '''

    parser.addoption("--testenv", action="store", default="auto",help="please input a testenv,eg.'test','dev','ci'")
    parser.addoption("--mydebug", action="store", default="no",help="input '--mydebug=yes' to print debug info.")
    parser.addoption("--dbg", action="store", default="no",help="set global DEBUG_LEVEL,example: '--dbg=1'")
    parser.addoption("--runflag", action="store", default="no",help="set global RUN_FLAG,example: '--runflag=ready'")
    parser.addoption("--author", action="store", default="",help="set global RUN_AUTHOR,example: '--author=YT'")


@pytest.fixture()
def init_conf(request):
    '''
    初始化
    :param request:
    '''
    print("\nInitializing environment...")
    env = request.config.getoption('--testenv')
    run_flag = request.config.getoption('--runflag')
    #debug = request.config.getoption('--mydebug')
    debug_level = request.config.getoption('--dbg')
    run_author = request.config.getoption('--author')
    print("DEBUG_LEVEL:%s"% debug_level)
    print("RUN_AUTHOR:%s"% run_author)
    cfg = get_config(env)
    Config.set_flag(1)
    Config.ENV = env
    Config.RUN_AUTHOR = run_author
    #os.environ["RUNFLAG"]=run_flag
    Config.RUN_FLAG = run_flag
    Config.DEBUG_LEVEL = debug_level
    print("Env:%s" % env)
    return cfg

@pytest.fixture()
def init_admin_api(request):
    '''
    初始化API模块
    :param request:
    '''
    print("\nAPI logining...")
    env = request.config.getoption('--testenv')
    cfg = get_config(env)

    init.api_login(cfg)
    print("Initializing api sets...")
    #Config.member = Member()
    Config.COMMON = Common()

@pytest.fixture()
def init_weixin_api(request):
    '''
    初始化微信API模块
    :param request:
    '''
    print("\nWeixin API logining...")
    env = request.config.getoption('--testenv')
    cfg = get_config(env)
    init.wx_api_login(cfg)
    print("Initializing weixin api sets...")


@pytest.fixture(scope="module")
def conf(request):
    '''
    全局功能及配置
    :param request:
    '''
    flag = Config.get_flag()
    env = request.config.getoption('--testenv')
    cfg = get_config(env)
    if flag == 1:
        return cfg
    else:
        cfg = init_conf(request)
        init_admin_api(request)
        init_weixin_api(request)
        #cfg.Ui = Ui(cfg)
        #cfg.Api = Api(cfg)
        #cfg.Param = Param(cfg)
        return cfg

# Reports

@pytest.fixture()
def pytest_collection_modifyitems(items,config):
    if config.getoption('author'):
        run_author_only_filter(items,config)
    case_count = count_testcase(items)
    print(case_count)

#not_ready = pytest.mark.skipif(flag==1,"Not Ready")

# 环境清理
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        print("失败的用例:%s" % rep.location[2])
        if hasattr(item.parent.obj,'driver'):
            item.parent.obj.driver.close()
            print("已关闭driver")


# 常用功能
@pytest.fixture
def u8filter():
    utils = Utils()
    return utils.utf8_filter

@pytest.fixture
def utils():
    Config.UTILS = Utils()

@pytest.fixture(scope="module")
def load_api():
    '''
    动态加载API模块
    :return:
    '''
    return Config.load_api_mod

