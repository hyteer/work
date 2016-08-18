## __新增秒杀活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/secondKill/create
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| activity.name | 是 | String(250) | 活动名称 |
| activity.desc | 否 | String(500) | 活动描述/规则 |
| activity.sort | 否 | Integer(11) | 排序 |
| activity.expire_type | 是 | Integer(4) | 有效期类型1.指定时间范围、2.无时间限制 |
| activity.start_time | 是 | Integer(11) | 活动开始时间 |
| activity.end_time | 是 | Integer(11) | 活动结束时间 |
| activity.shop_id | 是 | Integer(11) | 商家id |
| activity.shop_sub_id | 是 | Integer(11) | 店铺id |
| activity.share_type | 是 | Integer(4) |显示和分享模式（1.显示且能分享、2.不能显示且能分享、3.不能显示且不能分享）|
| postageSetting.type | 否 | Integer(11) | 包邮类型（1.满金额包邮、2.满件数包邮、3.免邮费）|
| postageSetting.num | 否 | Integer(11) | 数量 |
| postageSetting.amount | 否 | Integer(11) | 金额 |
| shareMessage.title | 否 | String(100) | 分享标题 |
| shareMessage.desc | 否 | String(100) | 分享描述 |
| shareMessage.pic_id | 否 | Integer(11) | document_lib表外键 |
| news.title | 否 | String(100) | 微信标题 |
| news.description | 否 | String(100) | 微信描述 |
| news.document_id | 否 | Integer(11) | document_lib表外键 |
| news.url | 否 | String(200) | 图文链接 |

* **注意：postageSetting 为非必要项，如设置其中一项，其他的均必须要设置**
* **注意：postageSetting.type=2时，postageSetting.num必须设置；postageSetting.type=1时，postageSetting.amount必须设置**

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "shareMessage": {
            "id": 1890,
            .....
        },
        "wxImagetxtReply": {
            "id": 1706,
            ......
        },
        "wxImagetxtReplyItems": [
            {
                "id": 2291,
                .....
            }
        ],
        "activity": {
            "id": 662,
            .....
        },
        "secondKill": {
            "id": 395,
            .....
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取秒杀活动列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/second-kill/find-second-kill-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| name | 否 | String(250) | 活动名称 |
| deleted | 否 | Integer(4) | 活动状态 |
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
            "id": 662,
            "activity_type": 1,
            ......
            "news": {
                "id": 1706,
                .....
                "wxImagetxtReplyItems": [
                    {
                        "id": 2291,
                        ......
                        "documentLib": {
                            "id": 1,
                            .....
                        }
                    }
                ]
            },
            "secondKill": {
                "id": 395,
                .......
                "seckillGoods": [
                    "id": 142,
                    .....
                ]
            }
        },
        {......}
    ],
    "page": {
        "per_page": 15,
        "total_count": 126,
        "current_page": 0,
        "total_page": 9
    }
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取秒杀活动详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/second-kill/get-second-kill
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 店铺id |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 662,
        .....
        "secondKill": {
            "id": 395,
            .....
        },
        "shareMessage": {
            "id": 1890,
            .....
            "documentLib": {
                "id": 7,
                .....
            }
        },
        "postageSetting": [],
        "news": {
            "id": 1706,
            "media_id": null,
            .....
            "wxImagetxtReplyItems": [
                {
                    "id": 2291,
                    "document_id": "1",
                    .....
                    "documentLib": {
                        "id": 1,
                        .....
                    }
                }
            ]
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __获取秒杀活动详情(带商品)__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/second-kill/get-second-kill-with-goods
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 店铺id |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 1,
        "activity_id": 1,
        .....
        "activity": {
            "id": 1,
            "activity_type": 1,
            "relate_product_type": 1,
            "postage_setting_id": 1,
            "name": "test90sa",
            "desc": null,
            "sort": null,
            "expire_type": 1,
            "start_time": 1434959487,
            "end_time": 1536000776,
            "wx_qrcode_id": null,
            "wx_imagetxt_reply_id": 0,
            "share_message_id": 59,
            "shop_id": 5,
            "shop_sub_id": 43,
            "created": 1434180888,
            "modified": 1435914364,
            "deleted": 1
        },
        "seckillGoods": [
            {
                "id": 1,
                "second_kill_id": 1,
                "product_sku_id": 23,
                .....
                "productSku": {
                    "id": 23,
                    "sku_no": "123",
                    "product_id": 44,
                    ......
                    "product": {
                        "id": 44,
                        .....
                        "covers_id": 2,
                        "covers": {
                            "id": 2,
                            .....
                        }
                    }
                }
            },
            {......}
        ]
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __修改秒杀活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/secondKill/to-update
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| activity.id | 是 | Integer(11) | 活动id |
| activity.name | 是 | String(250) | 活动名称 |
| activity.postage_setting_id | 否 | Integer(11) | 邮费外键 |
| activity.desc | 否 | String(500) | 活动描述/规则 |
| activity.sort | 否 | Integer(11) | 排序 |
| activity.expire_type | 是 | Integer(4) | 有效期类型1.指定时间范围、2.无时间限制 |
| activity.start_time | 是 | Integer(11) | 活动开始时间 |
| activity.end_time | 是 | Integer(11) | 活动结束时间 |
| activity.share_type | 是 | Integer(4) |显示和分享模式（1.显示且能分享、2.不能显示且能分享、3.不能显示且不能分享）|
| postageSetting.type | 否 | Integer(11) | 包邮类型（1.满金额包邮、2.满件数包邮、3.免邮费）|
| postageSetting.num | 否 | Integer(11) | 数量 |
| postageSetting.amount | 否 | Integer(11) | 金额 |
| secondKill.id | 是 | Integer(11) | 秒杀id |
| shareMessage.title | 否 | String(100) | 分享标题 |
| shareMessage.desc | 否 | String(100) | 分享描述 |
| shareMessage.pic_id | 否 | Integer(11) | document_lib表外键 |
| news.title | 否 | String(100) | 分享标题 |
| news.description | 否 | String(100) | 分享描述 |
| news.document_id | 否 | Integer(11) | document_lib表外键 |

* **注意：activity.postage_setting_id设置为0即不设置邮费规则时，postageSetting项不需要设置**
* **注意：postageSetting 为非必要项，如设置其中一项，其他的均必须要设置**
* **注意：postageSetting.type=2时，postageSetting.num必须设置；postageSetting.type=1时，postageSetting.amount必须设置**

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "shareMessage": {
            "id": 1890,
            .....
        },
        "activity": {
            "id": 662,
            .....
            "secondKill": {
                "id": 395,
                "activity_id": 662,
                .....
            }
        },
        "secondKill": {
            "id": 395,
            ......
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __删除秒杀活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/secondKill/general-del
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 商家id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":null
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __开启秒杀活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/secondKill/general-enable
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 商家id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 661,
        .....
        "secondKill": {
            "id": 394,
            "activity_id": 661,
            .....
        },
        "shareMessage": {
            "id": 1875,
            .....
            "documentLib": {
                "id": 7,
                .....
            }
        },
        "postageSetting": [],
        "news": {
            "id": 1661,
            .....
            "wxImagetxtReplyItems": [
                {j
                    "id": 2201,
                    .....
                    "documentLib": {
                        "id": 1,
                        .....
                    }
                }
            ]
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __关闭秒杀活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/secondKill/general-disable
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 商家id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok"
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __新增秒杀商品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/secondKill/create-seckill-goods
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| second_kill_id | 是 | Integer(11) | 秒杀活动id |
| product_id | 是 | Integer(11) | 关联的商品id |
| shop_id | 是 | Integer(11) | 商家id |
| product_sku_id | 是 | Integer(11) | 关联的sku ID |
| quota | 是 | Integer(11) | 商品配额 |
| buy_price | 是 | Integer(11) | 秒杀价 |
| limit_buy | 是 | Integer(11) | 限购 |
| shop_sub_id | 是 | Integer(11) | 店铺id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok"
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __更新秒杀商品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/secondKill/update-seckill-goods
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 秒杀商品id |
| shop_id | 是 | Integer(11) | 商家id |
| quota | 否 | Integer(11) | 商品配额 |
| buy_price | 否 | Integer(11) | 秒杀价 |
| limit_buy | 否 | Integer(11) | 限购 |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "sales_num": 0,
        "shop_sub_id": 0,
        "second_kill_id": 399,
        "product_id": 313,
        "product_sku_id": 850,
        "buy_price": 1200,
        "quota": "10",
        "limit_buy": "1",
        "shop_id": 30,
        "product_name": "tt",
        "product_price": 2333300,
        "created": 1454293963,
        "modified": 1454293963,
        "deleted": 1,
        "id": 144
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取秒杀商品列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/second-kill/find-seckill-goods-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| second-kill-id | 否 | Integer(11) | 活动外键id |
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
    "errcode": 0,
    "errmsg": "ok",
    "data": [
        {
            "id": 144,
            "second_kill_id": 399,
            "product_id": 313,
            "product_sku_id": 850,
            "product_name": "tt",
            "product_price": 2333300,
            "buy_price": 1200,
            "quota": 10,
            "limit_buy": 1,
            "sales_num": 0,
            "shop_id": 30,
            "shop_sub_id": 0,
            "created": 1454293963,
            "modified": 1454293963,
            "deleted": 1,
            "productSku": {
                "id": 850,
                "sku_no": "54bgf3",
                "product_id": 313,
                "name": "tt",
                "reserves": 101,
                "freez_reserve": 10,
                "market_price": 3400,
                "cost_price": null,
                "retail_price": 2333300,
                "sales": null,
                "status": 1,
                "barcode": "9655815",
                "barcode_pic": null,
                "shop_id": 30,
                "shop_sub_id": 0,
                "created": 1451548047,
                "modified": 1454293963,
                "kindValues": [
                    {
                        "id": 95,
                        "name": "-1",
                        "product_kind_id": 113,
                        "shop_id": 30,
                        "created": 1441849408,
                        "modified": 1441878380,
                        "deleted": 1
                    }
                ],
                "kinds": [
                    {
                        "id": 113,
                        "name": "你好1111111111111",
                        "shop_id": 30,
                        "created": 1440402850,
                        "modified": 1453705477,
                        "deleted": 1
                    }
                ]
            },
            "product": {
                "id": 313,
                "product_category_id": 11,
                "product_category_path": "/86/11/",
                "product_kind_ids": "113;",
                "name": "tt",
                "subtitle": null,
                "keyword": null,
                "product_type": 1,
                "product_no": null,
                "show_price": 1200,
                "prod_weight": "54.000",
                "shop_id": 30,
                "shop_sub_id": 0,
                "hits": 0,
                "sales": 3,
                "status": 1,
                "postage_fee_type": 0,
                "quota": 23,
                "sort": 1,
                "is_pre_sale": 2,
                "pre_sale_id": 0,
                "show_sale_num": 2,
                "share_message_id": 1652,
                "sync_offline_sku": 2,
                "sale_scope": 1,
                "covers_id": 1303,
                "is_recommend": 2,
                "created": 1451548047,
                "modified": 1454050003,
                "deleted": 1,
                "productCategory": {
                    "id": 11,
                    "name": "自定义",
                    "pid": 86,
                    "level": 2,
                    "path": "/86/11/",
                    "sort": 0,
                    "desc": null,
                    "shop_id": 0,
                    "is_sys_cate": 1,
                    "created": 1441508942,
                    "modified": 1441508942,
                    "deleted": null
                }
            }
        },
        {......}
    ],
    "page": {
        "per_page": 3,
        "total_count": 1,
        "current_page": 0,
        "total_page": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取秒杀商品详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/second-kill/get-seckill-goods
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 秒杀商品id |
| second-kill-id | 否 | Integer(11) | 活动外键id |
| shop_id | 是 | Integer(11) | 店铺id |
| deleted | 否 | Integer(4) | 商品状态 |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 128,
        "second_kill_id": 370,
        "product_id": 320,
        "product_sku_id": 863,
        "product_name": "测试",
        "product_price": 100,
        "buy_price": 100,
        "quota": 3,
        "limit_buy": 1,
        "sales_num": 0,
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": 1453084100,
        "modified": 1453084100,
        "deleted": 1,
        "productSku": {
            "id": 863,
            "sku_no": "22211",
            "product_id": 320,
            "name": "测试",
            "reserves": 8,
            "freez_reserve": 3,
            "market_price": 100,
            "cost_price": null,
            "retail_price": 100,
            "sales": null,
            "status": 1,
            "barcode": "11122",
            "barcode_pic": null,
            "shop_id": 30,
            "shop_sub_id": 0,
            "created": 1452844717,
            "modified": 1453084100,
            "product": {
                "id": 320,
                "product_category_id": 11,
                "product_category_path": "/86/11/",
                "product_kind_ids": "126;",
                "name": "测试",
                "subtitle": null,
                "keyword": null,
                "product_type": 1,
                "product_no": null,
                "show_price": 100,
                "prod_weight": "50.000",
                "shop_id": 30,
                "shop_sub_id": 0,
                "hits": 0,
                "sales": 100,
                "status": 1,
                "postage_fee_type": 0,
                "quota": 0,
                "sort": 1,
                "is_pre_sale": 2,
                "pre_sale_id": 0,
                "show_sale_num": 2,
                "share_message_id": 1742,
                "sync_offline_sku": 2,
                "sale_scope": 1,
                "covers_id": 1364,
                "is_recommend": 2,
                "created": 1452844717,
                "modified": 1452844747,
                "deleted": 1,
                "covers": {
                    "id": 1364,
                    "name": "p3_6",
                    "desc": null,
                    "category_id": 0,
                    "tag_id": 1,
                    "file_cdn_path": "http://imgcache.vikduo.com/static/b5f03a39e4f480fcc2081d2766876ddb.png",
                    "file_type": 1,
                    "shop_id": 30,
                    "shop_sub_id": 0,
                    "created": 1452837348,
                    "modified": 1452837348,
                    "deleted": 1
                },
                "productInfo": {
                    "id": 276,
                    "product_id": 320,
                    "detail_pic": "1364,",
                    "description": null,
                    "detail": "<p><img src=\"http://imgcache.vikduo.com/static/2deeb56356defa9283661bc62fc234db.jpg\" style=\"\"/></p><p><img src=\"http://imgcache.vikduo.com/static/0844adbe52cb19d07c785ac6b0cf7dec.png\" style=\"\"/></p><p><img src=\"http://imgcache.vikduo.com/static/b5f03a39e4f480fcc2081d2766876ddb.png\" style=\"\"/></p><p><img src=\"http://imgcache.vikduo.com/static/e83c9aedf53adf9a1a40da0fd623ffcf.jpg\" style=\"\"/></p><p><img src=\"http://imgcache.vikduo.com/static/5b6580f581db09337dc4b41bb954877f.jpg\" style=\"\"/></p><p><img src=\"http://imgcache.vikduo.com/static/58bcbb9cb42e644373ae22d615f398c3.jpg\" style=\"\"/></p><p><img src=\"http://imgcache.vikduo.com/static/780a2c3392ea5a5f6c44a0012314f11b.jpg\" style=\"\"/></p><p><img src=\"http://imgcache.vikduo.com/static/b14d1a30c410c99f6746140730dd5631.jpg\" style=\"\"/></p><p><img src=\"http://imgcache.vikduo.com/static/7afe5bc6edb73a54465f7e4d335b9902.jpg\" style=\"\"/></p><p><br/></p>"
                }
            },
            "kindValues": [
                {
                    "id": 92,
                    "name": "红色",
                    "product_kind_id": 126,
                    "shop_id": 30,
                    "created": 1441533949,
                    "modified": 1441533949,
                    "deleted": 1
                }
            ],
            "kinds": [
                {
                    "id": 126,
                    "name": "颜色",
                    "shop_id": 30,
                    "created": 1441533941,
                    "modified": 1441533941,
                    "deleted": 1
                }
            ]
        },
        "secondKill": {
            "id": 370,
            "activity_id": 628,
            "shop_id": 30,
            "shop_sub_id": 0,
            "activity": {
                "id": 628,
                "activity_type": 1,
                "relate_product_type": 1,
                "postage_setting_id": 0,
                "name": "01/18-01/22",
                "desc": "秒杀活动规则",
                "sort": 50,
                "expire_type": 1,
                "start_time": 1453084121,
                "end_time": 1453429633,
                "wx_qrcode_id": null,
                "wx_imagetxt_reply_id": 1544,
                "share_message_id": 1761,
                "shop_id": 30,
                "shop_sub_id": 0,
                "created": 1453084033,
                "modified": 1453084123,
                "deleted": 1,
                "shareMessage": {
                    "id": 1761,
                    "title": "只要一秒时间，顺手就捡个便宜！",
                    "desc": "秒杀进行时，走过路过不容错过，随手一点，没准捡个大便宜呢~",
                    "pic_id": 7,
                    "shop_id": 30,
                    "shop_sub_id": 0,
                    "created": 1453084033,
                    "modified": 1453084123,
                    "deleted": 1,
                    "documentLib": {
                        "id": 7,
                        "name": "秒杀默认分享图片",
                        "desc": "秒杀默认分享图片",
                        "category_id": 0,
                        "tag_id": 1,
                        "file_cdn_path": "http://imgcache.vikduo.com/static/ac426542bed1756d6517a4127e3de1e0.jpg",
                        "file_type": 1,
                        "shop_id": 0,
                        "shop_sub_id": 0,
                        "created": 1442239226,
                        "modified": 1442239226,
                        "deleted": 1
                    }
                }
            }
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __删除秒杀商品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/secondKill/seckill-goods-del
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 商家id |

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

## __用户秒杀已买数量__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/secondKill/user-seckill-buy
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| activity_id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 商家id |
| uid | 是 | Integer(11) | 用户id |
| product_sku_id | 是 | Integer(11) | 产品skuid |


<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data": 2
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

