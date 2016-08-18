## __获取杂志模板详情__


##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/get-magazine-template
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 模板id |
<br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": "107",
    "name": "模板1",
    "share_message_id": 944,
    "face_document_id": 351,
    "music_document_id": 352,
    "flag": 2,
    "category_id": "1",
    "index": "100",
    "use_count": 2,
    "created": null,
    "modified": 1441503698,
    "deleted": 1,
    "templateInfo": [
      {
        "id": "1",
        "template_id": "107",
        "content": "ehsahdfsgfds",
        "page": 1,
        "created": null,
        "modified": null
      }
    ],
    "shareMessage": {
      "id": 944,
      "title": "杂志分享",
      "desc": "呵呵哒",
      "pic_id": 348,
      "shop_id": 30,
      "shop_sub_id": 0,
      "created": 1441077920,
      "modified": 1441077920,
      "deleted": 1,
      "documentLib": {
        "id": 348,
        "name": "bg",
        "desc": null,
        "tag_id": 1,
        "file_cdn_path": "http://imgcache.vikduo.com/static/2d36c4a760add3e782ced63cab384114.jpg",
        "file_type": 1,
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": 1440404441,
        "modified": 1440404441,
        "deleted": 1
      }
    },
    "face": {
      "id": 351,
      "name": "QQ图片20150608155118",
      "desc": null,
      "tag_id": 1,
      "file_cdn_path": "http://imgcache.vikduo.com/static/57cbdb6c373f42659dfb7c9e1c501de7.jpg",
      "file_type": 1,
      "shop_id": 30,
      "shop_sub_id": 0,
      "created": 1440469850,
      "modified": 1440469850,
      "deleted": 1
    },
    "music": {
      "id": 352,
      "name": "QQ图片20150608155118",
      "desc": null,
      "tag_id": 1,
      "file_cdn_path": "http://imgcache.vikduo.com/static/57cbdb6c373f42659dfb7c9e1c501de7.jpg",
      "file_type": 1,
      "shop_id": 30,
      "shop_sub_id": 0,
      "created": 1440470150,
      "modified": 1440470150,
      "deleted": 1
    }
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取杂志模板列表__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/find-magazine-template
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| name | 否 | String(30) | 模板名称 |
| flag | 否 | Integer(4) | 是否经典 1是 2否 |
| category_id | 否 | Integer(11) | 分类id |
| tag_id | 否 | Integer(11)/Array | 标签id/id数组 |
| page | 否 | Integer(11) | 页码 |
| count| 否 | Integer(11) | 每页总数 |
| sortStr| 否 | Array | 排序 |
**注：不传入分页参数则获取所有模板**
<br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": "107",
      "name": "模板1",
      "share_message_id": 944,
      "face_document_id": 351,
      "music_document_id": 352,
      "flag": 2,
      "category_id": "1",
      "index": "100",
      "use_count": 2,
      "created": null,
      "modified": 1441503698,
      "deleted": 1,
      "face": {
        "id": 351,
        "name": "QQ图片20150608155118",
        "desc": null,
        "tag_id": 1,
        "file_cdn_path": "http://imgcache.vikduo.com/static/57cbdb6c373f42659dfb7c9e1c501de7.jpg",
        "file_type": 1,
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": 1440469850,
        "modified": 1440469850,
        "deleted": 1
      }
    }
  ],
  "page": {
    "per_page": 20,
    "total_count": 1,
    "current_page": 0,
    "total_page": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取杂志模板分类列表__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/find-magazine-template-category
<br  /><br  />

##### 参数说明
空
<br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": "1",
      "name": "分类1",
      "created": null,
      "modified": null
    },
    {
      "id": "2",
      "name": "分类2",
      "created": null,
      "modified": null
    }
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取杂志页面模板详情__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/get-magazine-page
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 页面模板id |
<br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": "29",
    "name": "页面1",
    "face_document_id": 351,
    "index": "100",
    "content": "sdfgsgfgsdfgsdfgsdfg",
    "category_id": "1",
    "created": null,
    "modified": null,
    "deleted": 1,
    "face": {
      "id": 351,
      "name": "QQ图片20150608155118",
      "desc": null,
      "tag_id": 1,
      "file_cdn_path": "http://imgcache.vikduo.com/static/57cbdb6c373f42659dfb7c9e1c501de7.jpg",
      "file_type": 1,
      "shop_id": 30,
      "shop_sub_id": 0,
      "created": 1440469850,
      "modified": 1440469850,
      "deleted": 1
    }
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取杂页面模板列表__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/find-magazine-page
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| name | 否 | String(30) | 页面模板名称 |
| category_id | 否 | Integer(11) | 模板分类id |
| page | 否 | Integer(11) | 页码 |
| count | 否 | Integer(11) | 每页总数 |
| sortStr | 否 | Array | 排序 |
<br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": "29",
      "name": "页面1",
      "face_document_id": 351,
      "index": "100",
      "content": "sdfgsgfgsdfgsdfgsdfg",
      "category_id": "1",
      "created": null,
      "modified": null,
      "deleted": 1,
      "face": {
        "id": 351,
        "name": "QQ图片20150608155118",
        "desc": null,
        "tag_id": 1,
        "file_cdn_path": "http://imgcache.vikduo.com/static/57cbdb6c373f42659dfb7c9e1c501de7.jpg",
        "file_type": 1,
        "shop_id": 30,
        "shop_sub_id": 0,
        "created": 1440469850,
        "modified": 1440469850,
        "deleted": 1
      }
    }
  ],
  "page": {
    "per_page": 10,
    "total_count": 1,
    "current_page": 0,
    "total_page": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取杂志页面模板分类列表__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/find-magazine-page-category
<br  /><br  />

##### 参数说明
空
<br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": "1",
      "name": "分类1",
      "created": "0",
      "modified": null
    },
    {
      "id": "2",
      "name": "分类2",
      "created": "0",
      "modified": null
    }
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取杂志模板标签列表__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/find-magazine-template-tag
<br  /><br  />

##### 参数说明
空
<br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": "76",
      "pid": "0",
      "name": "标签1",
      "type": 1,
      "created": null,
      "modified": null,
      "subTag": [
        {
          "id": "77",
          "pid": "76",
          "name": "标签2",
          "type": 1,
          "created": null,
          "modified": null
        }
      ]
    }
  ]
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

