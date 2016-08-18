## __获取wifi列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wifi/find-wifi-client
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| shop_name | 否 | String(50) | 店铺名称 |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取2000个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
* **注意：sort排序可选字段['id']**

##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": 10002,
      "device_id": 5,
      "pin_code": "1205032015091010000400000143",
      "mac_addr": "0001E16520B278",
      "brand_name": "test",
      "ssid": "测试wifi",
      "qrcode_addr": "http://p.qpic.cn/ecc_merchant/0/fc1954e46624e2a3_1441868491169/0",
      "action_code": "A0002",
      "ad_page_url": "http://new.cc/slltwg1/Activity/couponList",
      "portal_page_url": "http://imgcache.vikduo.com/static/e0cc32f8ddcfae0edddfa3f6d9ebbe0c.jpg",
      "comment": "备注一下",
      "model": null,
      "model_id": 0,
      "factory": 1,
      "shop_id": 30,
      "shop_sub_id": 198,
      "created": 1441855125,
      "modified": 1441869824,
      "deleted": 1,
      "shopInfo": {
        "id": 178,
        "shop_id": 30,
        "shop_sub_id": 198,
        "name": "这里有个直营店",
        "bg_img": "http://imgcache.vikduo.com/static/446eb23c7062bb203f21d5c6108cb76a.png",
        "description": "http://www.shanghu.com/terminal/add",
        "theme": null,
        "category_del_id": null,
        "ewm_img": "https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=gQG%2F8ToAAAAAAAAAASxodHRwOi8vd2VpeGluLnFxLmNvbS9xL29Vem1aTS1sTG05WE1TNy1WR0NVAAIEzbiHVAMEAAAAAA%3D%3D",
        "scene_id": 0,
        "site_img": "http://imgcache.vikduo.com/static/2d36c4a760add3e782ced63cab384114.jpg",
        "lbs": 1,
        "phone": "13252535335",
        "province_id": 1,
        "city_id": 2,
        "district_id": 3,
        "circle_id": 4,
        "address": "比克科技大厦9楼aaaaaa",
        "businesshour": "10:00-12:00",
        "url": "http://www.shanghu.com/terminal/add",
        "wx_categories": "[{\"id\":98,\"name\":\"\u57fa\u7840\u8bbe\u65bd\"},{\"id\":99,\"name\":\"\u4ea4\u901a\u8bbe\u65bd\"},{\"id\":100,\"name\":\"\u4ea4\u901a\u670d\u52a1\u76f8\u5173\"}]",
        "available_status": 0,
        "poi_id": null,
        "created": 1440420477,
        "modified": 1441764436,
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
错误时接口平台会返回错误码等信息，请参照：[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取wifi详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wifi/get-wifi-client
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 设备id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |

##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 10002,
    "device_id": 5,
    "pin_code": "1205032015091010000400000143",
    "mac_addr": "0001E16520B278",
    "brand_name": "test",
    "ssid": "测试wifi",
    "qrcode_addr": "http://p.qpic.cn/ecc_merchant/0/fc1954e46624e2a3_1441868491169/0",
    "action_code": "A0002",
    "ad_page_url": "http://new.cc/slltwg1/Activity/couponList",
    "portal_page_url": "http://imgcache.vikduo.com/static/e0cc32f8ddcfae0edddfa3f6d9ebbe0c.jpg",
    "comment": "备注一下",
    "model": null,
    "model_id": 0,
    "factory": 1,
    "shop_id": 30,
    "shop_sub_id": 198,
    "created": 1441855125,
    "modified": 1441869824,
    "deleted": 1,
    "shopInfo": {
      "id": 178,
      "shop_id": 30,
      "shop_sub_id": 198,
      "name": "这里有个直营店",
      "bg_img": "http://imgcache.vikduo.com/static/446eb23c7062bb203f21d5c6108cb76a.png",
      "description": "http://www.shanghu.com/terminal/add",
      "theme": null,
      "category_del_id": null,
      "ewm_img": "https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=gQG%2F8ToAAAAAAAAAASxodHRwOi8vd2VpeGluLnFxLmNvbS9xL29Vem1aTS1sTG05WE1TNy1WR0NVAAIEzbiHVAMEAAAAAA%3D%3D",
      "scene_id": 0,
      "site_img": "http://imgcache.vikduo.com/static/2d36c4a760add3e782ced63cab384114.jpg",
      "lbs": 1,
      "phone": "13252535335",
      "province_id": 1,
      "city_id": 2,
      "district_id": 3,
      "circle_id": 4,
      "address": "比克科技大厦9楼aaaaaa",
      "businesshour": "10:00-12:00",
      "url": "http://www.shanghu.com/terminal/add",
      "wx_categories": "[{\"id\":98,\"name\":\"\u57fa\u7840\u8bbe\u65bd\"},{\"id\":99,\"name\":\"\u4ea4\u901a\u8bbe\u65bd\"},{\"id\":100,\"name\":\"\u4ea4\u901a\u670d\u52a1\u76f8\u5173\"}]",
      "available_status": 0,
      "poi_id": null,
      "created": 1440420477,
      "modified": 1441764436,
      "deleted": 1
    },
    "device": {
      "id": 5,
      "to_shop_id": 30,
      "device_type": 3,
      "pin_code": "1205032015091010000400000143",
      "device_code": "0001E16520B278",
      "device_params": null,
      "status": 2
    }
  }
}
```
错误时接口平台会返回错误码等信息，请参照：[全局返回码说明](/error-code.html)
<br  /><br  />

## __修改wifi信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wifi/update-wifi-client
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 设备id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| comment | 否 | String(255) | 备注信息 |
| model | 否 | Integer(11) | 回复类型 |
| model_id | 否 | String(50) | 回复类型id |
| ssid | 是 | String(30) | ssid |
| brand_name | 是 | String(8) | 商家品牌名称 |
| action_code | 是 | String(8) | 动作名称 |
| ad_page_url | 是 | String(255) | 广告页面链接 |
| portal_page_url | 是 | String(255) | 拦截页面链接 |
| appid | 是 | String(50) | 商家appid |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 10002,
    "device_id": 5,
    "pin_code": "1205032015091010000400000143",
    "mac_addr": "0001E16520B278",
    "brand_name": "test",
    "ssid": "测试wifi",
    "qrcode_addr": "http://p.qpic.cn/ecc_merchant/0/f9f8e59a66ea00d7_1441866880426/0",
    "action_code": "A0012",
    "ad_page_url": "/second-kill/list?id=508",
    "portal_page_url": "http://imgcache.vikduo.com/static/51ed771cb303bc7acd395f20bab74b9c.jpg",
    "comment": "备注一下",
    "model": null,
    "model_id": 0,
    "factory": 1,
    "shop_id": 30,
    "shop_sub_id": 198,
    "created": 1441855125,
    "modified": 1442197126,
    "deleted": 1,
    "device": {
      "id": 5,
      "to_shop_id": 30,
      "device_type": 3,
      "pin_code": "1205032015091010000400000143",
      "device_code": "0001E16520B278",
      "device_params": null,
      "status": 2
    }
  }
}
```
错误时接口平台会返回错误码等信息，请参照：[全局返回码说明](/error-code.html)
<br  /><br  />
