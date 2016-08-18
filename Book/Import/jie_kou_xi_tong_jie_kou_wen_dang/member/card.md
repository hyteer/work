## 初始化会员卡
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/init-member-card
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
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## 初始化会员通知
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/init-member-notice
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
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## 初始化会员卡赠送设置
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/init-member-gift
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
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## 获取会员卡信息
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/get-member-card
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
  "data":{
      "id": "328",
      "shop_id": "30",
      "is_sync_wx": "2",
      "share_message_id": "206481",
      "logo_url": "http://imgcache.vikduo.com/static/5c80e7a0d561186605c0513eb826bfd6.jpg",
      "color": "#55bd47",
      "title": "会员卡名称",
      "notice": "引导提醒",
      "prerogative": "特权说明",
      "description": "使用须知",
      "code_type": "CODE_TYPE_BARCODE",
      "location_id_list": "0",
      "quantity": "99999999",
      "brand_name": "沈阳鸿腾创展健康科技有限",
      "examine_type": "1",
      "created": "1464337350",
      "modified": "1464337350",
      "deleted": "1",
      "memberCardActivateSetting": {
        "id": "94",
        "member_card_id": "328",
        "content": {
          "item": [
            {
              "ismust": "1",
              "nametag": "phone",
              "type": "text",
              "key": "手机",
              "value": "请输入您的手机",
              "check": "1",
              "addtype": "system"
            },
            {
              "ismust": "1",
              "nametag": "name",
              "type": "text",
              "key": "姓名",
              "value": "请输入您的名字",
              "check": "1",
              "addtype": "system"
            },
            {
              "nametag": "bookedDate",
              "type": "calendar",
              "key": "生日",
              "value": "点击输入",
              "addtype": "system"
            },
            {
              "nametag": "sex",
              "type": "select",
              "key": "性别",
              "value": "男|女",
              "addtype": "system"
            },
            {
              "nametag": "area",
              "type": "customArea",
              "key": "地区",
              "value": "中国",
              "addtype": "system"
            },
            {
              "nametag": "address",
              "type": "text",
              "key": "详细地址",
              "value": "请输入您的地址",
              "addtype": "system"
            },
            {
              "nametag": "email",
              "type": "text",
              "key": "邮箱",
              "value": "请输入您的邮箱地址",
              "addtype": "system"
            }
          ]
        },
        "shop_id": "30",
        "is_gift": "2",
        "is_gift_point": "2",
        "is_gift_card": "2",
        "is_gift_mall_packet": "2",
        "is_gift_cash_packet": "2"
      },
      "shareMessage": {
        "id": "206481",
        "title": "会员卡投放图文标题",
        "desc": "会员卡投放图文描述，例如免费领取会员卡，开卡激活立即享受会员权益",
        "pic_id": "500001",
        "shop_id": "30",
        "shop_sub_id": "0",
        "created": "1464337350",
        "modified": "1464337350",
        "deleted": "1",
        "documentLib": {
          "id": "500001",
          "name": "会员等级默认图片",
          "category_id": "0",
          "tag_id": "1",
          "file_cdn_path": "http://imgcache.vikduo.com/static/95732d33bcc08b3be41b71d7b78d20fb.png",
          "file_type": "1",
          "shop_id": "0",
          "shop_sub_id": "0",
          "created": "1462932672",
          "modified": "1462932672",
          "deleted": "1"
        }
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## 添加会员卡访问
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/access-member-card
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| member_card_id | 是 | Integer(11) | 会员卡id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "member_card_id": "30",
      "access_count": "1",
      "shop_id": "30",
      "date": "1464537600",
      "created": "1464602248",
      "modified": "1464602248",
      "deleted": "1",
      "id": "55"
    }
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

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
| id | 是 | Integer(11) | id |
| title | 是 | String(11) | 标题 |
| desc | 是 | Integer(11) | 排序 |
| pic_id | 是 | Integer(11) | 关联id |
<br  /><br  />
##### 返回说明
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
      "modified": "1464602471",
      "deleted": "1"
    }
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## 修改会员卡
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/update-member-card
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| location_id_list | 否 | Integer(11) | 适用门店 |
| title | 是 | String(30) | 标题 |
| brand_name | 是 | String(12) | 名称 |
| notice | 是 | String(16) | 引导提醒 |
| logo_url | 是 | String(100) | 卡券头像 |
| color | 是 | String(50) | 十六进制颜色码 |
| service_phone | 否 | String(50) | 客服电话 |
| description | 是 | String(1024) | 使用须知 |
| prerogative | 是 | String(1024) | 特权说明 |
| code_type | 是 | String(20) | Code展示类）一维码：CODE_TYPE_BARCODE，二维码：CODE_TYPE_QRCODE，文本：CODE_TYPE_TEXT |
| custom_url_name | 否 | String(5) | 激活后自定义的入口名字 |
| promotion_url_name | 否| String(5) | 商户自定义入口名称 |
| custom_cell1_name | 否 | String(5) | 激活后自定义的入口名字 |
| custom_url | 否 | String(128) | 自定义入口跳转外链的地址链接 |
| promotion_url | 否 | String(128) | 自定义入口跳转外链的地址链接 |
| custom_cell1_url | 否 | String(128) | 激活后显示在入口右侧的tips |
| custom_url_sub_title | 否 | String(6) | 显示在入口右侧的tips |
| promotion_url_sub_title | 否 | String(6) | 显示在入口右侧的tips |
| custom_cell1_tips | 否 | String(6) | 激活后右侧显示的tips |
| memberCardActivateSetting | 是 | Integer(11) | 会员卡活动设置 |
<br  /><br  />
##### 返回说明
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
      "modified": "1464602471",
      "deleted": "1"
    }
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## 同步商家会员卡到微信
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/member-card-sync-wx
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
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## 会员同步微信会员卡
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/sync-wx-card
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| content | 是 | String(100) | 内容 |
| id | 否 | Integer(11) | id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## 同步会员数据到微信会员卡券
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/sync-data-to-wx
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| wx_code | 是 | String(50) | 微信码 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## 获取会员卡激活设置
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/get-member-card-activate-setting
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
  "data":{
    "id": "96",
      "member_card_id": "330",
      "content": "[{\"ismust\":true,\"nametag\":\"phone\",\"type\":\"text\",\"key\":\"\\u624b\\u673a\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u624b\\u673a\",\"check\":true,\"addtype\":\"system\"},{\"ismust\":true,\"nametag\":\"name\",\"type\":\"text\",\"key\":\"\\u59d3\\u540d\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u540d\\u5b57\",\"check\":true,\"addtype\":\"system\"},{\"ismust\":false,\"nametag\":\"bookedDate\",\"type\":\"calendar\",\"key\":\"\\u751f\\u65e5\",\"value\":\"\\u70b9\\u51fb\\u8f93\\u5165\",\"check\":false,\"addtype\":\"system\"},{\"ismust\":false,\"nametag\":\"sex\",\"type\":\"select\",\"key\":\"\\u6027\\u522b\",\"value\":\"\\u7537|\\u5973\",\"check\":false,\"addtype\":\"system\"},{\"ismust\":false,\"nametag\":\"area\",\"type\":\"customArea\",\"key\":\"\\u5730\\u533a\",\"value\":\"\\u4e2d\\u56fd\",\"check\":false,\"addtype\":\"system\"},{\"ismust\":false,\"nametag\":\"address\",\"type\":\"text\",\"key\":\"\\u8be6\\u7ec6\\u5730\\u5740\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u5730\\u5740\",\"check\":false,\"addtype\":\"system\"},{\"ismust\":false,\"nametag\":\"email\",\"type\":\"text\",\"key\":\"\\u90ae\\u7bb1\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u90ae\\u7bb1\\u5730\\u5740\",\"check\":false,\"addtype\":\"system\"}]",
      "shop_id": "32",
      "is_gift_point": "2",
      "is_gift": "2",
      "is_gift_card": "2",
      "is_gift_mall_packet": "2",
      "is_gift_cash_packet": "2"
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## 修改会员卡激活设置
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/update-member-card-activate-setting
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| is_gift | 否 | Integer(11) | 是否开启开卡赠送）1：开启，2：关闭 |
| is_gift_point | 否 | Integer(11) | 是否开卡赠送积分 |
| gift_point | 否 | Integer(11) | 开卡赠送积分 |
| gift_growth | 否 | Integer(11) | 开卡赠送成长值 |
| is_gift_card | 否 | Integer(11) | 是否开卡赠送卡券）1：开启，2：关闭 |
| gift_card_type | 否 | Integer(11) | 开卡赠送卡券方式）1：随机赠送，2：全部赠送 |
| is_gift_mall_packet | 否 | Integer(11) | 是否开卡赠送现金红包）1：开启，2：关闭 |
| gift_mall_packet_type | 否 | Integer(11) | 开卡赠送商城红包方式）1：随机赠送，2：全部赠送 |
| is_gift_cash_packet | 否 | Integer(11) | 是否开卡赠送现金红包）1：开启，2：关闭 |
| gift_cash_packet_type | 否 | Integer(11) | 开卡赠送现金红包方式）1：随机赠送，2：全部赠送 |
| content | 否 | String(11) | 表单字段json |
| gift_card_ids | 否 | String(11) | 开卡赠送卡券id（是卡券表的id） |
| gift_mall_packet_ids | 否 | Integer(11) | 开卡赠送商城红包id |
| gift_cash_packet_ids | 否 | Integer(11) | 开卡赠送现金红包id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": "94",
      "member_card_id": "328",
      "content": "[{\"ismust\":true,\"nametag\":\"phone\",\"type\":\"text\",\"key\":\"\\u624b\\u673a\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u624b\\u673a\",\"check\":true,\"addtype\":\"system\"},{\"ismust\":true,\"nametag\":\"name\",\"type\":\"text\",\"key\":\"\\u59d3\\u540d\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u540d\\u5b57\",\"check\":true,\"addtype\":\"system\"},{\"ismust\":false,\"nametag\":\"bookedDate\",\"type\":\"calendar\",\"key\":\"\\u751f\\u65e5\",\"value\":\"\\u70b9\\u51fb\\u8f93\\u5165\",\"check\":false,\"addtype\":\"system\"},{\"ismust\":false,\"nametag\":\"sex\",\"type\":\"select\",\"key\":\"\\u6027\\u522b\",\"value\":\"\\u7537|\\u5973\",\"check\":false,\"addtype\":\"system\"},{\"ismust\":false,\"nametag\":\"area\",\"type\":\"customArea\",\"key\":\"\\u5730\\u533a\",\"value\":\"\\u4e2d\\u56fd\",\"check\":false,\"addtype\":\"system\"},{\"ismust\":false,\"nametag\":\"address\",\"type\":\"text\",\"key\":\"\\u8be6\\u7ec6\\u5730\\u5740\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u5730\\u5740\",\"check\":false,\"addtype\":\"system\"},{\"ismust\":false,\"nametag\":\"email\",\"type\":\"text\",\"key\":\"\\u90ae\\u7bb1\",\"value\":\"\\u8bf7\\u8f93\\u5165\\u60a8\\u7684\\u90ae\\u7bb1\\u5730\\u5740\",\"check\":false,\"addtype\":\"system\"}]",
      "shop_id": "30",
      "is_gift_point": "2",
      "is_gift": "2",
      "is_gift_card": "2",
      "is_gift_mall_packet": "2",
      "is_gift_cash_packet": "2"
    }
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## 修改微信会员卡审核状态
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/update-member-card-examine
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| wx_card_id | 是 | String(11) | 微信卡id |
| examine_type | 是 | In(11) | 检查类型|
<br  /><br  />
##### 返回说明
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
      "modified": "1464602471",
      "deleted": "1"
    }
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## 修改微信会员卡个人信息
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/update-user-info
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | In(11) | 用户id |
| shop_id | 是 | Integer(11) | 商家id |
| name| 是 | String(30) | 会员名称|
| sex | 否 | Integer(11) | 性别 |
| bookedDate | 否 | Integer(11) | 生日 |
| email | 否 | String(11) | 邮件|
| address | 否 | String(11) | 地址 |
| custom_field_1 | 否 | String(11) | 自定义 |
| custom_field_2 | 否 | String(11) | 自定义 |
| custom_field_3 | 否 | String(11) | 自定义 |
| custom_field_4 | 否 | String(11) | 自定义 |
| custom_field_5 | 否 | String(11) | 自定义 |
| province | 否 | String(11) | 省 |
| city | 否 | String(11) | 市 |
| county | 否 | String(11) | 区|
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": []
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## 获取门店会员归属
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/fans-belong-store
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | In(11) | 用户id |
| shop_id | 是 | Integer(11) | 商家id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "item": {
      "id": "292",
      "shop_id": "30",
      "shop_sub_id": "292",
      "name": "tang",
      "bg_img": "http://imgcache.vikduo.com/static/664933ac4ec84eaeaf679c9ba41e5a9b.jpg",
      "description": "sdg",
      "ewm_img": "https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=gQFh8DoAAAAAAAAAASxodHRwOi8vd2VpeGluLnFxLmNvbS9xL1lrTndJNnJtYUpFUnlTNkFHR19wAAIEHjG%2FVQMEAAAAAA%3D%3D",
      "scene_id": "64",
      "lbs": "1",
      "phone": "13800138000",
      "province_id": "214",
      "city_id": "215",
      "district_id": "216",
      "circle_id": "217",
      "address": "sdg",
      "businesshour": "09:00-21:00",
      "url": "http://www.baidu.com",
      "wx_categories": "[{\"id\":\"1\",\"name\":\"\\u7f8e\\u98df\"},{\"id\":\"21\",\"name\":\"\\u5ddd\\u83dc\"},{\"id\":22,\"name\":\"\\u81ea\\u8d21\\u76d0\\u5e2e\\u83dc\"}]",
      "available_status": "4",
      "recommend": "fdsg",
      "special": "sdg",
      "avg_price": "4",
      "poi_id": "402029207",
      "fail_msg": "商户名称不规范:",
      "update_status": "0",
      "created": "1450862254",
      "modified": "1464147567",
      "deleted": "1",
      "pid": "0",
      "lng": "116.18935882745",
      "lat": "39.67027573897",
      "sync_setting": "1",
      "shop_type": "1",
      "agent_id": "0",
      "is_pickup_shop": "2",
      "is_fx": "1",
      "qrcode_policy_id": "39"
    }
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## 获取会员成长值明细
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/find-member-growth-detail
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| member_id | 是 | In(11) | 会员id |
| shop_id | 是 | Integer(11) | 商家id |
| type | 否 | In(11) | 数据类型 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
      "item": {
        "id": "16",
        "shop_id": "30",
        "uid": "0",
        "member_id": "1811",
        "before_growth": "0",
        "growth": "1",
        "type": "1",
        "event": "4",
        "source": "成长值变动记录",
        "created": "1466403763",
        "modified": "1466403763",
        "deleted": "1"
      }
    },
    "page": {
      "per_page": "20",
      "total_count": "1",
      "current_page": "0",
      "total_page": "1"
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
