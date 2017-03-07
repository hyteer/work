# coding: utf-8
COMMON = {
    '关闭': '''//i[@ng-click="close()"]''',
    '返回': '''//div[@ng-click="goBack()"]''',
    '保存': '''//a[@ng-click="save()"]''',
    '取消': '''//*([@ng-click="cancel()"]''',
    '确认': '''//a[@ng-click="determine()"]''',
    '确定': '//*[@ng-click="comfrim()"]',
}

BOTTOM_MENU = {
    '首页': '''//li[@ng-click="switchTab('../mall/index')"]''',
    '商品': '''//li[@ng-click="switchTab('../product/category')"]''',
    '购物车': '''//li[@ng-click="switchTab(col3.href)"]''',
    '惊喜': '''//li[@ng-click="switchTab(col4.href)"]''',
    '我': '''//li[@ng-click="switchTab('../user/home')"]''',
}

USERHOME = {
    '红包': '''//a[@href="../user/redpack?is_use=2"]''',
    '卡券': '''//a[@href="../card-coupons/list"]''',
    '积分': '''//a[@href="../member/member-point"]''',
    #
    '待付款': '''//a[@href="../order/list?_status=1"]''',
    '待发货': '''//a[@href="../order/list?_status=2"]''',
    '待收货': '''//a[@href="../order/list?_status=3"]''',
    '已完成': '''//a[@href="../order/list?_status=4"]''',
    '售后': '''//a[@href="../order/list?_status=5"]''',
    '会员卡': '''//a[@ng-click="getMember()"]''',
    #
    '我的拼团': '''//a[@href="../together-buy/my-queue"]''',
    '我的活动': '''//a[@href="../user/activity"]''',
    '我的地址': {
        '我的地址': '''//a[@href="../user/address-list"]''',
        '新增收货地址': '''//a[@href="../user/address-add"]''',
    },
    '我的地址2': '''//a[@href="../user/address-list"]''',
    '我的预约': '''//a[@href="../user/reserve"]''',
    '兑奖二维码': '''//a[@href="../user/qrcode"]''',
    '我的资产': '''//a[@href="../user/property"]''',

}

ADDRESS = {
    '我的地址': '''//a[@href="../user/address-list"]''',
    '新增收货地址': '''//a[@href="../user/address-add"]''',
    '收货人': '''//input[@ng-model="model.consignee"]''',
    '手机号码': '''//input[@ng-model="model.tel"]''',
    '详细地址': '''//input[@ng-model="model.detail"]''',
    '所在地区': '''//dd[@ng-click="gotoChoose()"]''',
    '选择省': '''//li[@ng-click="clickProvince($event, $index, list)"]''',
    '选择市': '''//div[@ng-repeat="list in cityList"]''',
    '选择区': '''//a[@ng-click="chooseAddress($event, $index, list)"]''',
    '设为默认地址': '''//input[@ng-model="is_default"]''',
    '从地址列表中设为默认': '''//i[@ng-click="changeCheck($index, list)" and not(contains(@class,"checked"))]''',
    '编辑': '''//i[@ng-click="changeCheck($index, list)" and not(contains(@class,"checked"))]/ancestor::div[@class="wsh_cell"]//a[starts-with(@href,"../user/address-edit?_id=")]''',
    '删除': '''//i[@ng-click="changeCheck($index, list)" and not(contains(@class,"checked"))]/ancestor::div[@class="wsh_cell"]//a[@ng-click="delete(list.id)"]''',

}

SUPRRISE = {
    '会员卡': '''//a[@href="../member/user-validate"]''',
    '卡券': '''//a[@href="../card-coupons/card-list"]''',
    '丘比特之箭': '''//a[@ng-click="jump('../market-activity/list?type=6')"]''',
    #
    '积分商城': '''//a[@ng-click="jump('../point-mall/list')"]''',
    '拼团活动': '''//a[@ng-click="jump('../together-buy/list')"]''',
    '秒杀活动': '''//a[@ng-click="jump('../second-kill/list')"]''',
    '红包活动': '''//a[@ng-click="jump('../redpack/list')"]''',
    '大转盘': '''//a[@ng-click="jump('../market-activity/list?type=1')"]''',
    '砸金蛋': '''//a[@ng-click="jump('../market-activity/list?type=4')"]''',
    '记忆翻翻看': '''//a[@href="../memory-fan/list""]''',
    '微预约': '''//a[@ng-click="jump('../reserve/list')"]''',

}

