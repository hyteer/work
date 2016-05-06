# encoding: utf-8
import random
import string

class runEnv():
    PLATFORM = "none"
    BROWSER = "no browser"
    desired_caps = {
            'platform': PLATFORM,
            'browserName': BROWSER
        }
    '''
    def setPlatform(self,platform):
        #self.PLATFORM = platform  # 用self则设置的是实例的变量值而不是类的变量值
        runEnv.PLATFORM = platform  # 设置类变量的值
    '''
def setGlb(pf,br):
    setPlatform(pf)
    setBrowser(br)
    runEnv.desired_caps['platform'] = getPlatform()
    runEnv.desired_caps['browserName'] = getBrowser()
def getGlb():
    return runEnv.desired_caps

def setBrowser(browser):
    runEnv.BROWSER = browser
def setPlatform(platform):
    runEnv.PLATFORM = platform
def getBrowser():
    return runEnv.BROWSER
def getPlatform():
    return runEnv.PLATFORM

#PLATFORM = 'WINDOWS'
#BROWSER = 'firefox'


# HOME='http://192.168.31.237:8090/bw_sms'    #home page url
HOME = 'http://58.96.175.0:8080/bestwonder/'  # Hongkong
HOME_LOGINED = 'http://58.96.175.0:8080/bestwonder/platform/console/main.ht'  # 登录后跳转页
DELAY=2

username = 'admin'
password = 'bestwonder'

# -------Table args-----------
# 表
tbName = 'auto_test_table'
tbDesc = 'auto_test_table desc'
tbRandName = 'a_testtable_' + str(random.randint(100, 999))
# 字段
fnum = 1
fname = 'field'
fname2 = fname + str(fnum)
fdesc = 'Just for testing'
# ----------Org----------------
uname = "autouser"
upass = "passwd"
randName = "autouser" + str(random.randint(100,999))
randName6X = string.join(random.sample(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','@','#','%','^','*','-'], 6)).replace(" ","")
randName8X = string.join(random.sample(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','@','#','%','^','*','-'], 6)).replace(" ","")
randPass6X = string.join(random.sample(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','@','#','%','^','*','-'], 8)).replace(" ","")





