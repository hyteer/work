## __会员等级列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/find-member-grade
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
      "id": 39,
      "shop_id": 30,
      "name": "默认等级",
      "remark": "默认等级asadasdfdfd",
      "discount": 10,
      "face_document_id": 264725,
      "level": 1,
      "growth": 0,
      "type": 1,
      "created": 1462785301,
      "modified": 1463801821,
      "face": {
        "id": 264725,
        "name": "level4",
        "desc": null,
        "category_id": 0,
        "tag_id": -1,
        "file_cdn_path": "http://imgcache.vikduo.com/static/29bc9e8e549a4cd764da92dcdbfbdece.png",
        "file_type": 1,
        "shop_id": 0,
        "shop_sub_id": 0,
        "created": 1462606977,
        "modified": 1462608065,
        "deleted": 1
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


## __创建会员等级__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/create-member-grade
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| name | 是 | String(30) | 名称，最多30字符 |
| discount | 否| Integer(11) | 等级折扣 |
| face_document_id | 是 | Integer(11) | 等级图标 |
| growth | 是 | Integer(11) | 等级所需成长值，最大10000000 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": 39,
      "shop_id": 30,
      "name": "默认等级",
      "remark": "默认等级asadasdfdfd",
      "discount": 10,
      "face_document_id": 264725,
      "level": 1,
      "growth": 0,
      "type": 1,
      "created": 1462785301,
      "modified": 1463801821,
      "face": {
        "id": 264725,
        "name": "level4",
        "desc": null,
        "category_id": 0,
        "tag_id": -1,
        "file_cdn_path": "http://imgcache.vikduo.com/static/29bc9e8e549a4cd764da92dcdbfbdece.png",
        "file_type": 1,
        "shop_id": 0,
        "shop_sub_id": 0,
        "created": 1462606977,
        "modified": 1462608065,
        "deleted": 1
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


## __修改会员等级__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/update-member-grade
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | id |
| shop_id | 是 | Integer(11) | 商家id |
| name | 否 | String(30) | 名称，最多30字符 |
| discount | 否| Integer(11) | 等级折扣 |
| face_document_id | 否 | Integer(11) | 等级图标 |
| growth | 否 | Integer(11) | 等级所需成长值，最大10000000 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": 39,
      "shop_id": 30,
      "name": "默认等级",
      "remark": "默认等级asadasdfdfd",
      "discount": 10,
      "face_document_id": 264725,
      "level": 1,
      "growth": 0,
      "type": 1,
      "created": 1462785301,
      "modified": 1463801821,
      "face": {
        "id": 264725,
        "name": "level4",
        "desc": null,
        "category_id": 0,
        "tag_id": -1,
        "file_cdn_path": "http://imgcache.vikduo.com/static/29bc9e8e549a4cd764da92dcdbfbdece.png",
        "file_type": 1,
        "shop_id": 0,
        "shop_sub_id": 0,
        "created": 1462606977,
        "modified": 1462608065,
        "deleted": 1
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


## __获取会员等级详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/get-member-grade
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | id |
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
      "id": 39,
      "shop_id": 30,
      "name": "默认等级",
      "remark": "默认等级asadasdfdfd",
      "discount": 10,
      "face_document_id": 264725,
      "level": 1,
      "growth": 0,
      "type": 1,
      "created": 1462785301,
      "modified": 1463801821,
      "face": {
        "id": 264725,
        "name": "level4",
        "desc": null,
        "category_id": 0,
        "tag_id": -1,
        "file_cdn_path": "http://imgcache.vikduo.com/static/29bc9e8e549a4cd764da92dcdbfbdece.png",
        "file_type": 1,
        "shop_id": 0,
        "shop_sub_id": 0,
        "created": 1462606977,
        "modified": 1462608065,
        "deleted": 1
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

## __删除会员等级__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/member/delete-member-grade
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | id |
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
