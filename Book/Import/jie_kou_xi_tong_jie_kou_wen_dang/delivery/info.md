
## __创建配送方式__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/delivery/create
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| name | 是 | String(20) | 配送方式名称 |
| logistics_company | 是 | String(20) | 物流公司 |
| default_money | 是 | double | 首重金额，单位分 |
| default_weight | 是 | String(20) | 首重 单位克|
| increase | 是 | double | 续重金额，单位分 |
| w_increase | 是 | double | 续重金额，单位克 |
| order | 否 | Integer(11) | 排序 |
| status | 是 | Integet(3) | 开启状态（1：开启,2：关闭） |
| remark | 否 | String(255) | 备注 |
| area.area | 是 | String | 发货地区列表，json格式 |
| area.default | 否 | double | 首重金额，单位元 |
| area.increase | 否 | double | 续重金额，单位元 |
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


## __获取配送方式列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/delivery/find-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
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


## __获取配送方式信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/delivery/get
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| delivery_id | 是 | Integer(11) | 配送方式id |
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


## __修改配送方式信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/delivery/to-update
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| delivery_id | 是 | Integer(11) | 配送方式id |
| name | 否 | String(20) | 配送方式名称 |
| logistics_company | 否 | String(20) | 物流公司 |
| default_money | 否 | double | 首重金额，单位分 |
| default_weight | 否 | String(20) | 首重 单位克|
| increase | 否 | double | 续重金额，单位分 |
| w_increase | 是 | double | 续重金额，单位克 |
| order | 否 | Integer(11) | 排序 |
| remark | 否 | String(255) | 备注 |
| area.area | 是 | String | 发货地区列表，json格式 |
| area.default_money | 否 | double | 首重金额，单位元 |
| area.increase | 否 | double | 续重金额，单位元 |
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


## __开启某个配送方式__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/delivery/open
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| delivery_id | 是 | Integer(11) | 配送方式id |
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


## __关闭某个配送方式__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/delivery/close
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| delivery_id | 是 | Integer(11) | 配送方式id |
| flag | 是 | boolean | flag标识不判断该邮费模板是否被商品关联 直接删除 |
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


## __删除某个配送方式__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/delivery/del
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| delivery_id | 是 | Integer(11) | 配送方式id |
| flag | 是 | boolean | flag标识不判断该邮费模板是否被商品关联 直接删除 |
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

## __删除邮费__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/delivery/del-shipping-fee
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 邮费id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |

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

