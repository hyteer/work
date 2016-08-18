## __添加普通订单__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/order/create-order
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|products.{key}.num|是|varchar(100)|购买数量|
|products.{key}.sku_id|是|Integer(11)|购买商品skuID|
|products.{key}.id|是|Integer(11)|购买商品id|
|products.{key}.mid|否|Integer(11)|分销员id|
|plat_id|是|varchar(250)|平台id|
|uid|否|Integer(11)|用户id|
|user_name|否|String(50)|用户名|
|ip|否|String(20)|ip|
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
|delivery_id|否|Integer(11)|用户收货地址id|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|是|Integer(11)|店铺id|
|mid|否|Integer(11)|分销员id|
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


## __确认收货__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/order/confirm-receipt
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|order_id|是|varchar(100)|订单id|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|是|Integer(11)|店铺id|
|uid|是|Integer(11)|用户id|
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data":
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __商家确认收货__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/order/staff-confirm-receipt
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|order_id|是|varchar(100)|订单id|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|是|Integer(11)|店铺id|
|shop_staff_id|是|Integer(11)|管理员id|
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data":
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __关闭订单__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/order/close-order
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|order_id|是|varchar(100)|订单id|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|否|Integer(11)|店铺id|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data":
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __商家取消订单__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/order/seller-cancel-order
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|order_id|是|varchar(100)|订单id|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|是|Integer(11)|店铺id|
|seller_mark|否|varchar(100)|用户备注|
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data":
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __用户取消订单__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/order/cancel-order
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|order_id|是|varchar(100)|订单id|
|uid|是|Integer(11)|用户id|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|否|Integer(11)|店铺id|
|customer_mark|否|varchar(100)|商家备注|
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data":
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __发货__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/order/deliver-done
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|order_id|是|varchar(100)|订单id|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|是|Integer(11)|店铺id|
|seller_mark|否|string(250)|卖家备注|
|express_type|是|Integer(4)|快递公司|
|express_no|是|varchar(20)|快递单号|
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data":
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取订单列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/order/find-order-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| uid | 否 | Integer(11) | 用户id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| order_no | 否 | String(50) | 订单号 |
| user_name | 否 | String(50) | 用户名 |
| order_status | 否 | Integer(4) | 订单状态 |
| deliver_status | 否 | Integer(4) | 发货状态：1.待发货，2.已发货，3.确认收货，4.已评价|
| after_sales_status | 否 | Integer(4) | 1.售后处理订单，2.非售后处理订单 |
| order_type | 否 | Integer(4) | 订单类型：1.普通订单，2.秒杀，3.预售，4.pos收银，5.pos订单，6.拍码打折 |
|pos_pin_code| 否 | String(64) |pos机pincode |
| createStart | 否 | Integer(11) |查询创建日期：开始时间 |
| createEnd | 否 | Integer(11) | 查询创建日期：结束时间 |
| modifyStart | 否 | Integer(11) |查询最后更新日期：开始时间 |
| modifyEnd | 否 | Integer(11) | 查询最后更新日期：结束时间 |
| order_status_in | 否 | array | 订单状态允许的值（in查询） |
| deliver_status_in | 否 | array | 发货状态允许的值（in查询） |
| is_refund | 否 | boolean | 是否退款类型的订单 |
| is_cod | 否 | integer(11) | 是否货到付款的订单1.是、2.否 |
| wait_send_flag | 否 | boolean | 待发货状态 |
| after_sales_flag | 否 | boolean | 售后相关订单 |
| pos_flag | 否 | boolean | pos相关订单 |
| doFilter | 否 | array | ['order_status'=>'1'] |
| agent_id | 否 | Integer | 代理商id |
| agent_path | 否 | String | 代理商路径 |
| pay_type | 否 | Integer | 支付方式（1.财付通、2.微信支付、3.货到付款、4.代收、5.新微信支付、6.现金支付、7、微信扫码支付、8.手Q扫码支付） |
| s_consignee | 否 | String | 收货人姓名 |
| s_tel | 否 | String | 收货电话 |
| ids | 否 | Array | 需要查找的id列表 |
| get_refund | 否 | boolean | 是否关联退款信息 |
| after_sales_happend | 否 | boolean | 是否申请过售后（1.是、2.否） |



* **注意：sort排序可选字段['id']

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok"
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取订单信息__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/order/get-order
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 订单id |
| shop_id | 是 | Integer(11) | 店铺id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok"
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __普通订单支付__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/order/simple-order-pay
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 订单id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| r_points | 否 | Integer(11) | 积分数 |
| red_packet_id | 否 | Integer(11) | 红包id |
| customer_mark | 否 | string(500) | 备注 |
| card_id | 否 | Integer(11) | 卡券id |
| orderPayInfo.{keys}.pay_type | 是 | Integer(11) | 支付类型 |
| orderPayInfo.{keys}.amount | 是 | Integer(11) | 付款金额 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok"
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __订单支付完成__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/order/pay-done
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| order_id | 是 | Integer(11) | 订单id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| uid | 否 | Integer(11) | 用户id |
| amount | 是 | Integer(11) | 金额 |
| pay_id | 否 | Integer(11) | 支付id |
| pay_type | 是 | Integer(11) | 支付类型 |
| trade_no | 否 | string(32) | 第三方支付号 |
<br  />
##### 返回说明

正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok"
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __用户修改订单收货地址__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/order/update-delivery
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| order_id | 是 | Integer(11) | 订单id |
| shop_id | 是 | Integer(11) | 商家id |
| uid | 是 | Integer(11) | 用户id |
| delivery_id | 是 | Integer(11) | 用户收货地址id |
<br  />
##### 返回说明


正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 16,
        "order_id": "33",
        "consignee": "sdfsdfsdf",
        "tel": "Tel",
        "zip": "Zip",
        "province": "province",
        "city": "City",
        "county": "County",
        "detail": "Detail",
        "shop_id": "5",
        "created": 1436323832
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __商家修改订单收货地址__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/order/update-delivery-hard
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| order_id | 是 | Integer(11) | 订单id |
| shop_id | 是 | Integer(11) | 商家id |
| consignee | 是 | string(20) | 店铺id |
| tel | 是 | string(20) | 收货人电话 |
| province | 是 | string(20) | 省 |
| city | 是 | string(20) | 市、县 |
| county | 是 | string(20) | 区域 |
| detail | 是 | string(100) | 地址详细 |
| zip | 否 | string(10) | 邮编 |
<br  />
##### 返回说明


正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 16,
        "order_id": "33",
        "consignee": "sdfsdfsdf",
        "tel": "Tel",
        "zip": "Zip",
        "province": "province",
        "city": "City",
        "county": "County",
        "detail": "Detail",
        "shop_id": "5",
        "created": 1436323832
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取订单日志列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/order/find-order-log-list
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| order_id | 是 | Integer(11) | 订单id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",

}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __获取订单日志__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/order/get-order-log
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 订单日志id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",

}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __手动备注日志__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/order/create-order-log
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| order_id | 是 | Integer(11) | 订单id |
| content | 是 | string(250) | 日志内容 |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",

}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __商家手动优惠__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/order/seller-update-order-discount
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 订单日志id |
| seller_cut | 是 | Integer(11) | 优惠金额 |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",

}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

