# 硬件

## __pos设置详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/pos/get-pos-client
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|pos设置id|
| shop_id|是|Integer(11)|商铺id|
| shop_sub_id|否|Integer(11)|分店id|
| token|否|Integer(11)|员工id|
| pin_code|否|Integer(11)|分店id|
| deleted|否|Integer(11)|状态(1.启用、2.禁用)|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 1,
        "pos_machine_id": 1,
        "description": "dsfsdf",
        "pin_code": "1111111",
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": 1440829190,
        "modified": 1440829190,
        "deleted": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __广告位列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/pos/find-ad-site
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| code|否|Integer(11)|广告标示|
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
      "id": 2,
      "name": "pos机广告位",
      "code": "A-1",
      "created": 1440582176,
      "modified": 1440582176
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



## __新增广告活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/pos/create-ad-activity
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| ad_site_id|是|Integer(11)|广告位置id|
| shop_id|是|Integer(11)|商户id|
| shop_sub_id|否|Integer(11)|门店id|
| avtivity_name|是|String(50)|广告位置id|
| range_type|是|Integer(11)|范围 1所有终端店 2指定终端店|
| played|是|Integer(11)|模式 1顺序 2随机|
| begin_time|是|Integer(11)|开始时间|
| end_time|是|Integer(11)|结束时间|
| ad_ranges|否|Array|指定的终端店集合|
| ad_ranges.shop_sub_id|是|Integer(11)|指定的终端店id|


<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "adActivity": {
      "shop_id": 30,
      "deleted": 2,
      "ad_site_id": 2,
      "avtivity_name": "biu",
      "range_type": 1,
      "played": 1,
      "begin_time": 1453274801,
      "end_time": 1453447603,
      "created": 1453274986,
      "modified": 1453274986,
      "id": 52
    },
    "adRange": []
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __修改广告活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/pos/update-ad-activity
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|活动id|
| ad_site_id|是|Integer(11)|广告位置id|
| shop_id|是|Integer(11)|商户id|
| shop_sub_id|否|Integer(11)|门店id|
| avtivity_name|是|String(50)|广告位置id|
| range_type|是|Integer(11)|范围 1所有终端店 2指定终端店|
| played|是|Integer(11)|模式 1顺序 2随机|
| begin_time|是|Integer(11)|开始时间|
| end_time|是|Integer(11)|结束时间|
| ad_ranges|否|Array|指定的终端店集合|
| ad_ranges.shop_sub_id|是|Integer(11)|指定的终端店id|
| ad_ranges.id|是|Integer(11)|ad_range的id(新增的给0)|


<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "adActivity": {
      "id": 52,
      "ad_site_id": 2,
      "shop_id": 30,
      "avtivity_name": "biu",
      "range_type": 1,
      "played": 1,
      "begin_time": 1453274801,
      "end_time": 1453447603,
      "deleted": 2,
      "created": 1453274986,
      "modified": 1453277000
    },
    "adRange": []
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __删除广告活动范围__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/pos/del-ad-range
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|广告范围id|
| shop_id|是|Integer(11)|商户id|
| ad_activity_id|是|String(50)|广告活动id|


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



## __启用广告活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/pos/enable-ad-activity
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|广告范围id|
| shop_id|是|Integer(11)|商户id|
| shop_sub_id|否|Integer(11)|店铺id|
| staff_id|否|Integer(11)|操作员工id|


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




## __禁用广告活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/pos/disable-ad-activity
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|广告范围id|
| shop_id|是|Integer(11)|商户id|
| shop_sub_id|否|Integer(11)|店铺id|
| staff_id|否|Integer(11)|操作员工id|


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

## __删除广告活动__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/pos/del-ad-activity
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|广告范围id|
| shop_id|是|Integer(11)|商户id|
| shop_sub_id|否|Integer(11)|店铺id|
| staff_id|否|Integer(11)|操作员工id|


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



## __广告活动列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/pos/find-ad-activity
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| shop_sub_id|否|Integer(11)|分店id|
| ad_site_id|否|Integer(11)|广告位id|
| range_type|否|Integer(11)|范围 1所有终端店 2指定终端店|
| played|否|Integer(11)|模式 1顺序 2随机|
| begin_time|否|Integer(11)|开始时间|
| end_time|否|Integer(11)|结束时间|
| avtivity_name|否|String(50)|活动名称|
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
          "id": 3,
          "name": "广告位2",
          "code": "B-1",
          "created": 1440516233,
          "modified": 1440516233
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


