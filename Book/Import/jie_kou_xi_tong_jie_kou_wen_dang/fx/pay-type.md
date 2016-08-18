
## __创建商家支付类型__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/create-pay-type
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| name | 是 | String(20) | 支付方式名称 |
| note | 是 | String(50) | 付款详细信息 |
| type | 是 | Integer(11) | 1.银行卡。2.第三方支付 |
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


## __获取商家支付类型列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/find-pay-type-list
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
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

## __获取商家支付类型信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/get-pay-type
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| type_id | 是 | Integer(11) | 支付类型id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
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

## __修改商家支付类型信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/update-pay-type
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| type_id | 是 | Integer(11) | 支付类型id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| name | 否 | String(20) | 支付方式名称 |
| note | 否 | String(50) | 付款详细信息 |
| type | 是 | Integer(11) | 1.银行卡。2.第三方支付 |
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

## __开启商家支付类型__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/open-pay-type
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| type_id | 是 | Integer(11) | 支付类型id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
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


## __关闭商家支付类型__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/close-pay-type
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| type_id | 是 | Integer(11) | 支付类型id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
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


## __删除商家支付类型__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/del-pay-type
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| type_id | 是 | Integer(11) | 支付类型id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
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
