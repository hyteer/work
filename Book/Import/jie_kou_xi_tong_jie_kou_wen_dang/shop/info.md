## __修改商家设置__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/shop/update-shop-setting
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| is_scan_pay | 否 | Integer(11) | 是否开启扫码支付，1是2否 |
| scan_limit_amount | 否 | Integer(11) | 单笔扫码支付最大金额 |
| reserves_warning_num | 否 | Integer(11) | 库存预警值 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 293,
    "shop_id": 30,
    "is_scan_pay": 1,
    "scan_limit_amount": 1000
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __修改店铺设置__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/shop/update-shopsub-setting
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| is_scan_pay | 否 | Integer(11) | 是否开启扫码支付，1是2否 |
| scan_limit_amount | 否 | Integer(11) | 单笔扫码支付最大金额 |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "is_scan_pay": 1,
    "scan_count": 0,
    "shop_id": 30,
    "shop_sub_id": 192,
    "id": 309
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __获取商家的店铺列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/shop/find-shopsub-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| ids | 否 | Array | 门店id |
| name | 否 | String(50) | 门店名称 |
| province_id | 否 | Integer(11) | 省id |
| city_id | 否 | Integer(11) | 市id |
| district_id | 否 | Integer(11) | 县id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_type | 否 | Integer(11) | 门店类型1.直营店、2.加盟店 |
| agent_id | 否 | Integer(11) | 代理商id |
| available_status | 否 | Integer(11) | 微信创建门店状态 1未同步 2审核中 3创建成功 4创建失败 |
| poi_id | 否 | Integer(11) | 微信小店id |
| doFilter | 否 | Array | 过滤字段指定值 |
| search_all | 否 | Boolean | 配合name参数，是否对address/phone/name多字段搜索 |
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
      "id": 192,
      "pid": 187,
      "shop_id": 30,
      "lng": 116.234275,
      "lat": 39.942327,
      "sync_setting": 1,
      "shop_type": 1,
      "agent_path": null,
      "agent_id": 0,
      "is_pickup_shop": 2,
      "is_fx": 1,
      "created": 1440406329,
      "modified": 1440419015,
      "deleted": 1,
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
        "modified": 1453085479,
        "deleted": 1,
        "after_sale_time_status": 1,
        "after_sale_handle_time": 6,
        "return_address": "广东省河源市龙川县老隆镇联丰村59栋59号",
        "return_consignee": "唐雄",
        "return_phone": "13632723451"
      },
      "shopSubSetting": {
        "id": 309,
        "shop_id": 30,
        "shop_sub_id": 192,
        "is_scan_pay": 1,
        "scan_count": 0
      },
      "shopInfo": {
        "id": 172,
        "shop_id": 30,
        "shop_sub_id": 192,
        "name": "122",
        "bg_img": "http://imgcache.vikduo.com/static/446eb23c7062bb203f21d5c6108cb76a.png",
        "description": "333",
        "theme": null,
        "category_del_id": null,
        "ewm_img": "http://imgcache.vikduo.com/static/57cbdb6c373f42659dfb7c9e1c501de7.jpg",
        "scene_id": 0,
        "site_img": "http://imgcache.vikduo.com/static/2d36c4a760add3e782ced63cab384114.jpg",
        "lbs": 1,
        "phone": "13232323232",
        "province_id": 1,
        "city_id": 2,
        "district_id": 3,
        "circle_id": 4,
        "address": "12",
        "businesshour": "09:00-12:00",
        "url": "http://www.shanghu.com/terminal/add",
        "wx_categories": "[{\"id\":98,\"name\":\"\u57fa\u7840\u8bbe\u65bd\"},{\"id\":99,\"name\":\"\u4ea4\u901a\u8bbe\u65bd\"},{\"id\":100,\"name\":\"\u4ea4\u901a\u670d\u52a1\u76f8\u5173\"}]",
        "available_status": 4,
        "recommend": null,
        "special": null,
        "avg_price": null,
        "poi_id": "402528528",
        "check_time": null,
        "fail_msg": "行政区划有误或坐标与地址不符",
        "update_status": 0,
        "created": 1440406329,
        "modified": 1452740565,
        "deleted": 1
      }
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



