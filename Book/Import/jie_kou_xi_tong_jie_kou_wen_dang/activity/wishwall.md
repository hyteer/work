## __新增祝福墙活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wish-wall/create-wish-wall
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| activity.name | 是 | String(250) | 活动名称 |
| activity.desc | 否 | String(500) | 活动描述/规则 |
| activity.sort | 否 | Integer(11) | 排序 |
| activity.start_time | 是 | Integer(11) | 活动开始时间 |
| activity.end_time | 是 | Integer(11) | 活动结束时间 |
| activity.shop_id | 是 | Integer(11) | 商家id |
| activity.shop_sub_id | 否 | Integer(11) | 店铺id |
| activity.share_type | 是 | Integer(4) |显示和分享模式（1.显示且能分享、2.不能显示且能分享、3.不能显示且不能分享）|
| wishWall.pc_bg_img | 是 | varchar(20) | 电脑端背景图 |
| wishWall.wx_bg_img | 是 | varchar(20) | 手机端背景图 |
| wishWall.wx_code_img | 否 | varchar(20) | 活动二维码 |
| wishWall.need_check | 是 | Integer(11) | 是否需要审核（1.是、2.否） |
| wishWall.lucky_number | 否 | text | 中奖号码（逗号分割） |
| wishWall.lucky_words | 是 | varchar(50) | 中奖祝福语 |
| wishWall.shop_id | 是 | Integer(11) | 商家id |
| wishWall.shop_sub_id | 否 | Integer(11) | 店铺id |
| shareMessage.title | 是 | String(100) | 分享标题 |
| shareMessage.desc | 是 | String(100) | 分享描述 |
| shareMessage.pic_id | 是 | Integer(11) | 文档id |
| news.title | 是 | String(50) | 微信图文标题 |
| news.description | 是 | String(250) | 微信图文描述 |
| news.document_id | 是 | Integer(11) | 文档id |
| news.url | 是 | String(11) | 微信图文链接 |
| news.content | 是 | String | 文档内容 |



