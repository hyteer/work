
## __添加二维码__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/create-persistent-qrcode
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| scene_id | 是 | String(250) | 二维码ticket自行设定参数 |
| ticket | 是 | String(250) |  |
| model | 是 | String(250) | 二维码类型 |
| model_id | 是 | String(250) | 二维码类型对应的id |
| type_id | 是 | String(20) |  |
| type | 否 | String(255) | 1：店铺 2：员工 |
<br  />
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


## __获取二维码列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/find-persistent-qrcode-list
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
* **注意：sort排序可选字段['id']**
<br  />
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

## __获取二维码详细信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/get-persistent-qrcode
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| scene_id | 是 | Integer(11) | 二维码ticket自行设定参数 |

<br  />
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

## __二维码扫码数增加一__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/increase-by-hit
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| scene_id | 是 | Integer(11) | 二维码ticket自行设定参数 |

<br  />
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

## __二维码通过扫码关注数增加一__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/increase-by-attention
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| scene_id | 是 | Integer(11) | 二维码ticket自行设定参数 |

<br  />
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



## __获取商家下二维码最大的scene_id__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/get-max-scene-id
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":1
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
**注意：该商家下最大scene_id为空时，返回的data为0**
