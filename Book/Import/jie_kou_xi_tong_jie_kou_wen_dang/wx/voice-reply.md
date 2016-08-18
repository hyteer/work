
## __添加语音回复素材__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/create-voice-material
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| title | 是 | Integer(11) | 素材标题 |
| media_id | 是 | Integer(11) | 通过微信接口上传多媒体文件，得到的id |
| document_id | 否 | String(20) | 文件库id |
| cdn_path | 否 | String(255) |cdn路径冗余 |
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


## __获取语音回复素材列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/find-voice-material-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
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


## __获取语音回复素材信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/get-voice-material
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


## __修改语音回复素材__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/update-voice-material
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| material_id | 是 | Integer(11) | 素材id |
| title | 否 | Integer(11) | 素材标题 |
| media_id | 否 | Integer(11) | 通过微信接口上传多媒体文件，得到的id |
| document_id | 否 | String(20) | 文件库id |
| cdn_path | 否 | String(255) |cdn路径冗余 |
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


## __删除语音回复素材__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/del-voice-material
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

