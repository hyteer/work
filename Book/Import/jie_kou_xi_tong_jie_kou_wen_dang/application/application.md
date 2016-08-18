# 第三方应用
## __创建应用__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/application/create-application
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| appid | 是 | Integer(11) | 应用id |
| name | 是 | String(60) | 应用名称 |
| desc | 是 | Text | 应用描述 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "appid": 2,
    "deleted": 1,
    "name": "name",
    "desc": "desc",
    "created": 1456470199,
    "modified": 1456470199,
    "id": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __应用列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/application/find-application
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| deleted | 否 | Integer(4) | 是否开启 1是 2否 |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": 1,
      "name": "name",
      "appid": 2,
      "desc": "desc",
      "created": 1456470199,
      "modified": 1456470199,
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
