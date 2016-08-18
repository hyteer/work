## __创建菜单__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/create-menu
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| pid|是|Integer(11)|上级菜单ID，顶级菜单的话填写0|
| title|是|varchar(50)|菜单标题|
| system|是|Integer(4)|所属系统（1.admin后台、2.店铺后台、3.代理商后台）|
| url_type|是|Integer(4)|地址类型（1为controller-action,2为直接地址，3为js）|
| url_param|否|varchar(255)|地址值（根据类型设置不同，json格式,例如如果是1则{"c":"shop","a":"index"}',）|
| is_target|否|Integer(4)|是否新窗口打开（1.是、2.否）|
| sort|否|Integer(11)|排序|
| auth_functions|否|varchar(255)|关联功能节点|
| remark|否|varchar(255)|备注|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": null
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取菜单列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/find-menu
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| system|是|Integer(4)|所属系统（1.admin后台、2.店铺后台、3.代理商后台）|
| pid|否|Integer(11)|上级菜单ID|
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": [
        {
            "id": 1,
            "pid": 0,
            "title": "menu1",
            "system": 2,
            "url_type": 1,
            "url_param": "{\"c\":\"shop\",\"a\":\"index\"}",
            "is_target": 1,
            "remark": "remark",
            "sort": null,
            "auth_functions": null,
            "created": null,
            "modified": null,
            "deleted": 1
        },
        {
            "id": 2,
            "pid": 1,
            "title": "menu22",
            "system": 2,
            "url_type": null,
            "url_param": null,
            "is_target": null,
            "remark": null,
            "sort": null,
            "auth_functions": null,
            "created": null,
            "modified": null,
            "deleted": 1
        }
    ],
    "page": {
        "per_page": 20,
        "total_count": 2,
        "current_page": 0,
        "total_page": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __获取菜单详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/get-menu
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|菜单ID|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 1,
        "pid": 0,
        "title": "menu1",
        "system": 2,
        "url_type": 1,
        "url_param": "{\"c\":\"shop\",\"a\":\"index\"}",
        "is_target": 1,
        "remark": "remark",
        "sort": null,
        "auth_functions": null,
        "created": null,
        "modified": null,
        "deleted": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __修改菜单__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/update-menu
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|菜单id|
| title|是|varchar(50)|菜单标题|
| pid|否|Integer(11)|上级菜单ID，顶级菜单的话填写0|
| title|是|varchar(50)|菜单标题|
| url_type|是|Integer(4)|地址类型（1为controller-action,2为直接地址，3为js）|
| url_param|否|varchar(255)|地址值（根据类型设置不同，json格式,例如如果是1则{"c":"shop","a":"index"}',）|
| is_target|否|Integer(4)|是否新窗口打开（1.是、2.否）|
| sort|否|Integer(11)|排序|
| auth_functions|否|varchar(255)|关联功能节点|
| remark|否|varchar(255)|备注|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": null
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __删除菜单__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/del-menu
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|菜单id|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": null
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

