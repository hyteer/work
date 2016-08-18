## __新增红包活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet-event/create
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
| activity.shop_sub_id | 是 | Integer(11) | 店铺id |
| activity.wx_qrcode_id | 否 | Integer(11) | 活动二维码 |
| activity.share_type | 是 | Integer(4) |显示和分享模式（1.显示且能分享、2.不能显示且能分享、3.不能显示且不能分享）|
| redPacketEvent.type | 是 | Integer(4) | 1.群红包、2.接龙红包 |
| redPacketEvent.red_packet_id | 是 | Integer(11) | 红包表外键 |
| redPacketEvent.red_packet_num | 是 | Integer(11) | 红包个数 |
| redPacketEvent.num_per_packet | 否 | Integer(11) | 人数/每个红包 |
| redPacketEvent.is_attention | 否 | Integer(11) | 是否强制关注1.是、2.否 |
| shareMessage.title | 否 | String(100) | 分享标题 |
| shareMessage.desc | 否 | String(100) | 分享描述 |
| shareMessage.pic_id | 否 | Integer(11) | document_lib表外键 |
| news.title | 否 | String(100) | 分享标题 |
| news.description | 否 | String(100) | 分享描述 |
| news.document_id | 否 | Integer(11) | document_lib表外键 |

* **注意：type，如为1，则num_per_packet必须填写**
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode":0,
    "errmsg":"ok",
    "data":{
        "activity":{
            "relate_product_type":1,
            "postage_setting_id":0,
            "expire_type":1,
            "wx_imagetxt_reply_id":0,
            "share_message_id":0,
            "name":"test2222",
            "start_time":2,
            "end_time":2,
            "shop_id":5,
            "shop_sub_id":43,
            "activity_type":6,
            "created":1436239222,
            "modified":1436239222,
            "deleted":1,
            "id":146
        },
        "redPacketEvent":{
            "type":1,
            "is_attention":2,
            "red_packet_id":1,
            "red_packet_num":10,
            "num_per_packet":2,
            "shop_id":5,
            "shop_sub_id":43,
            "activity_id":146,
            "id":1
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __修改红包活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet-event/to-update
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| activity.id | 是 | Integer(11) | 活动id |
| activity.name | 否 | String(250) | 活动名称 |
| activity.desc | 否 | String(500) | 活动描述/规则 |
| activity.sort | 否 | Integer(11) | 排序 |
| activity.end_time | 否 | Integer(11) | 活动结束时间 |
| activity.shop_id | 是 | Integer(11) | 商家id |
| activity.wx_qrcode_id | 否 | Integer(11) | 活动二维码 |
| activity.share_type | 是 | Integer(4) |显示和分享模式（1.显示且能分享、2.不能显示且能分享、3.不能显示且不能分享）|
| redPacketEvent.id | 是 | Integer(4) | 红包活动id |
| redPacketEvent.is_attention | 否 | Integer(11) | 是否强制关注1.是、2.否 |
| shareMessage.title | 否 | String(100) | 分享标题 |
| shareMessage.desc | 否 | String(100) | 分享描述 |
| shareMessage.pic_id | 否 | Integer(11) | document_lib表外键 |
| news.title | 否 | String(100) | 分享标题 |
| news.description | 否 | String(100) | 分享描述 |
| news.document_id | 否 | Integer(11) | document_lib表外键 |

<br  /><br  />
提示：shareMessage、news非必填项。
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "activity":{
            "id":146,
            "activity_type":6,
            "relate_product_type":1,
            "postage_setting_id":0,
            "name":"test2222",
            "desc":null,
            "sort":null,
            "expire_type":1,
            "start_time":2,
            "end_time":2,
            "wx_qrcode_id":null,
            "wx_imagetxt_reply_id":0,
            "share_message_id":0,
            "shop_id":5,
            "shop_sub_id":43,
            "created":1436239222,
            "modified":1436240057,
            "deleted":1,
            "redPacketEvent":{
                "id":1,
                "activity_id":146,
                "type":1,
                "red_packet_id":1,
                "num_per_packet":2,
                "red_packet_num":10,
                "is_attention":1,
                "shop_id":5,
                "shop_sub_id":43
            }
        },
        "redPacketEvent":{
            "id":1,
            "activity_id":146,
            "type":1,
            "red_packet_id":1,
            "num_per_packet":2,
            "red_packet_num":10,
            "is_attention":1,
            "shop_id":5,
            "shop_sub_id":43
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取红包活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet-event/get
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动的id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| type | 否 | Integer(4) | 类型 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":660,
        "activity_type":6,
        "relate_product_type":1,
        "postage_setting_id":0,
        "name":"gdfg",
        "desc":"1. 活动时间：#年#月#日#时 至 #年#月#日#时； 2. 用户进入活动主页抢群红包，分享给好友瓜分群红包，瓜分到的红包金额自动发放到用户的商城账户； 3. 用户必须关注微信公众号才能抢群红包；（打开强制关注后）； 4. 每个用户只能发起一次活动，但可以瓜分不同用户转发的群红包； 5. 瓜分群红包，先到先得，该群红包分完为止； 6. 本活动最终解释权归XX商家所有。",
        "sort":null,
        "expire_type":1,
        "start_time":1453799521,
        "end_time":1454058721,
        "wx_qrcode_id":null,
        "wx_imagetxt_reply_id":1660,
        "share_message_id":1874,
        "shop_id":30,
        "shop_sub_id":0,
        "created":1453713167,
        "modified":1453713167,
        "deleted":2,
        "share_type":1,
        "redPacketEvent":{
            "id":144,
            "activity_id":660,
            "type":1,
            "red_packet_id":65,
            "num_per_packet":10,
            "red_packet_num":10,
            "is_attention":2,
            "shop_id":30,
            "shop_sub_id":0,
            "redPacket":{
                "id":65,
                "name":"测试",
                "type":1,
                "total_amount":10000,
                "order_limit":1000,
                "start_time":1453685438,
                "end_time":1454549440,
                "remark":"广东核电",
                "shop_id":30,
                "shop_sub_id":0,
                "created":1453685488,
                "modified":1453685488,
                "deleted":1
            }
        },
        "shareMessage":{
            "id":1874,
            "title":"拼的是手气，抢的是红包~",
            "desc":"#商家店名#发红包啦，不要白不要啊！",
            "pic_id":10,
            "shop_id":30,
            "shop_sub_id":0,
            "created":1453713167,
            "modified":1453713167,
            "deleted":1,
            "documentLib":{
                "id":10,
                "name":"群红包活动默认分享图片",
                "desc":"群红包活动默认分享图片",
                "category_id":0,
                "tag_id":1,
                "file_cdn_path":"http://imgcache.vikduo.com/static/d939802d74dc39989f659a20c92fcc8e.png",
                "file_type":1,
                "shop_id":0,
                "shop_sub_id":0,
                "created":1442239227,
                "modified":1442239227,
                "deleted":1
            }
        },
        "news":{
            "id":1660,
            "title":"拼的是手气，抢的是红包~",
            "type":2,
            "is_wsh":2,
            "media_id":null,
            "shop_id":30,
            "shop_sub_id":0,
            "created":1453713167,
            "modified":1453713167,
            "deleted":1,
            "wxImagetxtReplyItems":[
                {
                    "id":2200,
                    "media_id":null,
                    "wx_imagetxt_reply_id":1660,
                    "title":"拼的是手气，抢的是红包~",
                    "description":"亲，点击进入活动主页，意外惊喜等着你！",
                    "cdn_path":null,
                    "document_id":"4",
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
                    "created":1453713167,
                    "modified":1453713167,
                    "deleted":1,
                    "documentLib":{
                        "id":4,
                        "name":"群红包活动默认图文图片",
                        "desc":"群红包活动默认图文图片",
                        "category_id":0,
                        "tag_id":1,
                        "file_cdn_path":"http://imgcache.vikduo.com/static/129827dfecdb16549f1be8986e9013bc.png",
                        "file_type":1,
                        "shop_id":0,
                        "shop_sub_id":0,
                        "created":1442239224,
                        "modified":1442239224,
                        "deleted":1
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


## __获取红包活动列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet-event/find-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| deleted | 否 | Integer(2) | 状态1.启用、2.禁用 |
| countFlag | 否 | boolean | true/false 是否返回派发统计信息|
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| name | 否 | String(100) | 活动名称 |
| ids | 否 | Array | id数组 |
* **注意：sort排序可选字段['id']**

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "0":{
            "id":660,
            "activity_type":6,
            "relate_product_type":1,
            "postage_setting_id":0,
            "name":"gdfg",
            "desc":"1. 活动时间：#年#月#日#时 至 #年#月#日#时； 2. 用户进入活动主页抢群红包，分享给好友瓜分群红包，瓜分到的红包金额自动发放到用户的商城账户； 3. 用户必须关注微信公众号才能抢群红包；（打开强制关注后）； 4. 每个用户只能发起一次活动，但可以瓜分不同用户转发的群红包； 5. 瓜分群红包，先到先得，该群红包分完为止； 6. 本活动最终解释权归XX商家所有。",
            "sort":null,
            "expire_type":1,
            "start_time":1453799521,
            "end_time":1454058721,
            "wx_qrcode_id":null,
            "wx_imagetxt_reply_id":1660,
            "share_message_id":1874,
            "shop_id":30,
            "shop_sub_id":0,
            "created":1453713167,
            "modified":1453713167,
            "deleted":2,
            "share_type":1,
            "redPacketEvent":{
                "id":144,
                "activity_id":660,
                "type":1,
                "red_packet_id":65,
                "num_per_packet":10,
                "red_packet_num":10,
                "is_attention":2,
                "shop_id":30,
                "shop_sub_id":0,
                "redPacket":{
                    "id":65,
                    "name":"测试",
                    "type":1,
                    "total_amount":10000,
                    "order_limit":1000,
                    "start_time":1453685438,
                    "end_time":1454549440,
                    "remark":"广东核电",
                    "shop_id":30,
                    "shop_sub_id":0,
                    "created":1453685488,
                    "modified":1453685488,
                    "deleted":1
                }
            },
            "news":{
                "id":1660,
                "title":"拼的是手气，抢的是红包~",
                "type":2,
                "is_wsh":2,
                "media_id":null,
                "shop_id":30,
                "shop_sub_id":0,
                "created":1453713167,
                "modified":1453713167,
                "deleted":1,
                "wxImagetxtReplyItems":[
                    {
                        "id":2200,
                        "media_id":null,
                        "wx_imagetxt_reply_id":1660,
                        "title":"拼的是手气，抢的是红包~",
                        "description":"亲，点击进入活动主页，意外惊喜等着你！",
                        "cdn_path":null,
                        "document_id":"4",
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
                        "created":1453713167,
                        "modified":1453713167,
                        "deleted":1,
                        "documentLib":{
                            "id":4,
                            "name":"群红包活动默认图文图片",
                            "desc":"群红包活动默认图文图片",
                            "category_id":0,
                            "tag_id":1,
                            "file_cdn_path":"http://imgcache.vikduo.com/static/129827dfecdb16549f1be8986e9013bc.png",
                            "file_type":1,
                            "shop_id":0,
                            "shop_sub_id":0,
                            "created":1442239224,
                            "modified":1442239224,
                            "deleted":1
                        }
                    }
                ]
            }
        },
        {.....}
    "page":{
        "per_page":15,
        "total_count":17,
        "current_page":0,
        "total_page":2
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __删除红包活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet-event/general-del
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



## __开启红包活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet-event/general-enable
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
    "data":{
        "id":569,
        "activity_type":6,
        "relate_product_type":1,
        "postage_setting_id":0,
        "name":"我都是",
        "desc":"wdsa",
        "sort":null,
        "expire_type":1,
        "start_time":1449114377,
        "end_time":1450755977,
        "wx_qrcode_id":null,
        "wx_imagetxt_reply_id":1321,
        "share_message_id":1420,
        "shop_id":30,
        "shop_sub_id":0,
        "created":1448941780,
        "modified":1454469241,
        "deleted":1,
        "share_type":1,
        "redPacketEvent":{
            "id":133,
            "activity_id":569,
            "type":1,
            "red_packet_id":62,
            "num_per_packet":10,
            "red_packet_num":10,
            "is_attention":2,
            "shop_id":30,
            "shop_sub_id":0,
            "redPacket":{
                "id":62,
                "name":"wqe",
                "type":1,
                "total_amount":1100,
                "order_limit":2200,
                "start_time":1447212368,
                "end_time":1453519569,
                "remark":"ewrw",
                "shop_id":30,
                "shop_sub_id":0,
                "created":1447212374,
                "modified":1447212374,
                "deleted":1
            }
        },
        "shareMessage":{
            "id":1420,
            "title":"拼的是手气，抢的是红包~",
            "desc":"#商家店名#发红包啦，不要白不要啊！",
            "pic_id":885,
            "shop_id":30,
            "shop_sub_id":0,
            "created":1448941780,
            "modified":1448941780,
            "deleted":1,
            "documentLib":{
                "id":885,
                "name":"55292eb4N695aa6bf",
                "desc":null,
                "category_id":0,
                "tag_id":1,
                "file_cdn_path":"http://imgcache.vikduo.com/static/90ce2f905bea7fb8bf85bc83baa409d6.jpg",
                "file_type":1,
                "shop_id":30,
                "shop_sub_id":0,
                "created":1447751550,
                "modified":1447751550,
                "deleted":1
            }
        },
        "news":{
            "id":1321,
            "title":"拼的是手气，抢的是红包~",
            "type":2,
            "is_wsh":2,
            "media_id":null,
            "shop_id":30,
            "shop_sub_id":0,
            "created":1448941780,
            "modified":1448941780,
            "deleted":1,
            "wxImagetxtReplyItems":[
                {
                    "id":1719,
                    "media_id":null,
                    "wx_imagetxt_reply_id":1321,
                    "title":"拼的是手气，抢的是红包~",
                    "description":"亲，点击进入活动主页，意外惊喜等着你！",
                    "cdn_path":null,
                    "document_id":"888",
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
                    "created":1448941780,
                    "modified":1448941780,
                    "deleted":1,
                    "documentLib":{
                        "id":888,
                        "name":"bg",
                        "desc":null,
                        "category_id":0,
                        "tag_id":1,
                        "file_cdn_path":"http://imgcache.vikduo.com/static/2d36c4a760add3e782ced63cab384114.jpg",
                        "file_type":1,
                        "shop_id":30,
                        "shop_sub_id":0,
                        "created":1447752413,
                        "modified":1447752413,
                        "deleted":1
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

## __关闭红包活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet-event/general-disable
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
    "data":{
        "id":569,
        "activity_type":6,
        "relate_product_type":1,
        "postage_setting_id":0,
        "name":"我都是",
        "desc":"wdsa",
        "sort":null,
        "expire_type":1,
        "start_time":1449114377,
        "end_time":1450755977,
        "wx_qrcode_id":null,
        "wx_imagetxt_reply_id":1321,
        "share_message_id":1420,
        "shop_id":30,
        "shop_sub_id":0,
        "created":1448941780,
        "modified":1454469241,
        "deleted":1,
        "share_type":1,
        "redPacketEvent":{
            "id":133,
            "activity_id":569,
            "type":1,
            "red_packet_id":62,
            "num_per_packet":10,
            "red_packet_num":10,
            "is_attention":2,
            "shop_id":30,
            "shop_sub_id":0,
            "redPacket":{
                "id":62,
                "name":"wqe",
                "type":1,
                "total_amount":1100,
                "order_limit":2200,
                "start_time":1447212368,
                "end_time":1453519569,
                "remark":"ewrw",
                "shop_id":30,
                "shop_sub_id":0,
                "created":1447212374,
                "modified":1447212374,
                "deleted":1
            }
        },
        "shareMessage":{
            "id":1420,
            "title":"拼的是手气，抢的是红包~",
            "desc":"#商家店名#发红包啦，不要白不要啊！",
            "pic_id":885,
            "shop_id":30,
            "shop_sub_id":0,
            "created":1448941780,
            "modified":1448941780,
            "deleted":1,
            "documentLib":{
                "id":885,
                "name":"55292eb4N695aa6bf",
                "desc":null,
                "category_id":0,
                "tag_id":1,
                "file_cdn_path":"http://imgcache.vikduo.com/static/90ce2f905bea7fb8bf85bc83baa409d6.jpg",
                "file_type":1,
                "shop_id":30,
                "shop_sub_id":0,
                "created":1447751550,
                "modified":1447751550,
                "deleted":1
            }
        },
        "news":{
            "id":1321,
            "title":"拼的是手气，抢的是红包~",
            "type":2,
            "is_wsh":2,
            "media_id":null,
            "shop_id":30,
            "shop_sub_id":0,
            "created":1448941780,
            "modified":1448941780,
            "deleted":1,
            "wxImagetxtReplyItems":[
                {
                    "id":1719,
                    "media_id":null,
                    "wx_imagetxt_reply_id":1321,
                    "title":"拼的是手气，抢的是红包~",
                    "description":"亲，点击进入活动主页，意外惊喜等着你！",
                    "cdn_path":null,
                    "document_id":"888",
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
                    "created":1448941780,
                    "modified":1448941780,
                    "deleted":2,
                    "documentLib":{
                        "id":888,
                        "name":"bg",
                        "desc":null,
                        "category_id":0,
                        "tag_id":1,
                        "file_cdn_path":"http://imgcache.vikduo.com/static/2d36c4a760add3e782ced63cab384114.jpg",
                        "file_type":1,
                        "shop_id":30,
                        "shop_sub_id":0,
                        "created":1447752413,
                        "modified":1447752413,
                        "deleted":1
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


## __获取单个活动生成红包__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet-event/get-item
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动红包的id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| status | 否 | Integer(4) | 状态 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":210861,
        "red_packet_event_id":144,
        "red_packet_id":65,
        "amount":10000,
        "type":1,
        "start_uid":507,
        "guess_uid":null,
        "start_time":1454469451,
        "guess_time":null,
        "shop_id":30,
        "shop_sub_id":0,
        "status":2,
        "created":1453713167,
        "modified":1454469451,
        "deleted":1,
        "startWxUserInfo":{
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
            "point":959629,
            "wsh_code":null,
            "created":1442224613,
            "modified":1453370886,
            "deleted":1
        },
        "redPacketEvent":{
            "id":144,
            "activity_id":660,
            "type":1,
            "red_packet_id":65,
            "num_per_packet":10,
            "red_packet_num":10,
            "is_attention":2,
            "shop_id":30,
            "shop_sub_id":0,
            "activity":{
                "id":660,
                "activity_type":6,
                "relate_product_type":1,
                "postage_setting_id":0,
                "name":"gdfg",
                "desc":"1. 活动时间：#年#月#日#时 至 #年#月#日#时； 2. 用户进入活动主页抢群红包，分享给好友瓜分群红包，瓜分到的红包金额自动发放到用户的商城账户； 3. 用户必须关注微信公众号才能抢群红包；（打开强制关注后）； 4. 每个用户只能发起一次活动，但可以瓜分不同用户转发的群红包； 5. 瓜分群红包，先到先得，该群红包分完为止； 6. 本活动最终解释权归XX商家所有。",
                "sort":null,
                "expire_type":1,
                "start_time":1453799521,
                "end_time":1459058721,
                "wx_qrcode_id":null,
                "wx_imagetxt_reply_id":1660,
                "share_message_id":1874,
                "shop_id":30,
                "shop_sub_id":0,
                "created":1453713167,
                "modified":1454469402,
                "deleted":1,
                "share_type":1,
                "shareMessage":{
                    "id":1874,
                    "title":"拼的是手气，抢的是红包~",
                    "desc":"#商家店名#发红包啦，不要白不要啊！",
                    "pic_id":10,
                    "shop_id":30,
                    "shop_sub_id":0,
                    "created":1453713167,
                    "modified":1453713167,
                    "deleted":1
                }
            }
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取活动生成红包列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet-event/find-item-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| start_uid | 否 | Integer(11) | 发起用户id |
| red_packet_event_id | 否 | Integer(11) | 红包活动id |
| status | 否 | Integer(4) | 状态 |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
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
            "id":210862,
            "red_packet_event_id":144,
            "red_packet_id":65,
            "amount":10000,
            "type":1,
            "start_uid":null,
            "guess_uid":null,
            "start_time":null,
            "guess_time":null,
            "shop_id":30,
            "shop_sub_id":0,
            "status":1,
            "created":1453713167,
            "modified":1453713167,
            "deleted":1,
            "startWxUserInfo":[

            ]
        },
        {.....}
    ],
    "page":{
        "per_page":1,
        "total_count":9,
        "current_page":0,
        "total_page":9
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __领取活动生成红包__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet-event/receive-item
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| activity_id | 是 | Integer(11) | 活动红包的id |
| shop_id | 是 | Integer(11) | 商家id |
| uid | 是 | Integer(11) | 用户id |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":210861,
        "red_packet_event_id":144,
        "red_packet_id":65,
        "amount":10000,
        "type":1,
        "start_uid":507,
        "guess_uid":null,
        "start_time":1454469451,
        "guess_time":null,
        "shop_id":30,
        "shop_sub_id":0,
        "status":2,
        "created":1453713167,
        "modified":1454469451,
        "deleted":1,
        "startWxUserInfo":{
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
            "point":959629,
            "wsh_code":null,
            "created":1442224613,
            "modified":1453370886,
            "deleted":1
        },
        "redPacketEvent":{
            "id":144,
            "activity_id":660,
            "type":1,
            "red_packet_id":65,
            "num_per_packet":10,
            "red_packet_num":10,
            "is_attention":2,
            "shop_id":30,
            "shop_sub_id":0,
            "activity":{
                "id":660,
                "activity_type":6,
                "relate_product_type":1,
                "postage_setting_id":0,
                "name":"gdfg",
                "desc":"1. 活动时间：#年#月#日#时 至 #年#月#日#时； 2. 用户进入活动主页抢群红包，分享给好友瓜分群红包，瓜分到的红包金额自动发放到用户的商城账户； 3. 用户必须关注微信公众号才能抢群红包；（打开强制关注后）； 4. 每个用户只能发起一次活动，但可以瓜分不同用户转发的群红包； 5. 瓜分群红包，先到先得，该群红包分完为止； 6. 本活动最终解释权归XX商家所有。",
                "sort":null,
                "expire_type":1,
                "start_time":1453799521,
                "end_time":1459058721,
                "wx_qrcode_id":null,
                "wx_imagetxt_reply_id":1660,
                "share_message_id":1874,
                "shop_id":30,
                "shop_sub_id":0,
                "created":1453713167,
                "modified":1454469402,
                "deleted":1,
                "share_type":1,
                "shareMessage":{
                    "id":1874,
                    "title":"拼的是手气，抢的是红包~",
                    "desc":"#商家店名#发红包啦，不要白不要啊！",
                    "pic_id":10,
                    "shop_id":30,
                    "shop_sub_id":0,
                    "created":1453713167,
                    "modified":1453713167,
                    "deleted":1
                }
            }
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __瓜分群红包__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet-event/get-group-item
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| item_id | 是 | Integer(11) | 活动红包的id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| uid | 是 | Integer(11) | 用户id |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "redPacketLog":{
            "shop_sub_id":0,
            "red_packet_event_id":144,
            "red_package_item_id":210861,
            "activity_id":660,
            "type":1,
            "amount":1184,
            "uid":507,
            "shop_id":30,
            "created":1454469890,
            "modified":1454469890,
            "id":109
        },
        "userRedPacket":{
            "type":1,
            "shop_sub_id":0,
            "is_use":2,
            "uid":507,
            "amount":1184,
            "order_limit":1000,
            "start_time":1453685438,
            "end_time":1454549440,
            "shop_id":30,
            "created":1454469891,
            "modified":1454469891,
            "deleted":1,
            "id":333
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __接龙红包猜金额__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet-event/get-transmit-item
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| item_id | 是 | Integer(11) | 活动红包的id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| uid | 是 | Integer(11) | 用户id |
| guess | 是 | Integer(11) | 猜金额 |
| pid | 是 | Integer(11) | 父节点 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "redPacketTransmitLog":{
            "pid":0,
            "shop_id":5,
            "shop_sub_id":43,
            "uid":158,
            "red_packet_event_id":3,
            "red_package_item_id":21,
            "guess_amount":3,
            "is_guess":2,
            "bd_amount":10,
            "created":1436258903,
            "id":1
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取群红包记录__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet-event/get-group-log
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 否 | Integer(11) | 群红包记录id |
| shop_id | 是 | Integer(11) | 商家id |
| uid | 否 | Integer(11) | 用户 |
| activity_id | 否 | Integer(11) | 活动id |
| red_packet_event_id | 否 | Integer(11) | 红包活动id |
| red_package_item_id | 否 | Integer(11) | 活动生成红包id |
<br  />
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


## __获取接龙红包记录__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet-event/get-transmit-log
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 否 | Integer(11) | 群红包记录id |
| shop_id | 是 | Integer(11) | 商家id |
| pid | 否 | Integer(11) | 父节点 |
| uid | 否 | Integer(11) | 用户 |
| activity_id | 否 | Integer(11) | 活动id |
| is_guess | 否 | Integer(4) | 是否猜中 |
| red_packet_event_id | 否 | Integer(11) | 红包活动id |
| red_package_item_id | 否 | Integer(11) | 活动生成红包id |
<br  />
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


## __查找群红包记录列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet-event/find-group-log-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| red_packet_event_id | 否 | Integer(11) | 红包活动id |
| red_package_item_id | 否 | Integer(11) | 活动生成红包id |
* **注意：sort排序可选字段['id']**

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


## __查找接龙红包记录列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/red-packet-event/find-transmit-log-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| red_packet_event_id | 否 | Integer(11) | 红包活动id |
| red_package_item_id | 否 | Integer(11) | 活动生成红包id |
* **注意：sort排序可选字段['id']**

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
