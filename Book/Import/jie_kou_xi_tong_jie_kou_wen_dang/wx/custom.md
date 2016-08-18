
## __添加自定义菜单__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/create-menu
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id|
| menuname | 是 | String(50) | 菜单名称 |
| pid | 是 | Integer(11) | 父级菜单id，父级菜单可设值为0 |
| menu_type | 是 | Integer(3) | 菜单类型1.事件、2.链接 |
| menu_url | 是 | String(100) | 当menu_type为1时是关键字id,当menu_type是2时为url |
| sort | 否 | Integer(3) | 排序，值越大越靠前 |
| display | 是 | Integer(3) | 是否显示(1.是、2.否) |
* **注意：回复[关联素材可选值参考](/reply_material.html)**

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

## __批量添加自定义菜单__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/create-all-menu
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| menus.shop_id | 是 | Integer(11) | 商家id |
| menus.shop_sub_id | 是 | Integer(11) | 店铺id |
| menus.menuname | 是 | String(50) | 菜单名称 |
| menus.pid | 是 | Integer(11) | 父级菜单id |
| menus.menu_type | 是 | Integer(3) | 菜单类型1.事件、2.链接 |
| menus.menu_url | 是 | String(100) | 当menu_type为1时是json数据{0:{type1:reply_id1}}当menu_type是2时为url |
| menus.sort | 是 | Integer(3) | 排序，值越大越靠前，最大为127 |
| menus.display | 是 | Integer(3) | 是否显示(1.是、2.否) |
* **注意：menus为二维索引数组，如 $var = ['0'=>['id'=>1,'name'=>'mch']]**

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


## __获取自定义菜单列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/find-menu-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
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


## __获取自定义菜单信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/get-menu
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| menu_id | 是 | Integer(11) | 菜单id |
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


## __修改自定义菜单__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/update-menu
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| menu_id | 是 | Integer(11) | 菜单id |
| menuname | 否 | String(50) | 菜单名称 |
| menu_type | 否 | Integer(3) | 菜单类型1.事件、2.链接 |
| menu_url | 否 | String(100) | 当menu_type为1时是json数据{0:{type_key:material_id}}当menu_type是2时为url |
| sort | 否 | Integer(3) | 排序，值越大越靠前，最大为127 |
| display | 否 | Integer(3) | 是否显示(1.是、2.否) |
* **注意：回复[关联素材可选值参考](/reply_material.html)**

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


## __删除自定义菜单__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/del-menu
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| menu_id | 是 | Integer(11) | 菜单id |
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

