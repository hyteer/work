## __添加Pos机订单__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/order/create-pos-order
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|products.{key}.num|是|varchar(100)|购买数量|
|products.{key}.sku_id|是|Integer(11)|购买商品skuID|
|products.{key}.id|是|Integer(11)|购买商品id|
|palt_id|是|varchar(250)|平台id|
|activity_id|是|Integer(11)|活动id|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|是|Integer(11)|店铺id|
|order_type|否|Integer(4)|订单类型|
|total_price|否|Integer(11)|订单总金额|
|uid|否|Integer(11)|用户id|
|discount|否|Integer(11)|优惠券折扣金额|
|seller_cut|否|Integer(11)|手动（促销）金额|
|red_packet_id|否|Integer(11)|红包id|
|card_id|否|Integer(11)|卡券id|
|r_points|否|Integer(11)|使用积分数|
|shop_staff_id|否|Integer(11)|员工id|
|share_message_id|否|Integer(11)|分享id|
|pickup_type|否|Integer(4)|提货方式：1.普通发货。2.到店自提。|
|pickup_shop_sub_id|否|Integer(11)|到店自提的店铺id|
|agent_id|否|Integer(11)|代理商id|

* **注意：products中{key}为索引数组序列号**
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

