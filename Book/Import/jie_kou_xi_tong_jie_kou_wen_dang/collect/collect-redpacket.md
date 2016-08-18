## __新增众筹红包__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/create-collect-redpacket
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|collect_id|是|Integer(11)|众筹活动id|
| red_packet_id|是|Integer(11)|关联红包id|
| give|否|Integer(11)|赠送金额|
| number|是|Integer(11)|代领人数|
| count|是|Integer(11)|礼品总数|
| lastCount|是|Integer(11)|礼品剩余数|
| shop_id|是|Integer(11)|商家id|
| shop_sub_id|否|Integer(11)|店铺id|
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "give": "0",
        "collect_id": "10",
        "red_packet_id": "3",
        "number": "1",
        "count": "1",
        "lastCount": "1",
        "shop_id": "5",
        "shop_sub_id": "43",
        "id": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __修改众筹红包__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/update-collect-redpacket
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|id|是|Integer(11)|众筹关联红包id|
|collect_id|是|Integer(11)|众筹活动id|
| red_packet_id|是|Integer(11)|关联红包id|
| give|是|Integer(11)|赠送金额|
| number|是|Integer(11)|代领人数|
| count|是|Integer(11)|礼品总数|
| lastCount|是|Integer(11)|礼品剩余数|
| shop_id|是|Integer(11)|商家id|
| shop_sub_id|是|Integer(11)|店铺id|
| shop_sub_id|是|Integer(11)|店铺id|
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 1,
        "collect_id": "10",
        "red_packet_id": "3",
        "give": "0",
        "number": "2",
        "count": "1",
        "lastCount": "1",
        "shop_id": "5",
        "shop_sub_id": "43"
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __删除众筹关联红包__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/del-collect-redpacket
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 关联产品id |
| collect_id | 是 | Integer(11) | 众筹id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |

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
