## __新增众筹__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/create-collect
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|type|是|Integer(11)|活动类型(1.代领、2.红包、3.点赞)|
| collect.name|是|varchar(200)|活动名称|
| collect.is_attention|是|Integer(11)|是否强制关注（1.是、2.否）|
| collect.start_time|是|Integer(11)|活动开始时间|
| collect.end_time|是|Integer(11)|活动结束时间|
| collect.document_id|否|varchar(80)|模块|
| collect.shop_id|是|Integer(11)|商家id|
| collect.share_type | 是 | Integer(4) |显示和分享模式（1.显示且能分享、2.不能显示且能分享、3.不能显示且不能分享）|
| shareMessage.title | 是 | String(100) | 分享标题 |
| shareMessage.desc | 是 | String(100) | 分享描述 |
| shareMessage.pic_id | 是 | Integer(11) | 文档id |
| news.title | 是 | String(50) | 微信图文标题 |
| news.description | 是 | String(250) | 微信图文描述 |
| news.document_id | 是 | Integer(11) | 文档id |
| news.url | 是 | String(11) | 微信图文链接 |
| news.content | 是 | String | 文档内容 |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "collect": {
            "share_message_id": 155,
            "wx_imagetxt_reply_id": 132,
            "is_attention": "1",
            "document_id": "3",
            "name": "代领众筹活动",
            "start_time": "1436752962",
            "end_time": "1436762962",
            "shop_id": "5",
            "shop_sub_id": "43",
            "type": 1,
            "created": 1436756966,
            "modified": 1436756966,
            "deleted": 1,
            "id": 7
        },
        "shareMessage": {
            "title": "分享的标题",
            "desc": "分享的描述",
            "pic_id": "1",
            "shop_id": "5",
            "shop_sub_id": "43",
            "created": 1436756966,
            "modified": 1436756966,
            "deleted": 1,
            "id": 155
        },
        "wxImagetxtReply": {
            "type": 2,
            "shop_id": "5",
            "shop_sub_id": "43",
            "title": "图文标题",
            "created": 1436756966,
            "modified": 1436756966,
            "deleted": 1,
            "id": 132
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
                "description": "图文描述",
                "document_id": "2",
                "url": "http://www.baidu.com",
                "content": "图文描述",
                "wx_imagetxt_reply_id": 132,
                "shop_id": "5",
                "shop_sub_id": "43",
                "created": 1436756966,
                "modified": 1436756966,
                "id": 165
            }
        ]
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __修改众筹__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/update-collect
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|type|是|Integer(11)|活动类型(1.代领、2.红包、3.点赞)|
| collect.id|是|Integer(11)|活动ID|
| collect.name|是|varchar(200)|活动名称|
| collect.is_attention|是|Integer(11)|是否强制关注（1.是、2.否）|
| collect.start_time|是|Integer(11)|活动开始时间|
| collect.end_time|是|Integer(11)|活动结束时间|
| collect.document_id|否|varchar(80)|模块|
| collect.shop_id|是|Integer(11)|商家id|
| collect.shop_sub_id|是|Integer(11)|店铺id|
| collect.share_type | 是 | Integer(4) |显示和分享模式（1.显示且能分享、2.不能显示且能分享、3.不能显示且不能分享）|
| shareMessage.title | 是 | String(100) | 分享标题 |
| shareMessage.desc | 是 | String(100) | 分享描述 |
| shareMessage.pic_id | 是 | Integer(11) | 文档id |
| news.title | 是 | String(50) | 微信图文标题 |
| news.description | 是 | String(250) | 微信图文描述 |
| news.document_id | 是 | Integer(11) | 文档id |
| news.url | 是 | String(11) | 微信图文链接 |
| news.content | 是 | String | 文档内容 |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "collect": {
            "id": 7,
            "name": "代领众筹活动修改",
            "share_message_id": 176,
            "is_attention": "1",
            "start_time": "1436752962",
            "end_time": "1436762962",
            "type": 1,
            "document_id": "3",
            "wx_imagetxt_reply_id": 138,
            "shop_id": "5",
            "shop_sub_id": "43",
            "created": 1436756966,
            "modified": 1436774870,
            "deleted": 1
        },
        "shareMessage": {
            "id": 176,
            "title": "分享的标题2",
            "desc": "分享的描述",
            "pic_id": "1",
            "shop_id": 5,
            "shop_sub_id": 43,
            "created": 1436774831,
            "modified": 1436774870,
            "deleted": 1
        },
        "wxImagetxtReply": {
            "id": 138,
            "title": "图文标题2",
            "type": 2,
            "shop_id": 5,
            "shop_sub_id": 43,
            "created": 1436774831,
            "modified": 1436774870,
            "deleted": 1,
            "wxImagetxtReplyItems": [
                {
                    "id": 171,
                    "wx_imagetxt_reply_id": 138,
                    "title": "图文标题",
                    "description": "图文描述",
                    "cdn_path": null,
                    "document_id": "2",
                    "url": "http://www.baidu.com",
                    "content": "图文描述",
                    "articles_comments_count": 0,
                    "hits": 0,
                    "likes": 0,
                    "is_top": 2,
                    "is_banner": 2,
                    "shop_id": 5,
                    "shop_sub_id": 43,
                    "release_time": 0,
                    "recommend": null,
                    "created": 1436774831,
                    "modified": 1436774831,
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
                "title": "图文标题2",
                "description": "图文描述",
                "document_id": "2",
                "url": "http://www.baidu.com",
                "content": "图文描述",
                "wx_imagetxt_reply_id": 138,
                "shop_id": 5,
                "shop_sub_id": 43,
                "created": 1436774870,
                "modified": 1436774870,
                "id": 172
            }
        ]
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取众筹明细__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/get-collect
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| type|是|Integer(11)|活动类型(1.代领、2.红包、3.点赞)|
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
        "id": 272,
        "name": "1111111",
        "share_message_id": 1834,
        "wx_imagetxt_reply_id": 1621,
        "is_attention": 2,
        "start_time": 1453273504,
        "end_time": 1453359889,
        "type": 3,
        "document_id": 0,
        "rule": "<p>由用户自主发起，利用微信分享好友参与活动，在指定时间内由好友帮忙点赞到指定集点数，发起人即可免费得到商品。</p><p>1.活动时间：××××年××月××日-××××年××月××日；</p><p>2.活动参与人必须关注活动商家微信公众号才能参与活动；（打开强制关注后）</p><p>3.在指定的时间内，集齐完点数，即可获得活动商品；</p><p>4.若发起人成功集齐赞数，则可免费获得活动商品，工作人员将会在15个工作日与发起人联系；</p><p>5. 若发起人成功集齐赞数，请尽快填写中奖资料；</p><p>6. 若发起人在指定结束时间内没有集齐完点数，则此次活动失败；</p>",
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": 1453273488,
        "modified": 1453273510,
        "deleted": 1,
        "share_type": 2,
        "shareMessage": {
            "id": 1834,
            "title": "谁是点赞狂魔，一点就知道！",
            "desc": "让好友来点赞，集够赞数免费获得指定大奖~",
            "pic_id": 11,
            "shop_id": 30,
            "shop_sub_id": 0,
            "created": 1453273488,
            "modified": 1453273507,
            "deleted": 1,
            "documentLib": {
                "id": 11,
                "name": "众筹点赞默认分享图片",
                "desc": "众筹点赞默认分享图片",
                "category_id": 0,
                "tag_id": 1,
                "file_cdn_path": "http://imgcache.vikduo.com/static/b3dd61f523da85cc18d8d3d6006a76ad.jpg",
                "file_type": 1,
                "shop_id": 0,
                "shop_sub_id": 0,
                "created": 1442239227,
                "modified": 1442239227,
                "deleted": 1
            }
        },
        "news": {
            "id": 1621,
            "title": "顺手点个赞，有惊喜哦~",
            "type": 2,
            "is_wsh": 2,
            "media_id": null,
            "shop_id": 30,
            "shop_sub_id": 0,
            "created": 1453273488,
            "modified": 1453273488,
            "deleted": 1,
            "wxImagetxtReplyItems": [
                {
                    "id": 2145,
                    "media_id": null,
                    "wx_imagetxt_reply_id": 1621,
                    "title": "顺手点个赞，有惊喜哦~",
                    "description": "亲，点击进入活动主页，意外惊喜等着你！",
                    "cdn_path": null,
                    "document_id": "6",
                    "link_type": null,
                    "link_param": "",
                    "url": null,
                    "wx_url": null,
                    "show_cover_pic": 2,
                    "author": "",
                    "content": "亲，点击进入活动主页，意外惊喜等着你！",
                    "articles_comments_count": 0,
                    "hits": 0,
                    "likes": 0,
                    "is_top": 2,
                    "is_banner": 2,
                    "shop_id": 30,
                    "shop_sub_id": 0,
                    "release_time": 0,
                    "recommend": null,
                    "created": 1453273488,
                    "modified": 1453273488,
                    "deleted": 1,
                    "documentLib": {
                        "id": 6,
                        "name": "众筹点赞默认图文图片",
                        "desc": "众筹点赞默认图文图片",
                        "category_id": 0,
                        "tag_id": 1,
                        "file_cdn_path": "http://imgcache.vikduo.com/static/4214d575b47b6bf2c662a50a56fdc00e.png",
                        "file_type": 1,
                        "shop_id": 0,
                        "shop_sub_id": 0,
                        "created": 1442239225,
                        "modified": 1442239225,
                        "deleted": 1
                    }
                }
            ]
        },
        "collectProducts": [],
        "collectRedpackets": [],
        "collectCustomGift": [
            {
                "id": 79,
                "collect_id": 272,
                "price": 1,
                "give": 0,
                "number": 1,
                "count": 1,
                "lastCount": 1,
                "name": "1",
                "document_id": 1363,
                "shop_id": 30,
                "shop_sub_id": 0,
                "documentLib": {
                    "id": 1363,
                    "name": "12",
                    "desc": null,
                    "category_id": 0,
                    "tag_id": 1,
                    "file_cdn_path": "http://imgcache.vikduo.com/static/e83c9aedf53adf9a1a40da0fd623ffcf.jpg",
                    "file_type": 1,
                    "shop_id": 30,
                    "shop_sub_id": 0,
                    "created": 1452836772,
                    "modified": 1452836772,
                    "deleted": 1
                }
            }
        ]
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取众筹活动列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/find-collect
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
|type|是|Integer(11)|活动类型(1.代领、2.红包、3.点赞)|
| deleted | 否 | Integer(11) | 活动状态（1.启用、2.禁用） |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| name | 否 | String(250) | 参与者姓名搜索 |
| nickname | 否 | String(250) | 微信昵称搜索 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": [
        {
            "id": 276,
            "name": "点赞活动名称",
            "share_message_id": 1898,
            "wx_imagetxt_reply_id": 1748,
            "is_attention": 2,
            "start_time": 1454313538,
            "end_time": 1454396338,
            "type": 3,
            "document_id": 0,
            "rule": "<p>由用户自主发起，利用微信分享好友参与活动，在指定时间内由好友帮忙点赞到指定集点数，发起人即可免费得到商品。</p><p>1.活动时间：××××年××月××日-××××年××月××日；</p><p>2.活动参与人必须关注活动商家微信公众号才能参与活动；（打开强制关注后）</p><p>3.在指定的时间内，集齐完点数，即可获得活动商品；</p><p>4.若发起人成功集齐赞数，则可免费获得活动商品，工作人员将会在15个工作日与发起人联系； </p><p>5. 若发起人成功集齐赞数，请尽快填写中奖资料；</p><p>6. 若发起人在指定结束时间内没有集齐完点数，则此次活动失败；</p><p>7.活动商品领完即止，先到先得。</p>",
            "shop_id": 30,
            "shop_sub_id": 0,
            "created": 1454309976,
            "modified": 1454309976,
            "deleted": 2,
            "share_type": 1,
            "wxImagetxtReply": {
                "id": 1748,
                "title": "顺手点个赞，有惊喜哦~",
                "type": 2,
                "is_wsh": 2,
                "media_id": null,
                "shop_id": 30,
                "shop_sub_id": 0,
                "created": 1454309976,
                "modified": 1454309976,
                "deleted": 1,
                "wxImagetxtReplyItems": [
                    {
                        "id": 2582,
                        "media_id": null,
                        "wx_imagetxt_reply_id": 1748,
                        "title": "顺手点个赞，有惊喜哦~",
                        "description": "亲，点击进入活动主页，意外惊喜等着你！",
                        "cdn_path": null,
                        "document_id": "6",
                        "link_type": null,
                        "link_param": "",
                        "url": null,
                        "wx_url": null,
                        "show_cover_pic": 2,
                        "author": "",
                        "content": "亲，点击进入活动主页，意外惊喜等着你！",
                        "articles_comments_count": 0,
                        "hits": 0,
                        "likes": 0,
                        "is_top": 2,
                        "is_banner": 2,
                        "shop_id": 30,
                        "shop_sub_id": 0,
                        "release_time": 0,
                        "recommend": null,
                        "created": 1454309976,
                        "modified": 1454309976,
                        "deleted": 1,
                        "documentLib": {
                            "id": 6,
                            "name": "众筹点赞默认图文图片",
                            "desc": "众筹点赞默认图文图片",
                            "category_id": 0,
                            "tag_id": 1,
                            "file_cdn_path": "http://imgcache.vikduo.com/static/4214d575b47b6bf2c662a50a56fdc00e.png",
                            "file_type": 1,
                            "shop_id": 0,
                            "shop_sub_id": 0,
                            "created": 1442239225,
                            "modified": 1442239225,
                            "deleted": 1
                        }
                    }
                ]
            }
        },
        {....}
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

## __启用众筹__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/enable-collect
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


## __禁用众筹__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/disable-collect
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


## __删除众筹__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/del-collect
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


