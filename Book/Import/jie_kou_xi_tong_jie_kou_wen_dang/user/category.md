## __创建用户分组__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/create-category
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| group_name | 是 | String(50) | 分组名称 |
| sort | 是 | Integer(3) | 排序，值越大越靠前 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "sort":100,
        "shop_sub_id":187,
        "group_name":"aa",
        "shop_id":30,
        "created":1440493089,
        "modified":1440493089,
        "id":17
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取用户分组列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/find-category-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":[
        {
            "id":16,
            "group_name":"我我",
            "sort":50,
            "shop_id":30,
            "shop_sub_id":192,
            "created":1440418758,
            "modified":1440418773
        },
        {
            "id":17,
            "group_name":"aa",
            "sort":100,
            "shop_id":30,
            "shop_sub_id":187,
            "created":1440493089,
            "modified":1440493089
        }
    ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取用户分组信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/get-category
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| group_id | 是 | Integer(11) | 分组id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":17,
        "group_name":"aa",
        "sort":100,
        "shop_id":30,
        "shop_sub_id":187,
        "created":1440493089,
        "modified":1440493089
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __修改用户分组信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/update-category
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
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
