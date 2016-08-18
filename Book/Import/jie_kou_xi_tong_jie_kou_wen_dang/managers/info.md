## __创建管理员__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/shop-manager/create-shop-manager
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| qq | 是 | Varchar(50) | QQ号 |
| password | 是 | Varchar(50) | 密码 |
| shop_id | 是 | Integer(11) | 商家id |
| role_id | 是 | Integer(11) | 角色id |
| name | 否 | Varchar(50) | 名称 |
| sex | 否 | Integer(1) | 性别 |
| email | 否 | Varchar(100) | 邮箱 |
| phone | 否 | Varchar(20) | 电话 |
| address | 否 | Varchar(100) | 地址 |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "qq":"1212123",
        "password":"21218cca77804d2ba1922c33e0151105",
        "role_id":56,
        "shop_id":30,
        "created":1440409995,
        "modified":1440409995,
        "deleted":1,
        "id":896
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __修改管理员信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/shop-manager/update-shop-manager
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 管理员id |
| qq | 否 | Varchar(50) | QQ号 |
| shop_id | 是 | Integer(11) | 商家id |
| name | 否 | Varchar(50) | 名称 |
| sex | 否 | Integer(1) | 性别 |
| email | 否 | Varchar(100) | 邮箱 |
| phone | 否 | Varchar(20) | 电话 |
| address | 否 | Varchar(100) | 地址 |
| role_id | 否 | Integer(11) | 角色id |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":896,
        "qq":"7878789",
        "password":"21218cca77804d2ba1922c33e0151105",
        "name":"管理员1",
        "sex":1,
        "email":null,
        "phone":null,
        "address":null,
        "shop_id":30,
        "review_status":3,
        "remark":null,
        "is_default":2,
        "role_id":56,
        "created":1440409995,
        "modified":1440411188,
        "deleted":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __删除管理员账号__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/shop-manager/delete-shop-manager
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 管理员id |
| shop_id | 是 | Integer(11) | 商家id |
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


