
## __添加商品分类__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/create-category
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| name | 是 | String(50） | 分类名称 |
| desc | 否 | String(50) | 分类描述 |
| pid | 是 | Integer(11) | 父级菜单id，父级菜单可设值为0 |
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


## __获取商品分类列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/find-category-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| pid | 否 | Integer(11) | 父级id |
| level | 否 | Integer(11) | 层级 |
| isAll | 否 | boolean | 是否返回带系统菜单 |
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


## __获取商品分类信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/get-category
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| category_id | 是 | Integer(11) | 分类id |
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


## __修改商品分类信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/update-category
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| category_id | 是 | Integer(11) | 分类id |
| name | 否 | String(50） | 分类名称 |
| desc | 否 | String(50) | 分类描述 |
| pid | 否 | Integer(11) | 父级菜单id，父级菜单可设值为0 |
| sort | 否 | Integer(3) | 排序，值越大越靠前 |
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
