## __pos机列表统计__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/statistics/pos-client-count
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| shop_sub_id|否|Integer(11)|分店id|
| token|否|Integer(11)|员工id|
| pin_code|否|String|分店id|
| deleted|否|Integer(11)|状态(1.启用、2.禁用)|
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
    "data": 2
}
```
<br  />
