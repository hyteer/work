
## __添加商品评论__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/create-comment
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| content | 是 | String(1000) | 评论内容 |
| product_id | 是 | Integer(11） | 商品id |
| uid | 是 | Integer(11) | 评论用户id |
| star | 否 | Integer(3) | 星级、评分（1、2、3、4、5） |
| ip | 否 | String(20) | ip |
| reply | 否 | String(1000) | 回复内容 |
| reply_uid | 否 | Integer(11) | 回复店员id |
| shop_id | 是 | Integer(11) | 商家id |
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


## __添加商品灌水评论__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/create-product-comment-no-user
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| content | 是 | String(1000) | 评论内容 |
| product_id | 是 | Integer(11） | 商品id |
| star | 是 | Integer(3) | 星级、评分（1、2、3、4、5） |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| created | 否 | Date | 创建时间（yyyy-MM-dd HH:mm:ss） |
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


## __回复商品评论__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/update-comment
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11） | 商品评论id |
| reply | 否 | String(1000) | 回复内容 |
| reply_uid | 否 | Integer(11) | 回复用户id |
| shop_id | 是 | Integer(11) | 商家id |
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


## __获取商品分类列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/find-comment-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| s_content | 否 | String(100) | 内容搜索 |
| s_product_name | 否 | String(100) | 产品名称搜索 |
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


## __删除商品评论或回复__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/del-comment
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| comment_id | 是 | Integer(11) | 评论id |
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



## __统计商品评论平均分__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/avg-star
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| product_id | 是 | Integer(11) | 商品id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": 0
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

