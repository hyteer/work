# 红包管理
## __添加红包__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/create-cash-redpack
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| send_name | 是 | String(32） | 商户名称 |
| act_name | 是 | String(32） | 活动名称 |
| type | 是 | Integer(4) | 红包类型 1定额 2随机|
| quantity | 否 | Integer(11) | 红包数量（open平台可不填） |
| min_value | 否 | Integer(11) |  最小金额(定额min=max，open平台可不填) |
| max_value | 否 | Integer(11) | 最大金额(定额min=max，open平台可不填) |
| total_num | 是 | Integer(11) | 定值为1 |
| wishing | 是 | String(128) | 祝福语 |
| remark | 是 | String(256) | 备注|
| can_share | 否 | Integer(4) | 是否可共享活动 1是 2否，默认2 |
| deleted | 否 | Integer(4) | 是否开启 1是 2否 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "type": 1,
    "quantity": 10,
    "send_num": 0,
    "min_value": 100,
    "max_value": 100,
    "total_num": 1,
    "platform": 1,
    "can_share": 2,
    "shop_sub_id": 0,
    "deleted": 1,
    "send_name": "商户名称",
    "act_name": "红包活动",
    "wishing": "祝福你妹！",
    "remark": "备注",
    "shop_id": 30,
    "created": 1451372010,
    "modified": 1451372010,
    "id": "4"
  }
}
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __编辑红包信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/update-cash-redpack
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 红包id |
| shop_id | 是 | Integer(11) | 商家id |
| act_name | 否 | String(32） | 活动名称 |
| send_name | 否 | String(32） | 发送方名称 |
| wishing | 否 | String(128) | 祝福语 |
| remark | 否 | String(256) | 备注|
| can_share | 否 | Integer(4) | 是否可共享活动 1是 2否 |
| deleted | 否 | Integer(4) | 是否开启 1是 2否 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": "1",
    "send_name": "商户名称",
    "act_name": "红包大派送",
    "type": 1,
    "quantity": 10,
    "send_num": 0,
    "min_value": 100,
    "max_value": 100,
    "total_num": 1,
    "amt_type": null,
    "wishing": "恭喜恭喜！",
    "remark": "备注",
    "platform": 1,
    "shop_id": 30,
    "shop_sub_id": 0,
    "deleted": 1,
    "created": 1451264923,
    "modified": 1451284192
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取红包详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/get-cash-redpack
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 红包id |
| shop_id | 是 | Integer(11) | 商家id |
| type | 否 | Integer(4) | 红包类型 1定额 2随机|
| can_share | 否 | Integer(4) | 是否可共享活动 1是 2否 |
| deleted | 否 | Integer(4) | 是否开启 1是 2否 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": "1",
    "send_name": "商户名称",
    "act_name": "红包大派送",
    "type": 1,
    "quantity": 10,
    "send_num": 0,
    "min_value": 100,
    "max_value": 100,
    "total_num": 1,
    "amt_type": null,
    "wishing": "恭喜恭喜！",
    "remark": "备注",
    "platform": 1,
    "can_share": 2,
    "shop_id": 30,
    "shop_sub_id": 0,
    "deleted": 1,
    "created": 1451264923,
    "modified": 1451372064
  }
}
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __获取红包列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/find-cash-redpack-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| type | 否 | Integer(4) | 红包类型 1定额 2随机|
| can_share | 否 | Integer(4) | 是否可共享活动 1是 2否 |
| deleted | 否 | Integer(4) | 是否开启 1是 2否 |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| valid | 否 | Boolean | 是否获取有效红包 true是 默认false否，（开启，库存足够） |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": "1",
      "act_name": "红包大派送",
      "type": "1",
      "total_num": "1",
      "quantity": "10",
      "deleted": "1",
      "received_num": "0",
      "not_received_num": "0",
      "refunded_num": "0",
      "failed_num": "0"
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



## __获取所有红包列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/find-all-redpack-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| type | 否 | Integer(4) | 红包类型 1定额 2随机|
| can_share | 否 | Integer(4) | 是否可共享活动 1是 2否 |
| deleted | 否 | Integer(4) | 是否开启 1是 2否 |
| valid | 否 | Boolean | 是否获取有效红包 true是 默认false否，（开启，库存足够） |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": "2",
      "send_name": "商户名称",
      "act_name": "红包活动",
      "type": 1,
      "quantity": 10,
      "send_num": 29,
      "min_value": 100,
      "max_value": 100,
      "total_num": 1,
      "amt_type": null,
      "wishing": "祝福你妹！",
      "remark": "备注",
      "platform": 1,
      "can_share": 2,
      "shop_id": 30,
      "shop_sub_id": 0,
      "deleted": 1,
      "created": 1451273292,
      "modified": 1451441550
    }
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __启用红包__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/enable-cash-redpack
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 红包id |
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



## __禁用红包__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/disable-cash-redpack
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 红包id |
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



## __删除红包__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/del-cash-redpack
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 红包id |
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
