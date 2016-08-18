## __添加普通订单__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/order/create-scan-order
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|uid|是|Integer(11)|用户id|
|total_price|是|Integer(11)|总价|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|否|Integer(11)|店铺id|
|staff_id|否|Integer(11)|员工id|
|agent_id|否|Integer(11)|代理商id|
|card_id|否|Integer(11)|卡券id|
|should_pay|是|Integer(11)|应付|
|user_name|否|String(50)|用户名|
|ip|否|String(20)|ip|
|fx_member_id|否|Integer(11)|分销员id|
* **注意：shop_sub_id、staff_id 二者有一个必须填写，并且不能同时填写。扫码订单没有先创建支付信息的流程，简化为支付后直接查询微信接口判断是否支付完成。（参见下方pay-done接口）**
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
* **注意：根据order_id查询出订单类型，对扫码订单进行单独处理，调用微信接口查询实际支付值，目前不支持部分付款。**
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


## __其余相关接口__
##### 请参照[普通订单](order/order.md)
<br  /><br  />
