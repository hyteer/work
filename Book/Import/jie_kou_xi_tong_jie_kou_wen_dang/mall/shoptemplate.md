## __新增、修改模版设置__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/website/save-website-templates-options
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|id|否|Integer(11)|导航名称|
|index|是|varchar(45)|首页模版|
|channel|是|varchar(45)|模版名称|
|articles|是|varchar(45)|模版名称|
|detail|否|varchar(45)|模版名称|
|albums|否|varchar(45)|模版名称|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|否|Integer(11)|店铺id|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 1,
        "index": "Index",
        "channel": "Channel",
        "articles": "Articles",
        "detail": "Detail",
        "albums": "Albums",
        "shop_id": 5,
        "shop_sub_id": 43,
        "created": 1436004948,
        "modified": 1436005124
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取模版设置详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/website/get-website-templates-options
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 导航id |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 1,
        "index": "Index",
        "channel": "Channel",
        "articles": "Articles",
        "detail": "Detail",
        "albums": "Albums",
        "shop_id": 5,
        "shop_sub_id": 43,
        "created": 1436004948,
        "modified": 1436005124
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
