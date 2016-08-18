
## __添加关键字回复__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/create-keyword-reply
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| keyword | 是 | String(50) | 关键字 |
| match_type | 是 | Integer(3) | 匹配模式（1：完全匹配，2：包含匹配） |
| reply_ids | 是 | String(250) | 回复关联素材（json格式 {0:{type_key:material_id}}） |
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


## __获取关键字回复列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/find-keyword-reply-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| keyword| 否 | string(250) | 关键字 |
| match_type| 否 |  Integer(1) | 匹配模式(1:完全匹配，2:包含匹配) |
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
* **注意：返回run_type参数表示关键字类型（1：普通关键词，2：系统关键词）**

错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取关键字回复信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/get-keyword-reply
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| keyword_id | 是 | String(50) | 关键字id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok"
}
```
* **注意：返回run_type参数表示关键字类型（1：普通关键词，2：系统关键词）**

错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __修改关键字回复__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/update-keyword-reply
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| keyword_id | 是 | String(50) | 关键字id |
| keyword | 否 | String(50) | 关键字 |
| match_type | 否 | Integer(3) | 匹配模式（1：完全匹配，2：包含匹配） |
| reply_ids | 是 | String(250) | 回复关联素材（json格式 {0:{type_key:material_id}}） |
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


## __删除关键字回复__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/del-keyword-reply
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| keyword_id | 是 | String(50) | 关键字id |
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


## __开启关键字回复__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/open-keyword-reply
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| keyword_id | 是 | String(50) | 关键字id |
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


## __关闭关键字回复__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/close-keyword-reply
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| keyword_id | 是 | String(50) | 关键字id |
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
