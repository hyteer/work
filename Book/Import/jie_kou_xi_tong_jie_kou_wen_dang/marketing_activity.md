## __新增抽奖活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/marketing-activity/create-marketing-activity
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| activity_name | 是 | String(250) | 活动名称 |
| template | 是 | Integer(4) | 1-大转盘2-刮刮乐3-翻卡牌4-砸金蛋5-摇一摇 |
| start_time | 是 | Integer(11) | 活动开始时间 |
| end_time | 是 | Integer(11) | 活动结束时间 |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| wx_qrcode_id | 否 | Integer(11) | 活动二维码 |
| buy_limit | 否 | Integer(2) | 抽奖对象 1:所有用户,2:购买过商品的用户 |
| limit_type | 否 | Integer(1) | 1-每天限制次数类型，2-限制总次数类型 |
| try_limit | 否 | Integer(3) | 限制次数 |
| expiry_time | 否 | Integer(10) | 兑奖结束时间 |
| winning_limit | 否 | Integer(11) | 1只能一次中奖，2可多次中奖 |
| share_award | 否 | Integer(4) | 分享赠送抽奖机会 1:开启，2:关闭 |
| share_award_limit | 否 | Integer(11) | 分享赠送抽奖机会次数 0或不填无限制|
| sorry_word | 否 | string(100) | 未中奖感谢词 |
| logo_img | 否 | string(150) | logo图片 |
| activity_desc | 否 | string(300) | 其他补充活动说明 |
| use_points | 否 | Integer(4) | 使用积分兑换抽奖机会 1:开启，2:关闭 |
| points_num | 否 | Integer(11) | 使用积分兑换抽奖机会次数 0或不填无限制|
| points_count | 否 | Integer(11) | 兑换一次抽奖机会使用积分数|
| is_subscribe | 否 | Integer(2) | 是否要关注1.是、2否|
| share_type | 是 | Integer(4) |显示和分享模式（1.显示且能分享、2.不能显示且能分享、3.不能显示且不能分享）|
| extend.level | 是 | Integer(2) | 12张图片 |
| extend.key | 是 | string(50) | 键 |
| extend.value | 否 | string | 值 |
| shareMessage.title | 否 | String(100) | 分享标题 |
| shareMessage.desc | 否 | String(100) | 分享描述 |
| shareMessage.pic_id | 否 | Integer(11) | document_lib表外键 |
| notstartNews.title | 否 | String(100) | 分享标题 |
| notstartNews.description | 否 | String(100) | 分享描述 |
| notstartNews.document_id | 否| Integer(11) | document_lib表外键 |
| startNews.title | 否 | String(100) | 分享标题 |
| startNews.description | 否 | String(100) | 分享描述 |
| startNews.document_id | 否| Integer(11) | document_lib表外键 |
| endNews.title | 否 | String(100) | 分享标题 |
| endNews.description | 否 | String(100) | 分享描述 |
| endNews.document_id | 否| Integer(11) | document_lib表外键 |
| prize.level | 是| Integer(2) | 奖项等级，例如 0表示未中奖，1表示一等奖，2表示二等奖 |
| prize.name | 是| String(80) | 奖项名称 |
| prize.num | 否| Integer(8) | 奖品数量 |
| prize.type | 否| Integer(11) | 类型 1:普通奖品 2：优惠券 3:积分 4:红包 |
| prize.type_id | 否| Integer(11) | 卡劵Id/红包ID |
| prize.probability | 是| number(10,3) | 中奖概率,三位小数 |
| prize.prize_pic | 否| String(150) | 图片 |

* **注意：prize 必须填写**
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "marketingActivity":{
            "share_type":1,
            "template":2,
            "buy_limit":1,
            "activity_name":"刮刮乐",
            "activity_desc":"",
            "start_time":1222,
            "end_time":1333,
            "limit_type":2,
            "try_limit":0,
            "expiry_time":0,
            "sorry_word":"",
            "winning_limit":1,
            "wx_qrcode_id":0,
            "logo_img":"",
            "share_award":2,
            "share_award_limit":0,
            "share_message_id":0,
            "wx_imagetxt_notstart_id":0,
            "wx_imagetxt_start_id":0,
            "wx_imagetxt_end_id":0,
            "use_points":2,
            "points_count":0,
            "points_num":0,
            "shop_id":5,
            "shop_sub_id":43,
            "is_subscribe":2,
            "created":1437099964,
            "modified":1437099964,
            "deleted":1,
            "id":11
        },
        "prize":[
            {
                "level":0,
                "name":"未中奖",
                "num":0,
                "type":1,
                "shop_id":5,
                "shop_sub_id":43,
                "created":1437099964,
                "modified":1437099964,
                "probability":70,
                "marketing_activity_id":11,
                "id":17
            },
            {
                "level":1,
                "name":"一等奖",
                "num":0,
                "type":1,
                "shop_id":5,
                "shop_sub_id":43,
                "created":1437099964,
                "modified":1437099964,
                "probability":9.798,
                "marketing_activity_id":11,
                "id":18
            },
            {
                "level":2,
                "name":"二等奖",
                "num":0,
                "type":1,
                "shop_id":5,
                "shop_sub_id":43,
                "created":1437099964,
                "modified":1437099964,
                "probability":10.2,
                "marketing_activity_id":11,
                "id":19
            },
            {
                "level":3,
                "name":"三等奖",
                "num":0,
                "type":1,
                "shop_id":5,
                "shop_sub_id":43,
                "created":1437099964,
                "modified":1437099964,
                "probability":10.002,
                "marketing_activity_id":11,
                "id":20
            }
        ]
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __更新抽奖活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/marketing-activity/update-marketing-activity
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | nteger(11) | 活动ID |
| activity_name | 否 | String(250) | 活动名称 |
| template | 否 | Integer(4) | 1-大转盘2-刮刮乐3-翻卡牌4-砸金蛋5-摇一摇 |
| start_time | 否 | Integer(11) | 活动开始时间 |
| end_time | 否 | Integer(11) | 活动结束时间 |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| wx_qrcode_id | 否 | Integer(11) | 活动二维码 |
| buy_limit | 否 | Integer(2) | 抽奖对象 1:所有用户,2:购买过商品的用户 |
| limit_type | 否 | Integer(1) | 1-每天限制次数类型，2-限制总次数类型 |
| try_limit | 否 | Integer(3) | 限制次数 |
| expiry_time | 否 | Integer(10) | 兑奖结束时间 |
| winning_limit | 否 | Integer(11) | 1只能一次中奖，2可多次中奖 |
| share_award | 否 | Integer(4) | 赠送抽奖机会 1:开启，2:关闭 |
| share_award_limit | 否 | Integer(11) | 分享赠送抽奖机会次数 0或不填无限制|
| sorry_word | 否 | string(100) | 未中奖感谢词 |
| logo_img | 否 | string(150) | logo图片 |
| activity_desc | 否 | string(300) | 其他补充活动说明 |
| use_points | 否 | Integer(4) | 使用积分兑换抽奖机会 1:开启，2:关闭 |
| points_num | 否 | Integer(11) | 使用积分兑换抽奖机会次数 0或不填无限制|
| points_count | 否 | Integer(11) | 兑换一次抽奖机会使用积分数|
| is_subscribe | 否 | Integer(2) | 是否要关注1.是、2否|
| share_type | 是 | Integer(4) |显示和分享模式（1.显示且能分享、2.不能显示且能分享、3.不能显示且不能分享）|
| extend.level | 是 | Integer(2) | 12张图片 |
| extend.key | 是 | string(50) | 键 |
| extend.value | 否 | string | 值 |
| shareMessage.title | 否 | String(100) | 分享标题 |
| shareMessage.desc | 否 | String(100) | 分享描述 |
| shareMessage.pic_id | 否 | Integer(11) | document_lib表外键 |
| notstartNews.title | 否 | String(100) | 分享标题 |
| notstartNews.description | 否 | String(100) | 分享描述 |
| notstartNews.document_id | 否| Integer(11) | document_lib表外键 |
| startNews.title | 否 | String(100) | 分享标题 |
| startNews.description | 否 | String(100) | 分享描述 |
| startNews.document_id | 否| Integer(11) | document_lib表外键 |
| endNews.title | 否 | String(100) | 分享标题 |
| endNews.description | 否 | String(100) | 分享描述 |
| endNews.document_id | 否| Integer(11) | document_lib表外键 |
| prize.level | 是| Integer(2) | 奖项等级，例如 0表示未中奖，1表示一等奖，2表示二等奖 |
| prize.name | 是| String(80) | 奖项名称 |
| prize.num | 否| Integer(8) | 奖品数量 |
| prize.type | 否| Integer(11) | 类型 1:普通奖品 2：优惠券 3:积分 4:红包 |
| prize.type_id | 否| Integer(11) | 卡劵Id/红包ID |
| prize.probability | 是| number(10,3) | 中奖概率,三位小数 |
| prize.prize_pic | 否| String(150) | 图片 |

