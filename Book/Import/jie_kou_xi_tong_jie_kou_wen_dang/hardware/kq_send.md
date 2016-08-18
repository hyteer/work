## __创建卡券赠送策略__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/create-strategy
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| card_type_id | 是 | Integer(11) | 卡券id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| name | 是 | String(11) | 规则名称 |
| type | 是 | Integer(4) | 1:消费指定金额2:购买指定商品 |
| amount | 否 | Integer(11) | 消费指定金额 |
| product_ids | 否 | String | 指定商品(多个逗号隔开) |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "cardStrategy":{
            "card_type_id":2,
            "type":2,
            "amount":0,
            "shop_id":30,
            "name":"song",
            "created":1441097708,
            "modified":1441097708,
            "id":4
        },
        "cardStrategyProduct":[
            {
                "card_strategy_id":4,
                "product_id":"202",
                "created":1441097708,
                "modified":1441097708,
                "id":1
            },
            {
                "card_strategy_id":4,
                "product_id":"200",
                "created":1441097708,
                "modified":1441097708,
                "id":2
            }
        ]
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />








## __修改卡券赠送策略__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/to-update-strategy
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| card_type_id | 否 | Integer(11) | 卡券id |
| type | 否 | Integer(4) | 1:消费指定金额2:购买指定商品 |
| name | 否 | String(11) | 规则名称 |
| amount | 否 | Integer(11) | 消费指定金额 |
| product_ids | 否 | String | 指定商品(多个逗号隔开) |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "cardStrategyProduct": [
      {
        "card_strategy_id": 56,
        "product_id": "329",
        "created": 1454485350,
        "modified": 1454485350,
        "id": 60
      },
      {
        "card_strategy_id": 56,
        "product_id": "300",
        "created": 1454485350,
        "modified": 1454485350,
        "id": 61
      }
    ],
    "cardStrategy": {
      "id": 56,
      "card_type_id": 132,
      "name": "1602031536",
      "type": 2,
      "amount": 0,
      "shop_id": 30,
      "shop_sub_id": null,
      "created": 1454485059,
      "modified": 1454485350,
      "deleted": 1
    }
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />








## __获取卡券赠送策略__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/get-strategy
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| card_type_id | 否 | String(100) | 卡券id |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 56,
    "card_type_id": 132,
    "name": "1602031536",
    "type": 2,
    "amount": 0,
    "shop_id": 30,
    "shop_sub_id": null,
    "created": 1454485059,
    "modified": 1454485350,
    "deleted": 1,
    "cardStrategyProducts": [
      {
        "id": 60,
        "card_strategy_id": 56,
        "product_id": 329,
        "created": 1454485350,
        "modified": 1454485350,
        "product": {
          "id": 329,
          "product_category_id": 221,
          "product_category_path": "/219/221/",
          "product_kind_ids": "113;",
          "name": "cs",
          "subtitle": null,
          "keyword": null,
          "product_type": 1,
          "product_no": null,
          "show_price": 0,
          "prod_weight": "20.000",
          "shop_id": 30,
          "shop_sub_id": 0,
          "hits": 0,
          "sales": 100,
          "status": 1,
          "postage_fee_type": 0,
          "quota": 0,
          "sort": 0,
          "is_pre_sale": 2,
          "pre_sale_id": 0,
          "show_sale_num": 2,
          "share_message_id": 1893,
          "sync_offline_sku": 2,
          "sale_scope": 1,
          "covers_id": 91759,
          "is_recommend": 2,
          "created": 1453964741,
          "modified": 1454079527,
          "deleted": 1
        }
      },
      {
        "id": 61,
        "card_strategy_id": 56,
        "product_id": 300,
        "created": 1454485350,
        "modified": 1454485350,
        "product": {
          "id": 300,
          "product_category_id": 203,
          "product_category_path": "/189/203/",
          "product_kind_ids": "113;",
          "name": "sd胜多负少",
          "subtitle": null,
          "keyword": null,
          "product_type": 1,
          "product_no": null,
          "show_price": 10000,
          "prod_weight": "10.000",
          "shop_id": 30,
          "shop_sub_id": 0,
          "hits": 0,
          "sales": 100,
          "status": 1,
          "postage_fee_type": 0,
          "quota": 10,
          "sort": 0,
          "is_pre_sale": 2,
          "pre_sale_id": 0,
          "show_sale_num": 2,
          "share_message_id": 1632,
          "sync_offline_sku": 2,
          "sale_scope": 1,
          "covers_id": 1375,
          "is_recommend": 2,
          "created": 1451378971,
          "modified": 1453951911,
          "deleted": 1
        }
      }
    ],
    "cardTypeInfo": {
      "id": 132,
      "wx_card_id": null,
      "card_type": 1,
      "wx_card_type": 1,
      "get_card_type": 1,
      "examine_type": 1,
      "card_money": 2200,
      "money_limit": 100,
      "logo_url": "http://imgcache.vikduo.com/static/8d665aa70eedd30e5ad62edcc7dc4979.png",
      "code_type": 1,
      "brand_name": "44444",
      "title": "4444",
      "color": "#55bd47",
      "notice": "1",
      "service_phone": "18765995632",
      "description": "11",
      "get_limit": 111,
      "can_share": 1,
      "can_give_friend": 2,
      "date_info_type": 2,
      "begin": 0,
      "end": 1,
      "quantity": 111,
      "stock": 81,
      "range": null,
      "deal_detail": "价值22元代金券1张，满1元可使用",
      "cancel_number": 0,
      "custom_url_name": null,
      "custom_url": null,
      "custom_url_sub_title": null,
      "promotion_url_name": null,
      "promotion_url": null,
      "promotion_url_sub_title": null,
      "shop_id": 30,
      "shop_sub_id": null,
      "created": 1453714491,
      "modified": 1454059910,
      "deleted": 1
    }
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __查找卡券赠送策略列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/find-strategy-list
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| card_type_id | 否 | Integer(11) | 卡券id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
* **注意：sort排序可选字段['id']**

