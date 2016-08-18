# __微预约__
###新增微预约
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reserve/create-reserve
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| reserveSetting.title | 是 | varchar(100) | 标题 |
| reserveSetting.summary | 是 | text | 活动简介 |
| reserveSetting.note | 是 | text | 报名须知 |
| reserveSetting.content | 是 | text | 预约正文 |
| reserveSetting.items | 是 | text | 预约填写项目 |
| reserveSetting.start_time | 否 | Integer(11) | 活动开始时间 |
| reserveSetting.end_time | 否 | Integer(11) | 活动结束时间 |
| reserveSetting.qrcode_id | 是 | Integer(11) | 二维码id |
| reserveSetting.shop_id | 是 | Integer(11) | 商家id |
| reserveSetting.shop_sub_id | 是 | Integer(11) | 门店id |
| reserveSetting.document_id | 否 | varchar(20) | 邀请函主图 |
| reserveSetting.per_count | 是 | Integer(11) | 预约人数上限 |
| reserveSetting.share_type | 是 | Integer(4) |显示和分享模式（1.显示且能分享、2.不能显示且能分享、3.不能显示且不能分享）|
| shareMessage.title | 否 | String(100) | 分享标题 |
| shareMessage.desc | 否 | String(100) | 分享描述 |
| shareMessage.pic_id | 否 | Integer(11) | document_lib表外键 |
| news.title | 否 | String(100) | 图文标题 |
| news.description | 否 | String(100) | 图文描述 |
| news.document_id | 否 | string(20) | document_lib表外键 |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
##eg：
```json
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "share_message_id": 0,
        "wx_imagetxe_reply_id": 1,
        "qrcode_id": 1,
        "deleted": 1,
        "title": "标题",
        "summary": "标题",
        "note": "标题",
        "content": "标题",
        "items": "标题",
        "start_time": 145858548,
        "end_time": 1458858995,
        "shop_id": 5,
        "shop_sub_id": 43,
        "document_id": "标题",
        "per_count": 0,
        "created": 1435739437,
        "modified": 1435739437,
        "id": 197
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取预约活动列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reserve/find-reserve
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| title | 否 | String(100) | 标题 |
| ids | 否 | Array | id数组 |
* **注意：sort排序可选字段['id']**

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
##eg：
```json
{
    "errcode": 0,
    "errmsg": "ok",
    "data": [
        {
            "id": 199,
            "share_message_id": 0,
            "title": "标题",
            "summary": "标题",
            "note": "标题",
            "content": "标题",
            "items": "标题",
            "start_time": 145858548,
            "end_time": 1458858995,
            "qrcode_id": 1,
            "shop_id": 5,
            "shop_sub_id": 43,
            "document_id": "标题",
            "per_count": 0,
            "created": 1435743523,
            "modified": 1435743523,
            "deleted": 1
        },
        ....
    ],
    "page": {
        "per_page": 20,
        "total_count": 5,
        "current_page": 0,
        "total_page": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取预约活动详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reserve/get-reserve
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
* **注意：sort排序可选字段['id']**

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
##eg：
```json
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 319,
        "wx_imagetxt_reply_id": 1614,
        "share_message_id": 0,
        "title": "线下活动",
        "summary": "活动简介",
        "note": "报名须知",
        "content": null,
        "items": "[{\"nametag\":\"name\",\"type\":\"text\",\"key\":\"\\u59d3\\u540d\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u540d\\u5b57\",\"check\":\"true\",\"addtype\":\"system\",\"$$hashKey\":\"object:25\"},{\"nametag\":\"sex\",\"type\":\"select\",\"key\":\"\\u6027\\u522b\",\"value\":\"\\u7537|\\u5973\",\"check\":\"true\",\"addtype\":\"system\",\"$$hashKey\":\"object:26\"},{\"nametag\":\"mobile\",\"type\":\"text\",\"key\":\"\\u624b\\u673a\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u624b\\u673a\",\"check\":\"false\",\"addtype\":\"system\",\"$$hashKey\":\"object:27\"},{\"nametag\":\"idCard\",\"type\":\"text\",\"key\":\"\\u8eab\\u4efd\\u8bc1\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u8eab\\u4efd\\u8bc1\\u53f7\\u7801\",\"check\":\"false\",\"addtype\":\"system\",\"$$hashKey\":\"object:28\"},{\"nametag\":\"bookedDate\",\"type\":\"calendar\",\"key\":\"\\u9884\\u7ea6\\u65e5\\u671f\",\"value\":\"\\u70b9\\u51fb\\u8f93\\u5165\",\"check\":\"false\",\"addtype\":\"system\",\"$$hashKey\":\"object:29\"},{\"nametag\":\"bookedTime\",\"type\":\"select\",\"key\":\"\\u9884\\u7ea6\\u65f6\\u95f4\",\"value\":\"0:00-1:00|1:00-2:00|2:00-3:00|3:00-4:00|4:00-5:00|5:00-6:00|6:00-7:00|7:00-8:00|8:00-9:00|9:00-10:00|10:00-11:00|11:00-12:00|12:00-13:00|13:00-14:00|14:00-15:00|15:00-16:00|16:00-17:00|17:00-18:00|18:00-19:00|19:00-20:00|20:00-21:00|21:00-22:00|22:00-23:00|23:00-24:00\",\"check\":\"false\",\"addtype\":\"system\",\"$$hashKey\":\"object:30\"},{\"nametag\":\"message\",\"type\":\"textarea\",\"key\":\"\\u7559\\u8a00\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u7559\\u8a00\\u5185\\u5bb9\",\"check\":\"false\",\"addtype\":\"system\",\"$$hashKey\":\"object:31\"},{\"nametag\":\"fShop\",\"type\":\"select\",\"key\":\"\\u9884\\u7ea6\\u5e97\\u94fa\",\"value\":\"aaa|lljtest|123|\\u5730\\u65b9\\u597d\\u5730\\u65b93ff|tang|ddf|k|tangxiong|gfhg|ui|klk|rre|1222|11|\\u74f6\\u5b5012|ee|\\u5510|\\u963f\\u8428\\u5fb7|das|sdfsdf\",\"check\":\"false\",\"addtype\":\"system\",\"$$hashKey\":\"object:32\"}]",
        "start_time": 1453268979,
        "end_time": 1453528182,
        "qrcode_id": 0,
        "shop_id": 30,
        "shop_sub_id": 0,
        "document_id": "250",
        "per_count": 10,
        "created": 1453268989,
        "modified": 1453268991,
        "deleted": 1,
        "share_type": 3,
        "documentLib": {
            "id": 250,
            "name": "百城万店邀请函-分享",
            "desc": null,
            "category_id": 0,
            "tag_id": null,
            "file_cdn_path": "http://imgcache.vikduo.com/static/4007f67107a5b828d863836ba440e38b.jpg",
            "file_type": 1,
            "shop_id": 0,
            "shop_sub_id": 0,
            "created": 1445398446,
            "modified": 1445398446,
            "deleted": 1
        },
        "news": {
            "id": 1614,
            "title": "各就各位，预约正式开始~",
            "type": 2,
            "is_wsh": 2,
            "media_id": null,
            "shop_id": 30,
            "shop_sub_id": 0,
            "created": 1453268989,
            "modified": 1453268989,
            "deleted": 1,
            "wxImagetxtReplyItems": [
                {
                    "id": 2136,
                    "media_id": null,
                    "wx_imagetxt_reply_id": 1614,
                    "title": "各就各位，预约正式开始~",
                    "description": "亲，点击进入活动主页，意外惊喜等着你！",
                    "cdn_path": null,
                    "document_id": "2",
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
                    "created": 1453268989,
                    "modified": 1453268989,
                    "deleted": 1,
                    "documentLib": {
                        "id": 2,
                        "name": "预约默认图文图片",
                        "desc": "预约默认图文图片",
                        "category_id": 0,
                        "tag_id": 1,
                        "file_cdn_path": "http://imgcache.vikduo.com/static/79dd184533bb16589939dd2c801bed00.jpg",
                        "file_type": 1,
                        "shop_id": 0,
                        "shop_sub_id": 0,
                        "created": 1442239224,
                        "modified": 1442239224,
                        "deleted": 1
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

## __修改预约活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reserve/update-reserve
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| reserveSetting.id | 是 | Integer(11) | 表主键 |
| reserveSetting.share_message | 是 | Integer(11) | share_message表外键 |
| reserveSetting.title | 是 | varchar(100) | 标题 |
| reserveSetting.summary | 是 | text | 活动简介 |
| reserveSetting.note | 是 | text | 报名须知 |
| reserveSetting.content | 是 | text | 预约正文 |
| reserveSetting.items | 是 | text | 预约填写项目 |
| reserveSetting.start_time | 否 | Integer(11) | 活动开始时间 |
| reserveSetting.end_time | 否 | Integer(11) | 活动结束时间 |
| reserveSetting.qrcode_id | 是 | Integer(11) | 二维码id |
| reserveSetting.shop_id | 是 | Integer(11) | 商家id |
| reserveSetting.shop_sub_id | 是 | Integer(11) | 门店id |
| reserveSetting.document_id | 否 | varchar(20) | 邀请函主图 |
| reserveSetting.per_count | 是 | Integer(11) | 预约人数上限 |
| reserveSetting.share_type | 是 | Integer(4) |显示和分享模式（1.显示且能分享、2.不能显示且能分享、3.不能显示且不能分享）|


<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```json
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 195,
        "share_message_id": "1",
        "title": "微预约",
        "summary": "预约参加漂流活动",
        "note": "古龙峡漂流",
        "content": "带家属自费",
        "items": "自带泳衣泳裤，谢谢合作",
        "start_time": 145858548,
        "end_time": 1458858995,
        "qrcode_id": 1,
        "shop_id": 5,
        "shop_sub_id": 43,
        "document_id": "标题",
        "per_count": 0,
        "created": 1435739318,
        "modified": 1435978959,
        "deleted": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __删除预约活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reserve/delete-reserve
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 表主键 |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 门店id |


<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```json
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 195,
        "share_message_id": 1,
        "title": "微预约",
        "summary": "预约参加漂流活动",
        "note": "古龙峡漂流",
        "content": "带家属自费",
        "items": "自带泳衣泳裤，谢谢合作",
        "start_time": 145858548,
        "end_time": 1458858995,
        "qrcode_id": 1,
        "shop_id": 5,
        "shop_sub_id": 43,
        "document_id": "标题",
        "per_count": 0,
        "created": 1435739318,
        "modified": 1435981372,
        "deleted": 3
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __启用预约活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reserve/general-enable
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 表主键 |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 门店id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```json
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 195,
        "share_message_id": 1,
        "title": "微预约",
        "summary": "预约参加漂流活动",
        "note": "古龙峡漂流",
        "content": "带家属自费",
        "items": "自带泳衣泳裤，谢谢合作",
        "start_time": 145858548,
        "end_time": 1458858995,
        "qrcode_id": 1,
        "shop_id": 5,
        "shop_sub_id": 43,
        "document_id": "标题",
        "per_count": 0,
        "created": 1435739318,
        "modified": 1435981372,
        "deleted": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __禁用预约活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reserve/general-disable
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 表主键 |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 门店id |


<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```json
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 195,
        "share_message_id": 1,
        "title": "微预约",
        "summary": "预约参加漂流活动",
        "note": "古龙峡漂流",
        "content": "带家属自费",
        "items": "自带泳衣泳裤，谢谢合作",
        "start_time": 145858548,
        "end_time": 1458858995,
        "qrcode_id": 1,
        "shop_id": 5,
        "shop_sub_id": 43,
        "document_id": "标题",
        "per_count": 0,
        "created": 1435739318,
        "modified": 1435981372,
        "deleted": 2
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __添加预约者__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reserve/create-reserve-user-data
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| reserve_setting_id | 是 | Integer(11) | 表主键 |
| user_id | 是 | Integer(11) | 用户id |
| user_data | 是 | text | 预约信息（json格式） |
| shop_sub_id | 是 | Integer(11) | 门店id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```json
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "deleted": 1,
        "reserve_setting_id": 197,
        "user_id": 195,
        "user_data": "{'':fk,'':}",
        "shop_sub_id": 43,
        "shop_id": 5,
        "status": 1,
        "created": 1436003100,
        "modified": 1436003100,
        "id": 292
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
## __获取预约者列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reserve/find-reserve-user-data
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| user_id | 否 | Integer(11) | 用户id |
| reserve_setting_id | 否 | Integer(11) | 预约活动id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| shop_id | 是 | Integer(11) | 商家id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```json
{
    "errcode": 0,
    "errmsg": "ok",
    "data": [
        {
            "id": 394,
            "reserve_setting_id": 302,
            "user_id": 479,
            "user_data": "{\"name\":\"sdad\",\"mobile\":\"13246641470\",\"sex\":\"\\u5973\"}",
            "shop_sub_id": 0,
            "shop_id": 30,
            "status": 1,
            "created": 1441961521,
            "modified": 1441964191,
            "deleted": 1,
            "reserveSetting": {
                "id": 302,
                "wx_imagetxt_reply_id": 1106,
                "share_message_id": 0,
                "title": "tret",
                "summary": "活动简介",
                "note": "报名须知",
                "content": null,
                "items": "[{\"nametag\":\"name\",\"type\":\"text\",\"key\":\"\\u59d3\\u540d\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u540d\\u5b57\",\"check\":\"true\",\"addtype\":\"system\",\"$$hashKey\":\"object:20\"},{\"nametag\":\"sex\",\"type\":\"select\",\"key\":\"\\u6027\\u522b\",\"value\":\"\\u7537|\\u5973\",\"check\":\"true\",\"addtype\":\"system\",\"$$hashKey\":\"object:21\"},{\"nametag\":\"mobile\",\"type\":\"text\",\"key\":\"\\u624b\\u673a\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u624b\\u673a\",\"check\":\"true\",\"addtype\":\"system\",\"$$hashKey\":\"object:22\"},{\"nametag\":\"idCard\",\"type\":\"text\",\"key\":\"\\u8eab\\u4efd\\u8bc1\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u8eab\\u4efd\\u8bc1\\u53f7\\u7801\",\"check\":\"false\",\"addtype\":\"system\",\"$$hashKey\":\"object:23\"},{\"nametag\":\"bookedDate\",\"type\":\"calendar\",\"key\":\"\\u9884\\u7ea6\\u65e5\\u671f\",\"value\":\"\\u70b9\\u51fb\\u8f93\\u5165\",\"check\":\"false\",\"addtype\":\"system\",\"$$hashKey\":\"object:24\"},{\"nametag\":\"bookedTime\",\"type\":\"select\",\"key\":\"\\u9884\\u7ea6\\u65f6\\u95f4\",\"value\":\"0:00-1:00|1:00-2:00|2:00-3:00|3:00-4:00|4:00-5:00|5:00-6:00|6:00-7:00|7:00-8:00|8:00-9:00|9:00-10:00|10:00-11:00|11:00-12:00|12:00-13:00|13:00-14:00|14:00-15:00|15:00-16:00|16:00-17:00|17:00-18:00|18:00-19:00|19:00-20:00|20:00-21:00|21:00-22:00|22:00-23:00|23:00-24:00\",\"check\":\"false\",\"addtype\":\"system\",\"$$hashKey\":\"object:25\"},{\"nametag\":\"message\",\"type\":\"textarea\",\"key\":\"\\u7559\\u8a00\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u7559\\u8a00\\u5185\\u5bb9\",\"check\":\"false\",\"addtype\":\"system\",\"$$hashKey\":\"object:26\"},{\"nametag\":\"fShop\",\"type\":\"select\",\"key\":\"\\u9884\\u7ea6\\u5e97\\u94fa\",\"value\":\"\\u96be\\u7537\\u7537\\u5973\\u5973\\u7537\\u7537\\u5973\\u5973\\u7537|999999|agagag|111|\\u6d4b\\u8bd5|3\\u7ea7|adsd|\\u4e8c\\u7ea7\\u4ee3\\u7406\\u5546\\u300b\\u300b\\u52a0\\u76df\\u5e97|\\u4e8c\\u7ea7\\u4ee3\\u7406\\u5546\\u7ec8\\u7aef\\u5e97|as|testtest|test|\\u8fd9\\u91cc\\u6709\\u4e2a\\u76f4\\u8425\\u5e97|23|32133|321|122|pp\",\"check\":\"false\",\"addtype\":\"system\",\"$$hashKey\":\"object:27\"}]",
                "start_time": 1441960367,
                "end_time": 1442392369,
                "qrcode_id": 0,
                "shop_id": 30,
                "shop_sub_id": 0,
                "document_id": "250",
                "per_count": 20,
                "created": 1441960385,
                "modified": 1441960385,
                "deleted": 1,
                "share_type": 1
            },
            "userInfo": {
                "id": 479,
                "mobile": null,
                "nickname": "Eve",
                "sex": 1,
                "province": null,
                "city": null,
                "country": "文莱",
                "headimgurl": "http://wx.qlogo.cn/mmopen/MpcUrIsNmadmZzpwwIceuvDygkeg3mcvfjmqezP4aHdAC7D6EiapeRcGeeADd8Dtbich18KxjIXPZIBicRvod6CnMS8SflPgnxN/0",
                "shop_id": 30,
                "shop_sub_id": 219,
                "staff_id": 110,
                "belong_to_staff_id": 0,
                "login_count": 42,
                "lastloginip": "101.226.33.203",
                "lastlogintime": 1441963428,
                "password": null,
                "type": 2,
                "status": 1,
                "member_refer": null,
                "scene_id": 30,
                "mpath": null,
                "mid": 70,
                "agent_id": 0,
                "agent_path": null,
                "sign_days": 0,
                "sign_time": 0,
                "is_subscribe": 1,
                "group_id": 1,
                "level_id": null,
                "point": 0,
                "wsh_code": null,
                "created": 1441874895,
                "modified": 1441963428,
                "deleted": 3
            }
        },
        {
            "id": 393,
            "reserve_setting_id": 302,
            "user_id": 492,
            "user_data": "{\"name\":\"\\u5218\\ud83d\\udc40\",\"mobile\":\"13246641470\",\"sex\":\"\\u5973\"}",
            "shop_sub_id": 219,
            "shop_id": 30,
            "status": 1,
            "created": 1441960442,
            "modified": 1441964702,
            "deleted": 1,
            "reserveSetting": {
                "id": 302,
                "wx_imagetxt_reply_id": 1106,
                "share_message_id": 0,
                "title": "tret",
                "summary": "活动简介",
                "note": "报名须知",
                "content": null,
                "items": "[{\"nametag\":\"name\",\"type\":\"text\",\"key\":\"\\u59d3\\u540d\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u540d\\u5b57\",\"check\":\"true\",\"addtype\":\"system\",\"$$hashKey\":\"object:20\"},{\"nametag\":\"sex\",\"type\":\"select\",\"key\":\"\\u6027\\u522b\",\"value\":\"\\u7537|\\u5973\",\"check\":\"true\",\"addtype\":\"system\",\"$$hashKey\":\"object:21\"},{\"nametag\":\"mobile\",\"type\":\"text\",\"key\":\"\\u624b\\u673a\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u624b\\u673a\",\"check\":\"true\",\"addtype\":\"system\",\"$$hashKey\":\"object:22\"},{\"nametag\":\"idCard\",\"type\":\"text\",\"key\":\"\\u8eab\\u4efd\\u8bc1\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u8eab\\u4efd\\u8bc1\\u53f7\\u7801\",\"check\":\"false\",\"addtype\":\"system\",\"$$hashKey\":\"object:23\"},{\"nametag\":\"bookedDate\",\"type\":\"calendar\",\"key\":\"\\u9884\\u7ea6\\u65e5\\u671f\",\"value\":\"\\u70b9\\u51fb\\u8f93\\u5165\",\"check\":\"false\",\"addtype\":\"system\",\"$$hashKey\":\"object:24\"},{\"nametag\":\"bookedTime\",\"type\":\"select\",\"key\":\"\\u9884\\u7ea6\\u65f6\\u95f4\",\"value\":\"0:00-1:00|1:00-2:00|2:00-3:00|3:00-4:00|4:00-5:00|5:00-6:00|6:00-7:00|7:00-8:00|8:00-9:00|9:00-10:00|10:00-11:00|11:00-12:00|12:00-13:00|13:00-14:00|14:00-15:00|15:00-16:00|16:00-17:00|17:00-18:00|18:00-19:00|19:00-20:00|20:00-21:00|21:00-22:00|22:00-23:00|23:00-24:00\",\"check\":\"false\",\"addtype\":\"system\",\"$$hashKey\":\"object:25\"},{\"nametag\":\"message\",\"type\":\"textarea\",\"key\":\"\\u7559\\u8a00\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u7559\\u8a00\\u5185\\u5bb9\",\"check\":\"false\",\"addtype\":\"system\",\"$$hashKey\":\"object:26\"},{\"nametag\":\"fShop\",\"type\":\"select\",\"key\":\"\\u9884\\u7ea6\\u5e97\\u94fa\",\"value\":\"\\u96be\\u7537\\u7537\\u5973\\u5973\\u7537\\u7537\\u5973\\u5973\\u7537|999999|agagag|111|\\u6d4b\\u8bd5|3\\u7ea7|adsd|\\u4e8c\\u7ea7\\u4ee3\\u7406\\u5546\\u300b\\u300b\\u52a0\\u76df\\u5e97|\\u4e8c\\u7ea7\\u4ee3\\u7406\\u5546\\u7ec8\\u7aef\\u5e97|as|testtest|test|\\u8fd9\\u91cc\\u6709\\u4e2a\\u76f4\\u8425\\u5e97|23|32133|321|122|pp\",\"check\":\"false\",\"addtype\":\"system\",\"$$hashKey\":\"object:27\"}]",
                "start_time": 1441960367,
                "end_time": 1442392369,
                "qrcode_id": 0,
                "shop_id": 30,
                "shop_sub_id": 0,
                "document_id": "250",
                "per_count": 20,
                "created": 1441960385,
                "modified": 1441960385,
                "deleted": 1,
                "share_type": 1
            },
            "userInfo": {
                "id": 492,
                "mobile": null,
                "nickname": "瓶子",
                "sex": 2,
                "province": "湖南",
                "city": "岳阳",
                "country": "中国",
                "headimgurl": "http://wx.qlogo.cn/mmopen/1Jm4XMIk9t2eOBibFm1vGcQleYicYBOlkIUic2H6SwfTxjryMgft1th9dBpIicwpdx3Gm9xFcuoXnAeA3n4LKP5XeJhibv2n8CKkD/0",
                "shop_id": 30,
                "shop_sub_id": 0,
                "staff_id": 0,
                "belong_to_staff_id": 0,
                "login_count": 1,
                "lastloginip": "183.12.66.187",
                "lastlogintime": 1441960414,
                "password": null,
                "type": 2,
                "status": 1,
                "member_refer": null,
                "scene_id": 45,
                "mpath": null,
                "mid": 0,
                "agent_id": 0,
                "agent_path": null,
                "sign_days": 0,
                "sign_time": 0,
                "is_subscribe": 1,
                "group_id": 1,
                "level_id": null,
                "point": 0,
                "wsh_code": null,
                "created": 1441958565,
                "modified": 1441960414,
                "deleted": 3
            }
        },
        {......}
    ],
    "page": {
        "per_page": 10,
        "total_count": 2,
        "current_page": 0,
        "total_page": 1
    }
}
```
## __获取预约者详细信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reserve/get-reserve-user-data
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 表主键 |
| reserve_setting_id | 是 | Integer(11) | 外键 |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 门店id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```json
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 394,
        "reserve_setting_id": 302,
        "user_id": 479,
        "user_data": "{\"name\":\"sdad\",\"mobile\":\"13246641470\",\"sex\":\"\\u5973\"}",
        "shop_sub_id": 0,
        "shop_id": 30,
        "status": 1,
        "created": 1441961521,
        "modified": 1441964191,
        "deleted": 1,
        "reserveSetting": {
            "id": 302,
            "wx_imagetxt_reply_id": 1106,
            "share_message_id": 0,
            "title": "tret",
            "summary": "活动简介",
            "note": "报名须知",
            "content": null,
            "items": "[{\"nametag\":\"name\",\"type\":\"text\",\"key\":\"\\u59d3\\u540d\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u540d\\u5b57\",\"check\":\"true\",\"addtype\":\"system\",\"$$hashKey\":\"object:20\"},{\"nametag\":\"sex\",\"type\":\"select\",\"key\":\"\\u6027\\u522b\",\"value\":\"\\u7537|\\u5973\",\"check\":\"true\",\"addtype\":\"system\",\"$$hashKey\":\"object:21\"},{\"nametag\":\"mobile\",\"type\":\"text\",\"key\":\"\\u624b\\u673a\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u624b\\u673a\",\"check\":\"true\",\"addtype\":\"system\",\"$$hashKey\":\"object:22\"},{\"nametag\":\"idCard\",\"type\":\"text\",\"key\":\"\\u8eab\\u4efd\\u8bc1\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u8eab\\u4efd\\u8bc1\\u53f7\\u7801\",\"check\":\"false\",\"addtype\":\"system\",\"$$hashKey\":\"object:23\"},{\"nametag\":\"bookedDate\",\"type\":\"calendar\",\"key\":\"\\u9884\\u7ea6\\u65e5\\u671f\",\"value\":\"\\u70b9\\u51fb\\u8f93\\u5165\",\"check\":\"false\",\"addtype\":\"system\",\"$$hashKey\":\"object:24\"},{\"nametag\":\"bookedTime\",\"type\":\"select\",\"key\":\"\\u9884\\u7ea6\\u65f6\\u95f4\",\"value\":\"0:00-1:00|1:00-2:00|2:00-3:00|3:00-4:00|4:00-5:00|5:00-6:00|6:00-7:00|7:00-8:00|8:00-9:00|9:00-10:00|10:00-11:00|11:00-12:00|12:00-13:00|13:00-14:00|14:00-15:00|15:00-16:00|16:00-17:00|17:00-18:00|18:00-19:00|19:00-20:00|20:00-21:00|21:00-22:00|22:00-23:00|23:00-24:00\",\"check\":\"false\",\"addtype\":\"system\",\"$$hashKey\":\"object:25\"},{\"nametag\":\"message\",\"type\":\"textarea\",\"key\":\"\\u7559\\u8a00\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u7559\\u8a00\\u5185\\u5bb9\",\"check\":\"false\",\"addtype\":\"system\",\"$$hashKey\":\"object:26\"},{\"nametag\":\"fShop\",\"type\":\"select\",\"key\":\"\\u9884\\u7ea6\\u5e97\\u94fa\",\"value\":\"\\u96be\\u7537\\u7537\\u5973\\u5973\\u7537\\u7537\\u5973\\u5973\\u7537|999999|agagag|111|\\u6d4b\\u8bd5|3\\u7ea7|adsd|\\u4e8c\\u7ea7\\u4ee3\\u7406\\u5546\\u300b\\u300b\\u52a0\\u76df\\u5e97|\\u4e8c\\u7ea7\\u4ee3\\u7406\\u5546\\u7ec8\\u7aef\\u5e97|as|testtest|test|\\u8fd9\\u91cc\\u6709\\u4e2a\\u76f4\\u8425\\u5e97|23|32133|321|122|pp\",\"check\":\"false\",\"addtype\":\"system\",\"$$hashKey\":\"object:27\"}]",
            "start_time": 1441960367,
            "end_time": 1442392369,
            "qrcode_id": 0,
            "shop_id": 30,
            "shop_sub_id": 0,
            "document_id": "250",
            "per_count": 20,
            "created": 1441960385,
            "modified": 1441960385,
            "deleted": 1,
            "share_type": 1
        }
    }
}
```
## __修改预约者信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reserve/update-reserve-user-data
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 表主键 |
| reserve_setting_id | 是 | Integer(11) | 外键 |
| shop_sub_id | 是 | Integer(11) | 门店id |
| user_id | 是 | Integer(11) | 用户id |
| shop_id | 是 | Integer(11) | 商家id |
| status | 否 | Integer(11) | 预约状态（1：预约成功，2：签到成功，3：已拒绝） |
| user_data | 否 | Integer(11) | 预约信息，json格式 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```json
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 293,
        "reserve_setting_id": 195,
        "user_id": 195,
        "user_data": "姓名：张三 性别：男 年龄：25",
        "shop_sub_id": 43,
        "shop_id": 5,
        "status": 1,
        "created": 1436152480,
        "modified": 1436155066,
        "deleted": 1
    }
}
```
## __启用预约者__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reserve/enable-reserve-user-data
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 表主键 |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 门店id |
| staff_id | 是 | Integer(11) |  员工id|
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```json
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 293,
        "reserve_setting_id": 195,
        "user_id": 195,
        "user_data": "{'':fk,'':}",
        "shop_sub_id": 43,
        "shop_id": 5,
        "status": 1,
        "created": 1436152480,
        "modified": 1436168397,
        "deleted": 1
    }
}
```
## __禁用预约者__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reserve/disable-reserve-user-data
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 表主键 |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 门店id |
| staff_id | 是 | Integer(11) |  员工id|
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```json
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 293,
        "reserve_setting_id": 195,
        "user_id": 195,
        "user_data": "{'':fk,'':}",
        "shop_sub_id": 43,
        "shop_id": 5,
        "status": 1,
        "created": 1436152480,
        "modified": 1436168397,
        "deleted": 2
    }
}
```
## __删除预约者信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reserve/delete-reserve-user-data
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 表主键 |
| reserve_setting_id | 是 | Integer(11) | 预约活动id |
| user_id | 是 | Integer(11) | 预约用户id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 门店id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```json
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 293,
        "reserve_setting_id": 195,
        "user_id": 195,
        "user_data": "{'':fk,'':}",
        "shop_sub_id": 43,
        "shop_id": 5,
        "status": 1,
        "created": 1436152480,
        "modified": 1436168397,
        "deleted": 2
    }
}
```
## __预约通过__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reserve/pass-user-data
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 表主键 |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 门店id |
| staff_id | 否 | Integer(11) |  员工id|
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```json
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 293,
        "reserve_setting_id": 195,
        "user_id": 195,
        "user_data": "{'':fk,'':}",
        "shop_sub_id": 43,
        "shop_id": 5,
        "status": 1,
        "created": 1436152480,
        "modified": 1436168397,
        "deleted": 1
    }
}
```
## __预约拒绝__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/reserve/reject-user-data
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 表主键 |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 门店id |
| staff_id | 否 | Integer(11) |  员工id|
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```json
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 293,
        "reserve_setting_id": 195,
        "user_id": 195,
        "user_data": "{'':fk,'':}",
        "shop_sub_id": 43,
        "shop_id": 5,
        "status": 2,
        "created": 1436152480,
        "modified": 1436168397,
        "deleted": 2
    }
}
```