## __广告活动详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/pos/get-ad-activity
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|活动id|
| shop_id|是|Integer(11)|商铺id|
| ad_site_id|否|Integer(11)|广告位id|
| range_type|否|Integer(11)|范围 1所有终端店 2指定终端店|
| played|否|Integer(11)|模式 1顺序 2随机|
| begin_time|否|Integer(11)|开始时间|
| end_time|否|Integer(11)|结束时间|
| avtivity_name|否|String(50)|活动名称|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 36,
    "ad_site_id": 3,
    "shop_id": 30,
    "avtivity_name": "1106860838",
    "range_type": 2,
    "played": 2,
    "begin_time": 1441961733,
    "end_time": 1442652935,
    "deleted": 1,
    "created": 1441961747,
    "modified": 1448245987,
    "adRanges": [
      {
        "id": 128,
        "ad_activity_id": 36,
        "shop_id": 30,
        "shop_sub_id": 192,
        "created": 1441964949,
        "modified": 1441964949,
        "shopSub": {
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
    ],
    "adSite": {
      "id": 3,
      "name": "广告位2",
      "code": "B-1",
      "created": 1440516233,
      "modified": 1440516233
    }
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __创建广告内容__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/pos/create-ad-content
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| shop_sub_id|否|Integer(11)|分店id|
| ad_activity_id|是|Integer(11)|广告活动id|
| type|是|Integer(11)|广告类型 1文本 2图片|
| content|是|Integer(11)|广告内容|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "type": 1,
    "show_count": 0,
    "shop_sub_id": 0,
    "deleted": 1,
    "ad_activity_id": 36,
    "shop_id": 30,
    "content": "content",
    "created": 1453950096,
    "modified": 1453950096,
    "id": 71
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __修改广告内容__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/pos/update-ad-content
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|广告内容id|
| shop_id|是|Integer(11)|商铺id|
| shop_sub_id|否|Integer(11)|分店id|
| ad_activity_id|是|Integer(11)|广告活动id|
| type|是|Integer(11)|广告类型 1文本 2图片|
| content|是|Integer(11)|广告内容|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 71,
    "ad_activity_id": 36,
    "type": 1,
    "content": "content",
    "shop_id": 30,
    "shop_sub_id": 0,
    "show_count": 0,
    "deleted": 1,
    "created": 1453950096,
    "modified": 1453950787
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __广告内容列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/pos/find-ad-content
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| ad_activity_id|否|Integer(11)|活动id|
| type|否|Integer(11)|广告类型 1文本 2图片|
| deleted|否|Integer(11)|状态1.启用、2.禁用|
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
      "id": 24,
      "ad_activity_id": 36,
      "type": 1,
      "content": "121",
      "shop_id": 30,
      "shop_sub_id": 0,
      "show_count": 0,
      "deleted": 1,
      "created": 1444873608,
      "modified": 1447740260
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

## __启用内容列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/pos/enable-ad-content
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|广告范围id|
| shop_id|是|Integer(11)|商户id|
| shop_sub_id|否|Integer(11)|店铺id|
| staff_id|否|Integer(11)|操作员工id|

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

## __禁用广告内容__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/pos/disable-ad-content
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| id|是|Integer(11)|广告范围id|
| shop_id|是|Integer(11)|商户id|
| shop_sub_id|否|Integer(11)|店铺id|
| staff_id|否|Integer(11)|操作员工id|

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

## __删除广告内容__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/pos/del-ad-content
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| id|是|Integer(11)|广告范围id|
| shop_id|是|Integer(11)|商户id|
| shop_sub_id|否|Integer(11)|店铺id|
| staff_id|否|Integer(11)|操作员工id|

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

## __选择活动的店铺列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/pos/choose-shop-sub
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商家id|
| name|否|String(11)|店铺名称|
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
      "id": 187,
      "pid": 0,
      "shop_id": 30,
      "lng": 0,
      "lat": 0,
      "sync_setting": 1,
      "shop_type": 1,
      "agent_path": null,
      "agent_id": 0,
      "is_pickup_shop": 2,
      "is_fx": 2,
      "created": 1440394985,
      "modified": 1440394985,
      "deleted": 1,
      "shopInfo": {
        "id": 167,
        "shop_id": 30,
        "shop_sub_id": 187,
        "name": "pp",
        "bg_img": "http://imgcache.vikduo.com/static/ef356219b4d5d567e13dd984c7132666.jpg",
        "description": "pp",
        "theme": null,
        "category_del_id": null,
        "ewm_img": null,
        "scene_id": 0,
        "site_img": null,
        "lbs": 1,
        "phone": "18577777777",
        "province_id": 1,
        "city_id": 2,
        "district_id": 7,
        "circle_id": 8,
        "address": "pp",
        "businesshour": "8:00-19:00",
        "url": "http://www.bbs.com",
        "wx_categories": null,
        "available_status": 1,
        "recommend": null,
        "special": null,
        "avg_price": null,
        "poi_id": "",
        "check_time": null,
        "fail_msg": null,
        "update_status": 0,
        "created": 1440394985,
        "modified": 1446707283,
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

## __员工广告统计__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/pos/staff-ad-count
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商家id|
| shop_sub_id|否|Integer(11)|店铺id|
| createStart | 否 | Integer(11) |查询日期：开始时间 |
| createEnd | 否 | Integer(11) | 查询日期：结束时间 |
| ad_content_id|是|Integer(11)|广告内容id|
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
  "data": [],
  "page": {
    "per_page": 20,
    "total_count": 0,
    "current_page": 0,
    "total_page": 0
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __修改POS机__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/pos/update-pos-client
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|POS id|
| shop_id|是|Integer(11)|商家id|
| shop_sub_id|否|Integer(11)|店铺id|
| description | 否 | String(255) |描述 |
* **注意：sort排序可选字段['id']**

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 1,
    "device_id": 2,
    "description": "pos测试",
    "pin_code": "00012015051300603000015772233392",
    "shop_id": 30,
    "shop_sub_id": 0,
    "created": 1440595697,
    "modified": 1453951941,
    "deleted": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