## __获取归属关系商家的店铺列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/shop/find-belong-shopsub-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| agent_id | 否 | Integer(11) | 代理商id |
| belong_to_staff_id | 否 | Integer(11)/Array | 归属员工id |
| mid | 否 | Integer(11)/Array | 归属分销员id |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": "167",
      "shop_id": "30",
      "shop_sub_id": "187",
      "name": "pp",
      "bg_img": "http://imgcache.vikduo.com/static/ef356219b4d5d567e13dd984c7132666.jpg",
      "description": "pp",
      "theme": null,
      "category_del_id": null,
      "ewm_img": null,
      "scene_id": "0",
      "site_img": null,
      "lbs": "1",
      "phone": "18577777777",
      "province_id": "1",
      "city_id": "2",
      "district_id": "7",
      "circle_id": "8",
      "address": "pp",
      "businesshour": "8:00-19:00",
      "url": "http://www.bbs.com",
      "wx_categories": null,
      "available_status": "1",
      "recommend": null,
      "special": null,
      "avg_price": null,
      "poi_id": "",
      "check_time": null,
      "fail_msg": null,
      "update_status": "0",
      "created": "1440394985",
      "modified": "1446707283",
      "deleted": "1"
    }
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __创建分店店铺__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/shop/create-shopsub
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shopSub.shop_id | 是 | Integer(11) | 商家id |
| shopSub.sync_setting | 否 | Integer(3) | 是否同步总店第三方的配置（1。是、2.否） |
| shopSub.lng | 否 | Double | 经度 |
| shopSub.lat | 否 | Double | 纬度 |
| shopSub.agent_path | 否 | String(255) | 分销路径 |
| shopSub.agent_id | 否 | Integer(11) | 分销商id |
| shopSub.shop_type | 是 | Integer(3) | 总店才有操作权限：店铺类型(1:直营店,2:加盟店) |
| shopSub.is_pickup_shop | 否 | Integer(3) | 总店才有操作权限：是否启用到店自提(1：启用，2：禁用)
| shopInfo.name | 是 | String(20) | 店铺名称 |
| shopInfo.phone | 否 | String(20) | 手机号码 |
| shopInfo.province_id | 否 | Integer(11) | 店铺省id |
| shopInfo.city_id | 否 | Integer(11) | 店铺城市id |
| shopInfo.district_id | 否 | Integer(11) | 店铺区id |
| shopInfo.address | 否 | String(255) | 店铺详细地址 |
| shopInfo.circle_id | 否 | Integer(11) | 商圈id |
| shopInfo.businesshour | 否 | String(20) | 营业时间 |
| shopInfo.url | 否 | String(255) | 网站 |
| shopInfo.bg_img | 否 | String(255) | 店铺背景图 |
| shopInfo.description | 否 | String(255) | 店铺描述 |
| shopInfo.theme | 否 | String(20) | 店铺模板 |
| shopInfo.site_img | 否 | String(255) |  |
| shopInfo.lbs | 否 | Integer(3) | 是否开启店铺定位（1：开启，2：不开启） |
| shopInfo.ewm_img | 否 | String(255) | 店铺二维码 |
| shopInfo.scene_id | 否 | Integer(11) | 推广二维码参数id |
| shopInfo.category_del_id | 否 | String(255) | 删除的分类id |
| shopInfo.wx_categories | 否 | String(255) | 微信小店分类格式：{''id'':"name","id":"name"}|
| shopInfo.recomment | 否 | String(500) | 推荐内容 |
| shopInfo.special | 否 | String(500) | 特色服务 |
| shopStaff.avg_price | 否 | Integer(11) | 人均价格 |
| shopStaff.user_name | 是 | String(20) | 员工登陆账号 |
| shopStaff.password | 是 | String(32) | 员工登陆密码 |
| shopStaff.real_name | 是 | String(20) | 员工真实姓名 |
| shopStaff.mobile | 否 | String(20) | 联系电话 |
| shopStaff.email | 否 | String(50) | 邮箱 |
| shopStaff.ewm_img | 否 | String(180) | 二维码图片 |
| shopStaff.scene_id | 否 | Integer(11) | 二维码参数 |
| shopStaff.path | 否 | Integer(500) | 员工路径 |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "shopSub": {
      "pid": 0,
      "shop_id": 30,
      "lng": "116.397128",
      "lat": "39.916527",
      "sync_setting": 1,
      "shop_type": "1",
      "agent_id": 0,
      "is_pickup_shop": 2,
      "is_fx": 1,
      "created": 1453089284,
      "modified": 1453089284,
      "deleted": 1,
      "id": 310
    },
    "shopInfo": {
      "shop_sub_id": 310,
      "scene_id": 0,
      "lbs": 1,
      "province_id": "214",
      "city_id": "215",
      "district_id": "216",
      "circle_id": "217",
      "available_status": 1,
      "update_status": 0,
      "created": 1453089284,
      "modified": 1453089284,
      "deleted": 1,
      "name": "lljtest",
      "bg_img": "http://imgcache.vikduo.com/static/0844adbe52cb19d07c785ac6b0cf7dec.png",
      "avg_price": "180",
      "recommend": "recommend",
      "special": "special",
      "description": "description",
      "address": "detailAddress",
      "businesshour": "08:00-21:00",
      "phone": "13088827340",
      "url": "http://www.baidu.com",
      "wx_categories": "[{\"id\":\"1\",\"name\":\"\\u7f8e\\u98df\"},{\"id\":\"2\",\"name\":\"\\u6c5f\\u6d59\\u83dc\"},{\"id\":\"3\",\"name\":\"\\u4e0a\\u6d77\\u83dc\"}]",
      "shop_id": 30,
      "id": 290
    },
    "shopStaff": {
      "role_id": 437,
      "shop_sub_id": 310,
      "shop_id": 30,
      "scene_id": 0,
      "last_login": 0,
      "is_bind": 2,
      "is_cancel": 2,
      "is_super_cancel": 2,
      "is_default": 1,
      "is_scan_pay": 2,
      "is_scan_refund": 2,
      "shop_manager_id": 0,
      "agent_id": 0,
      "created": 1453089285,
      "modified": 1453089285,
      "deleted": 1,
      "scan_count": 0,
      "user_name": "1260106386",
      "password": "e10adc3949ba59abbe56e057f20f883e",
      "real_name": "llj",
      "agent_path": null,
      "id": 270
    }
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取店铺信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/shop/get-shopsub
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| shop_type | 否 | Integer(11) | 店铺类型 1直营店 2加盟店 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 192,
    "pid": 187,
    "shop_id": 30,
    "lng": 116.234275,
    "lat": 39.942327,
    "sync_setting": 1,
    "shop_type": 1,
    "agent_path": null,
    "agent_id": 0,
    "is_pickup_shop": 2,
    "is_fx": 1,
    "created": 1440406329,
    "modified": 1440419015,
    "deleted": 1,
    "shopSubSetting": {
      "id": 309,
      "shop_id": 30,
      "shop_sub_id": 192,
      "is_scan_pay": 1,
      "scan_count": 0
    },
    "shopInfo": {
      "id": 172,
      "shop_id": 30,
      "shop_sub_id": 192,
      "name": "122",
      "bg_img": "http://imgcache.vikduo.com/static/446eb23c7062bb203f21d5c6108cb76a.png",
      "description": "333",
      "theme": null,
      "category_del_id": null,
      "ewm_img": "http://imgcache.vikduo.com/static/57cbdb6c373f42659dfb7c9e1c501de7.jpg",
      "scene_id": 0,
      "site_img": "http://imgcache.vikduo.com/static/2d36c4a760add3e782ced63cab384114.jpg",
      "lbs": 1,
      "phone": "13232323232",
      "province_id": 1,
      "city_id": 2,
      "district_id": 3,
      "circle_id": 4,
      "address": "12",
      "businesshour": "09:00-12:00",
      "url": "http://www.shanghu.com/terminal/add",
      "wx_categories": "[{\"id\":98,\"name\":\"\u57fa\u7840\u8bbe\u65bd\"},{\"id\":99,\"name\":\"\u4ea4\u901a\u8bbe\u65bd\"},{\"id\":100,\"name\":\"\u4ea4\u901a\u670d\u52a1\u76f8\u5173\"}]",
      "available_status": 4,
      "recommend": null,
      "special": null,
      "avg_price": null,
      "poi_id": "402528528",
      "check_time": null,
      "fail_msg": "行政区划有误或坐标与地址不符",
      "update_status": 0,
      "created": 1440406329,
      "modified": 1452740565,
      "deleted": 1
    }
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
请求地址：/shop/add-shopsub-scan-count
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 店铺id |
| shop_id | 是 | Integer(11) | 商家id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 293,
    "shop_id": 30,
    "shop_sub_id": 292,
    "is_scan_pay": 1,
    "scan_count": 877
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __修改店铺信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/shop/update-shopsub
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shopSub.shop_id | 是 | Integer(11) | 商家id |
| shopSub.id | 是 | Integer(11) | 店铺id |
| shopSub.sync_setting | 否 | Integer(3) | 是否同步总店第三方的配置（1。是、2.否） |
| shopSub.lng | 否 | Double | 经度 |
| shopSub.lat | 否 | Double | 纬度 |
| shopSub.shop_type | 否 | Integer(3) | 总店才有操作权限：店铺类型(1:直营店,2:加盟店) |
| shopSub.is_pickup_shop | 否 | Integer(3)  |总店才有操作权限：是否启用到店自提(1：启用，2：禁用) |
| shopSub.agent_path | 否 | String(255) | 代理商路径 |
| shopInfo.name | 否 | String(20) | 店铺名称 |
| shopInfo.phone | 否 | String(20) | 手机号码 |
| shopInfo.province_id | 否 | Integer(11) | 店铺省id |
| shopInfo.city_id | 否 | Integer(11) | 店铺城市id |
| shopInfo.district_id | 否 | Integer(11) | 店铺区id |
| shopInfo.address | 否 | String(255) | 店铺详细地址 |
| shopInfo.circle_id | 否 | Integer(11) | 商圈id |
| shopInfo.businesshour | 否 | String(20) | 营业时间 |
| shopInfo.url | 否 | String(255) | 网站 |
| shopInfo.bg_img | 否 | String(255) | 店铺背景图 |
| shopInfo.description | 否 | String(255) | 店铺描述 |
| shopInfo.theme | 否 | String(20) | 店铺模板 |
| shopInfo.site_img | 否 | String(255) |  |
| shopInfo.lbs | 否 | Integer(3) | 是否开启店铺定位（1：开启，2：不开启） |
| shopInfo.ewm_img | 否 | String(255) | 店铺二维码 |
| shopInfo.scene_id | 否 | Integer(11) | 推广二维码参数id |
| shopInfo.category_del_id | 否 | String(255) | 删除的分类id |
| shopInfo.wx_categories | 否 | String(255) | 微信小店分类格式：{''id'':"name","id":"name"}|
| shopInfo.recomment | 否 | String(500) | 推荐内容 |
| shopInfo.special | 否 | String(500) | 特色服务 |
| shopStaff.avg_price | 否 | Integer(11) | 人均价格 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "shopSub": {
      "id": 310,
      "pid": 0,
      "shop_id": 30,
      "lng": "112.146818",
      "lat": "37.568119",
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
        "wx_categories": "[{\"id\":\"1\",\"name\":\"\u7f8e\u98df\"},{\"id\":\"2\",\"name\":\"\u6c5f\u6d59\u83dc\"},{\"id\":\"3\",\"name\":\"\u4e0a\u6d77\u83dc\"}]",
        "available_status": 1,
        "recommend": "recommend",
        "special": "special",
        "avg_price": 180,
        "poi_id": null,
        "check_time": null,
        "fail_msg": null,
        "update_status": 0,
        "created": 1453089284,
        "modified": 1453100058,
        "deleted": 1
      }
    },
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
      "wx_categories": "[{\"id\":\"1\",\"name\":\"\u7f8e\u98df\"},{\"id\":\"2\",\"name\":\"\u6c5f\u6d59\u83dc\"},{\"id\":\"3\",\"name\":\"\u4e0a\u6d77\u83dc\"}]",
      "available_status": 1,
      "recommend": "recommend",
      "special": "special",
      "avg_price": 180,
      "poi_id": null,
      "check_time": null,
      "fail_msg": null,
      "update_status": 0,
      "created": 1453089284,
      "modified": 1453100058,
      "deleted": 1
    }
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __更新店铺二维码__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/shop/update-shopsub-ewm
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| shop_id | 是 | Integer(11) | 商家id |
| ewm_img | 是 | String(255) | 店铺二维码 |
| scene_id | 是 | Integer(11) | 二维码参数 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
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
    "wx_categories": "[{\"id\":\"1\",\"name\":\"\u7f8e\u98df\"},{\"id\":\"2\",\"name\":\"\u6c5f\u6d59\u83dc\"},{\"id\":\"3\",\"name\":\"\u4e0a\u6d77\u83dc\"}]",
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
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __删除分店__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/shop/del-shopsub
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_sub_id | 是 | Integer(11) | 店铺id |
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



