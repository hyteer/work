# 平台红包
## __创建红包模板__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/platform-create
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| act_name | 是 | String(32） | 活动名称 |
| wishing | 是 | String(128) | 祝福语 |
| remark | 是 | String(256) | 备注|
| platform | 是 | Integer(11) | 发放平台 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "type": 1,
    "quantity": 0,
    "send_num": 0,
    "min_value": 0,
    "max_value": 0,
    "total_num": 1,
    "platform": "2",
    "can_share": 2,
    "shop_id": 0,
    "shop_sub_id": 0,
    "deleted": 1,
    "act_name": "平台红包",
    "wishing": "祝福",
    "remark": "备注",
    "created": 1453450066,
    "modified": 1453450066,
    "id": "45"
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __派发红包__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/platform-send
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| cash_redpack_id | 是 | Integer(11) | 红包活动id |
| uid | 是 | Integer(11)/Array | 接收用户id（单用户id，或多用户id数组） |
| send_amount | 是 | Integer(11) | 发放金额，单位分，100-20000 |
| platform | 是 | Integer(11) | 发放平台 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": "397",
    "mch_billno": "1260789701201601220000000000",
    "mch_id": "1260700000",
    "sub_mch_id": "1265800000",
    "wxappid": "wx488f739479400000",
    "msgappid": "wx0df9c8ff7b000000",
    "appsecret": "",
    "key": "bhghhnthtnhhnythnynhyn0000000000",
    "shop_id": "0",
    "nick_name": "",
    "send_name": "尽快形成顺畅高效的",
    "re_openid": "obUMWuG0Ma9hDaJ0CiA9emu00000",
    "total_amount": "200",
    "min_value": "0",
    "max_value": "0",
    "total_num": "1",
    "wishing": "祝福",
    "client_ip": "10.20.50.183",
    "act_name": "平台红包",
    "remark": "备注",
    "logo_imgurl": "",
    "share_content": "",
    "share_url": "",
    "share_imgurl": "",
    "bill_type": null,
    "send_listid": "0010442823201601220446400000",
    "send_time": "20160122165514",
    "detail_id": null,
    "send_type": null,
    "hb_type": null,
    "hblist": null,
    "status": "1",
    "created": "2147483647",
    "modified": "2147483647",
    "Rcv_time": null,
    "amount": null,
    "wxstatus": null,
    "openid": null,
    "Refund_amount": null,
    "Refund_time": null,
    "reason": null,
    "plat_id": "2",
    "user_id": "3"
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __修改红包模板信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/platform-update
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 红包模板id |
| act_name | 否 | String(32） | 活动名称 |
| wishing | 否 | String(128) | 祝福语 |
| remark | 否 | String(256) | 备注|
| platform | 是 | Integer(11) | 平台id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": "45",
    "send_name": null,
    "act_name": "平台红包",
    "type": 1,
    "quantity": 0,
    "send_num": 12,
    "min_value": 0,
    "max_value": 0,
    "total_num": 1,
    "amt_type": null,
    "wishing": "祝福",
    "remark": "备注",
    "platform": "2",
    "can_share": 2,
    "shop_id": 0,
    "shop_sub_id": 0,
    "deleted": 1,
    "created": 1453450066,
    "modified": 1453455720
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __获取红包模板列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/platform-find
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| platform | 是 | Integer(11) | 平台id |
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
      "id": "44",
      "act_name": "平台红包",
      "send_num": "0",
      "type": "1",
      "total_num": "1",
      "min_value": "0",
      "max_value": "0",
      "quantity": "0",
      "deleted": "1",
      "received_num": "0",
      "received_amount": null,
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



## __获取红包模板详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/platform-get
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 红包模板id |
| platform | 是 | Integer(11) | 平台id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": "45",
    "send_name": null,
    "act_name": "平台红包",
    "type": 1,
    "quantity": 0,
    "send_num": 12,
    "min_value": 0,
    "max_value": 0,
    "total_num": 1,
    "amt_type": null,
    "wishing": "祝福",
    "remark": "备注",
    "platform": 2,
    "can_share": 2,
    "shop_id": 0,
    "shop_sub_id": 0,
    "deleted": 1,
    "created": 1453450066,
    "modified": 1453455720
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __删除红包模板__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/platform-del
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 红包模板id |
| platform | 是 | Integer(11) | 平台id |
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
