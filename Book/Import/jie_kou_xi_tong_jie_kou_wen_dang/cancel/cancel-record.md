## __获取核销记录详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cancel/get-cancel-records
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) |  核销记录id |
| cancel_type | 否 | Integer(11) | 核销类型id （1.卡券、2.抽奖活动、3.到店自提）|
| cancel_id | 否 | Integer(11) |  对应类型的id |
| staff_id | 否 | Integer(11) | 员工id |
| code | 否 | String(50) | 核销码 |
| shop_id | 是 | Integer(11) |  商户id |
| shop_sub_id | 否 | Integer(11) | 店铺id |

<br  /><br  />
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

## __获取核销员列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cancel/find-cancel-records
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) |  核销记录id |
| cancel_type | 否 | Integer(11) | 核销类型id （1.卡券、2.抽奖活动、3.到店自提）|
| cancel_id | 否 | Integer(11) |  对应类型的id |
| staff_id | 否 | Integer(11) | 员工id |
| code | 否 | String(50) | 核销码 |
| shop_id | 是 | Integer(11) |  商户id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| createStart | 否 | Integer(11) | 核销查询起始时间 |
| createEnd | 否 | Integer(11) | 查询核销结束时间 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": [],
    "page": {
        "per_page": 20,
        "total_count": 0,
        "current_page": 0,
        "total_page": 0
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __核销门店__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cancel/find-cancel-shop
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| cancel_type | 否 | Integer(11) | 核销类型id （1.卡券、2.抽奖活动、3.到店自提）|
| cancel_id | 否 | Integer(11) |  对应类型的id |
| staff_id | 否 | Integer(11) | 员工id |
| shop_id | 是 | Integer(11) |  商户id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个
| createStart | 否 | Integer(11) | 核销查询起始时间 |
| createEnd | 否 | Integer(11) | 查询核销结束时间 |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
      ["num":1,"name":"kk","shop_sub_id":133]
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __核销员统计__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cancel/count-cancel-staff
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| cancel_type | 否 | Integer(11) | 核销类型id （1.卡券、2.抽奖活动、3.到店自提）|
| cancel_id | 否 | Integer(11) |  对应类型的id |
| staff_id | 否 | Integer(11) | 员工id |
| shop_id | 是 | Integer(11) |  商户id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
      ["num":1,"user_name":"zz","real_name":"zz","shop_sub_id":133]
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
