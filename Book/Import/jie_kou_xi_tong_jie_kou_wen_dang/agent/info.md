## __代理商登录__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/agent/agent-login
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| user_name | 是 | String | 代理商用户名 |
| password | 是 | String | 代理商密码 |
| wx_account | 是 | String | 商家微信帐号 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "shop": {
      "id": 30,
      "name": "尽快形成顺畅高效的，尽快形成顺畅高效的联合作战",
      "category_f": 1,
      "category_s": 2,
      "qq": null,
      "company_sid": 0,
      "pickup_status": 2,
      "self_platform": 1,
      "platform_info_id": 1,
      "contract_no": "111111",
      "contract_start": "2015-08-01",
      "contract_end": "2015-08-29",
      "group_id": 17,
      "tel": "13632723453",
      "website": "http://www.shanghu.com/shop/edit?id=5",
      "addr": "sdfsdadasa",
      "desc": " ",
      "bg_img": "http://imgcache.vikduo.com/static/1b13a2005cc2d1a91f72f32d05da6c3a.jpg",
      "logo": "http://imgcache.vikduo.com/static/2d36c4a760add3e782ced63cab384114.jpg",
      "review_status": 1,
      "auto_refund": 1,
      "version": 3,
      "created": 1440394985,
      "modified": 1453106008,
      "deleted": 1,
      "after_sale_time_status": 2,
      "after_sale_handle_time": 5,
      "return_address": "广东省河源市龙川县老隆镇联丰村59栋59号",
      "return_consignee": "唐雄",
      "return_phone": "13632723451"
    },
    "shop_agent": {
      "id": 28,
      "pid": 27,
      "user_name": "bottle",
      "real_name": "瓶子",
      "role_id": 80,
      "mobile": "13247895874",
      "email": null,
      "shop_id": 30,
      "last_login": 0,
      "agent_name": "三级代理商",
      "path": "/26/27/28/",
      "area": "华北",
      "level": 3,
      "is_default": 1,
      "created": 1440573848,
      "modified": 1440639818,
      "deleted": 1
    },
    "permissions": [
      "agent/index"
    ],
    "menus": [
      {
        "id": 102,
        "pid": 0,
        "title": "系统设置",
        "system": 3,
        "url_type": 1,
        "url_param": null,
        "is_target": 1,
        "remark": null,
        "sort": 1,
        "key": "_shop_manage",
        "auth_functions": null,
        "created": 1440420236,
        "modified": 1440420236,
        "deleted": 1
      }
    ]
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __创建代理商__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/agent/create-agents-by-admin
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| pid | 是 | Integer(11) | 上级代理商id（没有设置为0） |
| shop_id | 是 | Integer(11) | 商家id |
| user_name | 是 | String(20) | 登录用户名 |
| password | 是 | String(32) | 登录密码 |
| real_name | 是 | String(20) | 真实姓名 |
| mobile | 否 | String(20) | 手机号码 |
| email | 否 | String(50) | 电子邮箱 |
| agent_name | 是 | String(100) | 代理商名称 |
| path | 否 | String(500) | 路径 |
| area | 否 | String(100) | 地区 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "pid": 27,
    "role_id": 471,
    "shop_id": 30,
    "last_login": 0,
    "level": 3,
    "is_default": 1,
    "created": 1453183962,
    "modified": 1453183962,
    "deleted": 1,
    "user_name": "llj",
    "real_name": "刘莉君",
    "agent_name": "深圳代理",
    "id": 53,
    "path": "/26/27/53/"
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取商家代理商列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/agent/find-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| agent_id | 否 | Integer(11) | 代理id，如果设了该值则读取该代理商下面的代理商，否则读取商家代理商 |
| nopid | 否 | Boolean | 是否一级代理商 |
| agent_name | 否 | String(100) | 代理商名称 |
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
      "id": 26,
      "pid": 0,
      "user_name": "1",
      "real_name": "2",
      "role_id": 72,
      "mobile": "18681515584",
      "email": null,
      "shop_id": 30,
      "last_login": 0,
      "agent_name": "1一级代理商",
      "path": "/26/",
      "area": "深圳",
      "level": 1,
      "is_default": 1,
      "created": 1440422379,
      "modified": 1452484290,
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


