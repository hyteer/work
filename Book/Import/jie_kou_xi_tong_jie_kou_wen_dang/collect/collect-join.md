## __新增众筹参与__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/create-collect-join
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|collect_id|是|Integer(11)|众筹活动id|
| title|否|String(100)|摘要|
| uid|是|Integer(11)|用户id|
| mobile|否|String(20)|手机号|
| name|否|String(10)|姓名|
| address|否|String(220)|住址|
| collect_product_id|否|Integer(11)|活动产品id|
| collect_redpacket_id|否|Integer(11)|活动关联的红包|
| collect_custom_gift_id|否|Integer(11)|用户自定义礼物|
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
        "uid": "157",
        "status": 2,
        "mobile": "15823568956",
        "name": "大幅减少地方",
        "address": "考虑国家实力可见弗兰克",
        "collect_product_id": "1",
        "collect_redpacket_id": "",
        "created": 1436944457,
        "collect_id": "7",
        "title": "呵呵",
        "collect_custom_gift_id": "",
        "shop_id": "5",
        "shop_sub_id": "43",
        "modified": 1436944457,
        "id": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __修改众筹参与__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/update-collect-join
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|众筹参与id|
| title|否|String(100)|摘要|
| mobile|否|String(20)|手机号|
| name|是|String(10)|姓名|
| address|是|String(220)|住址|
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
        "uid": "157",
        "status": 2,
        "mobile": "15823568956",
        "name": "大幅减少地方",
        "address": "考虑国家实力可见弗兰克",
        "collect_product_id": "1",
        "collect_redpacket_id": "",
        "created": 1436944457,
        "collect_id": "7",
        "title": "呵呵",
        "collect_custom_gift_id": "",
        "shop_id": "5",
        "shop_sub_id": "43",
        "modified": 1436944457,
        "id": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __获取众筹参与详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/get-collect-join
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 参与id |
| collect_id | 是 | Integer(11) | 众筹id |
| uid | 否 | Integer(11) | 用户id |
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
        "id": 1,
        "collect_id": 2,
        "title": "呵呵",
        "uid": 157,
        "status": 1,
        "mobile": "15823568956",
        "name": "大幅减少地方",
        "address": "考虑国家实力可见弗兰克",
        "collect_product_id": 1,
        "collect_redpacket_id": null,
        "collect_custom_gift_id": null,
        "current_num": 0,
        "current_user_num": null,
        "shop_id": 5,
        "shop_sub_id": 43,
        "created": 1436944457,
        "modified": 1436949601,
        "collect": {
            "id": 2,
            "name": "未知点赞活动名称",
            "share_message_id": 198,
            "wx_imagetxt_reply_id": 178,
            "is_attention": 2,
            "start_time": 1436936675,
            "end_time": 1437023075,
            "type": 3,
            "document_id": 0,
            "rule": "未知点赞活动规则",
            "shop_id": 5,
            "shop_sub_id": 43,
            "created": 1436936675,
            "modified": 1437011720,
            "deleted": 1
        },
        "collectProduct": {
            "id": 1,
            "collect_id": 7,
            "product_id": 59,
            "product_sku_id": 38,
            "price": 1,
            "give": 0,
            "number": 2,
            "count": 1,
            "lastCount": 1,
            "minus": 1,
            "shop_id": 5,
            "shop_sub_id": 43,
            "product": {
                "id": 59,
                "product_category_id": 66,
                "product_category_path": "1/65/66/",
                "product_kind_ids": "1,2,3,",
                "name": "商品ss",
                "subtitle": "副标题ff",
                "keyword": "关键字",
                "product_type": 1,
                "product_no": "21313",
                "show_price": 123,
                "prod_weight": "12.000",
                "shop_id": 5,
                "shop_sub_id": 43,
                "hits": 123,
                "sales": 2,
                "status": 1,
                "postage_fee_type": 1,
                "quota": 0,
                "sort": 1,
                "is_pre_sale": 1,
                "pre_sale_id": 2,
                "show_sale_num": 1,
                "share_message_id": 28,
                "sync_offline_sku": 2,
                "sale_scope": 1,
                "covers_id": 2,
                "is_recommend": 2,
                "created": 1435225334,
                "modified": 1436967416,
                "deleted": 3,
                "covers": []
            },
            "productSku": {
                "id": 38,
                "sku_no": "123",
                "product_id": 59,
                "name": "sku",
                "reserves": 412,
                "freez_reserve": 10000,
                "market_price": 1,
                "cost_price": 1,
                "retail_price": 1,
                "sales": 456,
                "status": 1,
                "barcode": "456",
                "barcode_pic": 456,
                "shop_id": 5,
                "shop_sub_id": 43,
                "created": 1435225334,
                "modified": 1435225334
            }
        },
        "collectRedpacket": [],
        "collectCustomGift": [],
        "userInfo": {
            "id": 157,
            "mobile": null,
            "nickname": "瓶子",
            "sex": 2,
            "province": "湖南",
            "city": "岳阳",
            "country": "中国",
            "headimgurl": "http://wx.qlogo.cn/mmopen/1n6F4evsEjQyhGVkxP88ZQwQcyEamo5ot4b1O0anibXqJ2FEqzCHZhuib5HOxlRKb0hlQRbg1HYKGBltjgTcpuDO9ic7p5JXFJo/0",
            "shop_id": 5,
            "shop_sub_id": 43,
            "staff_id": 0,
            "login_count": 0,
            "lastloginip": null,
            "lastlogintime": 0,
            "password": null,
            "type": 2,
            "status": 1,
            "member_refer": null,
            "weixin": null,
            "scene_id": null,
            "mpath": null,
            "mid": null,
            "code": null,
            "sign_days": 0,
            "sign_time": 0,
            "is_subscribe": 1,
            "group_id": 1,
            "level_id": null,
            "point": null,
            "wsh_code": null,
            "created": 1436170179,
            "modified": 1436170194,
            "deleted": 1
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />




## __兑奖__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/sent-join-gift
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 参与id |
| collect_id | 是 | Integer(11) | 众筹id |
| uid | 是 | Integer(11) | 用户id |
| staff_id | 是 | Integer(11) | 员工id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
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


## __获取众筹参与详情包含参与者信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/get-collect-join-with-click
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 参与id |
| collect_id | 是 | Integer(11) | 众筹id |
| u_id | 否 | Integer(11) | 用户id |
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
        "id": 1,
        "collect_id": 2,
        "title": "呵呵",
        "uid": 157,
        "status": 1,
        "mobile": "15823568956",
        "name": "大幅减少地方",
        "address": "考虑国家实力可见弗兰克",
        "collect_product_id": 1,
        "collect_redpacket_id": null,
        "collect_custom_gift_id": null,
        "current_num": 0,
        "current_user_num": null,
        "shop_id": 5,
        "shop_sub_id": 43,
        "created": 1436944457,
        "modified": 1436949601,
        "collect": {
            "id": 2,
            "name": "未知点赞活动名称",
            "share_message_id": 198,
            "wx_imagetxt_reply_id": 178,
            "is_attention": 2,
            "start_time": 1436936675,
            "end_time": 1437023075,
            "type": 3,
            "document_id": 0,
            "rule": "未知点赞活动规则",
            "shop_id": 5,
            "shop_sub_id": 43,
            "created": 1436936675,
            "modified": 1437011720,
            "deleted": 1
        },
        "collectProduct": {
            "id": 1,
            "collect_id": 7,
            "product_id": 59,
            "product_sku_id": 38,
            "price": 1,
            "give": 0,
            "number": 2,
            "count": 1,
            "lastCount": 1,
            "minus": 1,
            "shop_id": 5,
            "shop_sub_id": 43,
            "product": {
                "id": 59,
                "product_category_id": 66,
                "product_category_path": "1/65/66/",
                "product_kind_ids": "1,2,3,",
                "name": "商品ss",
                "subtitle": "副标题ff",
                "keyword": "关键字",
                "product_type": 1,
                "product_no": "21313",
                "show_price": 123,
                "prod_weight": "12.000",
                "shop_id": 5,
                "shop_sub_id": 43,
                "hits": 123,
                "sales": 2,
                "status": 1,
                "postage_fee_type": 1,
                "quota": 0,
                "sort": 1,
                "is_pre_sale": 1,
                "pre_sale_id": 2,
                "show_sale_num": 1,
                "share_message_id": 28,
                "sync_offline_sku": 2,
                "sale_scope": 1,
                "covers_id": 2,
                "is_recommend": 2,
                "created": 1435225334,
                "modified": 1436967416,
                "deleted": 3,
                "covers": []
            },
            "productSku": {
                "id": 38,
                "sku_no": "123",
                "product_id": 59,
                "name": "sku",
                "reserves": 412,
                "freez_reserve": 10000,
                "market_price": 1,
                "cost_price": 1,
                "retail_price": 1,
                "sales": 456,
                "status": 1,
                "barcode": "456",
                "barcode_pic": 456,
                "shop_id": 5,
                "shop_sub_id": 43,
                "created": 1435225334,
                "modified": 1435225334
            }
        },
        "collectRedpacket": [],
        "collectCustomGift": [],
        "userInfo": {
            "id": 157,
            "mobile": null,
            "nickname": "瓶子",
            "sex": 2,
            "province": "湖南",
            "city": "岳阳",
            "country": "中国",
            "headimgurl": "http://wx.qlogo.cn/mmopen/1n6F4evsEjQyhGVkxP88ZQwQcyEamo5ot4b1O0anibXqJ2FEqzCHZhuib5HOxlRKb0hlQRbg1HYKGBltjgTcpuDO9ic7p5JXFJo/0",
            "shop_id": 5,
            "shop_sub_id": 43,
            "staff_id": 0,
            "login_count": 0,
            "lastloginip": null,
            "lastlogintime": 0,
            "password": null,
            "type": 2,
            "status": 1,
            "member_refer": null,
            "weixin": null,
            "scene_id": null,
            "mpath": null,
            "mid": null,
            "code": null,
            "sign_days": 0,
            "sign_time": 0,
            "is_subscribe": 1,
            "group_id": 1,
            "level_id": null,
            "point": null,
            "wsh_code": null,
            "created": 1436170179,
            "modified": 1436170194,
            "deleted": 1
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __获取众筹参与列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/find-collect-join
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| collect_id | 否 | Integer(11) | 众筹id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| uid | 否 | Integer(11) | 用户id |
| collect_product_id|否|Integer(11)|众筹关联产品id|
| collect_redpacket_id | 否 | Integer(11) | 众筹关联红包id |
| collect_custom_gift_id | 否 | Integer(11) | 众筹关联自定义礼品id |
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
            "collect_id": 7,
            "title": "呵呵",
            "uid": 157,
            "status": 2,
            "mobile": "15823568956",
            "name": "大幅减少地方",
            "address": "考虑国家实力可见弗兰克",
            "collect_product_id": 1,
            "collect_redpacket_id": null,
            "collect_custom_gift_id": null,
            "current_num": 0,
            "shop_id": 5,
            "shop_sub_id": 43,
            "created": 1436944457,
            "modified": 1436949601
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
