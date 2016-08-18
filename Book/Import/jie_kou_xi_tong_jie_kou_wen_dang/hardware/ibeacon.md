## __修改ibeacon__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/ibeacon/update-client
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 门店id |
| comment | 否 | String(255） | 备注 |
| pages | 否 | array | 关联页面 |
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









## __获取ibeacon__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/ibeacon/get-client
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动的id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
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








## __查找ibeacon列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/ibeacon/find-client-list
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| deleted | 否 | Integer(11) | 状态1.是、2.否 |
| device_id | 否 | Integer(4) | 设备id |
| wx_device_id | 否 | Integer(2) | 卡券类型，1代金券 2优惠券，目前只有代金券 |
| uuid | 否 | String(255) | ibeacon设备uuid |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取2000个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| major | 否 | Integer(10) | ibeacon设备major |
| minor | 否 | Integer(10) | ibeacon设备minor |
| pin_code | 否 | String | 设备的唯一标识 |
| shop_name | 否 | String | 店铺名称 |
* **注意：sort排序可选字段['id']**

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













## __创建页面__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/ibeacon/create-page
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| title | 是 | String(6) | 标题 |
| page_url | 是 | String(255) | 跳转链接 |
| cdn_url | 否 | String(255) | 图片的cdn地址 |
| description | 是 | String(7) | 副标题 |
| comment | 是 | String(15) | 备注 |
| model | 否 | 回复model |
| model_id | 否 | 回复model_id |
| type | 否 | Integer(4) | 是不是默认页面 1是  2 不是 |
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












## __更新页面__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/ibeacon/update-page
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| title | 否 | String(6) | 标题 |
| page_url | 否 | String(255) | 跳转链接 |
| cdn_url | 否 | String(255) | 图片的cdn地址 |
| description | 否 | String(7) | 副标题 |
| comment | 否 | String(15) | 备注 |
| model | 否 | 回复model |
| model_id | 否 | 回复model_id |
| type | 否 | Integer(4) | 是不是默认页面 1是  2 不是 |
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













## __获取页面__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/ibeacon/get-page
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动的id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
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







## __查找页面列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/ibeacon/find-page-list
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| deleted | 否 | Integer(11) | 状态1.是、2.否 |
| page_id | 否 | Integer(11) | 微信返回的页面id |
| type | 否 | Integer(4) | 是不是默认页面 1是  2 不是 |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取2000个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| title | 否 | String(6) | 标题 |
| comment | 否 | String(15) | 备注 |
* **注意：sort排序可选字段['id']**

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











## __删除页面__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/ibeacon/del-page
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动的id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
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







## __获取统计__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/ibeacon/get-statistics
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 主键 |
| shop_id | 是 | Integer(11) | 商家id |
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







## __查找统计列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/ibeacon/find-statistics-list
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| device_id | 否 | Integer(11) | 设备号ID |
| ftime | 否 | Integer(11) | 当天0点对应的时间戳 |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取2000个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| pin_code | 否 | String | 设备的唯一标识 |
| shop_name | 否 | String | 店铺名称 |
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











## __查找总统计列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/ibeacon/find-main-statistic
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| device_id | 否 | Integer(11) | 设备号ID |
| ftime | 否 | Integer(11) | 当天0点对应的时间戳 |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取2000个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":[
        {
            "click_pv":10,
            "click_uv":4,
            "shake_pv":28,
            "shake_uv":14,
            "ftime":1432742400
        },
        {
            "click_pv":19,
            "click_uv":11,
            "shake_pv":25,
            "shake_uv":14,
            "ftime":1432828800
        },
        {
            "click_pv":699,
            "click_uv":61,
            "shake_pv":1825,
            "shake_uv":426,
            "ftime":1432915200
        },
        {
            "click_pv":4,
            "click_uv":2,
            "shake_pv":14,
            "shake_uv":4,
            "ftime":1433109600
        },
        {
            "click_pv":2,
            "click_uv":1,
            "shake_pv":3,
            "shake_uv":2,
            "ftime":1433865600
        },
        {
            "click_pv":164,
            "click_uv":84,
            "shake_pv":487,
            "shake_uv":133,
            "ftime":1434384000
        },
        {
            "click_pv":380,
            "click_uv":861,
            "shake_pv":497,
            "shake_uv":1381,
            "ftime":1434643200
        },
        {
            "click_pv":433,
            "click_uv":214,
            "shake_pv":1512,
            "shake_uv":369,
            "ftime":1434729600
        },
        {
            "click_pv":488,
            "click_uv":237,
            "shake_pv":1755,
            "shake_uv":393,
            "ftime":1434816000
        }
    ],
    "page":{
        "per_page":20,
        "total_count":9,
        "current_page":0,
        "total_page":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取总人数的统计__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/ibeacon/get-sum-shake-uv
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| device_id | 否 | Integer(11) | 设备id |
| shop_id | 是 | Integer(11) | 商家id |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":"2736"
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
