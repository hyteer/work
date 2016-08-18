## __创建用户消息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/create-message
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| to_user_name | 否 | String(200) | 发消息者用户名 |
| content | 是 | String | 消息内容 |
| type | 否 | Integer(3) | 1是实时信息，2是咨询顾问信息 |
| is_reply | 否 | Integer(3) | 1是回复信息，2非回复信息 |
| user_id | 是 | Integer(11) | 用户id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "type":1,
        "shop_sub_id":0,
        "is_reply":2,
        "mark":2,
        "content":"23333333",
        "user_id":457,
        "shop_id":30,
        "created":1440571385,
        "id":644
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取用户消息列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/find-message-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| content | 否 | Varchar | 消息内容 |
| mark | 否 | Integer(4) | 是否星标，1是，2否 |
| is_reply | 否 | Integer(3) | 1是回复信息，2非回复信息 |
| user_id | 否 | Integer(11) | 用户id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":[
        {
            "id":644,
            "to_user_name":null,
            "content":"23333333",
            "type":1,
            "user_id":457,
            "shop_id":30,
            "shop_sub_id":0,
            "is_reply":2,
            "mark":2,
            "created":1440571385
        }
    ],
    "page":{
        "per_page":10,
        "total_count":1,
        "current_page":0,
        "total_page":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取用户消息信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/get-message
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| message_id | 是 | Integer(11) | 消息id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":644,
        "to_user_name":null,
        "content":"23333333",
        "type":1,
        "user_id":457,
        "shop_id":30,
        "shop_sub_id":0,
        "is_reply":2,
        "mark":2,
        "created":1440571385
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __回复用户消息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/reply-message
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| message_id | 是 | Integer(11) | 消息id |
| content | 是 | String | 消息内容 |
| type | 是 | Integer(3) | 1是实时信息，2是咨询顾问信息 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "type":1,
        "shop_sub_id":0,
        "is_reply":1,
        "mark":2,
        "content":"我是回复的？？",
        "shop_id":30,
        "to_user_name":null,
        "user_id":457,
        "created":1440572829,
        "id":645
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __收藏用户消息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/like-message
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| message_id | 是 | Integer(11) | 消息id |
| mark | 是 | Integer(11) | 1：收藏消息，2：取消收藏消息 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":644,
        "to_user_name":null,
        "content":"23333333",
        "type":1,
        "user_id":457,
        "shop_id":30,
        "shop_sub_id":0,
        "is_reply":2,
        "mark":2,
        "created":1440571385
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