## __获取商家信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/shop/get-shop
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| qq | 否 | Varchar(30) | 商家qq号 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
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
    "modified": 1453085479,
    "deleted": 1,
    "after_sale_time_status": 1,
    "after_sale_handle_time": 6,
    "return_address": "广东省河源市龙川县老隆镇联丰村59栋59号",
    "return_consignee": "唐雄",
    "return_phone": "13632723451",
    "shopSetting": {
      "id": 293,
      "shop_id": 30,
      "is_scan_pay": 1,
      "scan_limit_amount": 1000
    }
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __修改商家信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/shop/update-shop
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| name | 否 | Varchar(50) | 商家名称 |
| category_f | 否 | Varchar(50) | 商品一级分类 |
| category_s | 否 | Varchar(50) | 商品二级分类 |
| tel | 否 | Varchar(50) | 联系电话 |
| website | 否 | Varchar(50) | 网址 |
| addr | 否 | Varchar(50) | 地址 |
| bg_img | 否 | Varchar(50) | 背景图 |
| logo | 否 | Varchar(50) | 商家logo |
| desc | 否 | Varchar(50) | 商家描述 |
| after_sale_time_status | 否 | Integer(11) | 售后订单处理时间限制 |
| after_sale_handle_time | 否 | Integer(11) | 售后订单处理时间 |
| return_address | 否 | Varchar(200) | 退货地址 |
| return_consignee | 否 | Varchar(50) | 退货联系人 |
| return_phone | 否 | Varchar(16) | 退货联系人电话 |
| auto_refund | 否 | Integer(11) | 是否自动退款1.是2.否 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
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
    "modified": 1453101479,
    "deleted": 1,
    "after_sale_time_status": 1,
    "after_sale_handle_time": 6,
    "return_address": "广东省河源市龙川县老隆镇联丰村59栋59号",
    "return_consignee": "唐雄",
    "return_phone": "13632723451"
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __查找距离指定地点最近的店铺__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/shop/find-nearest-shopsub-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| lat | 是 | Double | 纬度 |
| lng | 是 | Double | 经度 |
| count | 是 | Integer(11) | 店铺展示条数 最小1最大10 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "185.30": {
      "shop_sub_id": 240,
      "name": "权限点 是山水",
      "site_img": "http://imgcache.vikduo.com/static/f15eb5075726aca28240adb3d3bce481.png",
      "phone": "15602326941",
      "distance": "185.30"
    },
    "196.12": {
      "shop_sub_id": 274,
      "name": "test555555",
      "site_img": "http://imgcache.vikduo.com/static/dd12b134d8cdbb4ab988e71d82054493.jpg",
      "phone": "15555555555",
      "distance": "196.12"
    },
    "203.45": {
      "shop_sub_id": 276,
      "name": "sdfsdf",
      "site_img": "http://imgcache.vikduo.com/static/1fc27c763a8bb8eab7a8bd41a6ec76dd.png",
      "phone": "15823568956",
      "distance": "203.45"
    }
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
