## 获取成长值设置
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/get-member-growth-setting
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": "3",
      "shop_id": "30",
      "is_cost_growth": "1",
      "cost_amount": "669900",
      "cost_growth": "2",
      "is_comment_growth": "2",
      "comment_growth": "1",
      "is_login_growth": "2",
      "login_growth": "1",
      "is_point_growth": "2",
      "get_point": "1",
      "get_point_growth": "1",
      "point_max_growth": "1",
      "is_month_cost_growth": "2",
      "is_month_cost_total_growth": "2",
      "month_cost_total_count": "1",
      "month_cost_total_growth": "1",
      "created": "1462785294",
      "modified": "1463130167",
      "deleted": "1"
    }
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## 修改成长值设置
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/get-member-growth-setting
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| is_cost_growth | 否 | Integer(11) | 是否开启消费获得成长值 ）1：开启，2：不开启 |
| cost_amount | 否 | Integer(11) | 消费支付金额 |
| cost_growth | 否 | Integer(11) | 消费支付金额获得的成长值 |
| is_comment_growth | 否 | Integer(11) | 是否开启评价订单获得成长值）1：开启，2：不开启 |
| comment_growth | 否 | Integer(11) | 评价订单获得的成长值 |
| is_login_growth | 否 | Integer(11) | 是否开启登陆获得成长值）1：开启，2：不开启 |
| login_growth | 否 | Integer(11) | 登陆获得的成长值 |
| is_point_growth | 否 | Integer(11) | 是否开启获取积分得到成长值）1：开启，2：不开启 |
| get_point | 否 | Integer(11) | 获取积分数 |
| get_point_growth | 否 | Integer(11) | 积分数对应成长值 |
| point_max_growth | 否 | Integer(11) | 通过积分获取成长值上限 |
| is_month_cost_total_growth | 否 | Integer(11) | 是否开启月购买得到成长值）1：开启，2：不开启 |
| month_cost_total_count | 否 | Integer(11) | 月消费次数 |
| month_cost_total_growth | 否 | Integer(11) | 月消费次数获得的成长值 |
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": "3",
      "shop_id": "30",
      "is_cost_growth": "1",
      "cost_amount": "669900",
      "cost_growth": "2",
      "is_comment_growth": "2",
      "comment_growth": "1",
      "is_login_growth": "2",
      "login_growth": "1",
      "is_point_growth": "2",
      "get_point": "1",
      "get_point_growth": "1",
      "point_max_growth": "1",
      "is_month_cost_growth": "2",
      "is_month_cost_total_growth": "2",
      "month_cost_total_count": "1",
      "month_cost_total_growth": "1",
      "created": "1462785294",
      "modified": "1463130167",
      "deleted": "1"
    }
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
