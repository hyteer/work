
## __获取分销员订单列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/find-order-list
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| member_id | 否 | Integer(11) | 分销员id |
| agent_id | 否 | Integer(11) | 代理商id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| createStart | 否 | Integer(11) | 核销查询起始时间 |
| createEnd | 否 | Integer(11) | 查询核销结束时间 |
| s_member_name | 否 | Integer(11) | 分销员名称 |
| member_name | 否 | Integer(11) | 订单冗余的分销员昵称 |
| s_order_no | 否 | Integer(11) | 订单号 |
| ids | 否 | Array | 指定id |
| status | 否 | Integer(11) | 分销订单状态1.未入账。2.已入账 |
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


## __获取分销订单信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/get-order
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| id | 是 | Integer(11) | 分销订单id|
| member_id | 是 | Integer(11) | 分销员id|
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


## __根据订单号获取分销订单信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/get-order-by-order-id
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| order_id | 是 | Integer(11) | 订单号id|
| member_id | 是 | Integer(11) | 分销员id|
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


## __设置分销订单为已入账__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/update-order
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| id | 是 | Integer(11) | 分销订单id |
| member_id | 是 | Integer(11) | 分销员id|
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
