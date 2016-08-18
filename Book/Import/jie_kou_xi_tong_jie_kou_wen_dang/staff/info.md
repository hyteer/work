## __创建员工__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/staff/create
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| user_name | 是 | String(20) | 登录用户名 |
| password | 是 | String(32) | 登录密码 |
| real_name | 是 | String(20) | 真实姓名 |
| head_img_url | 否 | String(250) | 员工头像图片 |
| role_id | 是 | Integer(3) | 角色ID |
| mobile | 否 | String(20) | 手机号码 |
| email | 否 | String(50) | 电子邮箱 |
| ewm_img | 否 | String(180) | 带参数二维码 |
| scene_id | 否 | Integer(11) | 二维码参数 |
| path | 否 | String(500) | 路径 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "role_id": 440,
    "shop_sub_id": 310,
    "shop_id": 30,
    "scene_id": 0,
    "last_login": 0,
    "is_bind": 2,
    "is_cancel": 2,
    "is_super_cancel": 2,
    "is_default": 2,
    "is_scan_pay": 2,
    "is_scan_refund": 2,
    "shop_manager_id": 0,
    "agent_id": 0,
    "created": 1453105780,
    "modified": 1453105780,
    "deleted": 1,
    "scan_count": 0,
    "user_name": "biubiu",
    "real_name": "君君",
    "head_img_url": "http://imgcache.vikduo.com/static/166fff617620f13a72f241600abddf4d.png",
    "mobile": "13211111111",
    "email": "bb@123.com",
    "agent_path": null,
    "id": 271
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __扫码支付增加扫码次数__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/staff/add-scan-count
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| id | 是 | Integer(11) | 员工id |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 271,
    "user_name": "biubiu",
    "real_name": "君君",
    "role_id": 440,
    "mobile": "13211111111",
    "email": "bb@123.com",
    "shop_sub_id": 310,
    "shop_id": 30,
    "ewm_img": null,
    "scene_id": 0,
    "last_login": 0,
    "path": null,
    "is_bind": 2,
    "is_cancel": 2,
    "is_super_cancel": 2,
    "is_default": 2,
    "is_scan_pay": 2,
    "is_scan_refund": 2,
    "shop_manager_id": 0,
    "agent_id": 0,
    "agent_path": null,
    "created": 1453105780,
    "modified": 1453106770,
    "deleted": 1,
    "scan_count": 1,
    "wxUserInfo": []
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取商家员工列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/staff/find-shop-staff
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| shop_type | 否 | Integer(4) | 店铺类型 1直营店 2加盟店 |
| is_bind | 否 | Integer(4) | 是否绑定微信 1是 2否 |
| is_cancel | 否 | Integer(4) | 是否核销员 1是 2否 |
| is_super_cancel | 否 | Integer(4) | 是否超级核销员 1是 2否 |
| role_id | 否 | Integer(11) | 角色id |
| real_name | 否 | String(20) | 关键字 |
| is_default | 否 | Integer(4) | 是否默认员工 1是 2否 |
| ids | 否 | Array | 过滤员工id数组 |
| in_ids | 否 | Array | 查找员工数组 |
| agent_id | 否 | Integer(11) | 代理商id |
| search_all | 否 | Boolean | 配合real_name字段，是否同时搜索real_name/mobile |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| createStart | 否 | Integer(11) | 核销查询起始时间 |
| createEnd | 否 | Integer(11) | 查询核销结束时间 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": 270,
      "user_name": "1260106386",
      "real_name": "llj",
      "head_img_url": "http://imgcache.vikduo.com/static/166fff617620f13a72f241600abddf4d.png",
      "role_id": 437,
      "mobile": null,
      "email": null,
      "shop_sub_id": 310,
      "shop_id": 30,
      "ewm_img": null,
      "scene_id": 0,
      "last_login": 0,
      "path": null,
      "is_bind": 2,
      "is_cancel": 2,
      "is_super_cancel": 2,
      "is_default": 1,
      "is_scan_pay": 2,
      "is_scan_refund": 2,
      "shop_manager_id": 0,
      "agent_id": 0,
      "agent_path": null,
      "created": 1453089285,
      "modified": 1453089285,
      "deleted": 1,
      "scan_count": 0,
      "shopSub": {
        "id": 310,
        "pid": 0,
        "shop_id": 30,
        "lng": 112.146818,
        "lat": 37.568119,
        "sync_setting": 1,
        "shop_type": 1,
        "agent_path": null,
        "agent_id": 0,
        "is_pickup_shop": 2,
        "is_fx": 1,
        "created": 1453089284,
        "modified": 1453100058,
        "deleted": 1,
        "shopInfo": {
          "id": 290,
          "shop_id": 30,
          "shop_sub_id": 310,
          "name": "lljtest",
          "bg_img": "http://imgcache.vikduo.com/static/0844adbe52cb19d07c785ac6b0cf7dec.png",
          "description": "description",
          "theme": null,
          "category_del_id": null,
          "ewm_img": "https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=gQFt8DoAAAAAAAAAASxodHRwOi8vd2VpeGluLnFxLmNvbS9xLy1rTVBtajNtSFpGa2U3SXpaMl9wAAIEs2X6VQMEAAAAAA%3D%3D",
          "scene_id": 112,
          "site_img": null,
          "lbs": 1,
          "phone": "13088827340",
          "province_id": 214,
          "city_id": 215,
          "district_id": 216,
          "circle_id": 217,
          "address": "detailAddress",
          "businesshour": "08:00-21:00",
          "url": "http://www.baidu.com",
          "wx_categories": "[{\"id\":\"1\",\"name\":\"\\u7f8e\\u98df\"},{\"id\":\"2\",\"name\":\"\\u6c5f\\u6d59\\u83dc\"},{\"id\":\"3\",\"name\":\"\\u4e0a\\u6d77\\u83dc\"}]",
          "available_status": 1,
          "recommend": "recommend",
          "special": "special",
          "avg_price": 180,
          "poi_id": null,
          "check_time": null,
          "fail_msg": null,
          "update_status": 0,
          "created": 1453089284,
          "modified": 1453101810,
          "deleted": 1
        }
      },
      "shopAgents": [ ],
      "authRole": {
        "id": 437,
        "title": "默认角色",
        "system": 2,
        "shop_id": 30,
        "shop_sub_id": 310,
        "is_default": 1,
        "created": 1453089285,
        "modified": 1453089285,
        "deleted": 1
      }
    }
  ],
  "page": {
    "per_page": 1,
    "total_count": 1,
    "current_page": 0,
    "total_page": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取商家员工归属关系列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/staff/find-belong-shop-staff
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 商铺id |
| agent_id | 否 | Integer(11) | 代理商id |
| mid | 否 | Integer(11) | 分销员id |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": "70",
      "user_name": "12",
      "real_name": "方法",
      "role_id": "55",
      "mobile": "18681515584",
      "email": "21@q.fb",
      "shop_sub_id": "192",
      "shop_id": "30",
      "ewm_img": null,
      "scene_id": "0",
      "is_scan_pay": null,
      "is_scan_refund": null,
      "scan_count": "0",
      "last_login": "0",
      "path": null,
      "is_bind": "1",
      "is_cancel": "2",
      "is_super_cancel": "2",
      "is_default": "2",
      "shop_manager_id": "0",
      "agent_id": null,
      "agent_path": null,
      "created": "1440414291",
      "modified": "1442820872",
      "deleted": "1"
    }
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取员工信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/staff/get
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| staff_id | 是 | Integer(11) | 员工id |
<br  />


