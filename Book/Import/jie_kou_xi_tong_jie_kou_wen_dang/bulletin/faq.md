
## __获取帮助明细__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/bulletin/get-faq
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 帮助id |
| title | 否 | String(100) | 帮助标题 |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 1,
        "faq_type_id": 1,
        "title": "怎么添加商品",
        "content": "怎么添加商品怎么添加商品怎么添加商品怎么添加商品怎么添加商品怎么添加商品",
        "created": 123456,
        "modified": 123456,
        "deleted": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取帮助列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/bulletin/find-faq
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| faq_type_id | 是 | Integer(11) | 帮助类型id |
| title | 否 | String(100) | 帮助标题 |
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
            "faq_type_id": 1,
            "title": "怎么添加商品",
            "content": "怎么添加商品怎么添加商品怎么添加商品怎么添加商品怎么添加商品怎么添加商品",
            "created": 123456,
            "modified": 123456,
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



## __获取帮助类型明细__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/bulletin/get-faq-type
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 帮助类型id |
| name | 否 | String(100) | 帮助类型名称 |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 1,
        "name": "商品",
        "created": 123456,
        "modified": 123456
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取帮助类型列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/bulletin/find-faq-type
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| name | 否 | String(100) | 帮助类型名称 |
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
            "name": "商品",
            "created": 123456,
            "modified": 123456
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
