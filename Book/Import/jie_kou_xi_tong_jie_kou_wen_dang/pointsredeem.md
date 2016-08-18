## __创建积分兑换__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-redeem/create
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| name | 是 | String(250) | 规则名称 |
| min_consumption | 是 | Integer(11) | 最低消费金额 |
| max_amount | 是 | Integer(11) | 最高金额 |
| type | 否 | Integer(4) | 1.金额、2.百分比 |
| unit_points | 是 | Integer(11) | 单位积分 |
| unit_amount | 是 | Integer(11) | 单位金额 |
| start_time | 否 | Integer(11) | 开始时间 |
| end_time | 否 | Integer(11) | 结束时间 |
| expire_type | 否 | Integer(11) | 有效期类型1.指定时间范围、2.无时间限制 |
* **注意：expire_type默认值为2，如为1，则start_time和end_time必须填写**

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "min_consumption":2,
        "type":1,
        "expire_type":2,
        "shop_id":5,
        "shop_sub_id":43,
        "name":"test19",
        "max_amount":2,
        "unit_points":2,
        "unit_amount":2,
        "created":1435738811,
        "modified":1435738811,
        "deleted":1,
        "id":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __修改积分兑换__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-redeem/to-update
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| points_redeem_id | 是 | Integer(11) | 主键id |
| shop_id | 是 | Integer(11) | 商家id |
| name | 是 | String(250) | 规则名称 |
| min_consumption | 是 | Integer(11) | 最低消费金额 |
| max_amount | 是 | Integer(11) | 最高金额 |
| type | 否 | Integer(4) | 1.金额、2.百分比 |
| unit_points | 是 | Integer(11) | 单位积分 |
| unit_amount | 是 | Integer(11) | 单位金额 |
| start_time | 否 | Integer(11) | 开始时间 |
| end_time | 否 | Integer(11) | 结束时间 |
| expire_type | 否 | Integer(11) | 有效期类型1.指定时间范围、2.无时间限制 |
* **注意：expire_type默认值为2，如为1，则start_time和end_time必须填写**

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
      "id":1,
      "name":"test29",
      "min_consumption":3,
      "max_amount":3,
      "shop_id":5,
      "shop_sub_id":43,
      "type":1,
      "unit_points":3,
      "unit_amount":3,
      "expire_type":2,
      "start_time":null,
      "end_time":null,
      "created":1435738811,
      "modified":1435743445,
      "deleted":1
   }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取积分兑换__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-redeem/get
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| points_redeem_id | 是 | Integer(11) | 主键id |
| shop_id | 是 | Integer(11) | 商家id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode":0,
  "errmsg":"ok",
  "data":{
    "id":1,
    "name":"test29",
    "min_consumption":3,
    "max_amount":3,
    "shop_id":5,
    "shop_sub_id":43,
    "type":1,
    "unit_points":3,
    "unit_amount":3,
    "expire_type":2,
    "start_time":null,
    "end_time":null,
    "created":1435738811,
    "modified":1435743445,
    "deleted":1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取积分兑换列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-redeem/find-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
* **注意：sort排序可选字段['id']**

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode":0,
  "errmsg":"ok",
  "data":[
    {
      "id":1,
      "name":"test29",
      "min_consumption":3,
      "max_amount":3,
      "shop_id":5,
      "shop_sub_id":43,
      "type":1,
      "unit_points":3,
      "unit_amount":3,
      "expire_type":2,
      "start_time":null,
      "end_time":null,
      "created":1435738811,
      "modified":1435743445,
      "deleted":1
    }
  ],
  "page":{
    "per_page":20,
    "total_count":1,
    "current_page":0,
    "total_page":1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __删除积分兑换__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-redeem/general-del
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 商家id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":null
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __启用积分兑换__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-redeem/general-enable
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 商家id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":null
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __禁用积分兑换__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-redeem/general-disable
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 商家id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":null
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
