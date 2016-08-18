
# __文件库__
## __添加文件__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/document-lib/create-doc
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|name|是|varchar(100)|文件名称|
|desc|是|Integer(11)|文件描述|
|category_id|否|Integer(11)|文件分类id|
|tag_id|否|Integer(11)|标签表外键|
|file_cdn_path|是|varchar(250)|文件路径cdn路径|
|file_type|是|Integer(11)|文件类型（1.图片、2.语音、3.音乐 、4.视频、5.word、6.excel）|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|是|Integer(11)|店铺id|
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 5,
        "name": "文件一",
        "desc": "这里是描述",
        "tag_id": "1",
        "file_cdn_path": "http://fdlskjflk.com",
        "file_type": "1",
        "shop_id": "5",
        "shop_sub_id": "43",
        "created": 1434599267,
        "modified": 1434599267,
        "deleted": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />













## __修改文件__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/document-lib/update-doc
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|id|是|Integer(11)|文件id|
|name|是|varchar(100)|文件名称|
|desc|是|Integer(11)|文件描述|
|category_id|否|Integer(11)|文件分类id|
|tag_id|否|Integer(11)|标签表外键|
|file_cdn_path|是|varchar(250)|文件路径cdn路径|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|是|Integer(11)|店铺id|
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 5,
        "name": "文件一",
        "desc": "这里是描述",
        "tag_id": "1",
        "file_cdn_path": "http://fdlskjflk.com",
        "file_type": "1",
        "shop_id": "5",
        "shop_sub_id": "43",
        "created": 1434599267,
        "modified": 1434599267,
        "deleted": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />









## __获取单个文件__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/document-lib/get-doc
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|id|否|Integer(11)|文件id|
|name|否|varchar(100)|文件名称|
|tag_id|否|Integer(11)|标签表外键|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|否|Integer(11)|店铺id|
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 5,
        "name": "文件一",
        "desc": "这里是描述",
        "tag_id": "1",
        "file_cdn_path": "http://fdlskjflk.com",
        "file_type": "1",
        "shop_id": "5",
        "shop_sub_id": "43",
        "created": 1434599267,
        "modified": 1434599267,
        "deleted": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />







## __获取文件列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/document-lib/find-doc
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|id|否|array/Integer(11)|文件id|
|name|否|varchar(100)|文件名称|
|category_id|否|Integer(11)|文件分类id|
|tag_id|否|Integer(11)|标签表外键|
|file_type|否|Integer(11)|文件类型（1.图片、2.语音、3.音乐 、4.视频、5.word、6.excel）|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|否|Integer(11)|店铺id|
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": 1320,
      "name": "f81ab07800d9a56e11f4c2ac5b80187bcf305481",
      "desc": null,
      "category_id": 22,
      "tag_id": 1,
      "file_cdn_path": "http://imgcache.vikduo.com/static/58bcbb9cb42e644373ae22d615f398c3.jpg",
      "file_type": 1,
      "shop_id": 30,
      "shop_sub_id": 0,
      "created": 1452130751,
      "modified": 1452130751,
      "deleted": 1
    },
    {
      "id": 1319,
      "name": "1452130672411",
      "desc": null,
      "category_id": 22,
      "tag_id": 1,
      "file_cdn_path": "http://imgcache.vikduo.com/static/c301828651c2f65a6194097656de2c83.png",
      "file_type": 1,
      "shop_id": 30,
      "shop_sub_id": 0,
      "created": 1452130675,
      "modified": 1452130675,
      "deleted": 1
    },
  ],
  "page": {
    "per_page": 15,
    "total_count": 4,
    "current_page": 0,
    "total_page": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />






## __启用文件__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/document-lib/enable-doc
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 文件id |
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







## __禁用文件__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/document-lib/disable-doc
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 文件id |
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







## __删除文件__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/document-lib/delete-doc
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 文件id |
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







## __批量删除文件__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/document-lib/multi-delete-doc
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| ids | 是 | array | 文件id |
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







## __添加文件分类__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/document-lib/create-doc-category
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|name|是|varchar(50)|文件名称|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|否|Integer(11)|店铺id|
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": "0",
    "errmsg": "ok",
    "data": {
      "shop_sub_id": "0",
      "name": "测试",
      "shop_id": "30",
      "modified": "1451282183",
      "created": "1451282183",
      "deleted": "1",
      "id": "3"
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />






## __修改文件分类__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/document-lib/update-doc-category
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|id|是|Integer(11)|文件id|
|name|是|varchar(50)|文件名称|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|否|Integer(11)|店铺id|
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": "0",
    "errmsg": "ok",
    "data": {
      "id": "3",
      "name": "测试1",
      "shop_id": "30",
      "shop_sub_id": "0",
      "created": "1451282183",
      "modified": "1451282702",
      "deleted": "1"
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />








## __批量修改文件分类__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/document-lib/multi-update-doc-category
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| ids | 是 | array | 文件id |
|category_id|否|Integer(11)|文件分类id|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|否|Integer(11)|店铺id|
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








## __删除文件分类__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/document-lib/delete-doc-category
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|id|是|Integer(11)|文件id|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|否|Integer(11)|店铺id|
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







## __获取文件分类列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/document-lib/find-doc-category
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|否|Integer(11)|店铺id|
|name|否|varchar(50)|文件名称|
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取2000个
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": "0",
    "errmsg": "ok",
    "data": {
      "item": [
        {
          "id": "1",
          "name": "服装",
          "shop_id": "30",
          "shop_sub_id": "0",
          "created": "1451112097",
          "modified": "1451112097",
          "deleted": "1"
        },
        {
          "id": "2",
          "name": "箱包",
          "shop_id": "30",
          "shop_sub_id": "0",
          "created": "1451112097",
          "modified": "1451112097",
          "deleted": "1"
        },
        {
          "id": "3",
          "name": "测试1",
          "shop_id": "30",
          "shop_sub_id": "0",
          "created": "1451282183",
          "modified": "1451282702",
          "deleted": "1"
        }
      ]
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />





## __获取文件分类详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/document-lib/get-doc-category
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|id|是|Integer(11)|文件id|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|否|Integer(11)|店铺id|
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": "0",
    "errmsg": "ok",
    "data": {
      "id": "3",
      "name": "测试1",
      "shop_id": "30",
      "shop_sub_id": "0",
      "created": "1451282183",
      "modified": "1451282702",
      "deleted": "1"
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
