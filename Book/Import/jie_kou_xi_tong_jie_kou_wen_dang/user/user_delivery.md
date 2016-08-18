## __创建用户收货地址__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/user-delivery/create-user-delivery
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 是 | Integer(11) | 商铺id |
| consignee | 是 | String(20) | 收货人姓名 |
| tel | 是 | String(20) | 联系电话 |
| zip | 否 | String(10) | 邮编 |
| province_id | 否 | Integer(11) | 省id |
| province | 是 | String(20) | 省名称 |
| city_id | 否 | Integer(11) | 市、县id |
| city | 是 | String(20) | 市、县名称 |
| county_id | 否 | Integer(11) | 区id |
| county | 是 | String(20) | 区名称 |
| detail | 是 | String(200) | 地址详细 |
| uid | 是 | Integer(11) | 用户id |
| check_flag | 否 | Boolean | 是否检测重复 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "consignee": "收货人",
        "tel": "15823568956",
        "zip": "235689",
        "province_id": "0",
        "province": "广东省",
        "city_id": "0",
        "city": "深圳市",
        "county_id": "0",
        "county": "南山区",
        "detail": "比克大厦",
        "shop_id": "5",
        "shop_sub_id": "43",
        "uid": "141",
        "created": 1436149381,
        "modified": 1436149381,
        "deleted": 1,
        "id": 4
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __修改用户收货地址__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/user-delivery/update-user-delivery
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 是 | Integer(11) | 商铺id |
| consignee | 是 | String(20) | 收货人姓名 |
| tel | 是 | String(20) | 联系电话 |
| zip | 否 | String(10) | 邮编 |
| province_id | 否 | Integer(11) | 省id |
| province | 是 | String(20) | 省名称 |
| city_id | 否 | Integer(11) | 市、县id |
| city | 是 | String(20) | 市、县名称 |
| county_id | 否 | Integer(11) | 区id |
| county | 是 | String(20) | 区名称 |
| detail | 是 | String(200) | 地址详细 |
| uid | 是 | Integer(11) | 用户id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "consignee": "收货人",
        "tel": "15823568956",
        "zip": "235689",
        "province_id": "0",
        "province": "广东省",
        "city_id": "0",
        "city": "深圳市",
        "county_id": "0",
        "county": "南山区",
        "detail": "比克大厦",
        "shop_id": "5",
        "shop_sub_id": "43",
        "uid": "141",
        "created": 1436149381,
        "modified": 1436149381,
        "deleted": 1,
        "id": 4
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __修改用户收货地址__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/user-delivery/update-user-delivery
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 收货地址id |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 是 | Integer(11) | 商铺id |
| consignee | 是 | String(20) | 收货人姓名 |
| tel | 是 | String(20) | 联系电话 |
| zip | 否 | String(10) | 邮编 |
| province_id | 否 | Integer(11) | 省id |
| province | 是 | String(20) | 省名称 |
| city_id | 否 | Integer(11) | 市、县id |
| city | 是 | String(20) | 市、县名称 |
| county_id | 否 | Integer(11) | 区id |
| county | 是 | String(20) | 区名称 |
| detail | 是 | String(200) | 地址详细 |
| uid | 是 | Integer(11) | 用户id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "consignee": "收货人",
        "tel": "15823568956",
        "zip": "235689",
        "province_id": "0",
        "province": "广东省",
        "city_id": "0",
        "city": "深圳市",
        "county_id": "0",
        "county": "南山区",
        "detail": "比克大厦",
        "shop_id": "5",
        "shop_sub_id": "43",
        "uid": "141",
        "created": 1436149381,
        "modified": 1436149381,
        "deleted": 1,
        "id": 4
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取用户收货地址列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/user-delivery/find-user-delivery
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 是 | Integer(11) | 商铺id |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| uid | 是 | Integer(11) | 用户id |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
* **注意：sort排序可选字段['id']**
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
            "consignee": "test",
            "tel": "1380000",
            "zip": "518000",
            "province_id": 1,
            "province": " 广东",
            "city_id": 2,
            "city": "深圳",
            "county_id": 3,
            "county": "南山",
            "detail": "test",
            "shop_id": 5,
            "shop_sub_id": 43,
            "uid": 2,
            "created": null,
            "modified": null,
            "deleted": 1
        },...
    ],
    "page": {
        "per_page": 20,
        "total_count": 4,
        "current_page": 0,
        "total_page": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取用户收货地址详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/user-delivery/get-user-delivery
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| id | 是 | Integer(11) | 收货地址id |
| uid | 是 | Integer(11) | 用户id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 2,
        "consignee": "收货人",
        "tel": "15823568956",
        "zip": "235689",
        "province_id": 0,
        "province": "广东省",
        "city_id": 0,
        "city": "深圳市",
        "county_id": 0,
        "county": "南山区",
        "detail": "比克大厦",
        "shop_id": 5,
        "shop_sub_id": 43,
        "uid": 141,
        "created": 1436149143,
        "modified": 1436149143,
        "deleted": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __删除用户收货地址详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/user-delivery/del-user-delivery
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| id | 是 | Integer(11) | 收货地址id |
| uid | 是 | Integer(11) | 用户id |
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
