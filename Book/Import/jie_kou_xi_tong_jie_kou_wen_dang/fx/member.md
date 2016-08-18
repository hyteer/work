
## __创建分销员__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/create-member
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| uid | 是 | Integer(11) | 用户id |
| real_name | 否 | String(50) | 真实姓名 |
| pid | 否 | Integer(11) | 推荐人id |
| recommend_name | 否 | String(20) | 推荐人 |

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


## __获取分销员列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/find-member-list
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| agent_id | 否 | Integer(11) | 代理商id |
| agent_path | 否 | Varchar(255) | 代理商路径 |
| real_name | 否 | Varchar(30) | 分销员姓名 |
| status | 否 | Integer(11) | 1.审核中2.审核通过 |
| fx_level_id | 否 | Integer(11) | 分销等级id |
| deleted | 否 | Integer(11) | 1.启用、2.禁用 |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| ids | 否 | Array | id数组 |
| gt_overage | 否 | Integer(11) | 大于的账户余额 |
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


## __获取分销员信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/get-member
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| member_id | 是 | Integer(11) | 分销员id|
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


## __修改分销员信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/update-member
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| member_id | 是 | String(100) | 分销员id |
| pay_id | 否 | Integer(11) | 收款渠道id |
| shop_theme | 否 | Integer(3) | 分销店铺皮肤 |
| fx_level_id | 否 | Integer(11) | 分销等级 |
| content | 否 | String | 店铺简介 |
| real_name | 否 | String(50) | 真实姓名 |
| pay_card | 否 | String(50) | 收款帐号 |
| subbranch | 否 | String(50) | 支行信息 |
| shop_name | 否 | String(50) | 分销员店铺名称 |
| payee | 否 | String(20) | 收款人 |
| x_brokerage | 否 | Integer(11) | 虚拟佣金 |
| x_order | 否 | Integer(11) | 虚拟订单金额 |
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

## __启用分销员__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/open-member
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| member_id | 是 | String(100) | 分销员id |
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

## __禁用分销员__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/close-member
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| member_id | 是 | String(100) | 分销员id |
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

## __分销员审核通过__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/review-member-ok
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| member_id | 是 | String(100) | 分销员id |
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

## __分销员审核不通过__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/review-member-no
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| member_id | 是 | String(100) | 分销员id |
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


## __分销员余额日志列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/find-member-overage-log-list
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| member_id | 是 | String(100) | 分销员id |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| money_sign | 否 | Integer(11) | 金额正负值标识（0全部，1正值，2负值） |
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

## __分销员会员数__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/count-member-user
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| mid | 是 | Integer(11) | 分销员id |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |


##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": "1"
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __分销员订单数__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/count-member-order
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| mid | 是 | String(100) | 分销员id |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| status | 否 | Integer(4) | 订单状态：1为未完成，2为已完成 |


##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": "1"
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __分销员订单金额统计__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/count-member-order-sum
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| mid | 是 | String(100) | 分销员id |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| status | 否 | Integer(4) | 订单状态：1为未完成，2为已完成 |
| sum | 是 | string | 统计值：total_price(订单总金额), brokerage(订单佣金)|


##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": "1"
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __分销员粉丝列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/find-member-user
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| member_id | 是 | String(100) | 分销员id |
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
    "errcode": 0,
    "errmsg": "ok",
    "data": "1"
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __分销员粉丝收益统计列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/find-member-user-brokerage
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| member_id | 是 | String(100) | 分销员id |
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
    "errcode": 0,
    "errmsg": "ok",
    "data": "1"
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __分销员升级__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/member-level-up
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| x_order | 是 | Integer(11) | 虚拟订单金额|
| x_brokerage | 是 | Integer(11) | 虚拟佣金|
| id | 是 | Integer(11) | 会员id|
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



## __未成为分销员或需要调整归属的员工帐号列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/find-staff-to-member-list
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
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



## __新增或修改店员对应的分销员__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/save-staff-fx-member
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| staff_id | 是 | Integer(11) | 员工id |
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
