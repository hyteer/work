## __创建签到积分规则__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-sign-in/create
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| points | 是 | Integer(11) | 赠送积分 |
| days | 是 | Integer(11) | 连续签到天数 |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "points":10,
        "days":2,
        "created":1437442966,
        "modified":1437442966,
        "deleted":2,
        "shop_id":5,
        "shop_sub_id":43,
        "id":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __更新签到积分规则__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-sign-in/to-update
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 签到积分id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| points | 否 | Integer(11) | 赠送积分 |
| days | 否 | Integer(11) | 连续签到天数 |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":1,
        "points":12,
        "days":2,
        "created":1437442966,
        "modified":1437443326,
        "deleted":2,
        "shop_id":5,
        "shop_sub_id":43
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __获取签到积分规则__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-sign-in/get
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 签到积分id |
| shop_id | 是 | Integer(11) | 商家id |

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



## __获取签到积分列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-sign-in/find-list
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

}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __删除签到积分规则__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-sign-in/general-del
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 签到积分id |
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



## __启用签到积分规则__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-sign-in/general-enable
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 签到积分id |
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


## __禁用签到积分规则__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-sign-in/general-disable
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 签到积分id |
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



## __签到__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-sign-in/sign-in
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| uid | 是 | Integer(11) | 签到积分id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":123,
        "mobile":null,
        "nickname":"1",
        "sex":3,
        "province":null,
        "city":null,
        "country":null,
        "headimgurl":null,
        "shop_id":5,
        "shop_sub_id":43,
        "staff_id":0,
        "login_count":0,
        "lastloginip":null,
        "lastlogintime":0,
        "password":"1321432",
        "type":2,
        "status":1,
        "member_refer":null,
        "weixin":null,
        "scene_id":1,
        "mpath":null,
        "mid":423432,
        "code":null,
        "sign_days":1,
        "sign_time":1437444123,
        "is_subscribe":1,
        "group_id":1,
        "level_id":null,
        "point":12,
        "wsh_code":null,
        "created":1433337342,
        "modified":1437444123,
        "deleted":1,
        "wxUsers":[

        ]
    }

}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
