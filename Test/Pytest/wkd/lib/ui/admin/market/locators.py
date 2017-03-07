# coding: utf-8
# 主菜单栏

COMMON={
    '图文标题': '''//input[@name="title"]''',
    '摘要内容': '''//*[@id="form-field-8"]''',
    '活动图片':'''//*[@id="home"]/div[2]/form/div[3]/div/div/a/label/span''',
    '下一步': '''//*[@id="btnConfirm"]''',
    '活动名称': '''//input[@name="name"]''',
    '活动说明': '''//textarea[@name="desc"]''',
    '活动开始时间': '''//*[@id="start_time"]''',
    '活动结束时间': '''//*[@id="end_time"]''',
    '运费策略': '''//select[@ng-model="model['postageSetting']['type']"]''',
    '选择商品按钮': '''//div[@class="page-content"]//a[@ng-click="concatd()"and text()=" 选择商品 "]''',
    '活动价': '''//input[@ng-model="list.buy_price"]''',
    '配额': '''//input[@ng-model="list.quota"]''',
    '每人限购':'''//input[@ng-model="list.limit_buy"]''',
    '保存': '''//a[@ng-click="save($index, list)"]''',
    '分享标题': '''//input[@name="heititle"]''',
    '分享描述': '''//input[@name="hdesc"]''',
    '分享图标': '''//span[@data-title="点击上传图片..."]''',
    '保存并关闭': '''//*[@id="post"]''',
    '»': '''ng-click="selectPage(page + 1, $event)"''',
    '页面总条数': '''//div[@class="page-content"]//span/span''',

}


MAIN_MENU = {
    '公众号': '''//*[@id="headactive"]/li/a[contains(text(),"公众号")]''',
    '微店铺': '''//*[@id="headactive"]/li/a[contains(text(),"微店铺")]''',
    '微会员': '''//*[@id="headactive"]/li/a[contains(text(),"微会员")]''',
    '微营销': '''//*[@id="headactive"]/li/a[contains(text(),"微营销")]''',
    '微杂志': '''//*[@id="headactive"]/li/a[contains(text(),"微杂志")]''',
    '微推广': '''//*[@id="headactive"]/li/a[contains(text(),"微推广")]''',
    '微分店': '''//*[@id="headactive"]/li/a[contains(text(),"微分店")]''',
    '代理商': '''//*[@id="headactive"]/li/a[contains(text(),"代理商")]''',
    '微渠道': '''//*[@id="headactive"]/li/a[contains(text(),"微渠道")]''',
    '微硬件': '''//*[@id="headactive"]/li/a[contains(text(),"微硬件")]''',
    '数据中心': '''//*[@id="headactive"]/li/a[contains(text(),"数据中心")]''',
    '一品一码': '''//*[@id="ypymLink"]/a[contains(text(),"一品一码")]''',
    '社交广告': '''//*[@id="ggtLink"]/a[contains(text(),"社交广告")]''',
    '我的微客多': '''//*[@id="headactive"]/li/a[contains(text(),"我的微客多")]''',
}

# 微店铺菜单栏
SHOP_MENU = {
    '页面管理': '''//a[@href="/page/list"]''',
    '页面分类': '''//a[@href="/page/category"]''',
    '店铺导航': '''//a[@href="/page/menu"]''',
    '商品库': '''//a[@href="/product/list"]''',
    '商品分类': '''//a[@href="/product/category-list"]''',
    '商品规格': '''//a[@href="/product/kind-list"]''',
    '商品评论': '''//a[@href="/product/comment-list"]''',
    '所有订单': '''//a[@href="/order/list"]''',
    '售后订单': '''//a[@href="/order/refund-list"]''',
    '交易设置': '''//a[@href="/order/order-set"]''',
    '快递配送': '''//a[@href="/order/shippingmode"]''',
    '到店自提': '''//a[@href="/order/shipping-way"]''',
    '地址库': '''//a[@href="/order/address-library"]''',
    '订单统计': '''//a[@href="/order/order-shop"]''',

}

# 微会员菜单栏
MEMBERS_MENU = {
    '客户列表': '''//a[@href="/member/list"]''',
    '客户分组': '''//a[@href="/member/group-list"]''',
    '标签管理': '''//a[@href="/members/tag"]''',
    '会员概况': '''//a[@href="/members/profile"]''',
    '会员列表': '''//a[@href="/members/list"]''',
    '实体店会员': '''//a[@href="/members/offline"]''',
    '会员分组': '''//a[@href="/members/group"]''',
    '会员消费记录': '''//a[@href="/members/consumption-record"]''',
    '会员卡设置': '''//a[@href="/members/card"]''',
    '开卡优惠': '''//a[@href="/members/card-gift"]''',
    '成长值管理': '''//a[@href="/members/growth"]''',
    '等级管理': '''//a[@href="/members/grade"]''',
    '会员通知': '''//a[@href="/members/notice"]''',
    '扫码开卡': '''//a[@href="/members/delivery"]''',
    '充值策略': '''//a[@href="/members/stored-policy-list"]''',
    '会员账户交易流水': '''//a[@href="/members/stored-trade"]''',
    '账户交易统计图': '''//a[@href="/members/stored-data"]''',
    '会员折扣': '''//a[@href="/members/discount"]''',
    '节日关怀': '''//a[@href="/members/member-gift-holiday-list"]''',
    '生日关怀': '''//a[@href="/members/member-gift-birth-list"]''',
    '积分流水记录': '''//a[@href="/members/point-flow-record"]''',
    '会员新增趋势': '''//a[@href="/members/member-statistics"]''',
    '消费分层统计': '''//a[@href="/members/cons-statistics"]''',
    '会员卡投放统计': '''//a[@href="/members/member-card-statistics"]''',
    '下拉滚动条': '''//a[@href="/members/member-card-statistics"]''',

}

