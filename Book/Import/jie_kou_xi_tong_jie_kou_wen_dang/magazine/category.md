
## __创建杂志分类__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/create-magazine-category
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| name | 是 | String(30) | 分类名称 |
<br  /><br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "name":"抗战纪念",
        "type":1,
        "shop_id":30,
        "created":1441091166,
        "modified":1441091166,
        "deleted":1,
        "id":"1"
    }
}
```

错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __修改杂志分类名称__


##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/update-magazine-category
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 分类id |
| shop_id | 是 | Integer(11) | 店铺id |
| name | 是 | String(30) | 分类名称 |
<br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":"2",
        "name":"过年",
        "type":2,
        "shop_id":30,
        "created":"1441091553",
        "modified":1441091614,
        "deleted":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取杂志分类列表__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/find-magazine-category
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| name | 否 | String(30) | 分类名称 |
| type | 否 | Integer(11) | 类别类型 1系统类别 2商家创建 |
| page | 否 | Integer(11) | 页码 |
| count | 否 | Integer(11) | 每页总数 |
| sortStr | 否 | Array | 排序 |
**注：不传入分页参数则返回所有分类**
<br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": "1",
      "name": "抗战纪念",
      "type": "1",
      "shop_id": "30",
      "created": "1441091166",
      "modified": "1441091166",
      "deleted": "1",
      "num": "2"
    },
    {
      "id": "2",
      "name": "过年",
      "type": "2",
      "shop_id": "30",
      "created": "1441091553",
      "modified": "1441092156",
      "deleted": "1",
      "num": "0"
    }
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __删除杂志分类__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/del-magazine-category
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 分类id |
| shop_id | 是 | Integer(11) | 店铺id |
<br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":null
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

