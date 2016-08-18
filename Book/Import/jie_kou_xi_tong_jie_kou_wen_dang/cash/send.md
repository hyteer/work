# 红包派发
## __获取红包个人发放列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/find-cash-redpack-data-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| cash_redpack_id | 否 | Integer(11) | 红包id |
| group_id | 否 | Integer(11) | 红包按组发放id |
| status | 否 | Integer(4) | 发放状态：1发放失败，2未领取，3已领取，4已退款，5发放中 |
| type | 否 | Integer(4) | 红包类型 1定额 2随机|
| source | 否 | Integer(4) | 红包来源 1扫码 2手动派发 3抽奖 4消费赠送 5游戏 6OPEN |
| keyword | 否 | String(30) | 关键字搜索（红包名称/用户昵称） |
| wx_keyword | 否 | String(30) | 按组发放下级数据关键字搜索（用户昵称/手机号） |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| createStart | 否 | Integer(11) | 发送起始时间 |
| createEnd | 否 | Integer(11) | 发送结束时间 |
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
      "min_value": "100",
      "max_value": "100",
      "nickname": null,
      "mobile": null,
      "uid": "213",
      "created": null,
      "status": "2"
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



## __获取红包群组发放列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/find-cash-redpack-group-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| cash_redpack_id | 否 | Integer(11) | 红包id |
| keyword | 否 | String(30) | 关键字搜索（红包名称/分组名称） |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| createStart | 否 | Integer(11) | 发送起始时间 |
| createEnd | 否 | Integer(11) | 发送结束时间 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "act_name": "红包大派送",
      "type": "1",
      "min_value": "100",
      "max_value": "100",
      "group_name": "我我",
      "send_time": "123123132",
      "group_count": "7",
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



## __按用户派发红包__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/send-cash-redpack
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| cash_redpack_id | 是 | Integer(11) | 红包活动id |
| uid | 是 | Integer(11)/Array | 接收用户id（单用户id，或多用户id数组） |
| source | 是 | Integer(4) | 红包来源 1扫码 2手动派发 3抽奖 4消费赠送 5游戏 6OPEN |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "send": 1,
    "success": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __按群组派发红包__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/group-send-cash-redpack
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| cash_redpack_id | 是 | Integer(11) | 红包活动id |
| wx_group_id | 是 | Integer(11)/Array | 接收群组id（单群组id，或多群组id数组） |
| source | 是 | Integer(4) | 红包来源 1扫码 2手动派发 3抽奖 4消费赠送 5游戏 6OPEN |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "send": 1,
    "success": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __重新派发__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/resend-cash-redpack
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 红包数据id |
| shop_id | 是 | Integer(11) | 商家id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "send": 1,
    "success": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __更新红包领取状态__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/update-cash-redpack-data-status
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11)/Array | 红包数据id(单条数据id，或多条数据id数组) |
| shop_id | 是 | Integer(11) | 商家id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "send": 1,
    "success": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __扫码派送__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/cash-redpack/scan-send
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| cash_redpack_id | 是 | Integer(11) | 红包id |
| shop_id | 是 | Integer(11) | 商家id |
| open_id | 是 | varchar(32) | 用户openid |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "redpackData": {
      "id": 51,
      "pid": 0,
      "uid": 794,
      "re_openid": "obUMWuG0Ma9hDaJ0CiA9emuNektg",
      "mch_billno": "1260789701201601082222602541",
      "cash_redpack_id": 3,
      "send_amount": 100,
      "send_time": 1452234126,
      "send_listid": "0010442823201601080407602944",
      "status": 2,
      "fail_code": "NOTENOUGH",
      "source": 1,
      "group_id": 0,
      "shop_id": 30,
      "shop_sub_id": 0,
      "created": 1452222604,
      "modified": 1452234126
    }
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