<br  /><br  />
提示：shareMessage、news非必填项。
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
"errcode": 0,
    "errmsg": "ok",
    "data": {
        "shareMessage": {
            "title": "分享信息标题",
            "desc": "分享信息详情。。。。。。。",
            "pic_id": "5",
            "shop_id": "5",
            "shop_sub_id": "45",
            "created": 1435736866,
            "modified": 1435736866,
            "deleted": 1,
            "id": 86
        },
        "wxImagetxtReply": {
            "type": 2,
            "shop_id": "5",
            "shop_sub_id": "45",
            "title": "图文标题",
            "created": 1435736866,
            "modified": 1435736866,
            "deleted": 1,
            "id": 19
        },
        "wxImagetxtReplyItem": [
            {
                "articles_comments_count": 0,
                "hits": 0,
                "likes": 0,
                "is_top": 2,
                "is_banner": 2,
                "release_time": 0,
                "deleted": 1,
                "title": "图文标题",
                "description": "图文的描述",
                "document_id": "6",
                "url": "http://baidu.com",
                "content": "内容诶。。。。。。。",
                "wx_imagetxt_reply_id": 19,
                "shop_id": "5",
                "shop_sub_id": "45",
                "created": 1435736866,
                "modified": 1435736866,
                "id": 13
            }
        ],
        "activity": {
            "relate_product_type": 1,
            "postage_setting_id": 0,
            "expire_type": 1,
            "wx_imagetxt_reply_id": 19,
            "share_message_id": 86,
            "name": "活动controller",
            "start_time": "1434180888",
            "end_time": "1434190888",
            "sort": "0",
            "wx_qrcode_id": "",
            "desc": "sdfsf",
            "shop_id": "5",
            "shop_sub_id": "45",
            "activity_type": 5,
            "created": 1435736866,
            "modified": 1435736866,
            "deleted": 1,
            "id": 59
        },
        "wishWall": {
            "need_check": "1",
            "count": 0,
            "pc_bg_img": "12",
            "wx_bg_img": "13",
            "wx_code_img": "15",
            "lucky_number": "1,11,111,",
            "lucky_words": "耶，中奖了哈",
            "shop_id": "5",
            "shop_sub_id": "45",
            "activity_id": 59,
            "id": 15
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __修改祝福墙活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wish-wall/update-wish-wall
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| activity.id | 是 | Integer(11) | 活动id |
| activity.name | 是 | String(250) | 活动名称 |
| activity.desc | 否 | String(500) | 活动描述/规则 |
| activity.sort | 否 | Integer(11) | 排序 |
| activity.start_time | 是 | Integer(11) | 活动开始时间 |
| activity.end_time | 是 | Integer(11) | 活动结束时间 |
| activity.share_type | 是 | Integer(4) |显示和分享模式（1.显示且能分享、2.不能显示且能分享、3.不能显示且不能分享）|
| activity.shop_id | 是 | Integer(11) | 商家id |
| activity.shop_sub_id | 否 | Integer(11) | 店铺id |
| wishWall.pc_bg_img | 是 | varchar(20) | 电脑端背景图 |
| wishWall.wx_bg_img | 是 | varchar(20) | 手机端背景图 |
| wishWall.wx_code_img | 是 | varchar(20) | 活动二维码 |
| wishWall.need_check | 是 | Integer(11) | 是否需要审核（1.是、2.否） |
| wishWall.lucky_number | 否 | text | 中奖号码（逗号分割） |
| wishWall.lucky_words | 是 | varchar(50) | 中奖祝福语 |
| wishWall.shop_id | 是 | Integer(11) | 商家id |
| wishWall.shop_sub_id | 否 | Integer(11) | 店铺id |
| shareMessage.title | 是 | String(100) | 分享标题 |
| shareMessage.desc | 是 | String(100) | 分享描述 |
| shareMessage.pic_id | 是 | Integer(11) | 文档id |
| news.title | 是 | String(50) | 微信图文标题 |
| news.description | 是 | String(250) | 微信图文描述 |
| news.document_id | 是 | Integer(11) | 文档id |
| news.url | 是 | String(11) | 微信图文链接 |
| news.content | 是 | String | 文档内容 |



<br  /><br  />
提示：shareMessage、news非必填项。
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "shareMessage": {
            "id": 86,
            "title": "分享信息标题",
            "desc": "分享信息详情。。。。。。。",
            "pic_id": "6",
            "shop_id": "5",
            "shop_sub_id": 45,
            "created": 1435736866,
            "modified": 1435740844,
            "deleted": 1
        },
        "wxImagetxtReply": {
            "id": 19,
            "title": "图文标题",
            "type": 2,
            "shop_id": "5",
            "shop_sub_id": 45,
            "created": 1435736866,
            "modified": 1435740844,
            "deleted": 1,
            "wxImagetxtReplyItems": [
                {
                    "id": 24,
                    "wx_imagetxt_reply_id": 19,
                    "title": "图文标题",
                    "description": "图文的描述",
                    "cdn_path": null,
                    "document_id": "6",
                    "url": "http://baidu.com",
                    "content": "图文的描述",
                    "articles_comments_count": 0,
                    "hits": 0,
                    "likes": 0,
                    "is_top": 2,
                    "is_banner": 2,
                    "shop_id": 5,
                    "shop_sub_id": 45,
                    "release_time": 0,
                    "recommend": null,
                    "created": 1435740784,
                    "modified": 1435740784,
                    "deleted": 1
                }
            ]
        },
        "wxImagetxtReplyItem": [
            {
                "articles_comments_count": 0,
                "hits": 0,
                "likes": 0,
                "is_top": 2,
                "is_banner": 2,
                "release_time": 0,
                "deleted": 1,
                "title": "图文标题",
                "description": "图文的描述",
                "document_id": "6",
                "url": "http://baidu.com",
                "content": "图文的描述",
                "wx_imagetxt_reply_id": 19,
                "shop_id": "5",
                "shop_sub_id": 45,
                "created": 1435740844,
                "modified": 1435740844,
                "id": 25
            }
        ],
        "activity": {
            "id": 59,
            "activity_type": 5,
            "relate_product_type": 1,
            "postage_setting_id": 0,
            "name": "活动标题",
            "desc": "活动描述",
            "sort": "0",
            "expire_type": 1,
            "start_time": "1434180888",
            "end_time": "1434190888",
            "wx_qrcode_id": "",
            "wx_imagetxt_reply_id": 19,
            "share_message_id": 86,
            "shop_id": "5",
            "shop_sub_id": "45",
            "created": 1435736866,
            "modified": 1435740844,
            "deleted": 1
        },
        "wishWall": {
            "id": 15,
            "activity_id": 59,
            "pc_bg_img": "12",
            "wx_bg_img": "13",
            "wx_code_img": "15",
            "need_check": "1",
            "lucky_number": "1,11,111,",
            "lucky_words": "耶，中奖了哈",
            "count": 0,
            "shop_id": "5",
            "shop_sub_id": "45"
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取单条祝福墙活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wish-wall/get-wish-wall
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
    "data": {
        "id": 30,
        "activity_type": 5,
        "relate_product_type": 1,
        "postage_setting_id": 0,
        "name": "活动controller",
        "desc": "sdfsf",
        "sort": 0,
        "expire_type": 1,
        "start_time": 1434180888,
        "end_time": 1434190888,
        "wx_qrcode_id": null,
        "shop_id": 5,
        "shop_sub_id": 45,
        "created": 1434631992,
        "modified": 1434632196,
        "deleted": 1,
        "wishWall": {
            "id": 8,
            "activity_id": 30,
            "pc_bg_img": "12",
            "wx_bg_img": "13",
            "wx_code_img": "15",
            "need_check": 1,
            "lucky_number": "1,11,111,",
            "lucky_words": "耶，中奖了哈",
            "count": 0,
            "shop_id": 5,
            "shop_sub_id": 45
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取祝福墙活动列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wish-wall/find-wish-wall
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
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
            "id": 2,
            "activity_type": 5,
            "relate_product_type": 1,
            "postage_setting_id": 0,
            "name": "wishWall",
            "desc": "dslkfjslfj;sdfj",
            "sort": 0,
            "expire_type": null,
            "start_time": null,
            "end_time": null,
            "wx_qrcode_id": null,
            "shop_id": 5,
            "shop_sub_id": 43,
            "created": 1434180888,
            "modified": 1434180888,
            "deleted": 1,
            "wishWall": {
                "id": 2,
                "activity_id": 2,
                "pc_bg_img": "12",
                "wx_bg_img": "13",
                "wx_code_img": "13",
                "need_check": 1,
                "lucky_number": ",1,11,111,",
                "lucky_words": "中奖祝福语",
                "count": 2,
                "shop_id": 5,
                "shop_sub_id": 20
            }
        },......

    ],
    "page": {
        "per_page": 20,
        "total_count": 8,
        "current_page": 0,
        "total_page": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __启用祝福墙活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wish-wall/enable-wish-wall
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


## __禁用祝福墙活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wish-wall/disable-wish-wall
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


## __删除祝福墙活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wish-wall/delete-wish-wall
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




## __创建祝福语__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wish-wall/create-wish-words
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| activity_id | 是 | Integer(11) | 活动id |
| uid | 是 | Integer(11) | 用户id |
| content | 是 | string(50) | 祝福语 |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 7,
        "wish_wall_id": 4,
        "content": ":-)",
        "floor": 4,
        "is_show": 2,
        "uid": "123",
        "is_win": 2,
        "shop_id": 5,
        "shop_sub_id": "43"
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __展示祝福语__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wish-wall/show-wish-words
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 祝福语id |
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

## __不展示祝福语__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wish-wall/not-show-wish-words
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 祝福语id |
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

## __获取祝福语详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wish-wall/get-wish-words
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 祝福语id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 6,
        "wish_wall_id": 4,
        "content": ":-)",
        "floor": 3,
        "is_show": 2,
        "uid": 123,
        "is_win": 2,
        "shop_id": 5,
        "shop_sub_id": 43
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __查找祝福语列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wish-wall/find-wish-words
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 祝福语id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": [
        {
            "id": 4,
            "wish_wall_id": 4,
            "content": ":-)",
            "floor": 1,
            "is_show": 2,
            "uid": 123,
            "is_win": 1,
            "shop_id": 5,
            "shop_sub_id": 43
        }
    ]....,
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
