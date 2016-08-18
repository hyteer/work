# 会员统计

## __粉丝统计总数(门店/员工/代理商/推广员)__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/statistics/count-wx-user
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| shop_count_type|否|Integer(4)|1为统计全部的，2为只统计直营店的,默认是2|
| shop_sub_id|否|Integer(11)|分店id|
| staff_id|否|Integer(11)|员工id (为0时查询未归属员工粉丝)|
| agent_ids|否|Array|代理商id数组|
| mid|否|Integer(11)|分销员id|
| start|否|Integer(11)|注册开始时间，包括当前值|
| end|否|Integer(11)|注册截止时间，包括当前值|
| is_subscribe|否|Integer(4)|是否关注1.是、2否|
| kind|是|Integer(4)|1为统计门店粉丝，2为统计员工粉丝，3为统计代理商，4为统计推广员|
**注：shop_sub_id有参数传入时，shop_count_type务必传入1**
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


## __按组进行粉丝统计(门店/员工/代理商/推广员)__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/statistics/group-count-wx-user
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| shop_count_type|否|Integer(4)|1为统计全部的，2为只统计直营店的,默认是2|
| shop_sub_id|否|Integer(11)|分店id|
| staff_id|否|Integer(11)|员工id|
| agent_ids|否|Array|代理商id数组|
| mid|否|Integer(11)|分销员id|
| group|是|Integer(4)|1为按终端店，2为按员工，3为按代理商，4为按推广员|
| start|否|Integer(11)|注册开始时间，包括当前值|
| end|否|Integer(11)|注册截止时间，包括当前值|
| is_subscribe|否|Integer(4)|是否关注1.是、2否|
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": [
      {
        "num":2,
        "id":31
      }
    ]
}
```
<br  />

## __获取会员明细统计__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/find-list-with-others
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| agent_id | 否 | Array | 代理商id数组 |
| createStart | 否 | Integer(11) | 创建开始时间（包括自己） |
| createEnd | 否 | Integer(11) | 创建截止时间（包括自己） |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
<br  /><br  />
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