# 微营销菜单栏
MARKET_MENU = {
    '秒杀活动': '''//a[@href="/second-kill/list"]''',
    '拼团活动': '''//a[@href="/together-buy/list"]''',
    '满减包邮': '''//a[@href="/reduction/list"]''',
    '众筹活动': '''//a[@href="/collect-zan/list"]''',
    '大转盘': '''//a[@href="/market-activity/list"]''',
    '砸金蛋': '''//a[@href="/market-activity/smashegg-list"]''',
    '现金红包': '''//a[@href="/cash-redpack/list"]''',
    '记忆翻翻看': '''//a[@href="/memory-fan/list"]''',
    '丘比特之箭': '''//a[@href="/market-activity/cupidarrow-list"]''',
    '积分活动': '''//a[@href="/activity-points/list"]''',
    '商城红包': '''//a[@href="/redpack/list"]''',
    '卡券活动': '''//a[@href="/card-coupons/list"]''',
    '节日礼包': '''//a[@href="/giftpack/list"]''',
    '购物礼包': '''//a[@href="/cardpack/list"]''',
    '预约活动': '''//a[@href="/reserve/list"]''',
    '摇电视': '''//a[@href="/tv-card-coupons/list"]''',
    '签到活动': '''//a[@href="/signin-setting/list"]''',
    '祝福墙': '''//a[@href="/wish-wall/list"]''',
}

# 微分店菜单栏
TERMINAL_MENU = {
    '分店列表': '''//a[contains(text(),"分店列表")]''',
    '基础设置': '''//a[@href="/terminal/basic-setting"]''',
    '商品管理': '''//a[@href="/terminal/product-list"]''',
    '分店通用首页': '''//a[@href="/terminal/home-setting"]''',
    '分店码推送策略': '''//a[@href="/employees-code/management-stores-policy"]''',
    '员工码推送策略': '''//a[@href="/employees-code/management-employee-policy"]''',
    '分店收款码': '''//a[@href="/terminal/scan-pay"]''',
    '员工收款码': '''//a[@href="/staff/scan-pay"]''',
    '结算报表': '''//a[@href="/cashier/settlement-report?shopType=1"]''',
    '结算设置': '''//a[@href="/cashier/set-up"]''',
    '分店收款码满减送': '''//a[@href="/terminal-reduction/list-by-terminal"]''',
    '员工收款码满减送': '''//a[@href="/terminal-reduction/list-by-staff"]''',
    '订单统计': '''//a[@href="/data/order-shop"]''',
    '售后统计': '''//a[@href="/data/customer-service"]''',
    '会员统计': '''//a[@href="/data/member-statistics"]''',
    '客户统计': '''//a[@href="/data/member-shop"]''',
    '推广统计': '''//a[@href="/data/fx-shop"]''',
}

#秒杀活动定位
SECOND_KILL_MENU={
    '添加活动':'''//a[@ng-click="haveTemplate()"]''',
    '选择秒杀活动模板':'''//ul[@class="template-list clearfix"]''',
    '秒杀活动名称': '''//*[@id="main-container"]/div[1]/div[2]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[1]''',
    '编辑秒杀活动': '''//div[@class="page-content"]//tbody/tr/td[contains(text(),"%s")]/parent::tr[1]/td[7]/div/a[2]/i''',
    '编辑商品': '''//a[@ng-click="edit($index, list)"]''',
    '修改后秒杀活动名称': '''//td[contains(text(),"%s")]''',
    '删除秒杀活动': '''//div[@class="page-content"]//tbody/tr/td[contains(text(),"%s")]/parent::tr[1]/td[7]/div/a[3]/i''',
    '删除': '''//button[@data-id="ok"]''',
    '活动名称栏': '''//div[@class="page-content"]//table/tbody/tr/td[1]''',
    '活动类型栏': '''//div[@class="page-content"]//table/tbody/tr/td[2]''',
    '关联商品数栏': '''//div[@class="page-content"]//table/tbody/tr/td[3]''',
    '开始时间栏': '''//div[@class="page-content"]//table/tbody/tr/td[4]''',
    '结束时间栏': '''//div[@class="page-content"]//table/tbody/tr/td[5]''',
    '活动状态栏': '''//div[@class="page-content"]//table/tbody/tr/td[6]''',
    '状态':'''//div[@class="page-content"]//tbody/tr/td[contains(text(),"%s")]/parent::tr[1]/td[6]//input[@ng-click="statues($index, list)"]''',
    '查看二维码按钮': '''//div[@class="page-content"]//tbody/tr/td[contains(text(),"%s")]/parent::tr[1]/td[7]/div/a[1]/i''',
    '查看日志按钮': '''//div[@class="page-content"]//tbody/tr/td[contains(text(),"%s")]/parent::tr[1]/td[7]/div/a[4]/i''',
    '操作日志页面':'''//*[@id="breadcrumbs"]''',
    '二维码页面': '''//*[@id="breadcrumbs"]/ul/li''',
    '二维码归属': '''//*[@id="main-container"]/div/div[2]/div[2]/div/div/div[1]/table/tbody/tr[3]/td[1]''',
    '查看二维码': '''//*[@id="main-container"]/div/div[2]/div[2]/div/div/div[1]/table/tbody/tr[1]/td[3]/a/i ''',
    '关闭二维码': '''//*[@id="query"]/div/div/div[1]/a''',




}


#拼团活动定位
TOGETHER_BUY_MENU={
    '添加活动':'''//a[@href="/together-buy/add"]''',


}