# 会员卡投放统计

## 获取会员卡激活数据
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/find-member-data-card
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| time_start | 是 | Integer(11) | 开始时间 |
| time_end | 是 | Integer(11) | 结束时间 |
| sorStr | 否 | Integer(11) | 排序 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "item": [
          {
            "id": "836",
            "shop_id": "30",
            "date": "1462809600",
            "access_count": "8",
            "activate_count": "4",
            "created": "1463552708",
            "modified": "1463552708"
          }
        ]
    }
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
