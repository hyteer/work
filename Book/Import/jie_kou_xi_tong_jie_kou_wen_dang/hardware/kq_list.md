## __添加卡券__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/create
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| title | 是 | String(50） | 卡券标题 |
| card_type | 是 | Integer(4) | 1:微商户 2：微信 |
| quantity | 是 | Integer(11) | 生成数量(上限100000000) |
| logo_url | 是 | String(100) | 卡券头像 |
| color | 是 | String(50） |  十六进制颜色码 |
| card_money | 是 | Integer(11) | 卡券面额 |
| money_limit | 是 | Integer(11) | 卡券使用限额 |
| get_limit | 是 | Integer(11) | 每人领取数量限制 |
| notice | 是 | String(100) | 卡券使用提醒(上限16个汉字) |
| description | 是 | String | 使用须知(上限1024个汉字) |
| service_phone | 是 | String(50) | 客服电话 |
| wx_card_id | 否 | String(100) | 微信卡券ID |
| wx_card_type | 否 | Integer(2) | 卡券类型，1代金券 2优惠券，目前只有代金券 |
| get_card_type | 否 | Integer(11) | 卡券分类类型：1普通卡券、2摇电视卡券 |
| examine_type | 否 | Integer(11) | 微信审核状态，1正常使用，2审核中，3审核失败 |
| code_type | 否 | Integer(4) | 显示卡券方式，1序列码 2条形码 3二维码，微商户卡券没有条形码 |
| brand_name | 否 | String(100) | 商家名称(上限12个汉字) |
| can_share | 否 | Integer(4) | 是否可分享 1是 2否 |
| can_give_friend | 否 | Integer(4) | 是否可转赠 1是 2否 |
| date_info_type | 否 | Integer(4) | 有效期类型 1:固定日期 2:固定时长 |
| begin | 否 | Integer(11) | 开始时间或者领取后多少天生效 |
| end | 否 | Integer(11) | 结束时间或者领取后多少天有效 |
| range | 否 | String | 使用范围(门店)，默认无限制 |
| deal_detail | 否 | String | 使用详情 |
| custom_url_name | 否 | String(15) | 商户自定义入口名称 |
| custom_url | 否 | String(128) | 自定义入口跳转外链的地址链接 |
| custom_url_sub_title | 否 | String(18) | 显示在入口右侧的tips |
| promotion_url_name | 否 | String(15) | 营销场景的自定义入口 |
| promotion_url | 否 | String(128) | 入口跳转外链的地址链接 |
| promotion_url_sub_title | 否 | String(18) | 显示在入口右侧的tips |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "card_type":1,
        "wx_card_type":1,
        "examine_type":1,
        "card_money":100,
        "money_limit":200,
        "code_type":1,
        "get_limit":1,
        "can_share":1,
        "can_give_friend":1,
        "date_info_type":2,
        "begin":1,
        "end":1,
        "quantity":100,
        "stock":100,
        "cancel_number":0,
        "shop_id":30,
        "wx_card_id":"123456",
        "logo_url":"http",
        "brand_name":"brand",
        "title":"wwww",
        "color":"#000000",
        "notice":"qqqqq",
        "service_phone":"000000",
        "description":"rrrrrr",
        "range":"123",
        "deal_detail":"ssssssssssssssssss",
        "created":1441090649,
        "modified":1441090649,
        "deleted":1,
        "id":2
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



























## __修改卡券__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/to-update
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 卡券id |
| title | 否 | String(50） | 卡券标题 |
| card_type | 否 | Integer(4) | 1:微商户 2：微信 |
| quantity | 否 | Integer(11) | 生成数量(上限100000000) |
| logo_url | 否 | String(100) | 卡券头像 |
| color | 是 | String(50） |  十六进制颜色码 |
| card_money | 是 | Integer(11) | 卡券面额 |
| money_limit | 是 | Integer(11) | 卡券使用限额 |
| get_limit | 否 | Integer(11) | 每人领取数量限制 |
| notice | 否 | String(100) | 卡券使用提醒(上限16个汉字) |
| description | 否 | String | 使用须知(上限1024个汉字) |
| service_phone | 否 | String(50) | 客服电话 |
| wx_card_id | 否 | String(100) | 微信卡券ID |
| wx_card_type | 否 | Integer(2) | 卡券类型，1代金券 2优惠券，目前只有代金券 |
| code_type | 否 | Integer(4) | 显示卡券方式，1序列码 2条形码 3二维码，微商户卡券没有条形码 |
| examine_type | 否 | Integer(11) | 微信审核状态，1正常使用，2审核中，3审核失败 |
| brand_name | 否 | String(100) | 商家名称(上限12个汉字) |
| can_share | 否 | Integer(4) | 是否可分享 1是 2否 |
| can_give_friend | 否 | Integer(4) | 是否可转赠 1是 2否 |
| date_info_type | 否 | Integer(4) | 有效期类型 1:固定日期 2:固定时长 |
| begin | 否 | Integer(11) | 开始时间或者领取后多少天生效 |
| end | 否 | Integer(11) | 结束时间或者领取后多少天有效 |
| range | 否 | String | 使用范围(门店)，默认无限制 |
| deal_detail | 否 | String | 使用详情 |
| custom_url_name | 否 | String(15) | 商户自定义入口名称 |
| custom_url | 否 | String(128) | 自定义入口跳转外链的地址链接 |
| custom_url_sub_title | 否 | String(18) | 显示在入口右侧的tips |
| promotion_url_name | 否 | String(15) | 营销场景的自定义入口 |
| promotion_url | 否 | String(128) | 入口跳转外链的地址链接 |
| promotion_url_sub_title | 否 | String(18) | 显示在入口右侧的tips |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| deleted | 否 | Integer(11) | 状态1.是、2.否 |
| rangeNullFlag | 否 | Integer(11) | 无门店限制的标识 |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 134,
    "wx_card_id": null,
    "card_type": 1,
    "wx_card_type": 1,
    "get_card_type": 1,
    "examine_type": 1,
    "card_money": 100,
    "money_limit": 1000,
    "logo_url": "http://imgcache.vikduo.com/static/a127a406ad4678fefd25f824ef2ec047.gif",
    "code_type": 1,
    "brand_name": "创刊111",
    "title": "2031349",
    "color": "#55bd47",
    "notice": "test",
    "service_phone": "13800138000",
    "description": "test1122",
    "get_limit": 50,
    "can_share": 1,
    "can_give_friend": 1,
    "date_info_type": 1,
    "begin": 1454457600,
    "end": 1455062400,
    "quantity": 100,
    "stock": 77,
    "range": ",311,",
    "deal_detail": "价值1元代金券1张，满10元可使用",
    "cancel_number": 0,
    "custom_url_name": "111",
    "custom_url": "http://baidu.com",
    "custom_url_sub_title": "222",
    "promotion_url_name": "333",
    "promotion_url": "http://baidu.com",
    "promotion_url_sub_title": "444",
    "shop_id": 30,
    "shop_sub_id": null,
    "created": 1454479166,
    "modified": 1454480047,
    "deleted": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



























## __更新卡券审核状态__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/update-examine
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| examine_type | 是 | Integer(4) | 审核状态 |
| wx_card_id | 是 | String(100) | 微信卡券ID |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 2,
    "wx_card_id": "p8uFCsxKuOby5mP3PySSP_KSMOr0",
    "card_type": 2,
    "wx_card_type": 1,
    "get_card_type": 1,
    "examine_type": "1",
    "card_money": 100,
    "money_limit": 200,
    "logo_url": "http://imgcache.vikduo.com/static/3e70ca4d483e7b65249fca8cf394a562.jpg",
    "code_type": 1,
    "brand_name": "WSH测试",
    "title": "微信卡券1027",
    "color": "#10ad61",
    "notice": "出示",
    "service_phone": "13245553344",
    "description": "使用须知",
    "get_limit": 11,
    "can_share": 1,
    "can_give_friend": 1,
    "date_info_type": 1,
    "begin": 1445904000,
    "end": 1448668800,
    "quantity": 111,
    "stock": 79,
    "range": ",192,",
    "deal_detail": "价值12元代金券1张，满33元可使用",
    "cancel_number": 0,
    "custom_url_name": null,
    "custom_url": null,
    "custom_url_sub_title": null,
    "promotion_url_name": null,
    "promotion_url": null,
    "promotion_url_sub_title": null,
    "shop_id": 30,
    "shop_sub_id": null,
    "created": 1441090649,
    "modified": 1454481619,
    "deleted": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取卡券__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/get
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动的id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| wx_card_id | 否 | String(100) | 微信卡券ID |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 2,
    "wx_card_id": "p8uFCsxKuOby5mP3PySSP_KSMOr0",
    "card_type": 2,
    "wx_card_type": 1,
    "get_card_type": 1,
    "examine_type": 1,
    "card_money": 100,
    "money_limit": 200,
    "logo_url": "http://imgcache.vikduo.com/static/3e70ca4d483e7b65249fca8cf394a562.jpg",
    "code_type": 1,
    "brand_name": "WSH测试",
    "title": "微信卡券1027",
    "color": "#10ad61",
    "notice": "出示",
    "service_phone": "13245553344",
    "description": "使用须知",
    "get_limit": 11,
    "can_share": 1,
    "can_give_friend": 1,
    "date_info_type": 1,
    "begin": 1445904000,
    "end": 1448668800,
    "quantity": 111,
    "stock": 79,
    "range": ",192,",
    "deal_detail": "价值12元代金券1张，满33元可使用",
    "cancel_number": 0,
    "custom_url_name": null,
    "custom_url": null,
    "custom_url_sub_title": null,
    "promotion_url_name": null,
    "promotion_url": null,
    "promotion_url_sub_title": null,
    "shop_id": 30,
    "shop_sub_id": null,
    "created": 1441090649,
    "modified": 1454481619,
    "deleted": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />




## __查找卡券列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/find-list
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| deleted | 否 | Integer(11) | 状态1.是、2.否 |
| card_type | 否 | Integer(4) | 显示卡券方式，1序列码 2条形码 3二维码，微商户卡券没有条形码 |
| wx_card_type | 否 | Integer(2) | 卡券类型，1代金券 2优惠券，目前只有代金券 |
| get_card_type | 否 | Integer(11) | 卡券分类类型：1普通卡券、2摇电视卡券 |
| examine_type | 否 | Integer(11) | 微信审核状态，1正常使用，2审核中，3审核失败 |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| valid | 否 | Boolean | 是否返回有效的卡券 |
| title | 否 | String(50） | 卡券标题 |
* **注意：sort排序可选字段['id']**

##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": 134,
      "wx_card_id": null,
      "card_type": 1,
      "wx_card_type": 1,
      "get_card_type": 1,
      "examine_type": 1,
      "card_money": 100,
      "money_limit": 1000,
      "logo_url": "http://imgcache.vikduo.com/static/a127a406ad4678fefd25f824ef2ec047.gif",
      "code_type": 1,
      "brand_name": "创刊111",
      "title": "2031349",
      "color": "#55bd47",
      "notice": "test",
      "service_phone": "13800138000",
      "description": "test1122",
      "get_limit": 50,
      "can_share": 1,
      "can_give_friend": 1,
      "date_info_type": 1,
      "begin": 1454457600,
      "end": 1455062400,
      "quantity": 100,
      "stock": 77,
      "range": ",311,",
      "deal_detail": "价值1元代金券1张，满10元可使用",
      "cancel_number": 0,
      "custom_url_name": "111",
      "custom_url": "http://baidu.com",
      "custom_url_sub_title": "222",
      "promotion_url_name": "333",
      "promotion_url": "http://baidu.com",
      "promotion_url_sub_title": "444",
      "shop_id": 30,
      "shop_sub_id": null,
      "created": 1454479166,
      "modified": 1454480047,
      "deleted": 1
    },
    ......
  ],
  "page": {
    "per_page": 15,
    "total_count": 11,
    "current_page": 0,
    "total_page": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />










## __删除卡券__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/general-del
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
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







## __启用卡券__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/general-enable
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
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






## __禁用卡券__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/card/general-disable
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 活动id |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
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