##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": 1,
      "card_type_id": 2,
      "name": "song2333",
      "type": 1,
      "amount": 100,
      "shop_id": 30,
      "shop_sub_id": null,
      "created": 1441097490,
      "modified": 1441160029,
      "deleted": 1,
      "cardTypeInfo": {
        "id": 2,
        "wx_card_id": "p8uFCsxKuOby5mP3PySSP_KSMOr0",
        "card_type": 2,
        "wx_card_type": 1,
        "get_card_type": 1,
        "examine_type": 1,
        "card_money": 100,
        "money_limit": 200,
        "logo_url": "http://imgcache.vikduo.com/static/3e70ca4d483e7b65249fca8cf394a562.jpg",
        "code_type": 1,
        "brand_name": "WSH测试",
        "title": "微信卡券1027",
        "color": "#10ad61",
        "notice": "出示",
        "service_phone": "13245553344",
        "description": "使用须知",
        "get_limit": 11,
        "can_share": 1,
        "can_give_friend": 1,
        "date_info_type": 1,
        "begin": 1445904000,
        "end": 1448668800,
        "quantity": 111,
        "stock": 79,
        "range": ",192,",
        "deal_detail": "价值12元代金券1张，满33元可使用",
        "cancel_number": 0,
        "custom_url_name": null,
        "custom_url": null,
        "custom_url_sub_title": null,
        "promotion_url_name": null,
        "promotion_url": null,
        "promotion_url_sub_title": null,
        "shop_id": 30,
        "shop_sub_id": null,
        "created": 1441090649,
        "modified": 1454481619,
        "deleted": 1
      }
    },
    ......
  ],
  "page": {
    "per_page": 20,
    "total_count": 39,
    "current_page": 0,
    "total_page": 2
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __删除卡券赠送策略__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/del-strategy
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
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

## __创建卡券直接领取活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/create-receive
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| card_type_id | 是 | Integer(11) | 卡券id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| begin_time | 否 | Integer(11) | 开始时间 |
| end_time | 否 | Integer(11) | 结束时间 |
| share_type | 是 | Integer(4) |显示和分享模式（1.显示且能分享、2.不能显示且能分享、3.不能显示且不能分享）|
| shareMessage.title | 否 | String(100) | 分享标题 |
| shareMessage.desc | 否 | String(100) | 分享描述 |
| shareMessage.pic_id | 否 | Integer(11) | document_lib表外键 |
| news.title | 否 | String(100) | 分享标题 |
| news.description | 否 | String(100) | 分享描述 |
| news.document_id | 否 | Integer(11) | document_lib表外键 |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "cardReceive":{
            "shop_id":30,
            "card_type_id":2,
            "begin_time":1441181465,
            "end_time":1441181465,
            "created":1441181514,
            "modified":1441181514,
            "id":2
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __更新卡券直接领取活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/to-update-receive
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | id |
| card_type_id | 否 | Integer(11) | 卡券id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| begin_time | 否 | Integer(11) | 开始时间 |
| end_time | 否 | Integer(11) | 结束时间 |
| share_type | 是 | Integer(4) |显示和分享模式（1.显示且能分享、2.不能显示且能分享、3.不能显示且不能分享
| shareMessage.title | 否 | String(100) | 分享标题 |
| shareMessage.desc | 否 | String(100) | 分享描述 |
| shareMessage.pic_id | 否 | Integer(11) | document_lib表外键 |
| news.title | 否 | String(100) | 分享标题 |
| news.description | 否 | String(100) | 分享描述 |
| news.document_id | 否 | Integer(11) | document_lib表外键 |
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



## __获取卡券直接领取活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/get-receive
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动的id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
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


## __查找卡券直接领取活动列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/find-receive-list
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| card_type_id | 否 | Integer(11) | 卡券id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
* **注意：sort排序可选字段['id']**

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


## __删除卡券直接领取活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/del-receive
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动的id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
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


## __手动派发卡券__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/hand-send-card-info
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| card_type_id | 是 | Integer(11) | 卡券的id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| to_user_ids | 否 | Array | 要派发的用户 |
| user_group | 否 | Integer(11) | 用户分组id |
| code | 否 | string(50) | 卡券code |
* **to_user_ids、user_group必须给一个**

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


## __领取手动派发卡券__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/accept-hand-send-card
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| wx_card_id | 是 | string(100) | 用户领取卡券的id |
| shop_id | 是 | Integer(11) | 商家id |
| user_open_id | 是 | string(100) | 领取的用户 |
| from_user_open_id | 否 | string(100) | 转赠来源用户 |
| code | 否 | string(100) | 领取的用户 |
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


## __直接领取卡券__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/receive-card-info
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| card_type_id | 是 | Integer(11) | 卡券的id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| to_user_id | 是 | Integer(11) | 要领取的用户 |
| code | 否 | string(50) | 卡券code |
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


## __接收赠送的卡券__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/accept-card-info
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| card_info_id | 是 | Integer(11) | 用户领取卡券的id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| to_user_id | 是 | Integer(11) | 领取的用户 |
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


## __获取用户的卡券__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/get-card-info
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 用户领取卡券的id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
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


## __查找用户的卡券列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/find-card-info-list
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| card_type_id | 否 | Integer(11) | 卡券id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| from_user_id | 否 | Integer(11) | 转赠的用户 |
| to_user_id | 否 | Integer(11) | 领取的用户 |
| status | 否 | array | 领取状态 |
| type | 否 | Integer(4) | 领券类型 默认1微商户系统 2微信 |
| receive_type | 否 | Integer(4) |
获取途径1直接领取,2手动派送,3抽奖活动,4购物赠送,5游戏奖励|
| deleted | 否 | Integer(11) | 状态1.是、2.否 |
| order_amount | 否 | Integer(11) | 订单金额 |
| valid_time | 否 | boolean | 是否在有效期内 |
* **注意：sort排序可选字段['id']**

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


## __删除用户的卡券__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/del-card-info
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 否 | Integer(11) | 用户领取卡券的id |
| code | 否 | string(100) | 用户领取卡券的code |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
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

## __核销用户的卡券__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/cancel-card
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| code | 是 | string(100) | 用户领取卡券的code|
| shop_id | 是 | Integer(11) | 商家id |
| staff_id | 否 | Integer(11) | 核销员id |
| staff_open_id | 否 | string(100) | 核销员openid |
| total_price | 否 | Integer(11) | 消费的金额 |
| weixin_sync | 否 | boolean | 是否同步到微信，默认同步 |
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
