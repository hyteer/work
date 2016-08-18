## 初始化会员分组
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/init-member-group
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
  "errmsg": "ok"
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## 获取会员分组列表
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/find-member-group
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| name | 否 | String(30) | 名称，最多30字符 |
| page | 否| Integer(11) | 分页 |
| count | 否 | Integer(11) | 数量 |
| sortStr | 否 | String(11) | 排序 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
        {
          "id": 51,
          "shop_id": 30,
          "member_count":0,
          "name": "默认分组",
          "description": "默认分组",
          "created": 1462785270,
          "modified": 1462785270,
          "deleted": 1,
          "type": 1,
          "sort": 100
        }
    ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## 获取全部会员分组
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/find-all-member-group
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
          "id": 51,
          "shop_id": 30,
          "member_count":0,
          "name": "默认分组",
          "description": "默认分组",
          "created": 1462785270,
          "modified": 1462785270,
          "deleted": 1
        }
    ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## 创建会员分组
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/create-member-group
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| name | 是 | String(30) | 名称，最多30字符 |
| description | 否 | String(100) | 描述 |
| sort | 否 | String(11) | 排序 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
        {
          "member_count": 0,
          "sort": 100,
          "type":2,
          "name": "aaasss",
          "description": "",
          "shop_id": 60,
          "created":1464327331,
          "modified": 1464327331,
          "deleted": 1,
          "id":60
        }
    ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## 获取会员分组基本信息
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/get-member-group
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
  "data": [
        {
          "member_count": 0,
          "sort": 100,
          "type":2,
          "name": "aaasss",
          "description": "",
          "shop_id": 60,
          "created":1464327331,
          "modified": 1464327331,
          "deleted": 1,
          "id":60
        }
    ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## 修改会员分组
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/update-member-group
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| id | 是 | Integer(11) | id |
| name | 否 | String(30) | 名称 |
| description | 否 | String(100) | 描述 |
| sort | 否 | String(11) | 排序 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
        {
          "member_count": 0,
          "sort": 100,
          "type":2,
          "name": "aaasss",
          "description": "",
          "shop_id": 60,
          "created":1464327331,
          "modified": 1464328559,
          "deleted": 1,
          "id":60
        }
    ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## 删除会员分组
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/delete-member-group
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
