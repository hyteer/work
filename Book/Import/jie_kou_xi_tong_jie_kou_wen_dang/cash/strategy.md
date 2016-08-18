# 消费赠送
## __添加消费赠送规则__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/create-cash-redpack-strategy
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| cash_redpack_id | 是 | Integer(11) | 红包活动id |
| type | 是 | Integer(4) | 1:消费指定金额2:购买指定商品 |
| name | 是 | String(50) | 规则名称 |
| amount | 否 | Integer(11) | 指定金额 |
| product_ids | 否 | Array | 指定商品id数组 |
| deleted | 否 | Integer(4) | 是否开启 1是 2否 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "cashRedpackStrategy": {
      "cash_redpack_id": 2,
      "type": 2,
      "shop_id": 30,
      "shop_sub_id": 0,
      "deleted": 2,
      "name": "满百送",
      "created": 1451378758,
      "modified": 1451378758,
      "id": 5
    },
    "cashRedpackStrategyProduct": [
      {
        "cash_redpack_strategy_id": 5,
        "product_id": 200,
        "created": 1451378758,
        "modified": 1451378758,
        "id": 1
      },
      {
        "cash_redpack_strategy_id": 5,
        "product_id": 201,
        "created": 1451378758,
        "modified": 1451378758,
        "id": 2
      }
    ]
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __修改消费赠送规则__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/update-cash-redpack-strategy
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 规则id |
| shop_id | 是 | Integer(11) | 商家id |
| cash_redpack_id | 是 | Integer(11) | 红包活动id |
| type | 是 | Integer(4) | 1:消费指定金额2:购买指定商品 |
| name | 是 | String(50) | 规则名称 |
| amount | 否 | Integer(11) | 指定金额 |
| product_ids | 否 | Array | 指定商品id数组 |
| deleted | 否 | Integer(4) | 是否开启 1是 2否 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "cashRedpackStrategy": {
      "id": 5,
      "cash_redpack_id": 2,
      "name": "满百送",
      "type": 1,
      "amount": 1000,
      "shop_id": 30,
      "shop_sub_id": 0,
      "deleted": 2,
      "created": 1451378758,
      "modified": 1451379042
    }
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __获取消费赠送规则详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/get-cash-redpack-strategy
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 规则id |
| shop_id | 是 | Integer(11) | 商家id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 1,
    "cash_redpack_id": 2,
    "name": "满百送",
    "type": 2,
    "amount": 10000,
    "shop_id": 30,
    "shop_sub_id": 0,
    "deleted": 2,
    "created": 1451378580,
    "modified": 1451378952,
    "product": [
      {
        "id": 200,
        "product_category_id": 157,
        "product_category_path": "/155/156/157/",
        "product_kind_ids": "113;114;115;",
        "name": "瓶子专属",
        "subtitle": null,
        "keyword": null,
        "product_type": 1,
        "product_no": null,
        "show_price": 12100,
        "prod_weight": "1.000",
        "shop_id": 30,
        "shop_sub_id": 0,
        "hits": 0,
        "sales": 5,
        "status": 1,
        "postage_fee_type": 0,
        "quota": 0,
        "sort": 2,
        "is_pre_sale": 2,
        "pre_sale_id": 0,
        "show_sale_num": 2,
        "share_message_id": 909,
        "sync_offline_sku": 2,
        "sale_scope": 1,
        "covers_id": 346,
        "is_recommend": 1,
        "created": 1440403773,
        "modified": 1449480088,
        "deleted": 1
      }
    ]
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __获取消费赠送规则列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/find-cash-redpack-strategy-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| cash_redpack_id | 否 | Integer(11) | 红包活动id |
| type | 否 | Integer(4) | 1:消费指定金额2:购买指定商品 |
| name | 否 | String(50) | 规则名称 |
| deleted | 否 | Integer(4) | 是否开启 1是 2否 |
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
      "cash_redpack_id": 2,
      "name": "满百送",
      "type": 2,
      "amount": 10000,
      "shop_id": 30,
      "shop_sub_id": 0,
      "deleted": 2,
      "created": 1451378580,
      "modified": 1451378952,
      "redpack": {
        "id": "2",
        "send_name": "商户名称",
        "act_name": "红包活动",
        "type": 1,
        "quantity": 10,
        "send_num": 0,
        "min_value": 100,
        "max_value": 100,
        "total_num": 1,
        "amt_type": null,
        "wishing": "祝福！",
        "remark": "备注",
        "platform": 1,
        "can_share": 2,
        "shop_id": 30,
        "shop_sub_id": 0,
        "deleted": 1,
        "created": 1451273292,
        "modified": 1451273292
      }
    }
  ],
  "page": {
    "per_page": 20,
    "total_count": 1,
    "current_page": 0,
    "total_page": 0
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __启用规则__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/enable-cash-redpack-strategy
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 规则id |
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



## __禁用规则__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/disable-cash-redpack-strategy
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 规则id |
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



## __删除规则__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/del-cash-redpack-strategy
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 规则id |
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

