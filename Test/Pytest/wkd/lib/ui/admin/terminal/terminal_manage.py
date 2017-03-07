# -*- coding: utf-8 -*- 

from ..actions import Action
from . import locators as LC
import time,random

class TerminalManage(Action):
    
    def __init__(self,conf):
        Action.__init__(self,conf)

    def click(self,key,param=None):
        '''
        点击
        '''
        if param:
            super(TerminalManage,self).click(LC.TERMINAL_LIST[key] %param)
        else:
            super(TerminalManage,self).click(LC.TERMINAL_LIST[key])

    def input(self,key,value):
        '''
        输入
        '''
        print("xpath:",LC.TERMINAL_LIST[key])
        super(TerminalManage,self).input(LC.TERMINAL_LIST[key], value)

    def choose(self,key,index=None):
        '''
        选择
        '''
        self.G.choose(self.conf.driver,LC.TERMINAL_LIST[key],index)
        
    def xpath_with_index(self,key,index):
        xpath = '(' + LC.TERMINAL_LIST[key] + ')'+ '[' + str(index) + ']'
        return xpath
    
    def get_matching_xpath_count(self,key):
        '''
        获取xpath个数
        '''
        return(super(TerminalManage,self).get_matching_xpath_count(LC.TERMINAL_LIST[key]))
    
    def get_text(self,key,index=None):
        '''
        获取text值
        '''
        xpath = ''
        if index:
            xpath = self.xpath_with_index(key, index)
        else:
            xpath = LC.TERMINAL_LIST[key]
        text = super(TerminalManage,self).get_text(xpath)
        return text
    
    def get_terminal_status(self,index):
        '''
        获取分店状态
        '''
        xpath = self.xpath_with_index("营业状态", index)
        return self.get_checkbox_status(xpath)
    
    def switch_terminal_status(self,index,status):
        '''
        切换分店状态
        '''
        xpath = self.xpath_with_index("营业状态", index)
        super(TerminalManage,self).click(xpath)
        message = self.conf.driver.switch_to.alert.text
        if status:
            message = '禁用成功'
        else:
            message = '开启成功'
        self.conf.driver.switch_to.alert.accept()
        time.sleep(2)
        
    def check_terminal_info(self,terminalList):
        terminalNum = len(terminalList)
        for i in range(terminalNum):
            #分店名称
            shopNameXpath = self.xpath_with_index("分店名称", i+1)
            shopName = super(TerminalManage,self).get_text(shopNameXpath)
            assert terminalList[i]['shopInfo']['name'] == shopName
            #创建时间
            createXpaht = self.xpath_with_index("分店创建时间", i+1)
            createTime = super(TerminalManage,self).get_text(createXpaht)
            createdTimeStr = terminalList[i]['shopInfo']['created']
            localTimeStr = time.localtime(createdTimeStr)
            createStr = time.strftime("%Y-%m-%d %H:%M:%S",localTimeStr)
            assert createTime == createStr
            #分店地址
            shopAddressXpath = self.xpath_with_index("分店地址", i+1)
            shopAddress = super(TerminalManage,self).get_text(shopAddressXpath)
            assert terminalList[i]['shopInfo']['address'] == shopAddress
            #联系电话
            phoneNumberXpath = self.xpath_with_index("分店联系电话", i+1)
            phoneNumber = super(TerminalManage,self).get_text(phoneNumberXpath)
            assert terminalList[i]['shopInfo']['phone'] == phoneNumber
            #营业状态
            shopStatus = self.get_terminal_status(i+1)
            if terminalList[i]['shopInfo']['deleted'] == 1:
                assert shopStatus is True
            elif terminalList[i]['shopInfo']['deleted'] == 1:
                assert shopStatus is False
            
    def get_select_list_items(self,key,attribute='label'):
        return(super(TerminalManage,self).get_select_list_items(LC.TERMINAL_LIST[key],attribute))    
     
    def select_from_list_by_index(self,key,index):
        print("xpath:",LC.TERMINAL_LIST[key])
        super(TerminalManage,self).select_from_list_by_index(LC.TERMINAL_LIST[key], index)
        
    def wait_until_element_is_visible(self,key):
        super(TerminalManage,self).wait_until_element_is_visible(LC.TERMINAL_LIST[key])
    
    def select_image(self):
        super(TerminalManage,self).wait_until_element_is_visible(LC.TERMINAL_LIST['图库选择列表'])
        time.sleep(1)
        imageCount = self.get_matching_xpath_count('图库选择列表')
        print("图片数:",imageCount)
        randomIndex = random.randint(1,imageCount)
        xpath = self.xpath_with_index('图库选择列表', randomIndex)
        print("image xpath:",xpath)
        super(TerminalManage,self).click(xpath)
        self.click('从图库选择确定按钮')
