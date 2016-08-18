# 会员投放

## 修改会员卡投放信息
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/update-member-card-share-message
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| id | 是 | Integer(11) | 分享内容ID |
| title | 是 | String(11) | 标题 |
| desc | 是 | String(11) | 消费支付金额获得的成长值 |
| pic_id | 否 | Integer(11) | 图片ID |
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": "206483",
      "title": "会员卡投放图文标题",
      "desc": "会员卡投放图文描述，例如免费领取会员卡，开卡激活立即享受会员权益",
      "pic_id": "500001",
      "shop_id": "32",
      "shop_sub_id": "0",
      "created": "1464576343",
      "modified": "1464600599",
      "deleted": "1"
    }
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

