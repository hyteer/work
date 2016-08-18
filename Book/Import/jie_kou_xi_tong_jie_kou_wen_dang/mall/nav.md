## __添加导航__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/website/create-website-category
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|name|是|varchar(45)|导航名称|
|describe|否|varchar(500)|导航描述|
|sort|是|Integer(11)|排序|
|type|是|Integer(11)|1.微官网、2.微商城|
|icon|是|varchar(225)|图标|
|face|否|varchar(225)|图片|
|type_url|否|varchar(300)|关联url|
|model|否|varchar(80)|模块|
|model_id|否|Integer(11)|模块id|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|是|Integer(11)|店铺id|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 3,
        "name": "微商城2",
        "describe": "微商户微商城",
        "parent_id": 0,
        "level": 1,
        "sort": 1,
        "face": "/img/init/shop.jpg",
        "icon": "icon-shopping-cart",
        "type_url": "/dpdchina/main/index",
        "model": "aaaa",
        "model_id": 1,
        "shop_id": 5,
        "shop_sub_id": 43,
        "created": 1435991153,
        "modified": 1435995865,
        "deleted": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __修改导航__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/website/update-website-category
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|id|是|Integer(11)|导航id|
|type|是|Integer(11)|1.微官网、2.微商城|
|name|是|varchar(45)|导航名称|
|describe|否|varchar(500)|导航描述|
|sort|是|Integer(11)|排序|
|icon|是|varchar(225)|图标|
|face|否|varchar(225)|图片|
|type_url|否|varchar(300)|关联url|
|model|否|varchar(80)|模块|
|model_id|否|Integer(11)|模块id|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|是|Integer(11)|店铺id|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 3,
        "name": "微商城2",
        "describe": "微商户微商城",
        "parent_id": 0,
        "level": 1,
        "sort": 1,
        "face": "/img/init/shop.jpg",
        "icon": "icon-shopping-cart",
        "type_url": "/dpdchina/main/index",
        "model": "aaaa",
        "model_id": 1,
        "shop_id": 5,
        "shop_sub_id": 43,
        "created": 1435991153,
        "modified": 1435995865,
        "deleted": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取导航列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/website/find-website-category
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
|shop_sub_id|否|Integer(11)|店铺id|
|type|否|Integer(11)|1.微官网、2.微商城|
|deleted|否|Integer(11)|1.启用、2.禁用|
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
* **注意：sort排序可选字段['id']**

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": [
        {
            "id": 3,
            "name": "微商城2",
            "describe": "微商户微商城",
            "parent_id": 0,
            "level": 1,
            "sort": 1,
            "face": "/img/init/shop.jpg",
            "icon": "icon-shopping-cart",
            "type_url": "/dpdchina/main/index",
            "model": "aaaa",
            "model_id": 1,
            "shop_id": 5,
            "shop_sub_id": 43,
            "created": 1435991153,
            "modified": 1435995865,
            "deleted": 1
        },...
    ],
    "page": {
        "per_page": 20,
        "total_count": 3,
        "current_page": 0,
        "total_page": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取导航详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/website/get-website-category
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 导航id |
|type|否|Integer(11)|1.微官网、2.微商城|
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 店铺id |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 3,
        "name": "微商城2",
        "describe": "微商户微商城",
        "parent_id": 0,
        "level": 1,
        "sort": 1,
        "face": "/img/init/shop.jpg",
        "icon": "icon-shopping-cart",
        "type_url": "/dpdchina/main/index",
        "model": "aaaa",
        "model_id": 1,
        "shop_id": 5,
        "shop_sub_id": 43,
        "created": 1435991153,
        "modified": 1435995865,
        "deleted": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __启用导航__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/website/enable-website-category
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 导航id |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 店铺id |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": null
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __禁用导航__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/website/disable-website-category
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 导航id |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 店铺id |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": null
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __删除导航__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/website/del-website-category
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 导航id |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 店铺id |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": null
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



