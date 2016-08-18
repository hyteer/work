
## __获取消息推送设置列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/notice/find-wx-setting-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| 无需参数 |  |  |  |  |
<br  /><br  />
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

## __创建微信消息推送设置__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/notice/create-wx-setting
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| cancel | 是 | Integer(3) | 未付款订单自动取消分钟，最大120,不设置自定取消值为0 |
| pay_alert_time | 是 | Integer(3) | 自动催付款分钟，最大120,不设置自定取消值为0  |
| cancel_notice | 是 | Integer(1) | 取消订单通知1：开启,2：关闭 |
| sucess_notice | 是 | Integer(1) | 支付成功通知1：开启,2：关闭 |
| send_notice | 是 | Integer(1) | 发货通知1：开启,2：关闭 |
| complain_notice | 是 | Integer(1) | 维权通知 1：开启,2：关闭 |
<br  /><br  />
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


## __获取微信消息推送设置__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/notice/get-wx-setting
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
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


## __修改微信消息推送设置__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/notice/update-wx-setting
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| setting_id | 是 | Integer(11) | 推送设置id |
| cancel | 否 | Integer(3) | 未付款订单自动取消分钟，最大120,不设置自定取消值为0 |
| pay_alert_time | 否 | Integer(3) | 自动催付款分钟，最大120,不设置自定取消值为0  |
| cancel_notice | 否 | Integer(1) | 取消订单通知1：开启,2：关闭 |
| sucess_notice | 否 | Integer(1) | 支付成功通知1：开启,2：关闭 |
| send_notice | 否 | Integer(1) | 发货通知1：开启,2：关闭 |
| complain_notice | 否 | Integer(1) | 维权通知 1：开启,2：关闭 |
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