## __获取归属关系代理商列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/agent/find-belong-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| agent_id | 否 | Integer(11) | 代理id，如果设了该值则读取该代理商下面的代理商，否则读取商家代理商 |
| nopid | 否 | Boolean | 是否一级代理商 |
| agent_name | 否 | String(100) | 代理商名称 |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| belong_to_staff_id | 否 | Integer(11) | 归属员工id |
| mid | 否 | Integer(11) | 分销员id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
* **注意：sort排序可选字段['id']**

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": "26",
      "pid": "0",
      "user_name": "1",
      "real_name": "2",
      "role_id": "72",
      "mobile": "18681515584",
      "email": null,
      "shop_id": "30",
      "last_login": "0",
      "created": "1440422379",
      "modified": "1452484290",
      "agent_name": "1一级代理商",
      "path": "/26/",
      "area": "深圳",
      "level": "1",
      "is_default": "1",
      "deleted": "1"
    }
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取代理商信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/agent/get
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| agent_id | 是 | Integer(11) | 代理商id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 26,
    "pid": 0,
    "user_name": "1",
    "real_name": "2",
    "role_id": 72,
    "mobile": "18681515584",
    "email": null,
    "shop_id": 30,
    "last_login": 0,
    "agent_name": "1一级代理商",
    "path": "/26/",
    "area": "深圳",
    "level": 1,
    "is_default": 1,
    "created": 1440422379,
    "modified": 1452484290,
    "deleted": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __修改代理商信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/agent/to-update
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| agent_id | 是 | Integer(11) | 代理商id |
| user_name | 否 | String(20) | 登录用户名 |
| real_name | 否 | String(20) | 真实姓名 |
| role_id | 否 | Integer(3) | 角色ID |
| mobile | 否 | String(20) | 手机号码 |
| email | 否 | String(50) | 电子邮箱 |
| agent_name | 是 | String(100) | 代理商名称 |
| area | 否 | String(100) | 地区 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 26,
    "pid": 0,
    "user_name": "1",
    "real_name": "2",
    "role_id": 72,
    "mobile": "18681515584",
    "email": null,
    "shop_id": 30,
    "last_login": 0,
    "agent_name": "1一级代理商",
    "path": "/26/",
    "area": "深圳",
    "level": 1,
    "is_default": 1,
    "created": 1440422379,
    "modified": 1453185236,
    "deleted": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __修改登陆密码__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/agent/update-pwd
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| agent_id | 是 | Integer(11) | 代理商id |
| old_pwd | 是 | String(32) | 旧登陆密码 |
| new_pwd | 是 | String(32) | 新登陆密码 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 26,
    "pid": 0,
    "user_name": "1",
    "real_name": "2",
    "role_id": 72,
    "mobile": "18681515584",
    "email": null,
    "shop_id": 30,
    "last_login": 0,
    "agent_name": "1一级代理商",
    "path": "/26/",
    "area": "深圳",
    "level": 1,
    "is_default": 1,
    "created": 1440422379,
    "modified": 1453185236,
    "deleted": 1
  }
}
```

错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __管理员修改登陆密码__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/agent/manager-update-pwd
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| agent_id | 是 | Integer(11) | 代理商id |
| new_pwd | 是 | String(32) | 新登陆密码 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 26,
    "pid": 0,
    "user_name": "1",
    "real_name": "2",
    "role_id": 72,
    "mobile": "18681515584",
    "email": null,
    "shop_id": 30,
    "last_login": 0,
    "agent_name": "1一级代理商",
    "path": "/26/",
    "area": "深圳",
    "level": 1,
    "is_default": 1,
    "created": 1440422379,
    "modified": 1453185236,
    "deleted": 1
  }
}
```

错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />




