## __获取支付类型、开启状态列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/payment/find-paytype-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取支付配置信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/payment/get-pay-config
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| type | 是 | Integer(11) | 支付类型 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __修改支付配置信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/payment/update-pay-config
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| config_id | 是 | Integer(11) | 支付配置信息编号id |
| account | 否 | String(100) | 商户号或账户号 |
| sign_key | 否 | String(50) | 验签 |
| key | 否 | String(50) | 加密key |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
