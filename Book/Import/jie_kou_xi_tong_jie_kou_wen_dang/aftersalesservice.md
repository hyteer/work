

## __订单申请退款__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/after-sales-service/apply-order-refund
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| order_id | 是 | Integer(11) | 订单id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| uid | 是 | Integer(11) | 用户id |
| content |  是 | string | 退款理由 |
| pic_list |  否 | string | 退款凭证 |
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



## __更新售后单信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/after-sales-service/to-update
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 退款单id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| content |  否 | string | 退款理由 |
| pic_list |  否 | string | 退款凭证 |
| reply |  否 | string | 回复信息 |
| status |  否 | Integer(4) | 处理状态 |
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


## __获取售后单信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/after-sales-service/get
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 退款单id |
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


## __查找售后单信息列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/after-sales-service/find-list
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| order_id | 否 | Integer(11) | 订单id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| order_type | 否 | Integer(11) | 订单类型 |
| order_no | 否 | String(50) | 订单号 |
| pay_type | 否 | Integer(11) |支付类型|
| consignee | 否 | String(20) | 联系人 |
| tel | 否 | String(20) | 联系人电话 |
| createStart | 否 | Integer(11) | 创建开始时间 |
| createEnd | 否 | Integer(11) | 创建结束时间 |
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



## __审核售后单（拒绝）__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/after-sales-service/refuse
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 退款单id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| reply | 否 | string | 回复信息 |
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



## __审核售后单（通过）__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/after-sales-service/pass
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 退款单id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| reply | 否 | string | 回复信息 |
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

## __审核售后单（确认）__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/after-sales-service/after-sales-confirm
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 退款单id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| staff_id | 是 | string | 操作员工id |
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
