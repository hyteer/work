## __订单统计__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/statistics/order-statistics
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|shop_id|是|Integer(11)|商家id|
|search_type|否|Integer(2)|统计类型：1按门店统计，2按员工统计,3按代理商统计|
|shop_sub_id|否|Integer(11)|店铺id|
|staff_id|否|Integer(11)|员工id|
|agent_ids|否|Array|代理商id数组|
|shop_count_type|否|Integer(11)|统计店铺类型，1所有，2直营店，默认不传为2|
|createStart|否|Integer(11)|搜索起始时间|
|createEnd|否|Integer(11)|搜索结束时间|
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
**注：若统计代理商、加盟店必须传入shop_count_type为1；**
<br  />
**search_type不传则统计整个商家订单**

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": "198",
      "name": "这里有个直营店",
      "num": "33",
      "not_belong_num": "6",
      "unpaySum": "219550",
      "codSum": "4000",
      "onlineSum": null,
      "posSum": null
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

## __订单总计__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/statistics/order-count
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|shop_id|是|Integer(11)|商家id|
|search_type|否|Integer(2)|统计类型：1按门店统计，2按员工统计，3按代理商统计|
|shop_sub_id|否|Integer(11)|店铺id|
|staff_id|否|Integer(11)|员工id|
|agent_ids|否|Array|代理商id数组|
|shop_count_type|否|Integer(11)|统计店铺类型，1所有，2直营店，默认不传为2|
|order_type|否|Array|订单类型（1.普通订单、2.秒杀、3.预售、4.pos收银、5.pos订单、6.拍码打折、7.扫码订单、8.拼团订单）|
|createStart|否|Integer(11)|搜索起始时间|
|createEnd|否|Integer(11)|搜索结束时间|
**注：若统计代理商、加盟店必须传入shop_count_type为1；**
<br  />
**search_type不传则统计整个商家订单**
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "num": "20",
    "sum": "108200",
    "completedNum": "10",
    "completedSum": "88200"
  }
}
```
**注：completedNum为已完成订单数，completedSum为已完成订单总额**
<br />
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __订单明细统计列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/statistics/order-list-by-agent
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|shop_id|是|Integer(11)|商家id|
|agent_ids|是|Array|代理商id数组集合|
|shop_sub_id|否|Integer(11)|店铺id|
|staff_id|否|Integer(11)|员工id|
|createStart|否|Integer(11)|搜索起始时间|
|createEnd|否|Integer(11)|搜索结束时间|
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
    "data": {

    },
    "page": {
        "per_page": 20,
        "total_count": 3,
        "current_page": 0,
        "total_page": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __app端统计员工订单__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/statistics/statistics-staff-order-for-app
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|shop_id|是|Integer(11)|商家id|
|staff_id|是|Integer(11)|员工id|
|createStart|是|Integer(11)|搜索起始时间|
|createEnd|是|Integer(11)|搜索结束时间|
|type|是|Integer(11)|统计类型：1按日统计 2按月统计|
|order_type|否|Array|订单类型（1.普通订单、2.秒杀、3.预售、4.pos收银、5.pos订单、6.拍码打折、7.扫码订单、8.拼团订单）|
**注：<br />按日统计，统计时间段为createStart当天0点到createEnd当天23:59:59。<br />
按月统计，统计时间段为createStart当月第一天0点到createEnd当月最后一天23:59:59**
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
<br />
**注：num为订单总数；sum为订单总额（单位分）**
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "2016-05-10": {
      "num": 1,
      "sum": 100
    },
    "2016-05-11": {
      "num": 1,
      "sum": 100
    },
    "2016-05-12": {
      "num": 0,
      "sum": 0
    }
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
