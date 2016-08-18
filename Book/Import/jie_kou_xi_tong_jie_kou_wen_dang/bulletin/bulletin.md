
## __获取公告明细__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/bulletin/get-bulletin
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 公告id |
| to_shop_id | 是 | Integer(11) | 商家id |
| to_shop_sub_id | 否 | Integer(11) | 店铺id |
| title | 否 | String(100) | 公告标题 |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 1,
        "to_shop_id": 5,
        "to_shop_sub_id": 0,
        "title": "dfsf",
        "content": "sdfsdfsdfsdf",
        "created": 122345678,
        "modified": 122345678,
        "deleted": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取公告列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/bulletin/find-bulletin
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 公告id |
| to_shop_id | 是 | Integer(11) | 商家id |
| to_shop_sub_id | 否 | Integer(11) | 店铺id |
| title | 否 | String(100) | 公告标题 |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": [
        {
            "id": 1,
            "to_shop_id": 5,
            "to_shop_sub_id": 0,
            "title": "dfsf",
            "content": "sdfsdfsdfsdf",
            "created": 122345678,
            "modified": 122345678,
            "deleted": 1
        }
    ],
    "page": {
        "per_page": 20,
        "total_count": 1,
        "current_page": 0,
        "total_page": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
