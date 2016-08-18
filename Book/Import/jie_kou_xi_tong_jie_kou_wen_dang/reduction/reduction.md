##### 接口调用请求说明

## __新增活动__
请求方式：POST
<br  />
请求地址：/reduction/create-full-reduction
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| name   |是| varchar(255)|名称|
| is_relate_all|是|tinyint|是否关联所有（1.是、2.否|
| start_time|是|Integer(11)|减免开始时间|
| end_time|是|Integer(11)|减免结束时间|
| sort|否|int(11)|排序|
| shop_id|是|Integer(11)|商家id|
| shop_sub_id|否|Integer(11)|商铺id|
|conditions.condition_type|是|Integer(4)|减免条件类型（1按金额2按数量）
|conditions.level|是|tinyint|条件层级|
|conditions.condition_min|是|Integer(11)|条件|
|conditions.strategys.{key}.reduction_type|是|tinyint|减免类型(1金额、2打折、3积分、4包邮、5卡券、6红包、7现金红包)|
|conditions.strategys.{key}.amount|选填|Integer(11)|减免金额|
|conditions.strategys.{key}.point|选填|Integer(11)|赠送积分|
|conditions.strategys.{key}.discount|选填|Integer(11)|折扣|
|conditions.strategys.{key}.reduction_type_id|是|Integer(11)|减免类型ID|
|conditions.strategys.{key}.is_all_area|是|tinyint|是否适用所有地区|
|conditions.strategys.{key}.area_id|否|text|适用地区ID|
|conditions.strategys.{key}.area_cn|否|text|适用地区中文|
|conditions.strategys.{key}.is_limit|否|text|是否上不封顶|
|products.{key}.product_id|是|Integer(11)|产品ID|
|products.{key}.shop_sub_id|是|Integer(11)|产品product_sku_id|

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


## __修改活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reduction/update-reduction
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|id|是|Integer(11)|活动ID|
|name|否|varchar(255)|活动名称|
|is_relate_all|否|Integer(11)|是否关联所有（1.是、2.否）|
|start_time|否|Integer(11)|活动开始时间|
|end_time|否|Integer(11)|活动结束时间|
|sort|否|int(11)|排序|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|是|Integer(11)|商铺id|

