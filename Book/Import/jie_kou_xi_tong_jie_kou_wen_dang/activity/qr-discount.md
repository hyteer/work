## __新增拍码活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/qr-discount/create
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| activity.relate_product_type | 是 | Integer(4) | 关联产品类型（1.按关联表、2.全部） |
| activity.name | 是 | String(250) | 活动名称 |
| activity.desc | 否 | String(500) | 活动描述/规则 |
| activity.sort | 否 | Integer(11) | 排序 |
| activity.expire_type | 是 | Integer(4) | 有效期类型1.指定时间范围、2.无时间限制 |
| activity.start_time | 是 | Integer(11) | 活动开始时间 |
| activity.end_time | 是 | Integer(11) | 活动结束时间 |
| activity.shop_id | 是 | Integer(11) | 商家id |
| activity.shop_sub_id | 否 | Integer(11) | 店铺id |
| activity.share_type | 是 | Integer(4) |显示和分享模式（1.显示且能分享、2.不能显示且能分享、3.不能显示且不能分享）|
| postageSetting.type | 否 | Integer(11) | 包邮类型（1.满金额包邮、2.满件数包邮、3.免邮费）|
| postageSetting.num | 否 | Integer(11) | 数量 |
| postageSetting.amount | 否 | Integer(11) | 金额 |
| qrDiscount.type | 是 | Integer(4) | 活动优惠类型（1.打折。2.满减） |
| qrDiscount.full | 否 | Integer(11) | 满 |
| qrDiscount.minus | 否 | Integer(11) | 减 |
| qrDiscount.discount | 否 | Integer(11) | 折扣百分比 |

* **注意：postageSetting 为非必要项，如设置其中一项，其他的均必须要设置**
* **注意：postageSetting.type=2时，postageSetting.num必须设置；postageSetting.type=1时，postageSetting.amount必须设置**
* **注意：qrDiscount.type=1时，qrDiscount.discount必须设置；qrDiscount.type=2时，qrDiscount.full和qrDiscount.minus必须设置；**

<br  /><br  />
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


## __获取拍码活动列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/qr-discount/find-qr-discount-list
<br  /><br  />
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


## __修改拍码打折活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/qr-discount/to-update
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| activity.id | 是 | Integer(11) | 活动id |
| activity.name | 是 | String(250) | 活动名称 |
| activity.postage_setting_id | 否 | Integer(11) | 邮费外键 |
| activity.desc | 否 | String(500) | 活动描述/规则 |
| activity.sort | 否 | Integer(11) | 排序 |
| activity.expire_type | 是 | Integer(4) | 有效期类型1.指定时间范围、2.无时间限制 |
| activity.start_time | 是 | Integer(11) | 活动开始时间 |
| activity.end_time | 是 | Integer(11) | 活动结束时间 |
| activity.share_type | 是 | Integer(4) |显示和分享模式（1.显示且能分享、2.不能显示且能分享、3.不能显示且不能分享）|
| postageSetting.type | 否 | Integer(11) | 包邮类型（1.满金额包邮、2.满件数包邮、3.免邮费）|
| postageSetting.num | 否 | Integer(11) | 数量 |
| postageSetting.amount | 否 | Integer(11) | 金额 |
| qrDiscount.id | 是 | Integer(11) | 拍码id |
| qrDiscount.type | 否 | Integer(4) | 活动优惠类型（1.打折。2.满减） |
| qrDiscount.full | 否 | Integer(11) | 满 |
| qrDiscount.minus | 否 | Integer(11) | 减 |
| qrDiscount.discount | 否 | Integer(11) | 折扣百分比 |

* **注意：activity.postage_setting_id设置为0即不设置邮费规则时，postageSetting项不需要设置**
* **注意：postageSetting 为非必要项，如设置其中一项，其他的均必须要设置**
* **注意：postageSetting.type=2时，postageSetting.num必须设置；postageSetting.type=1时，postageSetting.amount必须设置**
* **注意：qrDiscount.type=1时，qrDiscount.discount必须设置；qrDiscount.type=2时，qrDiscount.full和qrDiscount.minus必须设置；**

<br  /><br  />
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


## __删除拍码活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/qr-discount/general-del
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 商家id |

<br  /><br  />
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


## __开启拍码活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/qr-discount/general-enable
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 商家id |

<br  /><br  />
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

## __关闭拍码活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/qr-discount/general-disable
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 商家id |

<br  /><br  />
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


## __新增拍码商品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/qr-discount/create-qr-discount-goods
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| qr_discount_id | 是 | Integer(11) | 秒杀活动id |
| product_id | 是 | Integer(11) | 关联的商品id |
| shop_id | 是 | Integer(11) | 商家id |
| product_sku_id | 是 | Integer(11) | 关联的sku ID |
| quota | 是 | Integer(11) | 商品配额 |
| limit_buy | 是 | Integer(11) | 限购 |
| shop_sub_id | 是 | Integer(11) | 店铺id |

<br  /><br  />
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

## __更新拍码商品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/qr-discount/update-qr-discount-goods
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 秒杀商品id |
| shop_id | 是 | Integer(11) | 商家id |
| quota | 否 | Integer(11) | 商品配额 |
| limit_buy | 否 | Integer(11) | 限购 |

<br  /><br  />
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


## __获取拍码商品列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/qr-discount/find-qr-discount-goods-list
<br  /><br  />
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



## __删除拍码商品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/qr-discount/qr-discount-goods-del
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 商家id |

<br  /><br  />
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

