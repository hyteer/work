## __创建用户分类__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/create-category
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 是 | Integer(11) | 商铺id |
| group_name | 是 | String(50) | 分组名称 |
| sort | 是 | Integer(3) | 排序，值越大越靠前 |
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

## __获取用户分类列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/find-category-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 是 | Integer(11) | 商铺id |
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

## __获取用户分类信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/get-category
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 是 | Integer(11) | 商铺id |
| group_id | 是 | Integer(11) | 分组id |
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

## __修改用户分类信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/update-category
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 是 | Integer(11) | 商铺id |
| group_id | 是 | Integer(11) | 分组id |
| group_name | 否 | String(50) | 分组名称 |
| sort | 否 | Integer(3) | 排序，值越大越靠前 |
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
