## __获取第三方平台配置信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/third-party/get-config
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| platform_type | 是 | Integer(3) | 平台类型（1.微信）|
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 54,
    "shop_id": 30,
    "url": "http://devnewwx.vikduo.com/scliveapp2015/wxapi/index",
    "appid": "wx0df9c8ff7b00587e",
    "secret": "2bb83fff28435d99ad7940edc5f6c38e",
    "token": "weishanghu",
    "account": "scliveapp2015",
    "platform_type": 1,
    "account_type": 1,
    "account_service": 1,
    "created": 0,
    "modified": 1452750702,
    "deleted": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __根据微信号获取第三方配置信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/third-party/get-config-byaccount
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| account | 是 | String(20) | 商家微信号 |
| platform_type | 是 | Integer(3) | 平台类型（1.微信）|
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 54,
    "shop_id": 30,
    "url": "http://devnewwx.vikduo.com/scliveapp2015/wxapi/index",
    "appid": "wx0df9c8ff7b00587e",
    "secret": "2bb83fff28435d99ad7940edc5f6c38e",
    "token": "weishanghu",
    "account": "scliveapp2015",
    "platform_type": 1,
    "account_type": 1,
    "account_service": 1,
    "created": 0,
    "modified": 1452750702,
    "deleted": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __修改微信平台配置信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/third-party/update-wx-config
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| third_party_id | 是 | Integer(11) | 第三方平台id |
| url | 否 | String(255) | 微信平台接口回调地址 |
| appid | 否 | String(60) | 微信平台appid |
| secret | 否 | String(60) | 微信平台secret |
| token | 否 | String(60) | 微信平台token |
| account | 否 | String(20) | 微信平台账号 |
| account_type | 否 | Integer(3) | 微信平台账号类型（1：服务号、2：订阅号） |
| account_service | 否 | Integer(3) | 是否开启微信平台高级接口（1：开通，2：未开通） |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 54,
    "shop_id": 30,
    "url": "http://devnewwx.vikduo.com/scliveapp2015/wxapi/index",
    "appid": "wx0df9c8ff7b00587e",
    "secret": "2bb83fff28435d99ad7940edc5f6c38e",
    "token": "weishanghu",
    "account": "scliveapp2015",
    "platform_type": 1,
    "account_type": 1,
    "account_service": 1,
    "created": 0,
    "modified": 1452750702,
    "deleted": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

