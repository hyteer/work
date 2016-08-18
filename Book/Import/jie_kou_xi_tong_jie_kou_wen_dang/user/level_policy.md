## __创建用户等级策略__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/create-level-policy
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| name | 是 | String(50) | 策略名称 |
| scope | 是 | Integer(3) | 策略作用类型（1.订单） |
| type | 是 | Integer(3) | 优惠类型（1.百分比、2.固定金额） |
| value | 是 | Decimal(10,2) | 优惠值 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "shop_sub_id":187,
        "name":"将将将",
        "scope":1,
        "type":1,
        "value":50,
        "shop_id":30,
        "created":1440499127,
        "modified":1440499127,
        "id":4
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取用户等级策略列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/find-level-policy-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
* **注意：sort排序可选字段['id']**

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":[
        {
            "id":4,
            "name":"将将将",
            "scope":1,
            "type":1,
            "value":"50.00",
            "shop_id":30,
            "shop_sub_id":187,
            "created":1440499127,
            "modified":1440499127
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

## __获取用户等级策略信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/get-level-policy
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| policy_id | 是 | Integer(11) | 策略id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":4,
        "name":"将将将",
        "scope":1,
        "type":1,
        "value":"50.00",
        "shop_id":30,
        "shop_sub_id":187,
        "created":1440499127,
        "modified":1440499127
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __修改用户等级策略信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/update-level-policy
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| policy_id | 是 | Integer(11) | 策略id |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| name | 否 | String(50) | 策略名称 |
| scope | 否 | Integer(3) | 策略作用类型（1.订单） |
| type | 否 | Integer(3) | 优惠类型（1.百分比、2.固定金额） |
| value | 否 | Decimal(10,2) | 优惠值 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":4,
        "name":"咚咚咚",
        "scope":1,
        "type":1,
        "value":50,
        "shop_id":30,
        "shop_sub_id":187,
        "created":1440499127,
        "modified":1440500165
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
