
## __创建权限类__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/create-class
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| name|是|string(50)|类名|
| system|是|Integer(4)|所属系统（1、admin后台 2、商户后台 3、代理商后台）|
| sort|否|Integer(11)|排序|
| remark|否|string(255)|备注|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 1,
        "name": "class1",
        "system": 2,
        "created": null,
        "modified": null,
        "deleted": 1
    }
}
```
<br  />
## __获取权限类详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/get-class
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|ID|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 1,
        "name": "class1",
        "system": 2,
        "created": null,
        "modified": null,
        "deleted": 1,
        "authFunction": [
            {
                "id": 1,
                "class_id": 1,
                "name": "function1",
                "system": 2,
                "sort": 1,
                "remark": "mark",
                "created": null,
                "modified": null,
                "deleted": 1
            },
            {
                "id": 2,
                "class_id": 1,
                "name": "function2",
                "system": 2,
                "sort": 1,
                "remark": "mark",
                "created": null,
                "modified": null,
                "deleted": 1
            }
        ]
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取权限类信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/get-class-info
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| name|是|string(50)|类名|
| system|是|Integer(4)|所属系统（1、admin后台 2、商户后台 3、代理商后台）|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 1,
        "name": "class1",
        "system": 2,
        "created": null,
        "modified": null,
        "deleted": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取权限类列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/find-class
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| system|是|Integer(4)|所属系统（1、admin后台 2、商户后台 3、代理商后台）|

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
            "name": "class1",
            "system": 2,
            "created": null,
            "modified": null,
            "deleted": 1,
            "authFunction": [
                {
                    "id": 1,
                    "class_id": 1,
                    "name": "function1",
                    "system": 2,
                    "sort": 1,
                    "remark": "mark",
                    "created": null,
                    "modified": null,
                    "deleted": 1
                },
                {
                    "id": 2,
                    "class_id": 1,
                    "name": "function2",
                    "system": 2,
                    "sort": 1,
                    "remark": "mark",
                    "created": null,
                    "modified": null,
                    "deleted": 1
                }
            ]
        }
    ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __删除权限类__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/del-class
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|类id|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok"
}
```
<br  />

## __创建权限方法__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/create-function
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| name|是|string(50)|类名|
| system|是|Integer(4)|所属系统（1、admin后台 2、商户后台 3、代理商后台）|
| class_id | 是 | Integer(11) | 所属类id |
| sort|否|Integer(11)|排序|
| remark|否|string(255)|备注|
| sync|否|Integer(4)|是否同步添加到默认权限模板和添加到默认角色，1是，其他为否|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 1,
        "name": "func",
        "class_id": 1,
        "system": 2,
        "created": null,
        "modified": null,
        "deleted": 1
    }
}
```
<br  />

## __批量创建权限方法__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/batch-create-function
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| funcs|是|string|方法数组|

<br  />
##### funcs数组参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| name|是|string(50)|类名|
| system|是|Integer(4)|所属系统（1、admin后台 2、商户后台 3、代理商后台）|
| class_id | 是 | Integer(11) | 所属类id |
| sort|否|Integer(11)|排序|
| remark|否|string(255)|备注|
| menus|否|string(255)|所属的权限菜单id,用逗号隔开|
| sync|否|Integer(4)|是否同步添加到默认权限模板和添加到默认角色，1是，其他为否|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",

}
```
<br  />
## __获取权限方法详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/get-function
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|方法id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 1,
        "class_id": 1,
        "name": "function1",
        "system": 2,
        "sort": 1,
        "remark": "mark",
        "created": null,
        "modified": null,
        "deleted": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __根据名称获取权限方法详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/get-function
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| name|是|string(50)|类名|
| system|是|Integer(4)|所属系统（1、admin后台 2、商户后台 3、代理商后台）|

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 1,
        "class_id": 1,
        "name": "function1",
        "system": 2,
        "sort": 1,
        "remark": "mark",
        "created": null,
        "modified": null,
        "deleted": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取权限方法列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/find-function
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| class_id | 是 | Integer(11) | 所属类id |
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
            "class_id": 1,
            "name": "function1",
            "system": 2,
            "sort": 1,
            "remark": "mark",
            "created": null,
            "modified": null,
            "deleted": 1
        },
        {
            "id": 2,
            "class_id": 1,
            "name": "function2",
            "system": 2,
            "sort": 1,
            "remark": "mark",
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


## __获取系统的全部权限方法列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/find-system-function
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| system | 是 | Integer(4) | 所属系统（1、admin后台 2、商户后台 3、代理商后台） |
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
            "class_id": 1,
            "name": "function1",
            "system": 2,
            "sort": 1,
            "remark": "mark",
            "created": null,
            "modified": null,
            "deleted": 1,
            "authClass":
            {
              "id":1,
              "name":"activity-points",
              "system": 2,
              "sort": 1,
              "remark": "mark"
            }
        },
        {
            "id": 2,
            "class_id": 1,
            "name": "function2",
            "system": 2,
            "sort": 1,
            "remark": "mark",
            "created": null,
            "modified": null,
            "deleted": 1,
            "authClass":
            {
              "id":2,
              "name":"kk",
              "system": 2,
              "sort": 1,
              "remark": "mark"
            }
        }
    ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __删除权限方法__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/del-function
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|方法id|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok"
}
```
<br  />


## __分配权限方法归属权限菜单__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/save-r-function-menu
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| function_id|是|Integer(11)|权限方法id|
| menu_ids|是|Array|权限菜单id数组|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok"
}
```
<br  />