* **注意：prize 必须填写**
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __参加活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/marketing-activity/join-activity
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| uid | 是 | Integer(11) | 用户id |
| shop_id | 是 | Integer(11) | 商家id |
| id | 是 | Integer(11) | 活动ID |
| from_uid | 否 | Integer(11) | 分享的用户id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "shareMessage":{
            "shop_sub_id":0,
            "title":"玩大转盘，轻轻一转好礼不断！",
            "pic_id":"9",
            "desc":"玩抽奖大转盘，千万奖品等你来，百分百赢中奖哟~",
            "shop_id":30,
            "created":1454479091,
            "modified":1454479091,
            "deleted":1,
            "id":1900
        },
        "wxImagetxtReply":{
            "type":2,
            "is_wsh":2,
            "shop_sub_id":0,
            "shop_id":30,
            "title":"极速大转盘，幸运转转转~",
            "created":1454479091,
            "modified":1454479091,
            "deleted":1,
            "id":1751
        },
        "wxImagetxtReplyItems":[
            {
                "link_param":"",
                "show_cover_pic":2,
                "author":"",
                "articles_comments_count":0,
                "hits":0,
                "likes":0,
                "is_top":2,
                "is_banner":2,
                "shop_sub_id":0,
                "release_time":0,
                "deleted":1,
                "title":"极速大转盘，幸运转转转~",
                "description":"亲，点击进入活动主页，意外惊喜等着你！",
                "document_id":"3",
                "url":null,
                "content":"亲，点击进入活动主页，意外惊喜等着你！",
                "wx_imagetxt_reply_id":1751,
                "shop_id":30,
                "created":1454479091,
                "modified":1454479091,
                "id":2585
            }
        ],
        "prize":[
            {
                "id":790,
                "level":"0",
                "name":"未中奖",
                "num":"0",
                "probability":"74.000",
                "marketing_activity_id":"178",
                "type":"1",
                "type_id":"",
                "prize_pic":null,
                "shop_id":"30",
                "shop_sub_id":"0",
                "created":"1454479076",
                "modified":1454479091
            },
            {
                "id":791,
                "level":"1",
                "name":"AA",
                "num":"12",
                "probability":"2.000",
                "marketing_activity_id":"178",
                "type":"1",
                "type_id":"",
                "prize_pic":"91751",
                "shop_id":"30",
                "shop_sub_id":"0",
                "created":"1454479076",
                "modified":1454479091
            },
            {
                "id":792,
                "level":"2",
                "name":"BB",
                "num":"12",
                "probability":"12.000",
                "marketing_activity_id":"178",
                "type":"1",
                "type_id":"",
                "prize_pic":"91751",
                "shop_id":"30",
                "shop_sub_id":"0",
                "created":"1454479076",
                "modified":1454479091
            },
            {
                "id":793,
                "level":"3",
                "name":"CC",
                "num":"12",
                "probability":"12.000",
                "marketing_activity_id":"178",
                "type":"1",
                "type_id":"",
                "prize_pic":"91751",
                "shop_id":"30",
                "shop_sub_id":"0",
                "created":"1454479076",
                "modified":1454479091
            }
        ],
        "marketingActivity":{
            "id":178,
            "template":"1",
            "buy_limit":"1",
            "activity_name":"活动名称：",
            "activity_desc":"1. 抽奖对象：所有用户； 2. 活动参与人必须关注活动商家微信公众号才能参与活动；（打开强制关注后） 3. #积分可以兑换一次抽奖机会，限制#次； 4. 中奖限制：每人限中奖一次； 5. 本活动最终解释权归XX商家所有。",
            "start_time":"1454651838",
            "end_time":"1455429440",
            "limit_type":"1",
            "try_limit":"12",
            "expiry_time":"1456466272",
            "sorry_word":"",
            "winning_limit":"2",
            "wx_qrcode_id":0,
            "logo_img":"",
            "share_award":"2",
            "share_award_limit":0,
            "share_message_id":1900,
            "wx_imagetxt_notstart_id":0,
            "wx_imagetxt_start_id":1751,
            "wx_imagetxt_end_id":0,
            "use_points":"2",
            "points_count":"0",
            "points_num":"0",
            "shop_id":30,
            "shop_sub_id":0,
            "is_subscribe":"2",
            "created":1454479076,
            "modified":1454479091,
            "deleted":2,
            "share_type":"1",
            "marketingExtends":[

            ],
            "marketingPrizes":[
                {
                    "id":790,
                    "level":0,
                    "name":"未中奖",
                    "num":0,
                    "probability":"74.000",
                    "marketing_activity_id":178,
                    "type":1,
                    "type_id":null,
                    "prize_pic":null,
                    "shop_id":30,
                    "shop_sub_id":0,
                    "created":1454479076,
                    "modified":1454479076
                },
                {
                    "id":791,
                    "level":1,
                    "name":"AA",
                    "num":12,
                    "probability":"2.000",
                    "marketing_activity_id":178,
                    "type":1,
                    "type_id":null,
                    "prize_pic":"91751",
                    "shop_id":30,
                    "shop_sub_id":0,
                    "created":1454479076,
                    "modified":1454479076
                },
                {
                    "id":792,
                    "level":2,
                    "name":"BB",
                    "num":12,
                    "probability":"12.000",
                    "marketing_activity_id":178,
                    "type":1,
                    "type_id":null,
                    "prize_pic":"91751",
                    "shop_id":30,
                    "shop_sub_id":0,
                    "created":1454479076,
                    "modified":1454479076
                },
                {
                    "id":793,
                    "level":3,
                    "name":"CC",
                    "num":12,
                    "probability":"12.000",
                    "marketing_activity_id":178,
                    "type":1,
                    "type_id":null,
                    "prize_pic":"91751",
                    "shop_id":30,
                    "shop_sub_id":0,
                    "created":1454479076,
                    "modified":1454479076
                }
            ]
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __执行抽奖，获取中奖奖品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/marketing-activity/get-marketing-activity-prize
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| activity_id | 是 | Integer(11) | 活动id |
| uid | 是 | Integer(11) | 用户id |
| shop_id | 是 | Integer(11) | 商家id |
| from_uid | 否 | Integer(11) | 分享的用户id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":792,
        "level":2,
        "name":"BB",
        "num":12,
        "probability":"12.000",
        "marketing_activity_id":178,
        "type":1,
        "type_id":null,
        "prize_pic":"91751",
        "shop_id":30,
        "shop_sub_id":0,
        "created":1454479076,
        "modified":1454479277,
        "documentLib":{
            "id":91751,
            "name":"实物奖品默认图片",
            "desc":"实物奖品默认图片",
            "category_id":0,
            "tag_id":1,
            "file_cdn_path":"http://imgcache.vikduo.com/static/463ad47a800772aa84aade7879749216.png",
            "file_type":1,
            "shop_id":0,
            "shop_sub_id":0,
            "created":1453426457,
            "modified":1453426457,
            "deleted":1
        },
        "marketingRecord":{
            "level":2,
            "exchange":2,
            "prize_type":1,
            "shop_id":30,
            "shop_sub_id":0,
            "created":1454479291,
            "modified":1454479291,
            "deleted":1,
            "marketing_activity_id":178,
            "uid":507,
            "prizes_name":"BB",
            "prize_type_id":null,
            "id":1006,
            "redpacket":null,
            "cardInfo":null
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取抽奖剩余次数__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/marketing-activity/get-left-chance-count
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| activity_id | 是 | Integer(11) | 活动id |
| uid | 是 | Integer(11) | 用户id |
| shop_id | 是 | Integer(11) | 商家id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":3
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __增加积分抽奖次数__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/marketing-activity/add-points-chance
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| activity_id | 是 | Integer(11) | 活动id |
| uid | 是 | Integer(11) | 用户id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
<br  />

* **注意：type，如为1，则from_uid必须填写**
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 138,
        "marketing_activity_id": 178,
        "uid": 507,
        "give_num": 11,
        "share_num": 0,
        "point_num": 1,
        "total_num": 1,
        "join_num": 1,
        "from_user_ids": null,
        "is_lock": 2,
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": 1454479291,
        "modified": 1454480324,
        "update_chance_time": 1454479291
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __获取用户抽奖次数记录__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/marketing-activity/get-marketing-chance
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| marketing_activity_id | 是 | Integer(11) | 活动id |
| uid | 是 | Integer(11) | 用户id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
<br  />

* **注意：type，如为1，则from_uid必须填写**
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    {
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 20,
        "marketing_activity_id": 65,
        "uid": 163,
        "give_num": 8,
        "share_num": 0,
        "point_num": 0,
        "total_num": 0,
        "join_num": 7,
        "from_user_ids": null,
        "is_lock": 2,
        "shop_id": 5,
        "shop_sub_id": 43,
        "created": 1439446286,
        "modified": 1439455499,
        "update_chance_time": 1454479291
    }
}
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取有效的活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/marketing-activity/get-valid-activity
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| activity_id | 是 | Integer(11) | 活动ID |
| shop_id | 是 | Integer(11) | 商家id |

<br  />
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


## __获取活动详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/marketing-activity/get-marketing-activity
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":178,
        "template":1,
        "buy_limit":1,
        "activity_name":"活动名称：",
        "activity_desc":"1. 抽奖对象：所有用户； 2. 活动参与人必须关注活动商家微信公众号才能参与活动；（打开强制关注后） 3. #积分可以兑换一次抽奖机会，限制#次； 4. 中奖限制：每人限中奖一次； 5. 本活动最终解释权归XX商家所有。",
        "start_time":1454480317,
        "end_time":1455429440,
        "limit_type":1,
        "try_limit":12,
        "expiry_time":1456466272,
        "sorry_word":"",
        "winning_limit":2,
        "wx_qrcode_id":0,
        "logo_img":"",
        "share_award":2,
        "share_award_limit":0,
        "share_message_id":1902,
        "wx_imagetxt_notstart_id":0,
        "wx_imagetxt_start_id":1753,
        "wx_imagetxt_end_id":0,
        "use_points":1,
        "points_count":1,
        "points_num":3,
        "shop_id":30,
        "shop_sub_id":0,
        "is_subscribe":2,
        "created":1454479076,
        "modified":1454480319,
        "deleted":1,
        "share_type":1,
        "marketingExtends":[

        ],
        "marketingPrizes":[
            {
                "id":790,
                "level":0,
                "name":"未中奖",
                "num":0,
                "probability":"74.000",
                "marketing_activity_id":178,
                "type":1,
                "type_id":null,
                "prize_pic":null,
                "shop_id":30,
                "shop_sub_id":0,
                "created":1454479076,
                "modified":1454480319,
                "documentLib":[

                ]
            },
            {
                "id":791,
                "level":1,
                "name":"AA",
                "num":12,
                "probability":"2.000",
                "marketing_activity_id":178,
                "type":1,
                "type_id":null,
                "prize_pic":"91751",
                "shop_id":30,
                "shop_sub_id":0,
                "created":1454479076,
                "modified":1454480319,
                "documentLib":{
                    "id":91751,
                    "name":"实物奖品默认图片",
                    "desc":"实物奖品默认图片",
                    "category_id":0,
                    "tag_id":1,
                    "file_cdn_path":"http://imgcache.vikduo.com/static/463ad47a800772aa84aade7879749216.png",
                    "file_type":1,
                    "shop_id":0,
                    "shop_sub_id":0,
                    "created":1453426457,
                    "modified":1453426457,
                    "deleted":1
                }
            },
            {
                "id":792,
                "level":2,
                "name":"BB",
                "num":12,
                "probability":"12.000",
                "marketing_activity_id":178,
                "type":1,
                "type_id":null,
                "prize_pic":"91751",
                "shop_id":30,
                "shop_sub_id":0,
                "created":1454479076,
                "modified":1454480319,
                "documentLib":{
                    "id":91751,
                    "name":"实物奖品默认图片",
                    "desc":"实物奖品默认图片",
                    "category_id":0,
                    "tag_id":1,
                    "file_cdn_path":"http://imgcache.vikduo.com/static/463ad47a800772aa84aade7879749216.png",
                    "file_type":1,
                    "shop_id":0,
                    "shop_sub_id":0,
                    "created":1453426457,
                    "modified":1453426457,
                    "deleted":1
                }
            },
            {
                "id":793,
                "level":3,
                "name":"CC",
                "num":12,
                "probability":"12.000",
                "marketing_activity_id":178,
                "type":1,
                "type_id":null,
                "prize_pic":"91751",
                "shop_id":30,
                "shop_sub_id":0,
                "created":1454479076,
                "modified":1454480319,
                "documentLib":{
                    "id":91751,
                    "name":"实物奖品默认图片",
                    "desc":"实物奖品默认图片",
                    "category_id":0,
                    "tag_id":1,
                    "file_cdn_path":"http://imgcache.vikduo.com/static/463ad47a800772aa84aade7879749216.png",
                    "file_type":1,
                    "shop_id":0,
                    "shop_sub_id":0,
                    "created":1453426457,
                    "modified":1453426457,
                    "deleted":1
                }
            }
        ],
        "startImageTxt":{
            "id":1753,
            "title":"极速大转盘，幸运转转转~",
            "type":2,
            "is_wsh":2,
            "media_id":null,
            "shop_id":30,
            "shop_sub_id":0,
            "created":1454480319,
            "modified":1454480319,
            "deleted":1,
            "wxImagetxtReplyItems":[
                {
                    "id":2587,
                    "media_id":null,
                    "wx_imagetxt_reply_id":1753,
                    "title":"极速大转盘，幸运转转转~",
                    "description":"亲，点击进入活动主页，意外惊喜等着你！",
                    "cdn_path":null,
                    "document_id":"3",
                    "link_type":null,
                    "link_param":"",
                    "url":null,
                    "wx_url":null,
                    "show_cover_pic":2,
                    "author":"",
                    "content":"亲，点击进入活动主页，意外惊喜等着你！",
                    "articles_comments_count":0,
                    "hits":0,
                    "likes":0,
                    "is_top":2,
                    "is_banner":2,
                    "shop_id":30,
                    "shop_sub_id":0,
                    "release_time":0,
                    "recommend":null,
                    "created":1454480319,
                    "modified":1454480319,
                    "deleted":1,
                    "documentLib":{
                        "id":3,
                        "name":"大转盘默认图文图片",
                        "desc":"大转盘默认图文图片",
                        "category_id":0,
                        "tag_id":1,
                        "file_cdn_path":"http://imgcache.vikduo.com/static/7f9d9cafe171ec26ff256336621c1623.png",
                        "file_type":1,
                        "shop_id":0,
                        "shop_sub_id":0,
                        "created":1442239224,
                        "modified":1442239224,
                        "deleted":1
                    }
                }
            ]
        },
        "shareMessage":{
            "id":1902,
            "title":"玩大转盘，轻轻一转好礼不断！",
            "desc":"玩抽奖大转盘，千万奖品等你来，百分百赢中奖哟~",
            "pic_id":9,
            "shop_id":30,
            "shop_sub_id":0,
            "created":1454480319,
            "modified":1454480319,
            "deleted":1,
            "documentLib":{
                "id":9,
                "name":"大转盘默认分享图片",
                "desc":"大转盘默认分享图片",
                "category_id":0,
                "tag_id":1,
                "file_cdn_path":"http://imgcache.vikduo.com/static/04680c4e83fad88436fc27a0b9a497a8.png",
                "file_type":1,
                "shop_id":0,
                "shop_sub_id":0,
                "created":1442239226,
                "modified":1442239226,
                "deleted":1
            }
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取活动列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/marketing-activity/find-marketing-activity-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| template | 否 | Integer(4) | 活动类型 |
| deleted | 否 | Integer(4) | 状态 |
| activity_name | 否 | String(100) | 活动名称 |
| ids | 否 | Array | id数组 |
* **注意：sort排序可选字段['id']**

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":[
        {
            "id":178,
            "template":1,
            "buy_limit":1,
            "activity_name":"活动名称：",
            "activity_desc":"1. 抽奖对象：所有用户； 2. 活动参与人必须关注活动商家微信公众号才能参与活动；（打开强制关注后） 3. #积分可以兑换一次抽奖机会，限制#次； 4. 中奖限制：每人限中奖一次； 5. 本活动最终解释权归XX商家所有。",
            "start_time":1454480317,
            "end_time":1455429440,
            "limit_type":1,
            "try_limit":12,
            "expiry_time":1456466272,
            "sorry_word":"",
            "winning_limit":2,
            "wx_qrcode_id":0,
            "logo_img":"",
            "share_award":2,
            "share_award_limit":0,
            "share_message_id":1902,
            "wx_imagetxt_notstart_id":0,
            "wx_imagetxt_start_id":1753,
            "wx_imagetxt_end_id":0,
            "use_points":1,
            "points_count":1,
            "points_num":3,
            "shop_id":30,
            "shop_sub_id":0,
            "is_subscribe":2,
            "created":1454479076,
            "modified":1454480319,
            "deleted":1,
            "share_type":1,
            "marketingExtends":[

            ],
            "marketingPrizes":[
                {
                    "id":790,
                    "level":0,
                    "name":"未中奖",
                    "num":0,
                    "probability":"74.000",
                    "marketing_activity_id":178,
                    "type":1,
                    "type_id":null,
                    "prize_pic":null,
                    "shop_id":30,
                    "shop_sub_id":0,
                    "created":1454479076,
                    "modified":1454480319
                },
                {
                    "id":791,
                    "level":1,
                    "name":"AA",
                    "num":12,
                    "probability":"2.000",
                    "marketing_activity_id":178,
                    "type":1,
                    "type_id":null,
                    "prize_pic":"91751",
                    "shop_id":30,
                    "shop_sub_id":0,
                    "created":1454479076,
                    "modified":1454480319
                },
                {
                    "id":792,
                    "level":2,
                    "name":"BB",
                    "num":12,
                    "probability":"12.000",
                    "marketing_activity_id":178,
                    "type":1,
                    "type_id":null,
                    "prize_pic":"91751",
                    "shop_id":30,
                    "shop_sub_id":0,
                    "created":1454479076,
                    "modified":1454480319
                },
                {
                    "id":793,
                    "level":3,
                    "name":"CC",
                    "num":12,
                    "probability":"12.000",
                    "marketing_activity_id":178,
                    "type":1,
                    "type_id":null,
                    "prize_pic":"91751",
                    "shop_id":30,
                    "shop_sub_id":0,
                    "created":1454479076,
                    "modified":1454480319
                }
            ],
            "startImageTxt":{
                "id":1753,
                "title":"极速大转盘，幸运转转转~",
                "type":2,
                "is_wsh":2,
                "media_id":null,
                "shop_id":30,
                "shop_sub_id":0,
                "created":1454480319,
                "modified":1454480319,
                "deleted":1,
                "wxImagetxtItem":{
                    "id":2587,
                    "media_id":null,
                    "wx_imagetxt_reply_id":1753,
                    "title":"极速大转盘，幸运转转转~",
                    "description":"亲，点击进入活动主页，意外惊喜等着你！",
                    "cdn_path":null,
                    "document_id":"3",
                    "link_type":null,
                    "link_param":"",
                    "url":null,
                    "wx_url":null,
                    "show_cover_pic":2,
                    "author":"",
                    "content":"亲，点击进入活动主页，意外惊喜等着你！",
                    "articles_comments_count":0,
                    "hits":0,
                    "likes":0,
                    "is_top":2,
                    "is_banner":2,
                    "shop_id":30,
                    "shop_sub_id":0,
                    "release_time":0,
                    "recommend":null,
                    "created":1454480319,
                    "modified":1454480319,
                    "deleted":1,
                    "documentLib":{
                        "id":3,
                        "name":"大转盘默认图文图片",
                        "desc":"大转盘默认图文图片",
                        "category_id":0,
                        "tag_id":1,
                        "file_cdn_path":"http://imgcache.vikduo.com/static/7f9d9cafe171ec26ff256336621c1623.png",
                        "file_type":1,
                        "shop_id":0,
                        "shop_sub_id":0,
                        "created":1442239224,
                        "modified":1442239224,
                        "deleted":1
                    }
                }
            }
        },
        {.....}
    ],
    "page":{
        "per_page":15,
        "total_count":64,
        "current_page":0,
        "total_page":5
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __删除活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/marketing-activity/general-del
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


## __启用活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/marketing-activity/general-enable
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":175,
        "template":1,
        "buy_limit":1,
        "activity_name":"333",
        "activity_desc":"1. 抽奖对象：所有用户； 2. 活动参与人必须关注活动商家微信公众号才能参与活动；（打开强制关注后） 3. #积分可以兑换一次抽奖机会，限制#次； 4. 中奖限制：每人限中奖一次； 5. 本活动最终解释权归XX商家所有。",
        "start_time":1453714532,
        "end_time":1454060134,
        "limit_type":1,
        "try_limit":111,
        "expiry_time":1454751428,
        "sorry_word":"",
        "winning_limit":1,
        "wx_qrcode_id":0,
        "logo_img":"",
        "share_award":2,
        "share_award_limit":0,
        "share_message_id":1883,
        "wx_imagetxt_notstart_id":0,
        "wx_imagetxt_start_id":1669,
        "wx_imagetxt_end_id":0,
        "use_points":2,
        "points_count":0,
        "points_num":0,
        "shop_id":30,
        "shop_sub_id":0,
        "is_subscribe":2,
        "created":1453714631,
        "modified":1454481422,
        "deleted":1,
        "share_type":1,
        "marketingExtends":[

        ],
        "marketingPrizes":[
            {
                "id":778,
                "level":0,
                "name":"11",
                "num":0,
                "probability":"0.000",
                "marketing_activity_id":175,
                "type":1,
                "type_id":null,
                "prize_pic":null,
                "shop_id":30,
                "shop_sub_id":0,
                "created":1453714631,
                "modified":1453714631,
                "documentLib":[

                ]
            },
            {
                "id":779,
                "level":1,
                "name":"shan",
                "num":11,
                "probability":"100.000",
                "marketing_activity_id":175,
                "type":2,
                "type_id":133,
                "prize_pic":"91750",
                "shop_id":30,
                "shop_sub_id":0,
                "created":1453714631,
                "modified":1453714631,
                "documentLib":{
                    "id":91750,
                    "name":"卡券奖品默认图片",
                    "desc":"卡券奖品默认图片",
                    "category_id":0,
                    "tag_id":1,
                    "file_cdn_path":"http://imgcache.vikduo.com/static/105807a761f0383a34502b0f5776b9ad.png",
                    "file_type":1,
                    "shop_id":0,
                    "shop_sub_id":0,
                    "created":1453426457,
                    "modified":1453426457,
                    "deleted":1
                }
            },
            {
                "id":780,
                "level":2,
                "name":"测试",
                "num":11,
                "probability":"0.000",
                "marketing_activity_id":175,
                "type":4,
                "type_id":65,
                "prize_pic":"91754",
                "shop_id":30,
                "shop_sub_id":0,
                "created":1453714631,
                "modified":1453714631,
                "documentLib":{
                    "id":91754,
                    "name":"红包奖品默认图片",
                    "desc":"红包奖品默认图片",
                    "category_id":0,
                    "tag_id":1,
                    "file_cdn_path":"http://imgcache.vikduo.com/static/68897ebd2baa044df7da38994b106d80.png",
                    "file_type":1,
                    "shop_id":0,
                    "shop_sub_id":0,
                    "created":1453426457,
                    "modified":1453426457,
                    "deleted":1
                }
            },
            {
                "id":781,
                "level":3,
                "name":"cc",
                "num":11,
                "probability":"0.000",
                "marketing_activity_id":175,
                "type":5,
                "type_id":32,
                "prize_pic":"91753",
                "shop_id":30,
                "shop_sub_id":0,
                "created":1453714631,
                "modified":1453714631,
                "documentLib":{
                    "id":91753,
                    "name":"现金红包奖品默认图片",
                    "desc":"现金红包奖品默认图片",
                    "category_id":0,
                    "tag_id":1,
                    "file_cdn_path":"http://imgcache.vikduo.com/static/b5e7d2d43dbac650c358c1c2f77e1188.png",
                    "file_type":1,
                    "shop_id":0,
                    "shop_sub_id":0,
                    "created":1453426457,
                    "modified":1453426457,
                    "deleted":1
                }
            }
        ],
        "startImageTxt":{
            "id":1669,
            "title":"极速大转盘，幸运转转转~",
            "type":2,
            "is_wsh":2,
            "media_id":null,
            "shop_id":30,
            "shop_sub_id":0,
            "created":1453714631,
            "modified":1453714631,
            "deleted":1,
            "wxImagetxtReplyItems":[
                {
                    "id":2209,
                    "media_id":null,
                    "wx_imagetxt_reply_id":1669,
                    "title":"极速大转盘，幸运转转转~",
                    "description":"亲，点击进入活动主页，意外惊喜等着你！",
                    "cdn_path":null,
                    "document_id":"3",
                    "link_type":null,
                    "link_param":"",
                    "url":null,
                    "wx_url":null,
                    "show_cover_pic":2,
                    "author":"",
                    "content":"亲，点击进入活动主页，意外惊喜等着你！",
                    "articles_comments_count":0,
                    "hits":0,
                    "likes":0,
                    "is_top":2,
                    "is_banner":2,
                    "shop_id":30,
                    "shop_sub_id":0,
                    "release_time":0,
                    "recommend":null,
                    "created":1453714631,
                    "modified":1453714631,
                    "deleted":1,
                    "documentLib":{
                        "id":3,
                        "name":"大转盘默认图文图片",
                        "desc":"大转盘默认图文图片",
                        "category_id":0,
                        "tag_id":1,
                        "file_cdn_path":"http://imgcache.vikduo.com/static/7f9d9cafe171ec26ff256336621c1623.png",
                        "file_type":1,
                        "shop_id":0,
                        "shop_sub_id":0,
                        "created":1442239224,
                        "modified":1442239224,
                        "deleted":1
                    }
                }
            ]
        },
        "shareMessage":{
            "id":1883,
            "title":"玩大转盘，轻轻一转好礼不断！",
            "desc":"玩抽奖大转盘，千万奖品等你来，百分百赢中奖哟~",
            "pic_id":9,
            "shop_id":30,
            "shop_sub_id":0,
            "created":1453714631,
            "modified":1453714631,
            "deleted":1,
            "documentLib":{
                "id":9,
                "name":"大转盘默认分享图片",
                "desc":"大转盘默认分享图片",
                "category_id":0,
                "tag_id":1,
                "file_cdn_path":"http://imgcache.vikduo.com/static/04680c4e83fad88436fc27a0b9a497a8.png",
                "file_type":1,
                "shop_id":0,
                "shop_sub_id":0,
                "created":1442239226,
                "modified":1442239226,
                "deleted":1
            }
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __禁用活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/marketing-activity/general-disable
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":175,
        "template":1,
        "buy_limit":1,
        "activity_name":"333",
        "activity_desc":"1. 抽奖对象：所有用户； 2. 活动参与人必须关注活动商家微信公众号才能参与活动；（打开强制关注后） 3. #积分可以兑换一次抽奖机会，限制#次； 4. 中奖限制：每人限中奖一次； 5. 本活动最终解释权归XX商家所有。",
        "start_time":1453714532,
        "end_time":1454060134,
        "limit_type":1,
        "try_limit":111,
        "expiry_time":1454751428,
        "sorry_word":"",
        "winning_limit":1,
        "wx_qrcode_id":0,
        "logo_img":"",
        "share_award":2,
        "share_award_limit":0,
        "share_message_id":1883,
        "wx_imagetxt_notstart_id":0,
        "wx_imagetxt_start_id":1669,
        "wx_imagetxt_end_id":0,
        "use_points":2,
        "points_count":0,
        "points_num":0,
        "shop_id":30,
        "shop_sub_id":0,
        "is_subscribe":2,
        "created":1453714631,
        "modified":1454481422,
        "deleted":2,
        "share_type":1,
        "marketingExtends":[

        ],
        "marketingPrizes":[
            {
                "id":778,
                "level":0,
                "name":"11",
                "num":0,
                "probability":"0.000",
                "marketing_activity_id":175,
                "type":1,
                "type_id":null,
                "prize_pic":null,
                "shop_id":30,
                "shop_sub_id":0,
                "created":1453714631,
                "modified":1453714631,
                "documentLib":[

                ]
            },
            {
                "id":779,
                "level":1,
                "name":"shan",
                "num":11,
                "probability":"100.000",
                "marketing_activity_id":175,
                "type":2,
                "type_id":133,
                "prize_pic":"91750",
                "shop_id":30,
                "shop_sub_id":0,
                "created":1453714631,
                "modified":1453714631,
                "documentLib":{
                    "id":91750,
                    "name":"卡券奖品默认图片",
                    "desc":"卡券奖品默认图片",
                    "category_id":0,
                    "tag_id":1,
                    "file_cdn_path":"http://imgcache.vikduo.com/static/105807a761f0383a34502b0f5776b9ad.png",
                    "file_type":1,
                    "shop_id":0,
                    "shop_sub_id":0,
                    "created":1453426457,
                    "modified":1453426457,
                    "deleted":1
                }
            },
            {
                "id":780,
                "level":2,
                "name":"测试",
                "num":11,
                "probability":"0.000",
                "marketing_activity_id":175,
                "type":4,
                "type_id":65,
                "prize_pic":"91754",
                "shop_id":30,
                "shop_sub_id":0,
                "created":1453714631,
                "modified":1453714631,
                "documentLib":{
                    "id":91754,
                    "name":"红包奖品默认图片",
                    "desc":"红包奖品默认图片",
                    "category_id":0,
                    "tag_id":1,
                    "file_cdn_path":"http://imgcache.vikduo.com/static/68897ebd2baa044df7da38994b106d80.png",
                    "file_type":1,
                    "shop_id":0,
                    "shop_sub_id":0,
                    "created":1453426457,
                    "modified":1453426457,
                    "deleted":1
                }
            },
            {
                "id":781,
                "level":3,
                "name":"cc",
                "num":11,
                "probability":"0.000",
                "marketing_activity_id":175,
                "type":5,
                "type_id":32,
                "prize_pic":"91753",
                "shop_id":30,
                "shop_sub_id":0,
                "created":1453714631,
                "modified":1453714631,
                "documentLib":{
                    "id":91753,
                    "name":"现金红包奖品默认图片",
                    "desc":"现金红包奖品默认图片",
                    "category_id":0,
                    "tag_id":1,
                    "file_cdn_path":"http://imgcache.vikduo.com/static/b5e7d2d43dbac650c358c1c2f77e1188.png",
                    "file_type":1,
                    "shop_id":0,
                    "shop_sub_id":0,
                    "created":1453426457,
                    "modified":1453426457,
                    "deleted":1
                }
            }
        ],
        "startImageTxt":{
            "id":1669,
            "title":"极速大转盘，幸运转转转~",
            "type":2,
            "is_wsh":2,
            "media_id":null,
            "shop_id":30,
            "shop_sub_id":0,
            "created":1453714631,
            "modified":1453714631,
            "deleted":1,
            "wxImagetxtReplyItems":[
                {
                    "id":2209,
                    "media_id":null,
                    "wx_imagetxt_reply_id":1669,
                    "title":"极速大转盘，幸运转转转~",
                    "description":"亲，点击进入活动主页，意外惊喜等着你！",
                    "cdn_path":null,
                    "document_id":"3",
                    "link_type":null,
                    "link_param":"",
                    "url":null,
                    "wx_url":null,
                    "show_cover_pic":2,
                    "author":"",
                    "content":"亲，点击进入活动主页，意外惊喜等着你！",
                    "articles_comments_count":0,
                    "hits":0,
                    "likes":0,
                    "is_top":2,
                    "is_banner":2,
                    "shop_id":30,
                    "shop_sub_id":0,
                    "release_time":0,
                    "recommend":null,
                    "created":1453714631,
                    "modified":1453714631,
                    "deleted":1,
                    "documentLib":{
                        "id":3,
                        "name":"大转盘默认图文图片",
                        "desc":"大转盘默认图文图片",
                        "category_id":0,
                        "tag_id":1,
                        "file_cdn_path":"http://imgcache.vikduo.com/static/7f9d9cafe171ec26ff256336621c1623.png",
                        "file_type":1,
                        "shop_id":0,
                        "shop_sub_id":0,
                        "created":1442239224,
                        "modified":1442239224,
                        "deleted":1
                    }
                }
            ]
        },
        "shareMessage":{
            "id":1883,
            "title":"玩大转盘，轻轻一转好礼不断！",
            "desc":"玩抽奖大转盘，千万奖品等你来，百分百赢中奖哟~",
            "pic_id":9,
            "shop_id":30,
            "shop_sub_id":0,
            "created":1453714631,
            "modified":1453714631,
            "deleted":1,
            "documentLib":{
                "id":9,
                "name":"大转盘默认分享图片",
                "desc":"大转盘默认分享图片",
                "category_id":0,
                "tag_id":1,
                "file_cdn_path":"http://imgcache.vikduo.com/static/04680c4e83fad88436fc27a0b9a497a8.png",
                "file_type":1,
                "shop_id":0,
                "shop_sub_id":0,
                "created":1442239226,
                "modified":1442239226,
                "deleted":1
            }
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取活动记录__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/marketing-activity/get-log
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 1931,
        "uid": 507,
        "marketing_activity_id": 178,
        "type": 1,
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": 1454479291
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取活动记录列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/marketing-activity/find-log-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| activity_id | 否 | Integer(4) | 活动id |

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
            "id": 1801,
            "uid": 775,
            "marketing_activity_id": 175,
            "type": 1,
            "shop_id": 30,
            "shop_sub_id": 0,
            "created": 1453714693
        },
        {....}
    ],
    "page": {
        "per_page": 15,
        "total_count": 10,
        "current_page": 0,
        "total_page": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取活动奖品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/marketing-activity/get-prize
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 778,
        "level": 0,
        "name": "11",
        "num": 0,
        "probability": "0.000",
        "marketing_activity_id": 175,
        "type": 1,
        "type_id": null,
        "prize_pic": null,
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": 1453714631,
        "modified": 1453714631
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取活动奖品列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/marketing-activity/find-prize-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| activity_id | 否 | Integer(4) | 活动id |

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
            "id": 778,
            "level": 0,
            "name": "11",
            "num": 0,
            "probability": "0.000",
            "marketing_activity_id": 175,
            "type": 1,
            "type_id": null,
            "prize_pic": null,
            "shop_id": 30,
            "shop_sub_id": 0,
            "created": 1453714631,
            "modified": 1453714631
        },
        {
            "id": 779,
            "level": 1,
            "name": "shan",
            "num": 11,
            "probability": "100.000",
            "marketing_activity_id": 175,
            "type": 2,
            "type_id": 133,
            "prize_pic": "91750",
            "shop_id": 30,
            "shop_sub_id": 0,
            "created": 1453714631,
            "modified": 1453714631
        },
        {
            "id": 780,
            "level": 2,
            "name": "测试",
            "num": 11,
            "probability": "0.000",
            "marketing_activity_id": 175,
            "type": 4,
            "type_id": 65,
            "prize_pic": "91754",
            "shop_id": 30,
            "shop_sub_id": 0,
            "created": 1453714631,
            "modified": 1453714631
        },
        {
            "id": 781,
            "level": 3,
            "name": "cc",
            "num": 11,
            "probability": "0.000",
            "marketing_activity_id": 175,
            "type": 5,
            "type_id": 32,
            "prize_pic": "91753",
            "shop_id": 30,
            "shop_sub_id": 0,
            "created": 1453714631,
            "modified": 1453714631
        }
    ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __更新中奖记录数据__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/marketing-activity/update-record
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| uid | 是 | Integer(11) | 用户id |
| id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| mobile | 否 | string(20) | 手机号 |
| username | 否 | string(20) | 收货人 |
| address | 否 | string(200) | 地址 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":1006,
        "uid":507,
        "marketing_activity_id":178,
        "level":2,
        "prizes_name":"BB",
        "exchange":2,
        "marketing_winning_source_id":null,
        "mobile":"13412232144",
        "username":"liup",
        "address":"dfsdf",
        "prize_type":1,
        "prize_type_id":null,
        "shop_id":30,
        "shop_sub_id":0,
        "expiry_qrimg":null,
        "created":1454479291,
        "modified":1454482276,
        "deleted":1,
        "wxUserInfos":{
            "id":507,
            "mobile":null,
            "nickname":"Eve",
            "sex":1,
            "province":null,
            "city":null,
            "country":"文莱",
            "headimgurl":"http://wx.qlogo.cn/mmopen/6dejCrP7ubpObELNV9wu3M8c0Arser6U1J1lFqKxRdVmbfAO68hognBK4jcAmms7WJNrSGN2gbslgE1O0peDlK9PPynDGJ6H/0",
            "shop_id":30,
            "shop_sub_id":219,
            "staff_id":69,
            "belong_to_staff_id":69,
            "login_count":141,
            "lastloginip":"127.0.0.1",
            "lastlogintime":1449566993,
            "password":null,
            "type":2,
            "status":1,
            "member_refer":null,
            "scene_id":1,
            "mpath":null,
            "mid":81,
            "agent_id":0,
            "agent_path":null,
            "sign_days":1,
            "sign_time":1451029210,
            "is_subscribe":2,
            "group_id":1,
            "level_id":null,
            "point":959628,
            "wsh_code":null,
            "created":1442224613,
            "modified":1454480324,
            "deleted":1
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __兑换奖品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/marketing-activity/exchange-record
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| staff_id | 是 | Integer(11) | 员工ID |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":1006,
        "uid":507,
        "marketing_activity_id":178,
        "level":2,
        "prizes_name":"BB",
        "exchange":1,
        "marketing_winning_source_id":null,
        "mobile":"13412232144",
        "username":"liup",
        "address":"dfsdf",
        "prize_type":1,
        "prize_type_id":null,
        "shop_id":30,
        "shop_sub_id":0,
        "expiry_qrimg":null,
        "created":1454479291,
        "modified":1454482346,
        "deleted":1,
        "wxUserInfos":{
            "id":507,
            "mobile":null,
            "nickname":"Eve",
            "sex":1,
            "province":null,
            "city":null,
            "country":"文莱",
            "headimgurl":"http://wx.qlogo.cn/mmopen/6dejCrP7ubpObELNV9wu3M8c0Arser6U1J1lFqKxRdVmbfAO68hognBK4jcAmms7WJNrSGN2gbslgE1O0peDlK9PPynDGJ6H/0",
            "shop_id":30,
            "shop_sub_id":219,
            "staff_id":69,
            "belong_to_staff_id":69,
            "login_count":141,
            "lastloginip":"127.0.0.1",
            "lastlogintime":1449566993,
            "password":null,
            "type":2,
            "status":1,
            "member_refer":null,
            "scene_id":1,
            "mpath":null,
            "mid":81,
            "agent_id":0,
            "agent_path":null,
            "sign_days":1,
            "sign_time":1451029210,
            "is_subscribe":2,
            "group_id":1,
            "level_id":null,
            "point":959628,
            "wsh_code":null,
            "created":1442224613,
            "modified":1454480324,
            "deleted":1
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __获取活动中奖列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/marketing-activity/find-record-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| activity_id | 否 | Integer(4) | 活动id |
| level | 否 | Integer(11) | 等级 |
| findName | 否 | String | 搜索名称 |
* **注意：sort排序可选字段['id']**

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":[
        {
            "id":1006,
            "uid":507,
            "marketing_activity_id":178,
            "level":2,
            "prizes_name":"BB",
            "exchange":1,
            "marketing_winning_source_id":null,
            "mobile":"13412232144",
            "username":"liup",
            "address":"dfsdf",
            "prize_type":1,
            "prize_type_id":null,
            "shop_id":30,
            "shop_sub_id":0,
            "expiry_qrimg":null,
            "created":1454479291,
            "modified":1454482346,
            "deleted":1,
            "wxUserInfos":{
                "id":507,
                "mobile":null,
                "nickname":"Eve",
                "sex":1,
                "province":null,
                "city":null,
                "country":"文莱",
                "headimgurl":"http://wx.qlogo.cn/mmopen/6dejCrP7ubpObELNV9wu3M8c0Arser6U1J1lFqKxRdVmbfAO68hognBK4jcAmms7WJNrSGN2gbslgE1O0peDlK9PPynDGJ6H/0",
                "shop_id":30,
                "shop_sub_id":219,
                "staff_id":69,
                "belong_to_staff_id":69,
                "login_count":141,
                "lastloginip":"127.0.0.1",
                "lastlogintime":1449566993,
                "password":null,
                "type":2,
                "status":1,
                "member_refer":null,
                "scene_id":1,
                "mpath":null,
                "mid":81,
                "agent_id":0,
                "agent_path":null,
                "sign_days":1,
                "sign_time":1451029210,
                "is_subscribe":2,
                "group_id":1,
                "level_id":null,
                "point":959628,
                "wsh_code":null,
                "created":1442224613,
                "modified":1454480324,
                "deleted":1
            },
            "marketingActivity":{
                "id":178,
                "template":1,
                "buy_limit":1,
                "activity_name":"活动名称：",
                "activity_desc":"1. 抽奖对象：所有用户； 2. 活动参与人必须关注活动商家微信公众号才能参与活动；（打开强制关注后） 3. #积分可以兑换一次抽奖机会，限制#次； 4. 中奖限制：每人限中奖一次； 5. 本活动最终解释权归XX商家所有。",
                "start_time":1454480317,
                "end_time":1455429440,
                "limit_type":1,
                "try_limit":12,
                "expiry_time":1456466272,
                "sorry_word":"",
                "winning_limit":2,
                "wx_qrcode_id":0,
                "logo_img":"",
                "share_award":2,
                "share_award_limit":0,
                "share_message_id":1902,
                "wx_imagetxt_notstart_id":0,
                "wx_imagetxt_start_id":1753,
                "wx_imagetxt_end_id":0,
                "use_points":1,
                "points_count":1,
                "points_num":3,
                "shop_id":30,
                "shop_sub_id":0,
                "is_subscribe":2,
                "created":1454479076,
                "modified":1454480319,
                "deleted":1,
                "share_type":1
            }
        },
        {.....}
    ],
    "page":{
        "per_page":20,
        "total_count":1,
        "current_page":0,
        "total_page":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __获取中奖记录信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/marketing-activity/get-record
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 中奖记录id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":1006,
        "uid":507,
        "marketing_activity_id":178,
        "level":2,
        "prizes_name":"BB",
        "exchange":1,
        "marketing_winning_source_id":null,
        "mobile":"13412232144",
        "username":"liup",
        "address":"dfsdf",
        "prize_type":1,
        "prize_type_id":null,
        "shop_id":30,
        "shop_sub_id":0,
        "expiry_qrimg":null,
        "created":1454479291,
        "modified":1454482346,
        "deleted":1,
        "wxUserInfos":{
            "id":507,
            "mobile":null,
            "nickname":"Eve",
            "sex":1,
            "province":null,
            "city":null,
            "country":"文莱",
            "headimgurl":"http://wx.qlogo.cn/mmopen/6dejCrP7ubpObELNV9wu3M8c0Arser6U1J1lFqKxRdVmbfAO68hognBK4jcAmms7WJNrSGN2gbslgE1O0peDlK9PPynDGJ6H/0",
            "shop_id":30,
            "shop_sub_id":219,
            "staff_id":69,
            "belong_to_staff_id":69,
            "login_count":141,
            "lastloginip":"127.0.0.1",
            "lastlogintime":1449566993,
            "password":null,
            "type":2,
            "status":1,
            "member_refer":null,
            "scene_id":1,
            "mpath":null,
            "mid":81,
            "agent_id":0,
            "agent_path":null,
            "sign_days":1,
            "sign_time":1451029210,
            "is_subscribe":2,
            "group_id":1,
            "level_id":null,
            "point":959628,
            "wsh_code":null,
            "created":1442224613,
            "modified":1454480324,
            "deleted":1
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __删除中奖记录信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/marketing-activity/general-del-record
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 中奖记录id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
<br  />
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