## __获取管理员详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/shop-manager/get-shop-manager
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 管理员id |
| shop_id | 是 | Integer(11) | 商家id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":896,
        "qq":"7878789",
        "password":"21218cca77804d2ba1922c33e0151105",
        "name":"管理员1",
        "sex":1,
        "email":null,
        "phone":null,
        "address":null,
        "shop_id":30,
        "review_status":3,
        "remark":null,
        "is_default":2,
        "role_id":56,
        "created":1440409995,
        "modified":1440411784,
        "deleted":1,
        "shopStaff":{
            "id":68,
            "user_name":null,
            "password":null,
            "real_name":"m-7878789",
            "role_id":0,
            "mobile":null,
            "email":null,
            "shop_sub_id":0,
            "shop_id":30,
            "ewm_img":null,
            "scene_id":0,
            "last_login":0,
            "path":null,
            "is_bind":2,
            "is_cancel":2,
            "is_super_cancel":2,
            "is_default":2,
            "shop_manager_id":896,
            "created":1440409995,
            "modified":1440411784,
            "deleted":1
        },
        "authRole":{
            "id":56,
            "title":"manager",
            "system":1,
            "shop_id":30,
            "shop_sub_id":0,
            "is_default":2,
            "created":null,
            "modified":1440410122,
            "deleted":1
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取管理员列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/shop-manager/find-shop-manager
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":[
        {
            "id":895,
            "qq":"7638800811",
            "password":"21218cca77804d2ba1922c33e0151105",
            "name":"",
            "sex":1,
            "email":null,
            "phone":null,
            "address":null,
            "shop_id":30,
            "review_status":3,
            "remark":null,
            "is_default":1,
            "role_id":47,
            "created":1440394986,
            "modified":1440395343,
            "deleted":1,
            "authRole":{
                "id":47,
                "title":"默认管理员",
                "system":1,
                "shop_id":30,
                "shop_sub_id":187,
                "is_default":1,
                "created":1440394985,
                "modified":1440394985,
                "deleted":1
            }
        }
    ],
    "page":{
        "per_page":10,
        "total_count":1,
        "current_page":0,
        "total_page":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />




## __修改密码__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/shop-manager/update-password
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 管理员id |
| password | 是 | String(50) | 密码 |
| shop_id | 是 | Integer(11) | 商家id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":896,
        "qq":"7878789",
        "password":"e10adc3949ba59abbe56e057f20f883e",
        "name":"管理员1",
        "sex":1,
        "email":null,
        "phone":null,
        "address":null,
        "shop_id":30,
        "remark":null,
        "is_default":2,
        "role_id":56,
        "created":1440409995,
        "modified":1440416871,
        "deleted":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __修改自己的密码__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/shop-manager/update-my-password
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 管理员id |
| old_password | 是 | String(50) | 旧密码 |
| password | 是 | String(50) | 新密码 |
| shop_id | 是 | Integer(11) | 商家id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":896,
        "qq":"7878789",
        "password":"e10adc3949ba59abbe56e057f20f883e",
        "name":"管理员1",
        "sex":1,
        "email":null,
        "phone":null,
        "address":null,
        "shop_id":30,
        "remark":null,
        "is_default":2,
        "role_id":56,
        "created":1440409995,
        "modified":1440416871,
        "deleted":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __管理员登录__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/shop-manager/shop-manager-login
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| qq | 是 | String(50) | qq |
| password | 是 | String(50) | 新密码 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "shop":{
            "id":30,
            "name":"pp",
            "category_f":0,
            "category_s":0,
            "qq":null,
            "company_sid":0,
            "pickup_status":2,
            "self_platform":1,
            "platform_info_id":1,
            "contract_no":"111111",
            "contract_start":"2015-08-01",
            "contract_end":"2015-08-29",
            "group_id":17,
            "tel":"18577777777",
            "website":"www.bbs.com",
            "addr":"pp",
            "desc":"pp",
            "bg_img":"http:\/\/imgcache.vikduo.com\/static\/ef356219b4d5d567e13dd984c7132666.jpg",
            "logo":null,
            "review_status":1,
            "created":1440394985,
            "modified":1440394985,
            "deleted":1
        },
        "shop_staff":{
            "id":68,
            "user_name":null,
            "real_name":"m-7878789",
            "role_id":0,
            "mobile":null,
            "email":null,
            "shop_sub_id":0,
            "shop_id":30,
            "ewm_img":null,
            "scene_id":0,
            "last_login":0,
            "path":null,
            "is_bind":2,
            "is_cancel":2,
            "is_super_cancel":2,
            "is_default":2,
            "shop_manager_id":896,
            "created":1440409995,
            "modified":1440412396,
            "deleted":1
        },
        "shop_manager":{
            "id":896,
            "qq":"7878789",
            "name":"管理员1",
            "sex":1,
            "email":null,
            "phone":null,
            "address":null,
            "shop_id":30,
            "remark":null,
            "is_default":2,
            "role_id":56,
            "created":1440409995,
            "modified":1440416871,
            "deleted":1
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __默认管理员QQ授权登录__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/shop-manager/default-manager-login
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| qq | 是 | String(50) | qq |
| token | 是 | String(100) | token值 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "shop":{
            "id":30,
            "name":"pp",
            "category_f":0,
            "category_s":0,
            "qq":null,
            "company_sid":0,
            "pickup_status":2,
            "self_platform":1,
            "platform_info_id":1,
            "contract_no":"111111",
            "contract_start":"2015-08-01",
            "contract_end":"2015-08-29",
            "group_id":17,
            "tel":"18577777777",
            "website":"www.bbs.com",
            "addr":"pp",
            "desc":"pp",
            "bg_img":"http:\/\/imgcache.vikduo.com\/static\/ef356219b4d5d567e13dd984c7132666.jpg",
            "logo":null,
            "review_status":1,
            "created":1440394985,
            "modified":1440394985,
            "deleted":1
        },
        "shop_staff":{
            "id":68,
            "user_name":null,
            "real_name":"m-7878789",
            "role_id":0,
            "mobile":null,
            "email":null,
            "shop_sub_id":0,
            "shop_id":30,
            "ewm_img":null,
            "scene_id":0,
            "last_login":0,
            "path":null,
            "is_bind":2,
            "is_cancel":2,
            "is_super_cancel":2,
            "is_default":2,
            "shop_manager_id":896,
            "created":1440409995,
            "modified":1440412396,
            "deleted":1
        },
        "shop_manager":{
            "id":896,
            "qq":"7878789",
            "name":"管理员1",
            "sex":1,
            "email":null,
            "phone":null,
            "address":null,
            "shop_id":30,
            "remark":null,
            "is_default":2,
            "role_id":56,
            "created":1440409995,
            "modified":1440416871,
            "deleted":1
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
