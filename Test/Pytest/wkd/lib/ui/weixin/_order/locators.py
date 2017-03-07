

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
    '取消指定订单': '//a[@href="../scan-pay/order-detail?id=%s"]/parent::div[@ng-if="list.orderStatusKey == 1"]/a[@ng-click="$root.cancel(list.id)"]',

    '商品金额': '//span[@ng-bind="model.total_price | number : 2"]',
    '会员优惠': '//span[@ng-bind="(member_discount && member_id && member.status != 2) ? discount_num : 0 | number:2"]',
    '运费': '//span[@ng-bind="model.delivery_fee || 0 | number : 2"]',
    '取消': '//button[text()="取消"]',
    '选择一条地址': '//li[@ng-repeat="list in model.data"]/div[@ng-click="save(list.id)"]',


}