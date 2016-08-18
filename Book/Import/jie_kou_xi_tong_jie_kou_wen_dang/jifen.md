## __新增积分活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-consumption/create
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| activity.relate_product_type | 是 | Integer(4) | 关联产品类型（1.按关联表、2.全部） |
| activity.name | 是 | String(250) | 活动名称 |
| activity.desc | 否 | String(500) | 活动描述/规则 |
| activity.sort | 否 | Integer(11) | 排序 |
| activity.expire_type | 是 | Integer(4) | 有效期类型1.指定时间范围、2.无时间限制 |
| activity.start_time | 是 | Integer(11) | 活动开始时间 |
| activity.end_time | 是 | Integer(11) | 活动结束时间 |
| activity.shop_id | 是 | Integer(11) | 商家id |
| activity.shop_sub_id | 否 | Integer(11) | 店铺id |
| pointsConsumption.type | 是 | Integer(4) | 积分赠送类型（1.消费送、2.单次消费满送） |
| pointsConsumption.amount | 是 | Integer(11) | 消费金额 |
| pointsConsumption.points | 是 | Integer(11) | 赠送积分 |
| shareMessage.title | 否 | String(100) | 分享标题 |
| shareMessage.desc | 否 | String(100) | 分享描述 |
| shareMessage.pic_id | 否 | Integer(11) | document_lib表外键 |
| news.title | 否 | String(100) | 微信标题 |
| news.description | 否 | String(100) | 微信描述 |
| news.document_id | 否 | Integer(11) | document_lib表外键 |
| news.url | 否 | String(200) | 图文链接 |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode":0,
  "errmsg":"ok",
  "data":{
    "activity":{
      "relate_product_type":2,
      "postage_setting_id":0,
      "expire_type":2,
      "wx_imagetxt_reply_id":0,
      "share_message_id":0,
      "name":"testssss",
      "start_time":2,
      "end_time":2,
      "shop_id":5,
      "shop_sub_id":43,
      "activity_type":4,
      "created":1435802697,
      "modified":1435802697,
      "deleted":1,
      "id":62
    },
    "pointsConsumption":{
      "type":1,
      "amount":1,
      "points":1,
      "shop_id":5,
      "shop_sub_id":43,
      "activity_id":62,
      "id":4
    }
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取积分活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-consumption/get
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动的id |
| shop_id | 是 | Integer(11) | 店铺id |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 622,
        "activity_type": 4,
        "relate_product_type": 2,
        "postage_setting_id": 0,
        "name": "日常积分",
        "desc": null,
        "sort": null,
        "expire_type": 2,
        "start_time": 0,
        "end_time": 0,
        "wx_qrcode_id": null,
        "wx_imagetxt_reply_id": 0,
        "share_message_id": 0,
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": 1452502727,
        "modified": 1452502730,
        "deleted": 2,
        "share_type": 1,
        "pointsConsumption": {
            "id": 89,
            "activity_id": 622,
            "type": 1,
            "amount": 100,
            "points": 1,
            "shop_id": 30,
            "shop_sub_id": 0
        },
        "shareMessage": [],
        "news": []
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取积分活动列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-consumption/find-points-consumption-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
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
            "id": 622,
            "activity_type": 4,
            "relate_product_type": 2,
            "postage_setting_id": 0,
            "name": "日常积分",
            "desc": null,
            "sort": null,
            "expire_type": 2,
            "start_time": 0,
            "end_time": 0,
            "wx_qrcode_id": null,
            "wx_imagetxt_reply_id": 0,
            "share_message_id": 0,
            "shop_id": 30,
            "shop_sub_id": 0,
            "created": 1452502727,
            "modified": 1452502730,
            "deleted": 2,
            "share_type": 1,
            "pointsConsumption": {
                "id": 89,
                "activity_id": 622,
                "type": 1,
                "amount": 100,
                "points": 1,
                "shop_id": 30,
                "shop_sub_id": 0
            }
        },
        {.....}
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


