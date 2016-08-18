
## __创建分销员商品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/create-member-product
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| uid | 是 | Integer(11) | 用户id |
| mid | 是 | Integer(11) | 分销员id |
| product_id | 是 | Integer(11) | 商品id |
| fx_product_id | 是 | Integer(11) | 分销商品id |
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


## __一键创建分销员所有商品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/create-member-product-a-key
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| uid | 是 | Integer(11) | 用户id |
| mid | 是 | Integer(11) | 分销员id |
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

## __获取分销员商品列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/find-member-product-list
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| member_id | 是 | Integer(11) | 分销员id |
| app | 否 | Integer(2) | app端调用需设置该值，值为1，只会显示商品上架的以及策略未过期的 |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
* **注意：sort排序可选字段['id']**

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


## __获取分销员商品信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/get-member-product
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| fx_member_product_id | 是 | Integer(11) | 分销员商品id|
| member_id | 是 | Integer(11) | 分销员id|
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


## __删除分销员商品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/del-member-product
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| fx_member_product_id | 是 | Integer(11) | 分销员商品id|
| member_id | 是 | Integer(11) | 分销员id|
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

## __一键删除分销员所有商品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/del-member-product-a-key
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id|
| mid | 是 | Integer(11) | 分销员id|
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
