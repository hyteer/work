
## __获取单个微信小店分类__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/get-category
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 分类id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 1,
        "name": "美食",
        "pid": 0,
        "level": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __查找微信小店分类__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wx/find-category
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| pid | 否 | Integer(11) | 分类父id |
| level | 否 | Integer(11) | 层级 |
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
            "name": "美食",
            "pid": 0,
            "level": 1
        },
        {
            "id": 2,
            "name": "江浙菜",
            "pid": 1,
            "level": 2
        },
        {
            "id": 3,
            "name": "上海菜",
            "pid": 2,
            "level": 3
        },
        {
            "id": 4,
            "name": "淮扬菜",
            "pid": 2,
            "level": 3
        },
        {
            "id": 5,
            "name": "浙江菜",
            "pid": 2,
            "level": 3
        }
    ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
