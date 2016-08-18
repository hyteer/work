
## __门店统计总数__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/statistics/count-shop-sub
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| shop_type|否|Integer(4)|1为直营店，2为加盟店|
| agent_id|否|Integer(11)|所属代理商id|
| sub_kind|否|Integer(4)|1为直接代理商门店数，2为代理商门店数（包括其代理商下的代理商的），当设置了agent_id值时此值才有效，默认是1|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": 2
}
```
<br  />

## __代理商直属门店统计总数__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/statistics/count-sub-agent-shop-sub
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| agent_id|否|array|所属代理商id|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "26": 0
    }
}
```
<br  />

## __代理商直属门店统计总数__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/statistics/count-sub-agent
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| pid|否|array|所属代理商id|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "26": "1",
        "27": "1"
    }
}
```
<br  />
