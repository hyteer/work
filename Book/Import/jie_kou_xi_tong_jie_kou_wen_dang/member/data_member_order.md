# 会员消费分层统计

## 消费次数分层统计
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/statistics/statistics-user-by-order-count
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "item": [
        {
          "user_num": "0",
          "num": "0",
          "total_user_num": "5"
        }
        ]
    }
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## 消费金额分层统计
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/statistics/statistics-user-by-should-pay
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "item": [
        {
          "user_num": "4",
          "num": "0-100",
          "total_user_num": "5"
        }
        ]
    }
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
