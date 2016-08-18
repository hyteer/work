# 开发者模式
## __开通开发者__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/developer/create-developer
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
  "data": {
    "app_id": "eQKYtHomCNXmvGPMAH",
    "app_secret": "05989a3d5f9a4ad9c0595ad3c638b662",
    "shop_id": 35,
    "created": 1456470199,
    "modified": 1456470199,
    "deleted": 1
    "id": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __获取开发者信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/developer/get-developer
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
  "data": {
    "id": 1,
    "app_id": "eQKYtHomCNXmvGPMAH",
    "app_secret": "05989a3d5f9a4ad9c0595ad3c638b662",
    "shop_id": 35,
    "created": 1456384638,
    "modified": 1456384638,
    "deleted": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