PRODUCT = {
    '商品列表': '//a[@ng-repeat="list in lists track by $index"]',
    '通过名称选择一个商品':  '//div[@ng-bind="list.name" and text()="%s"]/ancestor::a[@ng-click="saveScroll(list, $event)"]',
    '商品分类': '//div[@ng-click="showProduct()"]',
    '切换显示方式': '//div[@ng-click="showSwitch()"]',
    '排序': '//div[@ng-click="middle()"]',
    '默认排序': '//li[@ng-click="clearSession(1)"]',
    '低格最低': '//li[@ng-click="clearSession(2)"]',
    '销量最高': '//li[@ng-click="clearSession(3)"]',
    '最新上架': '//li[@ng-click="clearSession(4)"]',
    # 商品详情
    '商品名称': '//div[@ng-bind="model.product.name"]',
    '价格': '//span[@ng-bind="model.product.show_price | number:2"]',
    '销量': '//span[@ng-bind="model.product.sales"]',
    '会员价': '//div[@ng-show="modelObj.can_use_member_discount && member_id && member.status!=2"]//span[contains(@ng-bind,"model.product.show_price")]',
    '会员等级': '//span[@ng-bind="member_name"]',
    '会员折扣': '//span[@ng-bind="is_discount"]',
    '已选': '//span[@ng-repeat="sku in choosedSkus"]',
    '店铺名称': '//span[@ng-bind="deliveryShop.name"]',
    # 立即购买&加入购物车
    '加入购物车': '//a[@ng-click="getCart()"]',
    '确定_加入购物车': '//a[@ng-click="joinShop()"]',
    '购物车': '//a[@href="../cart/index"]',
    '增加数量': '//button[@ng-click="addNum(skunum, modelObj.reserves)"]',
    '减少数量': '//button[@ng-click="skunum = skunum - 1"]',
    '数量': '//input[@name="quantity"]',
    '规格': '//label[@ng-repeat="o in list.value"]',
    '总价': '//span[@ng-bind="modelObj.retail_price*skunum | number: 2"]',
    '库存': '//span[@ng-bind="modelObj.reserves"]',
    '快递配送': '//label[@ng-if="shipping_status === 1"]',
    '到店自提': '//label[@ng-if="self_pickup_status === 1 && deliveryShop.shopSub.shop_type != 3"]',
    '立即购买': '//a[@ng-click="showModal()"]',
    '确认购买': '//a[@ng-click="buy()"]',
    '返回': '//a[@ng-click="back()"]',



}

CART = {
    '全选': '//a[@href="../card-coupons/card-list"]',
    '加': '''//button[@ng-click="add($index, list, '', list.quota)"]''',
    '减': '''//button[@ng-click="reduce($index, list)"]''',
    '配送方式': '//label[@for="express_get"]',
    '勾选商品': '//i[@ng-click="changeCheck($index, list)"]',
    '去结算': '//a[@ng-click="buy()"]',
    '删除': '//a[@ng-click="deleteList()"]',


#
}

ORDER = {
    # 动态
    '立即支付': '//a[@href="../scan-pay/order-detail?id=%s"]',

    # 静态
    '其它支付': '//button[@ng-click="clickOther()"]',
    '货到付款': '//button[@ng-click="pay(3)"]',
    '选择地址': '//section[contains(@class,"floor") and not(contains(@class,"ng-hide"))]//div[@ng-click="changeAddr()"]',
    '收货地址列表': '//a[@href="../order/choose-address?id=%s"]',
    '会员优惠开关': '//div[@ng-show="model.can_use_member_discount && member_id && member.status !=2"]',
    #'卡券': '//*[@id="bg_card"]',
    '卡券': '//*[@id="bg_card"]//dt[@ng-click="cardCouponBox();"]',
    '留言': '//*[@id="customer_mark"]',
    '取消一个订单': '//a[@ng-click="$root.cancel(list.id)"]',
    '取消指定订单': '//a[@href="../order/detail?id=%s"]/parent::div[@ng-if="list.orderStatusKey == 1"]/a[@ng-click="$root.cancel(list.id)"]',

    '商品金额': '//span[@ng-bind="model.total_price | number : 2"]',
    '会员优惠': '//span[@ng-bind="(member_discount && member_id && member.status != 2) ? discount_num : 0 | number:2"]',
    '运费': '//span[@ng-bind="model.delivery_fee || 0 | number : 2"]',
    '取消': '//button[text()="取消"]',
    '选择一条地址': '//li[@ng-repeat="list in model.data"]/div[@ng-click="save(list.id)"]',

    # 订单状态
    '订单详情': '//a[@href="../order/detail?id=%s"]',
    '订单号': '//a[@href="../order/detail?id=%s"]//em[@ng-bind="list.order_no"]',

    #订单列表
    '订单状态': '//a[@href="../order/detail?id=%s"]//strong[@ng-bind="list.orderStatusText"]',


}
