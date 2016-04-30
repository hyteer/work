# encoding: utf-8

###### 框架元素 ######
frame_form_table = "83"
frame_form_form = "86"
frame_form_search = "88"
frame_pop = "//div[@ligeruiid='Dialog1001']//iframe"

###### Common ######
# 添加
add = "//div[@class='panel-toolbar']//a/span/parent::a[contains(text(),'添加')]"
# 添加列
add_col = "//div[@class='panel-toolbar']//a[@onclick='clickAddRow()']"
# 关闭
close = "//div[@class='panel-toolbar']//a[@onclick='dialog.close();']"

###### 登录 ######
login_name = 'username'
login_pass = 'password'


###### 流程 ######
process_main_id = '80'

###### 表单 ######
table_main = "//label[contains(text(),'主表')]/input"
table_slave = "//label[contains(text(),'从表')]/input"








