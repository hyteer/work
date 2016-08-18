## __新增众筹商品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/create-collect-product
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|collect_id|是|Integer(11)|众筹活动id|
| product_id|是|Integer(11)|关联商品id|
| product_sku_id|是|Integer(11)|关联商品SKUid|
| price|否|Integer(11)|众筹金额|
| give|否|Integer(11)|赠送金额|
| number|是|Integer(11)|代领人数|
| count|是|Integer(11)|礼品总数|
| lastCount|是|Integer(11)|礼品剩余数|
| minus|否|Integer(11)|是否允许负数值（1：允许 ，2：不允许）|
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
        "price": "1",
        "give": "0",
        "minus": "1",
        "collect_id": "10",
        "product_id": "59",
        "product_sku_id": "38",
        "number": "2",
        "count": "1",
        "lastCount": "1",
        "shop_id": "5",
        "shop_sub_id": "43",
        "id": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __修改众筹商品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/update-collect-product
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|id|是|Integer(11)|众筹关联商品id|
|collect_id|是|Integer(11)|众筹活动id|
| product_id|否|Integer(11)|关联商品id|
| product_sku_id|否|Integer(11)|关联商品SKUid|
| price|否|Integer(11)|众筹金额|
| give|否|Integer(11)|赠送金额|
| number|是|Integer(11)|代领人数|
| count|是|Integer(11)|礼品总数|
| lastCount|是|Integer(11)|礼品剩余数|
| minus|否|Integer(11)|是否允许负数值（1：允许 ，2：不允许）|
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
        "price": "1",
        "give": "0",
        "minus": "1",
        "collect_id": "10",
        "product_id": "59",
        "product_sku_id": "38",
        "number": "2",
        "count": "1",
        "lastCount": "1",
        "shop_id": "5",
        "shop_sub_id": "43",
        "id": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __删除众筹关联商品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/del-collect-product
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



## __获取众筹关联商品列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/find-collect-product
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
            "collect_id": 20,
            "product_id": 138,
            "product_sku_id": 124,
            "price": 63,
            "give": 0,
            "number": 0,
            "count": 3,
            "lastCount": 3,
            "minus": 2,
            "shop_id": 5,
            "shop_sub_id": 43,
            "product": {
                "id": 138,
                "product_category_id": 1,
                "product_category_path": "1/",
                "product_kind_ids": "86;",
                "name": "12490564141",
                "subtitle": null,
                "keyword": null,
                "product_type": 1,
                "product_no": null,
                "show_price": 133,
                "prod_weight": "1.000",
                "shop_id": 5,
                "shop_sub_id": 43,
                "hits": 0,
                "sales": 1,
                "status": 1,
                "postage_fee_type": 2,
                "quota": 100,
                "sort": 1,
                "is_pre_sale": 2,
                "pre_sale_id": 0,
                "show_sale_num": 2,
                "share_message_id": 266,
                "sync_offline_sku": 2,
                "sale_scope": 1,
                "covers_id": 66,
                "is_recommend": 2,
                "created": 1437187316,
                "modified": 1437187354,
                "deleted": 1,
                "covers": {
                    "id": 66,
                    "name": "1323213121",
                    "desc": null,
                    "tag_id": 1,
                    "file_cdn_path": "http://imgcache.vikduo.com/static/4c5095da696b515767f79f4b2169f69e.jpg",
                    "file_type": 1,
                    "shop_id": 5,
                    "shop_sub_id": 43,
                    "created": 1436951989,
                    "modified": 1436965043,
                    "deleted": 1
                }
            },
            "productSku": {
                "id": 124,
                "sku_no": "1",
                "product_id": 138,
                "name": "12490564141",
                "reserves": 123132,
                "freez_reserve": null,
                "market_price": 1,
                "cost_price": 1,
                "retail_price": 1,
                "sales": 0,
                "status": 1,
                "barcode": "1",
                "barcode_pic": null,
                "shop_id": 5,
                "shop_sub_id": 43,
                "created": 1437187316,
                "modified": 1437191209
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