## __修改积分打折活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-consumption/to-update
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| activity.id | 是 | Integer(11) | 活动id |
| activity.name | 是 | String(250) | 活动名称 |
| activity.desc | 否 | String(500) | 活动描述/规则 |
| activity.sort | 否 | Integer(11) | 排序 |
| activity.expire_type | 是 | Integer(4) | 有效期类型1.指定时间范围、2.无时间限制 |
| activity.start_time | 是 | Integer(11) | 活动开始时间 |
| activity.end_time | 是 | Integer(11) | 活动结束时间 |
| activity.shop_id | 是 | Integer(11) | 商家id |
| pointsConsumption.id | 是 | Integer(11) | 拍码id |
| pointsConsumption.amount | 否 | Integer(11) | 消费金额 |
| pointsConsumption.points | 否 | Integer(11) | 赠送积分 |


<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "activity": {
            "id": 669,
            "activity_type": 4,
            "relate_product_type": 2,
            "postage_setting_id": 0,
            "name": "活动名称",
            "desc": null,
            "sort": null,
            "expire_type": 1,
            "start_time": 1454549105,
            "end_time": 1455585905,
            "wx_qrcode_id": null,
            "wx_imagetxt_reply_id": 0,
            "share_message_id": 0,
            "shop_id": 30,
            "shop_sub_id": 0,
            "created": 1454462712,
            "modified": 1454462741,
            "deleted": 2,
            "share_type": 1,
            "pointsConsumption": {
                "id": 90,
                "activity_id": 669,
                "type": 2,
                "amount": 100,
                "points": 1,
                "shop_id": 30,
                "shop_sub_id": 0
            }
        },
        "pointsConsumption": {
            "id": 90,
            "activity_id": 669,
            "type": 2,
            "amount": 100,
            "points": 1,
            "shop_id": 30,
            "shop_sub_id": 0
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __删除积分活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-consumption/general-del
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
    "data":null
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __开启积分活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-consumption/general-enable
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
        "id": 669,
        "activity_type": 4,
        "relate_product_type": 2,
        "postage_setting_id": 0,
        "name": "活动名称",
        "desc": null,
        "sort": null,
        "expire_type": 1,
        "start_time": 1454549105,
        "end_time": 1455585905,
        "wx_qrcode_id": null,
        "wx_imagetxt_reply_id": 0,
        "share_message_id": 0,
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": 1454462712,
        "modified": 1454462787,
        "deleted": 1,
        "share_type": 1,
        "pointsConsumption": {
            "id": 90,
            "activity_id": 669,
            "type": 2,
            "amount": 100,
            "points": 1,
            "shop_id": 30,
            "shop_sub_id": 0
        },
        "shareMessage": [],
        "news": []
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __关闭积分活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-consumption/general-disable
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
        "id": 669,
        "activity_type": 4,
        "relate_product_type": 2,
        "postage_setting_id": 0,
        "name": "活动名称",
        "desc": null,
        "sort": null,
        "expire_type": 1,
        "start_time": 1454549105,
        "end_time": 1455585905,
        "wx_qrcode_id": null,
        "wx_imagetxt_reply_id": 0,
        "share_message_id": 0,
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": 1454462712,
        "modified": 1454463086,
        "deleted": 2,
        "share_type": 1,
        "pointsConsumption": {
            "id": 90,
            "activity_id": 669,
            "type": 2,
            "amount": 100,
            "points": 1,
            "shop_id": 30,
            "shop_sub_id": 0
        },
        "shareMessage": [],
        "news": []
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __新增积分商品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-consumption/create-points-consumption-goods
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| points_consumption_id | 是 | Integer(11) | 积分活动id |
| product_id | 是 | Integer(11) | 关联的商品id |
| shop_id | 是 | Integer(11) | 商家id |
| product_sku_id | 是 | Integer(11) | 关联的sku ID |
| shop_sub_id | 是 | Integer(11) | 店铺id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "points_consumption_id":1,
        "product_id":45,
        "product_sku_id":24,
        "shop_id":5,
        "shop_sub_id":43,
        "created":1435804327,
        "modified":1435804327,
        "id":4
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取积分商品列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-consumption/find-points-consumption-goods-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| points_consumption_id | 否 | Integer(11) | 积分规则id |
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
            "id":3,
            "points_consumption_id":1,
            "product_id":65,
            "product_sku_id":44,
            "shop_id":5,
            "shop_sub_id":43,
            "created":1435717709,
            "modified":1435804125
        }
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



## __删除积分商品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/points-consumption/del-points-consumption-goods
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