##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 271,
    "user_name": "biubiu",
    "real_name": "君君",
    "head_img_url": "http://imgcache.vikduo.com/static/166fff617620f13a72f241600abddf4d.png",
    "role_id": 440,
    "mobile": "13211111111",
    "email": "bb@123.com",
    "shop_sub_id": 310,
    "shop_id": 30,
    "ewm_img": null,
    "scene_id": 0,
    "last_login": 0,
    "path": null,
    "is_bind": 2,
    "is_cancel": 2,
    "is_super_cancel": 2,
    "is_default": 2,
    "is_scan_pay": 2,
    "is_scan_refund": 2,
    "shop_manager_id": 0,
    "agent_id": 0,
    "agent_path": null,
    "created": 1453105780,
    "modified": 1453106770,
    "deleted": 1,
    "scan_count": 1,
    "wxUserInfo": []
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __修改员工信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/staff/to-update
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| staff_id | 是 | Integer(11) | 员工id |
| user_name | 否 | String(20) | 登录用户名 |
| real_name | 否 | String(20) | 真实姓名 |
| head_img_url | 否 | String(250) | 员工头像图片 |
| role_id | 否 | Integer(3) | 角色ID |
| mobile | 否 | String(20) | 手机号码 |
| email | 否 | String(50) | 电子邮箱 |
| ewm_img | 否 | String(180) | 带参数二维码 |
| scene_id | 否 | Integer(11) | 二维码参数 |
| path | 否 | String(500) | 路径 |
| is_scan_pay | 否 | Integer(4) | 是否开启扫码支付 |
| is_scan_refund | 否 | Integer(4) | 是否开启扫码退款 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 271,
    "user_name": "biubiu",
    "real_name": "君君",
    "head_img_url": "http://imgcache.vikduo.com/static/166fff617620f13a72f241600abddf4d.png",
    "role_id": 440,
    "mobile": "13211111111",
    "email": "bb@123.com",
    "shop_sub_id": 310,
    "shop_id": 30,
    "ewm_img": null,
    "scene_id": 0,
    "last_login": 0,
    "path": null,
    "is_bind": 2,
    "is_cancel": 2,
    "is_super_cancel": 2,
    "is_default": 2,
    "is_scan_pay": 2,
    "is_scan_refund": 2,
    "shop_manager_id": 0,
    "agent_id": 0,
    "agent_path": null,
    "created": 1453105780,
    "modified": 1453107774,
    "deleted": 1,
    "scan_count": 1,
    "wxUserInfo": []
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __禁用员工__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/staff/close
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| staff_id | 是 | Integer(11) | 员工id |
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


