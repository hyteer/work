## __创建角色__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/create-role
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| title|是|string(50)|角色名称|
| system|是|integer(4)|所属系统（1.admin后台、2.店铺后台、3.代理商后台）|
| shop_id|是|Integer(11)|商家id|
| shop_sub_id|否|Integer(11)|店铺id|
| is_default|否|Integer(4)|是否是默认角色，1是，2不是，默认否|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "title": "role6",
        "system": 2,
        "shop_id": 5,
        "shop_sub_id": 43,
        "created": 1438848854,
        "modified": 1438848854,
        "deleted": 1,
        "id": 6
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __获取角色详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/get-role
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|角色ID|
| shop_id|是|Integer(11)|商家id|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 6,
        "title": "role6-6",
        "system": 2,
        "shop_id": 5,
        "shop_sub_id": 43,
        "created": 1438848854,
        "modified": 1438851462,
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
                "deleted": 1,
                "authClass": {
                    "id": 1,
                    "name": "class1",
                    "system": 2,
                    "created": null,
                    "modified": null,
                    "deleted": 1
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
                "authClass": {
                    "id": 1,
                    "name": "class1",
                    "system": 2,
                    "created": null,
                    "modified": null,
                    "deleted": 1
                }
            }
        ]
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取角色列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/find-role
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| system | 是 | Integer(4) | 所属系统（1.admin后台、2.店铺后台、3.代理商后台） |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": [
        {
            "id": 3,
            "title": "role1",
            "system": 2,
            "shop_id": 5,
            "shop_sub_id": null,
            "created": 1438677992,
            "modified": 1438677992,
            "deleted": 1
        },
        {
            "id": 6,
            "title": "role6",
            "system": 2,
            "shop_id": 5,
            "shop_sub_id": 43,
            "created": 1438848854,
            "modified": 1438848854,
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

## __修改角色信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/update-role
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 角色id |
| title | 是 | string(50) | 角色名称 |
| shop_id | 是 | Integer(11) | 商家id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 6,
        "title": "role6-6",
        "system": 2,
        "shop_id": 5,
        "shop_sub_id": 43,
        "created": 1438848854,
        "modified": 1438851462,
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
                "deleted": 1,
                "authClass": {
                    "id": 1,
                    "name": "class1",
                    "system": 2,
                    "created": null,
                    "modified": null,
                    "deleted": 1
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
                "authClass": {
                    "id": 1,
                    "name": "class1",
                    "system": 2,
                    "created": null,
                    "modified": null,
                    "deleted": 1
                }
            }
        ]
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __删除角色__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/del-role
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 角色id |
| shop_id | 是 | Integer(11) | 商家id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php

```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __分配角色功能权限__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/save-role-function-menu
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| auth_role_id | 是 | Integer(11) | 角色id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| function_menu_ids | 是 | Array | 权限方法id数组集合 |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "auth_role_id": 6,
        "shop_id": 5,
        "auth_function_id": 2
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __获取角色功能权限(权限id,权限方法名，类名)__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/find-role-function
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| role_id | 是 | Integer(11) | 角色id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "func_id": 6,
        "func_name": "function1",
        "class_name": "class1"
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __获取角色权限菜单列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/find-role-function-menus
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| role_id | 是 | Integer(11) | 角色id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
      "RAuthRoleAuthFunction": [
        {
          "auth_role_id": "66",
          "auth_function_menu_id": "1756",
          "shop_id": "30",
          "shop_sub_id": "193"
        },
        {
          "auth_role_id": "66",
          "auth_function_menu_id": "1757",
          "shop_id": "30",
          "shop_sub_id": "193"
        }
      ]
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
