## __会员列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/find-member
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| create_start | 否 | Integer(11) | 创建时间 |
| create_end | 否 | Integer(11) | 创建时间 |
| level | 否 | Array | 等级 |
| province | 否 | Array | 所在省 |
| city | 否 | Array | 所在市 |
| country | 否 | Array | 所在国家 |
| county | 否 | Array | 所在区 |
| real_name | 否 | Array | 姓名 |
| mobile | 否 | Array | 手机号 |
| status | 否 | Array | 状态）1：正常，2：冻结，3未绑定 |
| is_get_card | 否 | Array | 是否领取会员卡）1：领取了，2：未领取 |
| source | 否 | Array | 来源类型）1：线上申请，2：线下导入 |
| member_group_id | 否 | Array | 会员分组id |
| tags | 否 | Array | 会员标签id |
| sex | 否 | Array | 性别（1：男，2：女，3：未知） |
| email | 否 | Array | 邮箱 |
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
      "id": 1,
      "member_no": "1000030012016051017054553283",
      "is_sync_wx": null,
      "wx_code": "12016051718050724001",
      "wx_card_id": null,
      "is_get_card": 1,
      "member_card_activate_id": 64,
      "custom_field_1": null,
      "custom_field_2": "Dirks",
      "custom_field_3": null,
      "custom_field_4": null,
      "custom_field_5": null,
      "shop_id": 30,
      "source": 1,
      "level": 2,
      "member_group_id": 52,
      "growth": 15,
      "status": 1,
      "created": 1462871325,
      "modified": 1463646379,
      "deleted": 1,
      "wxUserInfos": [],
      "memberGroup": {
        "id": 52,
        "shop_id": 30,
        "member_count": 1,
        "sort": 100,
        "type": 2,
        "name": "腹股沟管",
        "description": "",
        "created": 1462785688,
        "modified": 1462785688,
        "deleted": 1
      },
      "memberGrade": {
        "id": 43,
        "shop_id": 30,
        "name": "你是",
        "remark": "asasa",
        "discount": 100,
        "face_document_id": 264718,
        "level": 2,
        "growth": 1,
        "type": 2,
        "created": 1462861847,
        "modified": 1463801821
      }
    }
  ],
  "page": {
    "per_page": 1,
    "total_count": 26,
    "current_page": 0,
    "total_page": 26
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __会员详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/get-member
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| id | 否 | Integer(11) | 会员id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":
       {
      "id": 1,
      "member_no": "1000030012016051017054553283",
      "is_sync_wx": null,
      "wx_code": "12016051718050724001",
      "wx_card_id": null,
      "is_get_card": 1,
      "member_card_activate_id": 64,
      "custom_field_1": null,
      "custom_field_2": "Dirks",
      "custom_field_3": null,
      "custom_field_4": null,
      "custom_field_5": null,
      "shop_id": 30,
      "source": 1,
      "level": 2,
      "member_group_id": 52,
      "growth": 15,
      "status": 1,
      "created": 1462871325,
      "modified": 1463646379,
      "deleted": 1,
      "wxUserInfos": [],
      "memberGroup": {
        "id": 52,
        "shop_id": 30,
        "member_count": 1,
        "sort": 100,
        "type": 2,
        "name": "腹股沟管",
        "description": "",
        "created": 1462785688,
        "modified": 1462785688,
        "deleted": 1
      },
      "memberGrade": {
        "id": 43,
        "shop_id": 30,
        "name": "你是",
        "remark": "asasa",
        "discount": 100,
        "face_document_id": 264718,
        "level": 2,
        "growth": 1,
        "type": 2,
        "created": 1462861847,
        "modified": 1463801821
      }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取会员标签信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/get-member-tag-relation
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| id | 否 | Integer(11) | 会员id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "member_tag_id": 9
    },
    {
      "member_tag_id": 10
    }
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __修改会员信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/update-member
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| id | 否 | Array | 会员id |
| status | 否 | Array | 状态）1：正常，2：冻结，3未绑定 |
| member_group_id | 否 | Array | 会员分组id |
| tags | 否 | Array | 会员标签id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":
       {
      "id": 1,
      "member_no": "1000030012016051017054553283",
      "is_sync_wx": null,
      "wx_code": "12016051718050724001",
      "wx_card_id": null,
      "is_get_card": 1,
      "member_card_activate_id": 64,
      "custom_field_1": null,
      "custom_field_2": "Dirks",
      "custom_field_3": null,
      "custom_field_4": null,
      "custom_field_5": null,
      "shop_id": 30,
      "source": 1,
      "level": 2,
      "member_group_id": 52,
      "growth": 15,
      "status": 1,
      "created": 1462871325,
      "modified": 1463646379,
      "deleted": 1,
      "wxUserInfos": [],
      "memberGroup": {
        "id": 52,
        "shop_id": 30,
        "member_count": 1,
        "sort": 100,
        "type": 2,
        "name": "腹股沟管",
        "description": "",
        "created": 1462785688,
        "modified": 1462785688,
        "deleted": 1
      },
      "memberGrade": {
        "id": 43,
        "shop_id": 30,
        "name": "你是",
        "remark": "asasa",
        "discount": 100,
        "face_document_id": 264718,
        "level": 2,
        "growth": 1,
        "type": 2,
        "created": 1462861847,
        "modified": 1463801821
      }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
