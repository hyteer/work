
## __设置分销设置__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/set-setting
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| setting_id | 否 | Integer(11) | 分销设置id,如果是空则创建否则修改 |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| agreement | 否 | String | 分销协议内容 |
| type | 否 | Integer(3) | 审核条件 |
| integral | 否 | Integer(11) | 积分要求 |
| money | 否 | Integer(11) | 消费金额要求 |
| img_empower | 否 | String(50) | 分销员授权证书 |
| img_top | 否 | String(50) | 前端顶部图 |
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
## __创建分销设置__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/create-setting
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| agreement | 是 | String | 分销协议内容 |
| type | 是 | Integer(3) | 审核条件 |
| integral | 是 | Integer(11) | 积分要求 |
| money | 是 | Integer(11) | 消费金额要求 |
| img_empower | 否 | String(50) | 分销员授权证书 |
| img_top | 是 | String(50) | 前端顶部图 |
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


## __获取分销设置__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/get-setting
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

## __修改分销设置__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/update-setting
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| setting_id | 是 | Integer(11) | 分销设置id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| agreement | 否 | String | 分销协议内容 |
| type | 否 | Integer(3) | 审核条件 |
| integral | 否 | Integer(11) | 积分要求 |
| money | 否 | Integer(11) | 消费金额要求 |
| img_empower | 否 | String(50) | 分销员授权证书 |
| img_top | 否 | String(50) | 前端顶部图 |
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

## __启用申请__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/open-apply
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

## __关闭申请__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/close-apply
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

## __导入数据__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/update_overage
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| operator | 否 | String | 操作者|
| overages | 是 | Array | 需要导入的数据|
| overages.mid | 是 | Integer(11) | 需要修改的分销员|
| overages.money | 是 | Integer(11) | 需要扣减的金额|
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
