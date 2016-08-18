##### 接口调用请求说明

## __新增积分商品__
请求方式：POST
<br  />
请求地址：/points/create-goods
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| product_name   |是| varchar(255)|名称|
| product_id|是|Integer|产品ID|
| product_sku_id|是|Integer(11)|产品sku_id|
| cost_point|是|Integer(11)|购买积分|
| quota|是|Integer(11)|配额|
| shop_id|是|Integer(11)|商家id|
| shop_sub_id|否|Integer(11)|商铺id|
<br  />
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


## __修改积分商品__
请求方式：POST
<br  />
请求地址：/points/update-goods
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|id|
| product_name|是| varchar(255)|名称|
| product_id|是|Integer(11)|产品ID|
| product_sku_id|是|Integer(11)|产品sku_id|
| quota|是|Integer(11)|配额|
| cost_point|否|Integer(11)|购买积分|
| shop_id|是|Integer(11)|商家id|
| shop_sub_id|否|Integer(11)|商铺id|
<br  />
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


## __删除积分商品__
请求方式：POST
<br  />
请求地址：/points/del-goods
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|id|
| shop_id|是|Integer(11)|商家id|
<br  />
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


## __查询积分商品__
请求方式：POST
<br  />
请求地址：/points/find-goods
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商家id|
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": 2,
      "product_id": 18536,
      "product_sku_id": 114957,
      "product_name": "爱拼才会赢抱团才优惠",
      "cost_point": 5,
      "quota": 4,
      "sales_num": 0,
      "shop_id": 514,
      "shop_sub_id": 0,
      "created": 1468844412,
      "modified": 1468846990,
      "deleted": 1
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

