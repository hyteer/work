# 日志管理
## __获取日志列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/operation-log/find-operation-log
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| user_id | 否 | Integer(11) | 操作员ID|
| user_name | 否 | String | 操作员姓名|
| user_type | 否 | Integer(1) | 操作员类型<br/>1 微信手机端用户<br/>2 终端店员工<br/>3 代理商员工<br/>4 商户管理员|
| type | 否 | String | 业务类型<br/>marketing_activity 活动（大转盘/砸金蛋）|
| record_id | 否 | Integer(11) | 记录ID|
| field_name | 否 | String | 字段名称|
| createStart | 否 | Integer(11) | 开始时间|
| createEnd | 否 | Integer(11) | 结束时间|
| page | 是 | Integer(11) | 分页值，第一页值为0 |
| count | 是 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": 77,
      "shop_id": 30,
      "user_id": 895,
      "user_name": "操作员姓名",
      "user_type": 4,
      "type": "marketing_activity",
      "record_id": 265,
      "field_name": "奖品数量",
      "value": "1",
      "format_value": "一等奖的数量改为1",
      "created": 1464921173
    },
    {
      "id": 75,
      "shop_id": 30,
      "user_id": 895,
      "user_name": "操作员姓名",
      "user_type": 4,
      "type": "marketing_activity",
      "record_id": 265,
      "field_name": "奖品数量",
      "value": "0",
      "format_value": "未中奖的数量改为0",
      "created": 1464921173
    }
  ],
  "page": {
    "per_page": 2,
    "total_count": 4,
    "current_page": 1,
    "total_page": 2
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

