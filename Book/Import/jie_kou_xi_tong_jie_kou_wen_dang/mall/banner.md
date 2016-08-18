## __添加轮播图__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/website/create-website-slide
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|name|是|varchar(45)|轮播图名称|
|description|否|varchar(500)|轮播图描述|
|sort|是|Integer(11)|排序|
|pic_url|是|varchar(225)|图片url|
|type_url|否|varchar(225)|关联url|
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
        "sort": "1",
        "model_id": "2",
        "name": "淘你所爱",
        "description": "陶时尚",
        "pic_url": "http://wsh.gaopeng.com/imgstore/422/1059/wkd_422_1403581448.jpg",
        "type_url": "http://wsh.gaopeng.com/noble-jewelry",
        "model": "sdfsdf",
        "shop_id": "5",
        "shop_sub_id": "43",
        "created": 1436002369,
        "modified": 1436002369,
        "deleted": 1,
        "id": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __修改轮播图__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/website/update-website-slide
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|name|是|varchar(45)|轮播图名称|
|description|否|varchar(500)|轮播图描述|
|sort|是|Integer(11)|排序|
|pic_url|是|varchar(225)|图标|
|type_url|否|varchar(225)|关联url|
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
        "sort": "1",
        "model_id": "2",
        "name": "淘你所爱",
        "description": "陶时尚",
        "pic_url": "http://wsh.gaopeng.com/imgstore/422/1059/wkd_422_1403581448.jpg",
        "type_url": "http://wsh.gaopeng.com/noble-jewelry",
        "model": "sdfsdf",
        "shop_id": "5",
        "shop_sub_id": "43",
        "created": 1436002369,
        "modified": 1436002369,
        "deleted": 1,
        "id": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取轮播图列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/website/find-website-slide
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
|shop_sub_id|否|Integer(11)|店铺id|
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
            "id": 1,
            "name": "淘你所爱",
            "description": "陶时尚",
            "sort": 1,
            "pic_url": "http://wsh.gaopeng.com/imgstore/422/1059/wkd_422_1403581448.jpg",
            "type_url": "http://wsh.gaopeng.com/noble-jewelry",
            "model": "sdfsdf",
            "model_id": 2,
            "shop_id": 5,
            "shop_sub_id": 43,
            "created": 1436002369,
            "modified": 1436002369,
            "deleted": 1
        },...
    ],
    "page": {
        "per_page": 20,
        "total_count": 2,
        "current_page": 0,
        "total_page": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取轮播图详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/website/get-website-slide
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
    "data": {
        "id": 1,
        "name": "淘你所爱",
        "description": "陶时尚",
        "sort": 1,
        "pic_url": "http://wsh.gaopeng.com/imgstore/422/1059/wkd_422_1403581448.jpg",
        "type_url": "http://wsh.gaopeng.com/noble-jewelry",
        "model": "sdfsdf",
        "model_id": 2,
        "shop_id": 5,
        "shop_sub_id": 43,
        "created": 1436002369,
        "modified": 1436002369,
        "deleted": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __启用轮播图__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/website/enable-website-slide
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

## __禁用轮播图__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/website/disable-website-slide
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

## __删除轮播图__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/website/del-website-slide
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

