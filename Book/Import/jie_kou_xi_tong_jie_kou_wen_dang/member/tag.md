## 获取会员标签列表
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/find-member-tag
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| name | 否 | String(30) | 名称 |
| page | 否 | Integer(11) | 分页 |
| count | 否 | Integer(11) | 数量 |
| sortStr | 否 | Integer(11) | 排序 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
      "item": [
        {
          "id": "9",
          "shop_id": "30",
          "name": "和嘎嘎嘎",
          "sort": "0",
          "member_count": "0",
          "created": "1462785697",
          "modified": "1462858237",
          "deleted": "1"
        }
        ]
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## 获取全部会员标签
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/find-all-member-tag
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
  "data": {
      "item": [
            {
              "id": "9",
              "shop_id": "30",
              "name": "和嘎嘎嘎",
              "sort": "0",
              "member_count": "0",
              "created": "1462785697",
              "modified": "1462858237",
              "deleted": "1"
            }
        ]
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## 创建会员标签
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/create-member-tag
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| name | 是 | String(11) | 名称 |
| sort | 否 | Integer(11) | 排序 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [{
      "sort": "100",
      "member_count": "0",
      "name": "asdasd",
      "shop_id": "60",
      "created": "1464330005",
      "modified": "1464330005",
      "deleted": "1",
      "id": "12"
    ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## 获取会员标签基本信息
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/get-member-tag
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| id | 是 | Integer(11) | id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [{
      "MemberTag": {
        "id": "12",
        "shop_id": "60",
        "name": "asdasd",
        "sort": "100",
        "member_count": "0",
        "created": "1464330005",
        "modified": "1464330005",
        "deleted": "1"
      }
    ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## 修改会员标签
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/update-member-tag
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| id | 是 | Integer(11) | id |
| name | 否 | String(30) | 名称 |
| sort | 否 | Integer(11) | 排序 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [{
      "id": "12",
      "shop_id": "60",
      "name": "asdasd",
      "sort": "100",
      "member_count": "0",
      "created": "1464330005",
      "modified": "1464330774",
      "deleted": "1"
        }
    ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## 删除员标签
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/delete-member-tag
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| id | 是 | Integer(11) | id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": ""
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
