## __添加消息模板__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx-message/create-msg-tpl
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| template_id | 是 | Integer(11) | 模板id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "template_id": 3,
    "remark": "用户收货通知",
    "shop_id": 32,
    "shop_sub_id": 0,
    "failed_num": 0,
    "total_num": 0,
    "deleted": 2,
    "header": "您已收货",
    "footer": "如有问题联系xxx！",
    "created": 1448353958,
    "modified": 1448353958,
    "id": 15
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __更新消息模板__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx-message/update-msg-tpl
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 模板id |
| shop_id | 是 | Integer(11) | 商家id |
| mp_id | 否 | Integer(11) | 微信平台模板ID |
| deleted | 否 | Integer(11) | 开关状态（1开启 2关闭） |
| header | 否 | String(200) | 模板消息头 |
| footer | 否 | String(200) | 模板消息尾 |
| remark | 否 | String(200) | 模板备注 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 10,
    "template_id": 3,
    "mp_id": "",
    "header": "您已收货",
    "footer": "如有问题联系xxx！",
    "remark": "用户收货通知",
    "shop_id": 30,
    "shop_sub_id": 0,
    "failed_num": 0,
    "total_num": 0,
    "deleted": 2,
    "created": 1448343658,
    "modified": 1448432672
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取消息模板详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx-message/get-msg-tpl-detail
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 模板id |
| shop_id | 是 | Integer(11) | 商家id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": "10",
    "template_id": "3",
    "mp_id": "",
    "header": "您已收货",
    "footer": "如有问题联系xxx！",
    "remark": "用户收货通知",
    "shop_id": "30",
    "shop_sub_id": "0",
    "failed_num": "0",
    "total_num": "0",
    "deleted": "2",
    "created": "1448343658",
    "modified": "1448432672",
    "status": "1",
    "body_params": "0",
    "no": "TM001",
    "name": "收货通知"
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取商家已选模板__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx-message/get-msg-tpl-by-shop-id
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 子商家id |
| to_user | 是 | Integer(11) | 模板归属（1买家，2商家） |
| count | 否 | Integer(11) | 单页数据量（默认20） |
| page | 否 | Integer(11) | 页码（默认0） |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": "4",
      "template_id": "1",
      "mp_id": null,
      "header": "您已成功付款",
      "footer": "如有问题联系xxx",
      "remark": "付款成功通知",
      "shop_id": "30",
      "shop_sub_id": "0",
      "failed_num": "0",
      "total_num": "0",
      "deleted": "2",
      "created": "1448334611",
      "modified": "1448334611",
      "status": "1"
    },
    {
      "id": "1",
      "template_id": "2",
      "mp_id": null,
      "header": null,
      "footer": null,
      "remark": "0",
      "shop_id": "30",
      "shop_sub_id": "0",
      "failed_num": "0",
      "total_num": "0",
      "deleted": "2",
      "created": null,
      "modified": null,
      "status": "1"
    },
    {
      "id": "14",
      "template_id": "3",
      "mp_id": null,
      "header": "您已收货",
      "footer": "如有问题联系xxx！",
      "remark": "用户收货通知",
      "shop_id": "30",
      "shop_sub_id": "0",
      "failed_num": "0",
      "total_num": "0",
      "deleted": "2",
      "created": "1448353262",
      "modified": "1448353262",
      "status": "1"
    }
  ],
  "page": {
    "per_page": 20,
    "total_count": 3,
    "current_page": 0,
    "total_page": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __获取可用模板__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx-message/get-optional-msg-tpl
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| to_user | 是 | Integer(11) | 模板归属（1买家，2商家） |
| count | 否 | Integer(11) | 单页数据量（1~2000 默认20） |
| page | 否 | Integer(11) | 页码（默认0） |
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
      "name": "付款成功通知",
      "no": "TM00398",
      "type_id": "1",
      "to_user": "1",
      "header": "您已成功付款",
      "body": "",
      "footer": "如有问题联系xxx",
      "body_params": "0",
      "remark": "付款成功通知",
      "deleted": "1",
      "created": null,
      "modified": null
    },
    {
      "id": "2",
      "name": "付款成功通知",
      "no": "TM004",
      "type_id": "1",
      "to_user": "1",
      "header": "付款成功",
      "body": "",
      "footer": "如有问题联系xxx@",
      "body_params": "0",
      "remark": "付款成功通知1",
      "deleted": "1",
      "created": null,
      "modified": null
    },
    {
      "id": "3",
      "name": "收货通知",
      "no": "TM001",
      "type_id": "1",
      "to_user": "1",
      "header": "您已收货",
      "body": "0",
      "footer": "如有问题联系xxx！",
      "body_params": "0",
      "remark": "用户收货通知",
      "deleted": "1",
      "created": null,
      "modified": null
    }
  ],
  "page": {
    "per_page": 20,
    "total_count": 3,
    "current_page": 0,
    "total_page": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
