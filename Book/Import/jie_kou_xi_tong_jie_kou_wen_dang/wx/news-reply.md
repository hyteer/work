
## __添加图文回复素材__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/create-news-material
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| news.shop_id | 是 | Integer(11) | 商家id |
| news.shop_sub_id | 是 | Integer(11) | 店铺id |
| news.title | 是 | String(30) | 素材名称 |
| item.title | 是 | String(30) | 图文标题 |
| item.description | 是 | String(250) | 图文描述 |
| item.url | 是 | String(250)  | 图文链接|
| item.content | 是 | String  | 图文内容 |
| item.document_id | 否 | String(20)  | 文件库id |
| itme.cdn_path | 否 | String(255) |cdn路径冗余 |
| item.img_src | 是 | String(250)  | 缩略图路径 |
* **注意：item为二维索引数组，如 $var = ['0'=>['id'=>1,'name'=>'mch']]**

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


## __获取图文回复素材列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/find-news-material-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| title | 否 | String(50) | 标题 |
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


## __获取图文回复素材信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/get-news-material
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| material_id | 是 | Integer(11) | 素材id |
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


## __修改图文回复素材__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/update-news-material
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| material_id | 是 | Integer(11) | 素材id |
| title | 是 | String(30) | 素材名称 |
| item.title | 否 | String(30) | 图文url |
| item.description | 否 | String(250) | 图文描述 |
| item.url | 否 | String(250)  | 图文链接|
| item.content | 否 | String()  | 图文内容 |
| item.document_id | 否 | String(20) | 文件库id |
| itme.cdn_path | 否 | String(255) |cdn路径冗余 |
| item.img_src | 是 | String(250)  | 缩略图路径 |
* **注意：item为二维索引数组，如 $var = ['0'=>['id'=>1,'name'=>'mch']]**

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


## __删除图文回复素材__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/delete-news-material
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| material_id | 是 | Integer(11) | 素材id |
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

