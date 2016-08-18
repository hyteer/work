
## __创建分销策略__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/create-policy
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| name | 是 | String(20) | 分销策略名称 |
| endtime | 是 | Integer(11) | 分销截止时间 |
| type | 是 | Integer(3) | 类型（1.按百分比、2.按固定金额单位分） |
| operator | 是 | String(20) | 操作员工姓名 |
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


## __创建分销策略以及等级配置__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/create-policy-and-level
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| name | 是 | String(20) | 分销策略名称 |
| endtime | 是 | Integer(11) | 分销截止时间 |
| type | 是 | Integer(3) | 类型（1.按百分比、2.按固定金额单位分） |
| operator | 是 | String(20) | 操作员工姓名 |
| levels.level_id | 是 | Integer(11) | 等级关联ID |
| levels.value | 是 | Double(10,2) | 分销等级数值 |
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


## __获取分销策略列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/find-policy-list
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
* **注意：sort排序可选字段['id']**

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


## __获取分销策略__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/get-policy
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| policy_id | 是 | Integer(11) | 策略id|
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
请求地址：/fx/update-policy
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| name | 否 | String(20) | 分销策略名称 |
| endtime | 否 | Integer(11) | 分销截止时间 |
| type | 否 | Integer(3) | 类型（1.按百分比、2.按固定金额单位分） |
| operator | 是 | String(20) | 操作员工姓名 |
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


## __修改分销策略以及等级配置__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/update-policy-and-level
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| policy_id | 是 | Integer(11) | 策略id|
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| name | 否 | String(20) | 分销策略名称 |
| endtime | 否 | Integer(11) | 分销截止时间 |
| type | 否 | Integer(3) | 类型（1.按百分比、2.按固定金额单位分） |
| operator | 是 | String(20) | 操作员工姓名 |
| levels.level_id | 否 | Integer(11) | 等级的ID |
| levels.value | 否 | Double(10,2) | 分销等级数值 |
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


## __启用分销设置__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/enable-policy
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 策略id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| operator | 是 | String(20) | 操作员工姓名 |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": null
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __禁用分销设置__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/disable-policy
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 策略id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| operator | 是 | String(20) | 操作员工姓名 |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": null
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __删除分销设置__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/del-policy
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 策略id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| operator | 是 | String(20) | 操作员工姓名 |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": null
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