## __取消禁用员工__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/staff/open
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| staff_id | 是 | Integer(11) | 员工id |
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


## __删除员工__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/staff/del
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 商铺id |
| staff_id | 是 | Integer(11) | 员工id |
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


## __员工修改登陆密码__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/staff/update-pwd
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 商铺id |
| staff_id | 是 | Integer(11) | 员工id |
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
    "id": 271,
    "user_name": "biubiu",
    "real_name": "君君",
    "role_id": 440,
    "mobile": "13211111111",
    "email": "bb@123.com",
    "shop_sub_id": 310,
    "shop_id": 30,
    "ewm_img": null,
    "scene_id": 0,
    "last_login": 0,
    "path": null,
    "is_bind": 2,
    "is_cancel": 2,
    "is_super_cancel": 2,
    "is_default": 2,
    "is_scan_pay": 2,
    "is_scan_refund": 2,
    "shop_manager_id": 0,
    "agent_id": 0,
    "agent_path": null,
    "created": 1453105780,
    "modified": 1453171448,
    "deleted": 1,
    "scan_count": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __商家修改员工登陆密码__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/staff/manager-update-pwd
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 商铺id |
| staff_id | 是 | Integer(11) | 员工id |
| new_pwd | 是 | String(32) | 新登陆密码 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 271,
    "user_name": "biubiu",
    "real_name": "君君",
    "role_id": 440,
    "mobile": "13211111111",
    "email": "bb@123.com",
    "shop_sub_id": 310,
    "shop_id": 30,
    "ewm_img": null,
    "scene_id": 0,
    "last_login": 0,
    "path": null,
    "is_bind": 2,
    "is_cancel": 2,
    "is_super_cancel": 2,
    "is_default": 2,
    "is_scan_pay": 2,
    "is_scan_refund": 2,
    "shop_manager_id": 0,
    "agent_id": 0,
    "agent_path": null,
    "created": 1453105780,
    "modified": 1453171525,
    "deleted": 1,
    "scan_count": 1,
    "wxUserInfo": []
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __员工登录__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/staff/shop_staff-login
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| username | 是 | String(40) | 登录用户名 |
| password | 是 | String(32) | 登录密码 |
| wx_account | 是 | String(20) | 商家微信号 |
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
        "shop_sub":{
            "id":187,
            "pid":0,
            "shop_id":30,
            "lng":0,
            "lat":0,
            "sync_setting":1,
            "shop_type":1,
            "agent_path":null,
            "agent_id":0,
            "is_pickup_shop":2,
            "is_fx":2,
            "created":1440394985,
            "modified":1440394985,
            "deleted":1
        },
        "shop_info":{
            "id":167,
            "shop_id":30,
            "shop_sub_id":187,
            "name":"pp",
            "bg_img":"http:\/\/imgcache.vikduo.com\/static\/ef356219b4d5d567e13dd984c7132666.jpg",
            "description":"pp",
            "theme":null,
            "category_del_id":null,
            "ewm_img":null,
            "scene_id":0,
            "site_img":null,
            "lbs":1,
            "phone":"18577777777",
            "province_id":1,
            "city_id":2,
            "district_id":7,
            "circle_id":8,
            "address":"pp",
            "businesshour":"8:00-19:00",
            "url":"http:\/\/www.bbs.com",
            "wx_categories":null,
            "created":1440394985,
            "modified":1440394985,
            "deleted":1
        },
        "shop_staff":{
            "id":73,
            "user_name":"LiSi",
            "real_name":"李四",
            "role_id":62,
            "mobile":null,
            "email":null,
            "shop_sub_id":187,
            "shop_id":30,
            "ewm_img":null,
            "scene_id":0,
            "last_login":0,
            "path":null,
            "is_bind":2,
            "is_cancel":2,
            "is_super_cancel":2,
            "is_default":2,
            "shop_manager_id":0,
            "created":1440418855,
            "modified":1440423383,
            "deleted":1
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __绑定员工微信帐号__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/staff/bind-staff-user
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| user_name | 是 | String(20) |  员工帐号 |
| pwd | 是 | String(20) |  员工密码 |
| uid | 是 | Integer(11) | 用户id |
| shop_id | 是 | Integer(11) |  商户id |
| isManager | 否 | Boolean |  是否管理员，默认false |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data":null
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __取消绑定员工微信帐号__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/staff/cancel-staff-user-bind
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| staff_id | 是 | String(20) |  员工id |
| shop_id | 是 | Integer(11) |  商户id |

<br  /><br  />
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



## __获取员工收款码地址__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/staff/get-staff-scan-pay-url
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| staff_id | 是 | String(20) |  员工id |
| shop_id | 是 | Integer(11) |  商户id |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": "http://scliveapp2015.wx333.newwsh.vikduo.com/scliveapp2015/scan-pay/staff?id=369"
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
