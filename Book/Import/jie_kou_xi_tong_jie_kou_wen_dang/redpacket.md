## __添加红包__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet/create
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| name | 是 | String(32） | 红包名称 |
| type | 是 | Integer(4) | 红包类型 |
| total_amount | 是 | Integer(11) | 发送总金额 |
| order_limit | 否 | Integer(11) | 订单限额 |
| start_time | 是 | Integer(11) | 开始时间 |
| end_time | 是 | Integer(11) |  结束时间 |
| remark | 否 | String(500) | 描述 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "type":1,
        "total_amount":500,
        "order_limit":1000,
        "end_time":1333333,
        "remark":"ssssssssssss",
        "shop_id":5,
        "shop_sub_id":43,
        "name":"dddddd",
        "start_time":1333333,
        "created":1436235017,
        "modified":1436235017,
        "deleted":1,
        "id":2
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __修改红包__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet/to-update
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| redpacket_id | 是 | Integer(11) | 红包id |
| shop_id | 是 | Integer(11) | 商家id |
| name | 否 | String(32） | 红包名称 |
| type | 否 | Integer(4) | 红包类型 |
| total_amount | 否 | Integer(11) | 发送总金额 |
| order_limit | 否 | Integer(11) | 订单限额 |
| start_time | 否 | Integer(11) | 开始时间 |
| end_time | 否 | Integer(11) |  结束时间 |
| remark | 否 | String(500) | 描述 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":64,
        "name":"11111",
        "type":"1",
        "total_amount":"1000",
        "order_limit":"1000",
        "start_time":"1449738084",
        "end_time":"1449910887",
        "remark":"12121212",
        "shop_id":30,
        "shop_sub_id":0,
        "created":1449738097,
        "modified":1454467007,
        "deleted":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取红包__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet/get
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 红包的id |
| shop_id | 是 | Integer(11) | 店铺id |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":64,
        "name":"11111",
        "type":"1",
        "total_amount":"1000",
        "order_limit":"1000",
        "start_time":"1449738084",
        "end_time":"1449910887",
        "remark":"12121212",
        "shop_id":30,
        "shop_sub_id":0,
        "created":1449738097,
        "modified":1454467007,
        "deleted":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取红包列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet/find-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| deleted | 否 | Integer(11) | 状态1.是、2.否 |
| type | 否 | Integer(11) | 红包类型（1.商城红包、2.现金红包） |
| now_time | 否 | Integer(11) | 当前时间 |
| is_not_end | 否 | boolean | 是否未结束 |
| type | 否 | Integer(4) | 类型 |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| name | 否 | String(32) | 红包名称 |
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
            "id":65,
            "name":"测试",
            "type":1,
            "total_amount":10000,
            "order_limit":1000,
            "start_time":1453685438,
            "end_time":1454549440,
            "remark":"广东核电",
            "shop_id":30,
            "shop_sub_id":0,
            "created":1453685488,
            "modified":1453685488,
            "deleted":1
        },
        {.....}
    ],
    "page":{
        "per_page":15,
        "total_count":12,
        "current_page":0,
        "total_page":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __删除红包__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet/general-del
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


## __获取用户红包__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet/get-user-red-packet
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 用户红包的id |
| uid | 是 | Integer(11) | 用户id |
| shop_id | 是 | Integer(11) | 店铺id |
| doFilter | 否 | Array | 需排除的条件 eg:['id'=>'3'] |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 170,
        "uid": 507,
        "type": 1,
        "amount": 1100,
        "order_limit": 0,
        "start_time": 1445430421,
        "end_time": 1446899222,
        "shop_id": 30,
        "shop_sub_id": 0,
        "is_use": 2,
        "created": 1446103092,
        "modified": 1446103092,
        "deleted": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取用户红包列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet/find-user-red-packet
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| uid | 是 | Integer(11) | 用户id |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 是 | Integer(11) | 门店id |
| deleted | 否 | Integer(11) | 红包状态（1.启用、2.禁用） |
| type | 否 | Integer(11) | 红包类型（1.商城红包、2.现金红包） |
| is_use | 否 | Integer(11) | 红包是否已使用（1已使用，2未使用） |
| order_amount | 否 | Integer(11) | 订单金额（判断红包是否符合要求） |
| time_in | 否 | Integer(11) | 红包是否在有效期 |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| doFilter | 否 | Array | 需排除的条件 eg:['id'=>'3'] |

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
            "id":170,
            "uid":507,
            "type":1,
            "amount":1100,
            "order_limit":0,
            "start_time":1445430421,
            "end_time":1446899222,
            "shop_id":30,
            "shop_sub_id":0,
            "is_use":2,
            "created":1446103092,
            "modified":1446103092,
            "deleted":1
        },
        {.....}
    ],
    "page":{
        "per_page":5,
        "total_count":54,
        "current_page":0,
        "total_page":11
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
