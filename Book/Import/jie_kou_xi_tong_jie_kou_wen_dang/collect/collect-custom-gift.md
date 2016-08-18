## __新增众筹自定义礼物__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/create-collect-custom-gift
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|collect_id|是|Integer(11)|众筹活动id|
| name|是|String(100)|礼物名称|
| document_id|是|Integer(11)|关联图片|
| number|是|Integer(11)|代领点数|
| count|是|Integer(11)|礼品总数|
| lastCount|是|Integer(11)|礼品剩余数|
| shop_id|是|Integer(11)|商家id|
| shop_sub_id|否|Integer(11)|店铺id|
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "give": 0,
        "number": "2",
        "count": "1",
        "lastCount": "1",
        "collect_id": "10",
        "name": "自定义的礼物哦",
        "document_id": "1",
        "shop_id": "5",
        "shop_sub_id": "43"
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __修改众筹自定义礼物__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/update-collect-custom-gift
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|id|是|Integer(11)|众筹关联自定义礼物id|
|collect_id|是|Integer(11)|众筹活动id|
| name|是|String(100)|礼物名称|
| document_id|是|Integer(11)|关联图片|
| number|是|Integer(11)|代领点数|
| count|是|Integer(11)|礼品总数|
| lastCount|是|Integer(11)|礼品剩余数|
| shop_id|是|Integer(11)|商家id|
| shop_sub_id|是|Integer(11)|店铺id|
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 1,
        "collect_id": "10",
        "give": 0,
        "number": "2",
        "count": "1",
        "lastCount": "1",
        "name": "自定义的礼物哦2222",
        "document_id": "1",
        "shop_id": "5",
        "shop_sub_id": "43"
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __删除众筹自定义礼物__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/del-collect-custom-gift
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 关联产品id |
| collect_id | 是 | Integer(11) | 众筹id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |

<br  /><br  />
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



## __获取众筹自定义商品列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/find-collect-custom-gift
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| collect_id | 是 | Integer(11) | 众筹id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
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
            "collect_id": 16,
            "price": null,
            "give": 0,
            "number": 2,
            "count": 3,
            "lastCount": 3,
            "name": "aaaa",
            "document_id": 79,
            "shop_id": 5,
            "shop_sub_id": 43,
            "documentLib": {
                "id": 79,
                "name": "d1e5fadaad81670a5d1b5ed7aa6b859d",
                "desc": null,
                "tag_id": 1,
                "file_cdn_path": "http://imgcache.vikduo.com/static/3e09042246ce738fc3424d02c5d88b24.jpg",
                "file_type": 1,
                "shop_id": 5,
                "shop_sub_id": 43,
                "created": 1437051160,
                "modified": 1437051160,
                "deleted": 1
            }
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