##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 45,
        "name": "qqqqccccc",
        "is_relate_all": 1,
        "start_time": 1463467641,
        "end_time": 1494950400,
        "sort": 10,
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": 1463467609,
        "modified": 1463562390,
        "deleted": 2
    }
}
```

## __删除满减免__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reduction/del-reduction
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
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

## __获取活动列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reduction/find-reduction
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
|is_relate_all|否|Integer(11)|是否关联所有（1.是、2.否）|
| name | 否 | String(255) | 活动名称 |
| start_time | 否 | String(255) | 开始时间 |
| end_time | 否 | String(255) | 结束时间 |
| deleted | 否 | Integer(11) | 活动状态（1.启用、2.禁用） |
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
            "id": 46,
            "name": "qqqq",
            "is_relate_all": 2,
            "start_time": 1463561745,
            "end_time": 1494950400,
            "sort": 10,
            "shop_id": 30,
            "shop_sub_id": 0,
            "created": 1463561747,
            "modified": 1463561747,
            "deleted": 2,
            "conditions": []
        }
    ],
    "page": {
        "per_page": 50,
        "total_count": 1,
        "current_page": 0,
        "total_page": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取活动明细__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reduction/get-reduction
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
|is_relate_all|否|Integer(11)|是否关联所有（1.是、2.否）|
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| deleted | 否 | Integer(11) | 活动状态（1.启用、2.禁用） |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 46,
        "name": "qqqq",
        "is_relate_all": 2,
        "start_time": 1463561745,
        "end_time": 1494950400,
        "sort": 10,
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": 1463561747,
        "modified": 1463561747,
        "deleted": 2,
        "conditions": []
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __启用满减免__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reduction/enable-reduction
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
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


## __禁用满减免__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：reduction/disable-reduction
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
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

## __获取满减免关联商品列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reduction/find-reduction-product
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| reduction_id | 是 | Integer(11) | 满减免id |
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
            "id": 296,
            "reduction_id": 337,
            "product_id": 392,
            "product_sku_id": 1118,
            "shop_id": 30,
            "shop_sub_id": 0,
            "expire": 0,
            "created": 1465196013,
            "modified": 1465196013,
            "deleted": 1,
            "product": {
                "id": 392,
                "product_category_id": 208,
                "product_category_path": "/207/208/",
                "product_kind_ids": "115;",
                "name": "tes",
                "subtitle": null,
                "keyword": null,
                "product_type": 1,
                "product_no": null,
                "show_price": 12300,
                "prod_weight": "11.000",
                "shop_id": 30,
                "shop_sub_id": 0,
                "hits": 0,
                "sales": 0,
                "status": 1,
                "postage_fee_type": 0,
                "quota": 0,
                "sort": 0,
                "is_pre_sale": 2,
                "pre_sale_id": 0,
                "show_sale_num": 1,
                "share_message_id": null,
                "sync_offline_sku": 2,
                "sale_scope": 1,
                "covers_id": 264744,
                "is_recommend": 2,
                "created": 1464076216,
                "modified": 1464761775,
                "deleted": 1,
                "covers": {
                    "id": 264744,
                    "name": "会员卡推广图",
                    "desc": null,
                    "category_id": 0,
                    "tag_id": 1,
                    "file_cdn_path": "http://imgcache.vikduo.com/static/0ccda10f46817bdf383325200256fa73.png",
                    "file_type": 1,
                    "shop_id": 30,
                    "shop_sub_id": 0,
                    "created": 1462791805,
                    "modified": 1462791805,
                    "deleted": 1
                },
                "productCategory": {
                    "id": 208,
                    "name": "华为",
                    "pid": 207,
                    "level": 2,
                    "path": "/207/208/",
                    "sort": 0,
                    "desc": null,
                    "shop_id": 30,
                    "is_sys_cate": 2,
                    "created": 1453105378,
                    "modified": 1453105788,
                    "deleted": 1
                }
            },
            "productSku": {
                "id": 1118,
                "sku_no": "11",
                "product_id": 392,
                "name": "tes",
                "reserves": 1,
                "freez_reserve": 10,
                "market_price": 110000,
                "cost_price": null,
                "retail_price": 110000,
                "sales": null,
                "status": 1,
                "barcode": "",
                "barcode_pic": null,
                "shop_id": 30,
                "shop_sub_id": 0,
                "created": 1464076216,
                "modified": 1465035244,
                "kinds": [
                    {
                        "id": 115,
                        "name": "厚度",
                        "shop_id": 30,
                        "created": 1440816618,
                        "modified": 1453285854,
                        "deleted": 1
                    }
                ],
                "kindValues": [
                    {
                        "id": 85,
                        "name": "厚",
                        "product_kind_id": 115,
                        "shop_id": 30,
                        "created": 1440816635,
                        "modified": 1440816635,
                        "deleted": 1
                    }
                ]
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


## __获取满减免已经使用商品列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reduction/find-used-product
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| reduction_id | 否 | Integer(11) | 活动id |
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
            "id": 201,
            "product_category_id": 157,
            "product_category_path": "/155/156/157/",
            "product_kind_ids": "113;114;",
            "name": "瓶子专属",
            "subtitle": null,
            "keyword": null,
            "product_type": 1,
            "product_no": null,
            "show_price": 22200,
            "prod_weight": "1.000",
            "shop_id": 30,
            "shop_sub_id": 0,
            "hits": 0,
            "sales": 24,
            "status": 2,
            "postage_fee_type": 0,
            "quota": 0,
            "sort": 2,
            "is_pre_sale": 2,
            "pre_sale_id": 0,
            "show_sale_num": 2,
            "share_message_id": 910,
            "sync_offline_sku": 2,
            "sale_scope": 3,
            "covers_id": 1051,
            "is_recommend": 1,
            "created": 1440403795,
            "modified": 1456999510,
            "deleted": 1,
            "covers": {
                "id": 1051,
                "name": "goods22",
                "desc": null,
                "category_id": 0,
                "tag_id": 1,
                "file_cdn_path": "http://imgcache.vikduo.com/static/1fc27c763a8bb8eab7a8bd41a6ec76dd.png",
                "file_type": 1,
                "shop_id": 30,
                "shop_sub_id": 0,
                "created": 1449565468,
                "modified": 1449565468,
                "deleted": 1
            }
        }}
    ],
    "page": {
        "per_page": 20,
        "total_count": 55,
        "current_page": 0,
        "total_page": 3
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __新增满减免商品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reduction/create-reduction-product
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| reduction_id | 是 | Integer(11) | 减免活动id |
| product_id | 是 | Integer(11) | 关联的商品id |
| product_sku_id| 是| Integer(11) |关联的sku ID|
| shop_id | 是 | Integer(11) | 商家id |
| sub_shop_id | 否 | Integer(11) | 商铺id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "shop_sub_id": 0,
        "reduction_id": 46,
        "product_id": 203,
        "product_sku_id": 612,
        "shop_id": 30,
        "created": 1463565704,
        "modified": 1463565704,
        "deleted": 1,
        "id": 7
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __批量新增满减免商品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reduction/create-reduction-products
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| reduction_id | 是 | Integer(11) | 减免活动id |
| shop_id | 是 | Integer(11) | 商家id |
| products{key}.product_id | 是 | Integer(11) | 关联的商品id |
| products{key}.product_sku_id| 是| Integer(11) |关联的sku ID|
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


## __删除满减免关联商品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reduction/del-reduction-product
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| product_id | 是 | Integer(11) | 关联产品id |
| product_sku_id| 是| Integer(11) |关联的sku ID|
| reduction_id | 是 | Integer(11) | 满减免id |
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


## __创建活动条件策略__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reduction/create-reduction-strategys
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|reduction_id|是|Integer(11)|满减免ID|
|condition_type|是|tinyint|条件类型|
|level|是|tinyint|条件层级|
|condition_min|是|int(11)|条件|
|shop_id|是|int(11)|商家ID|
|shop_sub_id|否|int(11)|商铺ID|
|strategys.{key}.reduction_type|是|tinyint|减免类型|
|strategys.{key}.amount|选填|Integer(11)|减免金额|
|strategys.{key}.point|选填|Integer(11)|赠送积分|
|strategys.{key}.discount|选填|Integer(11)|折扣|
|strategys.{key}.reduction_type_id|是|Integer(11)|减免类型ID|
|strategys.{key}.is_all_area|是|tinyint|是否适用所有地区|
|strategys.{key}.area_id|否|text|适用地区ID|
|strategys.{key}.area_cn|否|text|适用地区中文|
|strategys.{key}.is_limit|否|text|是否上不封顶|


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


## __更新活动条件策略__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reduction/update-reduction-strategys
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|id|是|Integer(11)|满减免条件ID|
|reduction_id|是|Integer(11)|满减免ID|
|condition_type|否|tinyint|条件类型|
|level|否|tinyint|条件层级|
|condition_min|否|int(11)|条件|
|shop_id|是|int(11)|商家ID|
|shop_sub_id|否|int(11)|商铺ID|
|strategys|否|Array|减免策略(覆盖旧策略)|
|strategys.{key}.reduction_type|是|tinyint|减免类型|
|strategys.{key}.amount|选填|Integer(11)|减免金额|
|strategys.{key}.point|选填|Integer(11)|赠送积分|
|strategys.{key}.discount|选填|Integer(11)|折扣|
|strategys.{key}.reduction_type_id|是|Integer(11)|减免类型ID|
|strategys.{key}.is_all_area|是|tinyint|是否适用所有地区|
|strategys.{key}.area_id|否|text|适用地区ID|
|strategys.{key}.area_cn|否|text|适用地区中文|
|strategys.{key}.is_limit|否|text|是否上不封顶|


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


## __删除活动条件策略__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reduction/del-reduction-strategys
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|id|是|Integer(11)|满减免条件ID|
|reduction_id|是|Integer(11)|满减免ID|
|shop_id|是|int(11)|商家ID|
|shop_sub_id|否|int(11)|商铺ID|

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

## __根据商品获取满减免列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reduction/find-product-reductions
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|product_id|是|Integer(11)|商品ID|
|product_sku_id|是|Integer(11)|商品属性ID|
|shop_id|是|int(11)|商家ID|
|shop_sub_id|否|int(11)|商铺ID|


<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": [
        "满50件减10元打8折减10元减10元",
        "满40元减10元打8折减60元",
        "满40元减10元打8折",
        "满40元减10元打8折",
        "满40元减10元打8折"
    ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />







