## __新增拼团活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/create
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
| togetherBuy.head_price | 否 | Integer(11) | 团长需要付的款项 |
| togetherBuy.is_discount | 否 | Integer(4) | 是否设置优惠（1.是、2.否） |
| togetherBuy.is_agree | 否 | Integer(4) | 是否同意协议（1：不同意，2：同意） |
| togetherBuy.is_time_limit | 否 | Integer(4) | 是否有参团时间限制（1.是、2.否） |
| togetherBuy.time_limit | 否 | Integer(11) | 参团时间限制，单位h |

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
        "togetherBuy": {
            "id": 395,
            .....
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取拼团活动列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/find-together-buy-list
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
            "togetherBuy": {
                "id": 395,
                .......
                "togetherBuyGoods": [
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


## __获取拼团活动详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/get-together-buy
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
        "togetherBuy": {
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

## __获取拼团活动详情(带商品)__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/get-together-buy-with-goods
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
        "togetherBuyGoods": [
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

## __进入商品详情（开启拼团）__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/get-together-buy-with--one-goods
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 拼团商品together_buy_goods表id |
| activity_id | 是 | Integer(11) | 活动activity表id |
| shop_id | 是 | Integer(11) | 店铺id |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {

    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __修改拼团活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/to-update
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
| togetherBuy.id | 是 | Integer(11) | 秒杀id |
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
            "togetherBuy": {
                "id": 395,
                "activity_id": 662,
                .....
            }
        },
        "togetherBuy": {
            "id": 395,
            ......
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __删除拼团活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/general-del
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


## __开启拼团活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/general-enable
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
        "togetherBuy": {
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

## __关闭拼团活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/general-disable
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


## __新增拼团商品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/create-together-buy-goods
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| together_buy_id | 是 | Integer(11) | 拼团活动together_buy表id |
| product_id | 是 | Integer(11) | 关联的商品id |
| product_sku_id | 是 | Integer(11) | 关联的sku ID |
| together_num | 是 | Integer(11) | 参团所需人数 |
| quota | 是 | Integer(11) | 商品配额 |
| buy_price | 是 | Integer(11) | 拼团价 |
| limit_buy | 是 | Integer(11) | 每人限购 |
| shop_id | 是 | Integer(11) | 商家id |
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

## __更新拼团商品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/update-together-buy-goods
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 拼团商品together_buy_goods表id |
| shop_id | 是 | Integer(11) | 商家id |
| quota | 否 | Integer(11) | 商品配额 |
| buy_price | 否 | Integer(11) | 秒杀价 |
| limit_buy | 否 | Integer(11) | 限购 |
| together_num | 否 | Integer(11) | 参团人数 |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取拼团商品列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/find-together-buy-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| together-buy-id | 否 | Integer(11) | together_buy表id |
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
      "id": 711,
      "activity_type": 7,
      "relate_product_type": 1,
      "postage_setting_id": 0,
      "name": "拼团活动名称",
      "desc": "1. 活动时间：#年#月#日#时 至 #年#月#日#时；\n2. 团长：开团且该团第一位支付成功的人\n3. 参加成员：通过团长邀请购买该商品的成员即为参团成员，参团成员也可邀请更多的成员参团\n4. 退款说明：若拼团失败系统会将支付的金额返还至参团成员的支付账号中\n5. 拼团是基于好友的组团购买，获取团购优惠，为了保证广大消费者的权益，商家有权判定为黄牛倒货的团解散并取消订单",
      "sort": 50,
      "expire_type": 1,
      "start_time": 1456974898,
      "end_time": 1457057698,
      "wx_qrcode_id": null,
      "wx_imagetxt_reply_id": 1838,
      "share_message_id": 1988,
      "shop_id": 30,
      "shop_sub_id": 0,
      "created": 1456971298,
      "modified": 1456971298,
      "deleted": 2,
      "share_type": 1,
      "news": {
        "id": 1838,
        "title": "成为团长带领小伙伴享受团购价！",
        "type": 2,
        "is_wsh": 2,
        "media_id": null,
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": 1456971298,
        "modified": 1456971298,
        "deleted": 1,
        "wxImagetxtReplyItems": [
          {
            "id": 2737,
            "media_id": null,
            "wx_imagetxt_reply_id": 1838,
            "title": "成为团长带领小伙伴享受团购价！",
            "description": "拼团活动开始啦，赶紧开团召集小伙伴一起团购吧！",
            "cdn_path": null,
            "document_id": "1",
            "link_type": null,
            "link_param": "",
            "url": null,
            "wx_url": null,
            "show_cover_pic": 2,
            "author": "",
            "content": "拼团活动开始啦，赶紧开团召集小伙伴一起团购吧！",
            "articles_comments_count": 0,
            "hits": 0,
            "likes": 0,
            "is_top": 2,
            "is_banner": 2,
            "shop_id": 30,
            "shop_sub_id": 0,
            "release_time": 0,
            "recommend": null,
            "created": 1456971298,
            "modified": 1456971298,
            "deleted": 1,
            "documentLib": {
              "id": 1,
              "name": "秒杀默认图文图片",
              "desc": "秒杀默认图文图片",
              "category_id": 0,
              "tag_id": 1,
              "file_cdn_path": "http://imgcache.vikduo.com/static/edc83542a3c2477eb9aa02f7f851e479.png",
              "file_type": 3,
              "shop_id": 0,
              "shop_sub_id": 0,
              "created": 1442239223,
              "modified": 1442239223,
              "deleted": 1
            }
          }
        ]
      },
      "togetherBuy": {
        "id": 1,
        "activity_id": 711,
        "head_price": 0,
        "is_discount": 2,
        "is_agree": 1,
        "is_time_limit": 2,
        "auth_icons": null,
        "is_auto_share": 2,
        "is_more": 2,
        "is_open": 2,
        "time_limit": 0,
        "description": null,
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": null,
        "modified": null,
        "togetherBuyGoods": []
      }
    },
    {
      "id": 712,
      "activity_type": 7,
      "relate_product_type": 1,
      "postage_setting_id": 0,
      "name": "拼团活动名称",
      "desc": "1. 活动时间：#年#月#日#时 至 #年#月#日#时；\n2. 团长：开团且该团第一位支付成功的人\n3. 参加成员：通过团长邀请购买该商品的成员即为参团成员，参团成员也可邀请更多的成员参团\n4. 退款说明：若拼团失败系统会将支付的金额返还至参团成员的支付账号中\n5. 拼团是基于好友的组团购买，获取团购优惠，为了保证广大消费者的权益，商家有权判定为黄牛倒货的团解散并取消订单",
      "sort": 50,
      "expire_type": 1,
      "start_time": 1456974900,
      "end_time": 1457057700,
      "wx_qrcode_id": null,
      "wx_imagetxt_reply_id": 1839,
      "share_message_id": 1989,
      "shop_id": 30,
      "shop_sub_id": 0,
      "created": 1456971300,
      "modified": 1456971300,
      "deleted": 2,
      "share_type": 1,
      "news": {
        "id": 1839,
        "title": "成为团长带领小伙伴享受团购价！",
        "type": 2,
        "is_wsh": 2,
        "media_id": null,
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": 1456971300,
        "modified": 1456971300,
        "deleted": 1,
        "wxImagetxtReplyItems": [
          {
            "id": 2738,
            "media_id": null,
            "wx_imagetxt_reply_id": 1839,
            "title": "成为团长带领小伙伴享受团购价！",
            "description": "拼团活动开始啦，赶紧开团召集小伙伴一起团购吧！",
            "cdn_path": null,
            "document_id": "1",
            "link_type": null,
            "link_param": "",
            "url": null,
            "wx_url": null,
            "show_cover_pic": 2,
            "author": "",
            "content": "拼团活动开始啦，赶紧开团召集小伙伴一起团购吧！",
            "articles_comments_count": 0,
            "hits": 0,
            "likes": 0,
            "is_top": 2,
            "is_banner": 2,
            "shop_id": 30,
            "shop_sub_id": 0,
            "release_time": 0,
            "recommend": null,
            "created": 1456971300,
            "modified": 1456971300,
            "deleted": 1,
            "documentLib": {
              "id": 1,
              "name": "秒杀默认图文图片",
              "desc": "秒杀默认图文图片",
              "category_id": 0,
              "tag_id": 1,
              "file_cdn_path": "http://imgcache.vikduo.com/static/edc83542a3c2477eb9aa02f7f851e479.png",
              "file_type": 3,
              "shop_id": 0,
              "shop_sub_id": 0,
              "created": 1442239223,
              "modified": 1442239223,
              "deleted": 1
            }
          }
        ]
      },
      "togetherBuy": {
        "id": 2,
        "activity_id": 712,
        "head_price": 0,
        "is_discount": 2,
        "is_agree": 1,
        "is_time_limit": 2,
        "auth_icons": null,
        "is_auto_share": 2,
        "is_more": 2,
        "is_open": 2,
        "time_limit": 0,
        "description": null,
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": null,
        "modified": null,
        "togetherBuyGoods": []
      }
    }
  ],
  "page": {
    "per_page": 2,
    "total_count": 209,
    "current_page": 0,
    "total_page": 105
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取拼团商品详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/get-together-buy-goods
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动商品together_buy_goods表id |
| together_buy_id | 否 | Integer(11) | 活动外键id |
| shop_id | 是 | Integer(11) | 店铺id |
| deleted | 否 | Integer(4) | 商品状态1.开启（这里只能传1） |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 267,
    "together_buy_id": 34,
    "product_id": 328,
    "product_sku_id": 890,
    "product_name": "qqqqqqqqqq",
    "product_price": 100,
    "buy_price": 100,
    "quota": 1,
    "together_num": 2,
    "limit_buy": 1,
    "sales_num": 0,
    "shop_id": 30,
    "shop_sub_id": 0,
    "created": 1457172837,
    "modified": 1457683261,
    "deleted": 1,
    "productSku": {
      "id": 890,
      "sku_no": "",
      "product_id": 328,
      "name": "qqqqqqqqqq",
      "reserves": 56,
      "freez_reserve": 2,
      "market_price": 100,
      "cost_price": null,
      "retail_price": 100,
      "sales": null,
      "status": 1,
      "barcode": "",
      "barcode_pic": null,
      "shop_id": 30,
      "shop_sub_id": 0,
      "created": 1456312144,
      "modified": 1457683261,
      "product": {
        "id": 328,
        "product_category_id": 221,
        "product_category_path": "/219/221/",
        "product_kind_ids": "115;",
        "name": "qqqqqqqqqq",
        "subtitle": null,
        "keyword": null,
        "product_type": 1,
        "product_no": null,
        "show_price": 100,
        "prod_weight": "2.000",
        "shop_id": 30,
        "shop_sub_id": 0,
        "hits": 0,
        "sales": 1,
        "status": 1,
        "postage_fee_type": 678,
        "quota": 3,
        "sort": 0,
        "is_pre_sale": 2,
        "pre_sale_id": 0,
        "show_sale_num": 2,
        "share_message_id": 1857,
        "sync_offline_sku": 2,
        "sale_scope": 1,
        "covers_id": 1380,
        "is_recommend": 2,
        "created": 1453444341,
        "modified": 1458705239,
        "deleted": 3,
        "covers": {
          "id": 1380,
          "name": "3",
          "desc": null,
          "category_id": 0,
          "tag_id": 1,
          "file_cdn_path": "http://imgcache.vikduo.com/static/8d665aa70eedd30e5ad62edcc7dc4979.png",
          "file_type": 1,
          "shop_id": 30,
          "shop_sub_id": 0,
          "created": 1453426184,
          "modified": 1453426184,
          "deleted": 1
        },
        "productInfo": {
          "id": 284,
          "product_id": 328,
          "detail_pic": "1380,1379,1382,1378,1381,",
          "description": null,
          "detail": "<p>42312</p>"
        }
      },
      "kindValues": [
        {
          "id": 86,
          "name": "薄",
          "product_kind_id": 115,
          "shop_id": 30,
          "created": 1440817850,
          "modified": 1453342915,
          "deleted": 1
        }
      ],
      "kinds": [
        {
          "id": 115,
          "name": "厚度",
          "shop_id": 30,
          "created": 1440816618,
          "modified": 1453285854,
          "deleted": 1
        }
      ]
    },
    "togetherBuy": {
      "id": 34,
      "activity_id": 764,
      "head_price": 0,
      "is_discount": 1,
      "is_agree": 2,
      "is_time_limit": 1,
      "auth_icons": null,
      "is_auto_share": 2,
      "is_more": 2,
      "is_open": 2,
      "time_limit": 0,
      "description": null,
      "shop_id": 30,
      "shop_sub_id": 0,
      "created": null,
      "modified": 1457172858,
      "activity": {
        "id": 764,
        "activity_type": 7,
        "relate_product_type": 1,
        "postage_setting_id": 52,
        "name": "拼团活动名称",
        "desc": "1. 活动时间：#年#月#日#时 至 #年#月#日#时；\n2. 团长：开团且该团第一位支付成功的人\n3. 参加成员：通过团长邀请购买该商品的成员即为参团成员，参团成员也可邀请更多的成员参团\n4. 退款说明：若拼团失败系统会将支付的金额返还至参团成员的支付账号中\n5. 拼团是基于好友的组团购买，获取团购优惠，为了保证广大消费者的权益，商家有权判定为黄牛倒货的团解散并取消订单",
        "sort": 50,
        "expire_type": 1,
        "start_time": 1457176403,
        "end_time": 1457604861,
        "wx_qrcode_id": null,
        "wx_imagetxt_reply_id": 1907,
        "share_message_id": 2062,
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": 1457172803,
        "modified": 1457604861,
        "deleted": 1,
        "share_type": 1,
        "shareMessage": {
          "id": 2062,
          "title": "成为团长带领小伙伴享受团购价！",
          "desc": "拼团活动开始啦，赶紧开团召集小",
          "pic_id": 7,
          "shop_id": 30,
          "shop_sub_id": 0,
          "created": 1457172803,
          "modified": 1457172858,
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


## __删除拼团商品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/together-buy-goods-del
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
    "errmsg": "ok"
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __团列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/find-together-buy-queue
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| together_buy_id | 是 | Integer(11) | 活动together_buy表id |
| shop_id | 是 | Integer(11) | 商家id |
| count | 否 | Integer(11) | 每页数 |
| page | 否 | Integer(11) | 查询页码 |
| sortStr | 否 | Array | 排序 |
| headNickname | 否 | String | 产品skuid |
| status | 否 | Integer(11) | 团状态1.创建中2.进行中3.已成团4.团失败 |
| reasonFlag | 否 | boolean(4) | 关闭理由不为空标识，传1 |
| is_help | 否 | Integer(4) | 是否直接成团1.是 2.否|
| validFlag | 否 | Integer(4) | 进行中的团标识(活动开启,时间未结束,团状态进行中) ,传1|

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": 263,
      "together_buy_id": 193,
      "head_uid": 507,
      "start_time": null,
      "remain_num": 5,
      "success_time": null,
      "status": 4,
      "close_reason": "到期，系统自动关闭。",
      "is_help": 2,
      "together_buy_goods_id": 368,
      "shop_id": 30,
      "shop_sub_id": null,
      "created": 1464167814,
      "modified": 1464340621,
      "togetherBuy": {
        "id": 193,
        "activity_id": 972,
        "head_price": 1,
        "is_discount": 1,
        "is_agree": 2,
        "is_time_limit": 2,
        "auth_icons": null,
        "is_auto_share": 1,
        "is_more": 2,
        "is_open": 2,
        "time_limit": 0,
        "description": null,
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": 1464167744,
        "modified": 1464167783,
        "activity": {
          "id": 972,
          "activity_type": 7,
          "relate_product_type": 1,
          "postage_setting_id": 0,
          "name": "拼团活动名称",
          "desc": "1. 活动时间：#年#月#日#时 至 #年#月#日#时；\n2. 团长：开团且该团第一位支付成功的人\n3. 参加成员：通过团长邀请购买该商品的成员即为参团成员，参团成员也可邀请更多的成员参团\n4. 退款说明：若拼团失败系统会将支付的金额返还至参团成员的支付账号中\n5. 拼团是基于好友的组团购买，获取团购优惠，为了保证广大消费者的权益，商家有权判定为黄牛倒货的团解散并取消订单",
          "sort": 50,
          "expire_type": 1,
          "start_time": 1464167775,
          "end_time": 1464340568,
          "wx_qrcode_id": null,
          "wx_imagetxt_reply_id": 2247,
          "share_message_id": 206442,
          "shop_id": 30,
          "shop_sub_id": 0,
          "created": 1464167744,
          "modified": 1464167787,
          "deleted": 1,
          "share_type": 1
        }
      },
      "userInfo": {
        "id": 507,
        "mobile": "13232323232",
        "member_id": 1836,
        "nickname": "eve🌞🌞哈哈hh",
        "real_name": "a1",
        "sex": 1,
        "birth": 1435449600,
        "email": "233@qq.com",
        "province": "北京市",
        "city": "北京市",
        "county": "朝阳区",
        "country": null,
        "address": "滴滴滴",
        "headimgurl": "http://wx.qlogo.cn/mmopen/0sDCa2E8S1u5LvyUOl13lhbG0R3Z3lD6ichbK4JK1e4u2LZwVsMf3HuoIdRkI63M26XoRS9w2YbGxdtdJ1Bp8wMwUbichLULFh/0",
        "shop_id": 30,
        "shop_sub_id": 292,
        "staff_id": 69,
        "belong_to_staff_id": 69,
        "login_count": 142,
        "lastloginip": "121.34.147.48",
        "lastlogintime": 1463539065,
        "password": null,
        "type": 2,
        "status": 1,
        "member_refer": null,
        "scene_id": 1,
        "mpath": null,
        "mid": 81,
        "agent_id": 0,
        "agent_path": null,
        "sign_days": 1,
        "sign_time": 1451029210,
        "is_subscribe": 1,
        "group_id": 1,
        "level_id": null,
        "point": 770,
        "wsh_code": null,
        "created": 1459823307,
        "modified": 1468305740,
        "deleted": 1,
        "test_nickname": "??",
        "bind_mobile": "13685855858"
      },
      "togetherBuyGoods": {
        "id": 368,
        "together_buy_id": 193,
        "product_id": 360,
        "product_sku_id": 1069,
        "product_name": "老爸豆腐干，儿时的味！拼团聚优惠！",
        "product_price": 90000,
        "buy_price": 1,
        "quota": 5,
        "together_num": 5,
        "limit_buy": 1,
        "sales_num": 0,
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": 1464167769,
        "modified": 1464167769,
        "deleted": 1
      },
      "joinCount": 0
    }
  ],
  "page": {
    "per_page": 2,
    "total_count": 1,
    "current_page": 0,
    "total_page": 1
  }
}
```

错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
## __获取某一个团的详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/get-together-buy-queue
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | together_buy_queue表id |
| shop_id | 是 | Integer(11) | 商家id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 68,
    "together_buy_id": 55,
    "head_uid": 507,
    "start_time": 1457694917,
    "remain_num": 0,
    "success_time": null,
    "status": 4,
    "close_reason": "dsad",
    "is_help": 2,
    "together_buy_goods_id": 277,
    "shop_id": 30,
    "shop_sub_id": null,
    "created": 1457694909,
    "modified": 1457918767,
    "togetherBuy": {
      "id": 55,
      "activity_id": 791,
      "head_price": 100,
      "is_discount": 1,
      "is_agree": 2,
      "is_time_limit": 2,
      "auth_icons": null,
      "is_auto_share": 2,
      "is_more": 2,
      "is_open": 2,
      "time_limit": 0,
      "description": null,
      "shop_id": 30,
      "shop_sub_id": 0,
      "created": 1457612036,
      "modified": 1457612104,
      "activity": {
        "id": 791,
        "activity_type": 7,
        "relate_product_type": 1,
        "postage_setting_id": 0,
        "name": "拼团活动测试",
        "desc": "1. 活动时间：#年#月#日#时 至 #年#月#日#时；\n2. 团长：开团且该团第一位支付成功的人\n3. 参加成员：通过团长邀请购买该商品的成员即为参团成员，参团成员也可邀请更多的成员参团\n4. 退款说明：若拼团失败系统会将支付的金额返还至参团成员的支付账号中\n5. 拼团是基于好友的组团购买，获取团购优惠，为了保证广大消费者的权益，商家有权判定为黄牛倒货的团解散并取消订单",
        "sort": 50,
        "expire_type": 1,
        "start_time": 1457612057,
        "end_time": 1457698394,
        "wx_qrcode_id": null,
        "wx_imagetxt_reply_id": 1953,
        "share_message_id": 2126,
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": 1457612036,
        "modified": 1457612106,
        "deleted": 1,
        "share_type": 1,
        "shareMessage": {
          "id": 2126,
          "title": "成为团长带领小伙伴享受团购价！",
          "desc": "拼团活动开始啦，赶紧开团召集小",
          "pic_id": 7,
          "shop_id": 30,
          "shop_sub_id": 0,
          "created": 1457612036,
          "modified": 1457612104,
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
        },
        "postageSetting": []
      }
    },
    "togetherBuyGoods": {
      "id": 277,
      "together_buy_id": 55,
      "product_id": 342,
      "product_sku_id": 1021,
      "product_name": "03100925",
      "product_price": 3400,
      "buy_price": 100,
      "quota": 3,
      "together_num": 2,
      "limit_buy": 1,
      "sales_num": 3,
      "shop_id": 30,
      "shop_sub_id": 0,
      "created": 1457612076,
      "modified": 1457695226,
      "deleted": 1,
      "productSku": {
        "id": 1021,
        "sku_no": "",
        "product_id": 342,
        "name": "03100925",
        "reserves": 6585,
        "freez_reserve": 19,
        "market_price": 3400,
        "cost_price": null,
        "retail_price": 3400,
        "sales": 3,
        "status": 1,
        "barcode": "",
        "barcode_pic": null,
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": 1457573220,
        "modified": 1466404085,
        "product": {
          "id": 342,
          "product_category_id": 218,
          "product_category_path": "/216/217/218/",
          "product_kind_ids": "113;",
          "name": "03100925",
          "subtitle": null,
          "keyword": null,
          "product_type": 1,
          "product_no": null,
          "show_price": 3400,
          "prod_weight": "100.000",
          "shop_id": 30,
          "shop_sub_id": 0,
          "hits": 0,
          "sales": 3,
          "status": 1,
          "postage_fee_type": 0,
          "quota": 0,
          "sort": 1,
          "is_pre_sale": 2,
          "pre_sale_id": 0,
          "show_sale_num": 2,
          "share_message_id": 2111,
          "sync_offline_sku": 2,
          "sale_scope": 1,
          "covers_id": 91786,
          "is_recommend": 2,
          "created": 1457573220,
          "modified": 1466404085,
          "deleted": 1,
          "covers": {
            "id": 91786,
            "name": "pic6",
            "desc": null,
            "category_id": 0,
            "tag_id": 1,
            "file_cdn_path": "http://imgcache.vikduo.com/static/27e2017e63acd5c38f4fcc52edc659cc.jpg.png",
            "file_type": 1,
            "shop_id": 30,
            "shop_sub_id": 0,
            "created": 1456800066,
            "modified": 1456800066,
            "deleted": 1
          },
          "productInfo": {
            "id": 298,
            "product_id": 342,
            "detail_pic": [
              {
                "id": 91786,
                "name": "pic6",
                "desc": null,
                "category_id": 0,
                "tag_id": 1,
                "file_cdn_path": "http://imgcache.vikduo.com/static/27e2017e63acd5c38f4fcc52edc659cc.jpg.png",
                "file_type": 1,
                "shop_id": 30,
                "shop_sub_id": 0,
                "created": 1456800066,
                "modified": 1456800066,
                "deleted": 1
              }
            ],
            "description": null,
            "detail": "<p><img src=\"http://imgcache.vikduo.com/static/71a8921921e7e4963f243a32bfeeeabb.jpg\" title=\"流程\"/><br style=\"font-family: &#39;Microsoft YaHei&#39;, Arial, Helvetica, sans-serif; line-height: 16px; white-space: normal;\"/><span style=\"font-family: &#39;Microsoft YaHei&#39;, Arial, Helvetica, sans-serif; line-height: 16px;\">商品，</span><br style=\"font-family: &#39;Microsoft YaHei&#39;, Arial, Helvetica, sans-serif; line-height: 16px; white-space: normal;\"/><span style=\"font-family: &#39;Microsoft YaHei&#39;, Arial, Helvetica, sans-serif; line-height: 16px;\">商品，</span><br style=\"font-family: &#39;Microsoft YaHei&#39;, Arial, Helvetica, sans-serif; line-height: 16px; white-space: normal;\"/><span style=\"font-family: &#39;Microsoft YaHei&#39;, Arial, Helvetica, sans-serif; line-height: 16px;\">商品，</span><br style=\"font-family: &#39;Microsoft YaHei&#39;, Arial, Helvetica, sans-serif; line-height: 16px; white-space: normal;\"/><span style=\"font-family: &#39;Microsoft YaHei&#39;, Arial, Helvetica, sans-serif; line-height: 16px;\">商品，</span><br style=\"font-family: &#39;Microsoft YaHei&#39;, Arial, Helvetica, sans-serif; line-height: 16px; white-space: normal;\"/><span style=\"font-family: &#39;Microsoft YaHei&#39;, Arial, Helvetica, sans-serif; line-height: 16px;\">商品，</span><br style=\"font-family: &#39;Microsoft YaHei&#39;, Arial, Helvetica, sans-serif; line-height: 16px; white-space: normal;\"/><span style=\"font-family: &#39;Microsoft YaHei&#39;, Arial, Helvetica, sans-serif; line-height: 16px;\">商品，</span><br style=\"font-family: &#39;Microsoft YaHei&#39;, Arial, Helvetica, sans-serif; line-height: 16px; white-space: normal;\"/><span style=\"font-family: &#39;Microsoft YaHei&#39;, Arial, Helvetica, sans-serif; line-height: 16px;\">商品，</span><br style=\"font-family: &#39;Microsoft YaHei&#39;, Arial, Helvetica, sans-serif; line-height: 16px; white-space: normal;\"/><span style=\"font-family: &#39;Microsoft YaHei&#39;, Arial, Helvetica, sans-serif; line-height: 16px;\">商品，</span></p>"
          }
        },
        "kindValues": [
          {
            "id": 79,
            "name": "M",
            "product_kind_id": 113,
            "shop_id": 30,
            "created": 1440402857,
            "modified": 1440402857,
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
      }
    },
    "joinCount": 2
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取参团列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/find-together-buy-join
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| uid | 否 | Integer(11) | 用户wx_user_infos表id |
| headNickname | 否 | String | 团长昵称 |
| together_buy_queue_id | 否 | Integer(11) | 团长together_buy_queue表id |
| count | 否 | Integer(11) | 每页条数 |
| page | 否 | Integer(11) | 查询页码 |
| sortStr | 否 | Array | 排序 |
| shop_id | 是 | Integer(11) | 商家id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": 135,
      "together_buy_id": 55,
      "together_buy_queue_id": 68,
      "is_head": 2,
      "uid": 507,
      "num": 1,
      "headimgurl": "",
      "nickname": "",
      "shop_id": 30,
      "shop_sub_id": null,
      "created": 1457694917,
      "modified": 1457694917,
      "togetherBuy": {
        "id": 55,
        "activity_id": 791,
        "head_price": 100,
        "is_discount": 1,
        "is_agree": 2,
        "is_time_limit": 2,
        "auth_icons": null,
        "is_auto_share": 2,
        "is_more": 2,
        "is_open": 2,
        "time_limit": 0,
        "description": null,
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": 1457612036,
        "modified": 1457612104
      },
      "togetherBuyQueue": {
        "id": 68,
        "together_buy_id": 55,
        "head_uid": 507,
        "start_time": 1457694917,
        "status": 4,
        "remain_num": 0,
        "close_reason": "dsad",
        "is_help": 2,
        "together_buy_goods_id": 277,
        "shop_id": 30,
        "shop_sub_id": null,
        "created": 1457694909,
        "modified": 1457918767,
        "success_time": null,
        "userInfo": {
          "id": 507,
          "mobile": "13232323232",
          "member_id": 1836,
          "nickname": "eve🌞🌞哈哈hh",
          "real_name": "a1",
          "sex": 1,
          "birth": 1435449600,
          "email": "233@qq.com",
          "province": "北京市",
          "city": "北京市",
          "county": "朝阳区",
          "country": null,
          "address": "滴滴滴",
          "headimgurl": "http://wx.qlogo.cn/mmopen/0sDCa2E8S1u5LvyUOl13lhbG0R3Z3lD6ichbK4JK1e4u2LZwVsMf3HuoIdRkI63M26XoRS9w2YbGxdtdJ1Bp8wMwUbichLULFh/0",
          "shop_id": 30,
          "shop_sub_id": 292,
          "staff_id": 69,
          "belong_to_staff_id": 69,
          "login_count": 142,
          "lastloginip": "121.34.147.48",
          "lastlogintime": 1463539065,
          "password": null,
          "type": 2,
          "status": 1,
          "member_refer": null,
          "scene_id": 1,
          "mpath": null,
          "mid": 81,
          "agent_id": 0,
          "agent_path": null,
          "sign_days": 1,
          "sign_time": 1451029210,
          "is_subscribe": 1,
          "group_id": 1,
          "level_id": null,
          "point": 770,
          "wsh_code": null,
          "created": 1459823307,
          "modified": 1468305740,
          "deleted": 1,
          "test_nickname": "??",
          "bind_mobile": "13685855858"
        },
        "togetherBuyGoods": {
          "id": 277,
          "together_buy_id": 55,
          "product_id": 342,
          "product_sku_id": 1021,
          "product_name": "03100925",
          "product_price": 3400,
          "buy_price": 100,
          "quota": 3,
          "together_num": 2,
          "limit_buy": 1,
          "sales_num": 3,
          "shop_id": 30,
          "shop_sub_id": 0,
          "created": 1457612076,
          "modified": 1457695226,
          "deleted": 1
        }
      },
      "joinCount": 2
    }
  ],
  "page": {
    "per_page": 2,
    "total_count": 1,
    "current_page": 0,
    "total_page": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取某团下参团成员列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/find-together-buy-join-by-queue
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| together_buy_queue_id | 是 | Integer(11) | 团长together_buy_queue表id |
| count | 否 | Integer(11) | 每页条数 |
| page | 否 | Integer(11) | 查询页码 |
| sortStr | 否 | Array | 排序 |
| shop_id | 是 | Integer(11) | 商家id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":[
    {
      "id": 135,
      "together_buy_id": 55,
      "together_buy_queue_id": 68,
      "is_head": 2,
      "uid": 507,
      "num": 1,
      "headimgurl": "",
      "nickname": "",
      "shop_id": 30,
      "shop_sub_id": null,
      "created": 1457694917,
      "modified": 1457694917,
      "userInfo": {
        "id": 507,
        "mobile": "13232323232",
        "member_id": 1836,
        "nickname": "eve🌞🌞哈哈hh",
        "real_name": "a1",
        "sex": 1,
        "birth": 1435449600,
        "email": "233@qq.com",
        "province": "北京市",
        "city": "北京市",
        "county": "朝阳区",
        "country": null,
        "address": "滴滴滴",
        "headimgurl": "http://wx.qlogo.cn/mmopen/0sDCa2E8S1u5LvyUOl13lhbG0R3Z3lD6ichbK4JK1e4u2LZwVsMf3HuoIdRkI63M26XoRS9w2YbGxdtdJ1Bp8wMwUbichLULFh/0",
        "shop_id": 30,
        "shop_sub_id": 292,
        "staff_id": 69,
        "belong_to_staff_id": 69,
        "login_count": 142,
        "lastloginip": "121.34.147.48",
        "lastlogintime": 1463539065,
        "password": null,
        "type": 2,
        "status": 1,
        "member_refer": null,
        "scene_id": 1,
        "mpath": null,
        "mid": 81,
        "agent_id": 0,
        "agent_path": null,
        "sign_days": 1,
        "sign_time": 1451029210,
        "is_subscribe": 1,
        "group_id": 1,
        "level_id": null,
        "point": 770,
        "wsh_code": null,
        "created": 1459823307,
        "modified": 1468305740,
        "deleted": 1,
        "test_nickname": "??",
        "bind_mobile": "13685855858"
      }
    },
    {.......}
  ],
  "page": {
    "per_page": 2,
    "total_count": 2,
    "current_page": 0,
    "total_page": 1
  }
    ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __用户对某拼团商品已购数量__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/count-user-buy
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| activity_id | 是 | Integer(11) | 活动activity表id |
| shop_id | 是 | Integer(11) | 商家id |
| uid | 是 | Integer(11) | 用户id |
| product_sku_id | 是 | Integer(11) | 产品product_sku表id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":2
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __用户开团（创建团）__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/open-queue
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| activity_id | 是 | Integer(11) | 活动activity表id |
| shop_id | 是 | Integer(11) | 商家id |
| uid | 是 | Integer(11) | 用户id |
| num | 是 | Integer(11) | 购买数量 |
| together_buy_goods_id | 是 | Integer(11) | 活动商品together_buy_goods表id |
| pickup_type | 否 | Integer(4) | 提货方式 1.快捷方式 2.到店自提（默认1） |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    ....//订单信息，详见订单详情接口
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __参团（加入团 创建订单）__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/join-queue
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| activity_id | 是 | Integer(11) | 活动activity表id |
| together_buy_queue_id | 是 | Integer(11) | 团together_buy_queue表id |
| shop_id | 是 | Integer(11) | 商家id |
| uid | 是 | Integer(11) | 用户id |
| num | 是 | Integer(11) | 购买数量 |
| together_buy_goods_id | 是 | Integer(11) | 活动商品together_buy_goods表id |
| pickup_type | 否 | Integer(4) | 提货方式 1.快捷方式 2.到店自提（默认1） |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    ....//订单信息
    "queue_end_time": 1469311592 //团结束时间撮
    "queue":{
      "id": 165,
      "together_buy_id": 1,
      "head_uid": 507,
      "start_time": 1458125012,
      "status": 2,
      "remain_num": 2,
      "close_reason": null,
      "is_help": 2,
      "together_buy_goods_id": 95,
      "shop_id": 30,
      "shop_sub_id": 30,
      "created": 1468311592,
      "modified": 1468311692,
      "success_time": null
    },
    "product":{.....} //商品信息 参考商品详情接口
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取用户参团信息，若不存在join记录，则判断是否存在未支付订单，存在则一并返回订单信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/get-user-buy-detail
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| together_buy_queue_id | 是 | Integer(11) | 团together_buy_queue表id |
| shop_id | 是 | Integer(11) | 商家id |
| uid | 是 | Integer(11) | 用户id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    "togetherBuyJoin":{
      "id": 165,
      "together_buy_id": 1,
      "together_buy_queue_id": 507,
      "is_head": 2,
      "uid": 2,
      "num": 2,
      "headimgurl": null,
      "nickname": 2,
      "shop_id": 30,
      "shop_sub_id": null,
      "created": 1468311592,
      "modified": 1468311692
    },
    "order":{.....} //订单信息 参考订单详情接口
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __关闭团__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/close-together-buy-queue
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 团together_buy_queue表id |
| shop_id | 是 | Integer(11) | 商家id |
| staff_id | 是 | Integer(11) | 员工id |
| close_reason | 是 | String | 关闭团的理由 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": 165,
      "together_buy_id": 1,
      "head_uid": 507,
      "start_time": 1458125012,
      "status": 2,
      "remain_num": 2,
      "close_reason": null,
      "is_help": 2,
      "together_buy_goods_id": 95,
      "shop_id": 30,
      "shop_sub_id": 30,
      "created": 1468311592,
      "modified": 1468311692,
      "success_time": null
    },
    {.....} //注水用户参团记录
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __直接成团（注水）__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/together-buy/help-success-queue
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 团together_buy_queue表id |
| shop_id | 是 | Integer(11) | 商家id |
| staff_id | 是 | Integer(11) | 员工id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "together_buy_queue_id": 165,
      "is_head": 1,
      "uid": 0,
      "num": 0,
      "headimgurl": "http://imgcache.vikduo.com/static/5660c762be283be3504e1637235df88b.jpg",
      "nickname": "强者之梦",
      "shop_sub_id": null,
      "created": 1468311692,
      "together_buy_id": 95,
      "shop_id": 30,
      "modified": 1468311692,
      "id": 235
    },
    {.....} //注水用户参团记录
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
