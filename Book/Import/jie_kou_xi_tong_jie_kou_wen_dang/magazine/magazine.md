
## __创建自定义杂志__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/create-magazine
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| name | 否 | String(255) | 杂志名称 |
| category_id | 否 | Integer(11) | 分类id |
| face_document_id | 否 | Integer(11) | 封面图片文档id |
| music_document_id | 否 | Integer(11) | 背景音乐文档id |
| version | 否 | String(20) | 版本号 |
| magazineInfo.$key.page | 是 | Integer(11) | 页码 |
| magazineInfo.$key.content | 否 | Text | 内容 |
| shareMessage.title | 否 | String(100) | 分享标题 |
| shareMessage.desc | 否 | String(100) | 分享描述 |
| shareMessage.pic_id | 否 | Integer(11) | 分享图片文档id |
<br  /><br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "name": "新杂志-0908150147",
    "category_id": "1",
    "type": 1,
    "share_message_id": 0,
    "face_document_id": 0,
    "music_document_id": 0,
    "pv": 0,
    "version": "2.1.7",
    "shop_id": 30,
    "deleted": 1,
    "created": 1441695707,
    "modified": 1441695707,
    "id": "13",
    "magazineInfo": [
      {
        "magazine_id": "13",
        "page": 1,
        "content": "",
        "shop_id": 30,
        "created": 1441695707,
        "modified": 1441695707,
        "id": "21"
      }
    ]
  }
}
```

错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __创建模板杂志__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/create-magazine-by-template
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| template_id | 是 | Integer(11) | 模板id |
<br  /><br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "name": "新杂志-20150906173354",
    "category_id": "1",
    "type": 1,
    "share_message_id": 959,
    "face_document_id": 351,
    "music_document_id": 352,
    "pv": 0,
    "version": "2.1.7",
    "shop_id": 30,
    "deleted": 1,
    "created": 1441532034,
    "modified": 1441532034,
    "id": "10",
    "shareMessage": {
      "shop_sub_id": 0,
      "title": "杂志分享",
      "desc": "呵呵哒",
      "pic_id": 348,
      "shop_id": 30,
      "created": 1441532034,
      "modified": 1441532034,
      "deleted": 1,
      "id": 959
    },
    "magazineInfo": [
      {
        "magazine_id": "10",
        "content": "ehsahdfsgfds",
        "page": 1,
        "created": 1441532034,
        "modified": 1441532034,
        "shop_id": 30,
        "id": "14"
      }
    ]
  }
}
```

错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __修改杂志信息__


##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/update-magazine
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 杂志id |
| shop_id | 是 | Integer(11) | 店铺id |
| name | 否 | String(255) | 杂志名称 |
| category_id | 否 | Integer(11) | 杂志分类id |
| face_document_id | 否 | Integer(11) | 封面文档id |
| music_document_id | 否 | Integer(11) | 背景音乐文档id |
| version | 否 | String(20) | 版本号 |
| magazineInfo.$key.id | 否 | String | 杂志页面id |
| magazineInfo.$key.content | 否 | String | 杂志页面内容 |
| magazineInfo.$key.page | 否 | Integer | 杂志页面页码 |
| shareMessage.id | 否 | Integer(11) | 自定义分享id |
| shareMessage.title | 否 | String(100) | 自定义分享标题 |
| shareMessage.desc | 否 | String(100) | 自定义分享描述 |
| shareMessage.pic_id | 否 | Integer(11) | 自定义分享图片文档id|
<br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":"1",
        "name":"新好杂志",
        "category_id":1,
        "type":1,
        "share_message_id":943,
        "face_document_id":346,
        "music_document_id":347,
        "pv":0,
        "version":"2.1.7",
        "shop_id":30,
        "created":1441076233,
        "modified":1441077280,
        "deleted":1,
        "shareMessage":{
            "id":943,
            "title":"杂志分享",
            "desc":"啊哈哈",
            "pic_id":348,
            "shop_id":30,
            "shop_sub_id":0,
            "created":1441076233,
            "modified":1441077280,
            "deleted":1
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取杂志详情__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/get-magazine
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 杂志id |
| shop_id | 是 | Integer(11) | 店铺id |
<br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": "3",
    "name": "棒棒哒",
    "category_id": "1",
    "type": 1,
    "share_message_id": 944,
    "face_document_id": 346,
    "music_document_id": 347,
    "pv": 10,
    "version": "2.1.7",
    "shop_id": "30",
    "created": 1441077746,
    "modified": 1441090113,
    "deleted": 1,
    "magazineInfo": [
      {
        "id": "3",
        "magazine_id": "3",
        "content": "1212121",
        "page": 1,
        "shop_id": 30,
        "created": 1441077746,
        "modified": 1441077920
      },
      {
        "id": "4",
        "magazine_id": "3",
        "content": "454564545454",
        "page": 2,
        "shop_id": 30,
        "created": 1441077746,
        "modified": 1441077920
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
      "id": 346,
      "name": "myjobdeer",
      "desc": null,
      "tag_id": 1,
      "file_cdn_path": "http://imgcache.vikduo.com/static/446eb23c7062bb203f21d5c6108cb76a.png",
      "file_type": 1,
      "shop_id": 30,
      "shop_sub_id": 0,
      "created": 1440402797,
      "modified": 1440402797,
      "deleted": 1
    },
    "music": {
      "id": 347,
      "name": "QQ图片20150608155118",
      "desc": null,
      "tag_id": 1,
      "file_cdn_path": "http://imgcache.vikduo.com/static/57cbdb6c373f42659dfb7c9e1c501de7.jpg",
      "file_type": 1,
      "shop_id": 30,
      "shop_sub_id": 0,
      "created": 1440403240,
      "modified": 1440403240,
      "deleted": 1
    }
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取杂志列表__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/find-magazine
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| name | 否 | String(255) | 杂志名称 |
| category_id | 否 | Integer(11) | 分类id |
| type | 否 | Integer(4) | 杂志类型 1商家 2系统 |
| createStart | 否 | Integer(11) | 杂志创建起始时间 |
| createEnd | 否 | Integer(11) | 杂志创建结束时间 |
| page | 否 | Integer(11) | 页码 |
| count | 否 | Integer(11) | 每页总数 |
| sortStr | 否 | Array | 排序 |
<br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":[
        {
            "id":"3",
            "name":"棒棒哒",
            "category_id":"1",
            "type":1,
            "share_message_id":944,
            "face_document_id":346,
            "music_document_id":347,
            "pv":0,
            "version":"2.1.7",
            "shop_id":"30",
            "created":1441077746,
            "modified":1441077920,
            "deleted":1
        },
        {
            "id":"1",
            "name":"新好杂志",
            "category_id":"1",
            "type":1,
            "share_message_id":943,
            "face_document_id":346,
            "music_document_id":347,
            "pv":0,
            "version":"2.1.7",
            "shop_id":"30",
            "created":1441076233,
            "modified":1441077583,
            "deleted":1
        }
    ],
    "page":{
        "per_page":10,
        "total_count":2,
        "current_page":0,
        "total_page":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __增加杂志访问量__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/add-magazine-pv
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 杂志id |
| shop_id | 是 | Integer(11) | 店铺id |
| add_pv | 是 | Integer(11) | 增加访问量 |
<br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":"3",
        "name":"棒棒哒",
        "category_id":"1",
        "type":1,
        "share_message_id":944,
        "face_document_id":346,
        "music_document_id":347,
        "pv":10,
        "version":"2.1.7",
        "shop_id":30,
        "created":1441077746,
        "modified":1441089812,
        "deleted":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __复制杂志__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/copy-magazine
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| magazine_id | 是 | Integer(11) | 杂志id |
| shop_id | 是 | Integer(11) | 店铺id |
<br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "name": "棒棒哒-复制",
    "category_id": "1",
    "type": 1,
    "share_message_id": 956,
    "face_document_id": 346,
    "music_document_id": 347,
    "pv": 10,
    "version": "2.1.7",
    "shop_id": "30",
    "deleted": 2,
    "created": 1441526746,
    "modified": 1441526747,
    "id": "6",
    "magazineInfo": [
      {
        "magazine_id": "6",
        "content": "1212121",
        "page": 1,
        "shop_id": 30,
        "created": 1441526746,
        "modified": 1441526746,
        "id": "10"
      },
      {
        "magazine_id": "6",
        "content": "454564545454",
        "page": 2,
        "shop_id": 30,
        "created": 1441526747,
        "modified": 1441526747,
        "id": "11"
      }
    ],
    "shareMessage": {
      "shop_sub_id": 0,
      "title": "杂志分享",
      "desc": "呵呵哒",
      "pic_id": 348,
      "shop_id": 30,
      "created": 1441526746,
      "modified": 1441526746,
      "deleted": 1,
      "id": 956
    }
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __删除杂志__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/del-magazine
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 杂志id |
| shop_id | 是 | Integer(11) | 店铺id |
<br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":null
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __添加杂志页面__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/create-single-magazine-info
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| magazine_id | 是 | Integer(11) | 杂志id |
| page | 是 | Integer(11) | 页码 |
| shop_id | 是 | Integer(11) | 店铺id |
| content | 是 | Text | 页面内容 |
<br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "magazine_id":1,
        "content":"adsffa",
        "page":2,
        "shop_id":30,
        "created":1441100322,
        "modified":1441100322,
        "id":"5"
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __删除杂志页面__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/del-magazine-info
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 页面id |
| magazine_id | 是 | Integer(11) | 杂志id |
| shop_id | 是 | Integer(11) | 店铺id |
<br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":null
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __启用杂志__


##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/enable-magazine
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 杂志id |
| shop_id | 是 | Integer(11) | 店铺id |
<br  />

##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":null
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __禁用杂志__


##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/disable-magazine
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 杂志id |
| shop_id | 是 | Integer(11) | 店铺id |
<br  />

##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":null
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __创建用户访问记录__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/create-magazine-access-log
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| magazine_id | 是 | Integer(11) | 杂志id |
| url | 否 | String(255) | 访问的完整url |
| device | 否 | String(10) | 访问者设备 |
| ip | 否 | String(30) | 访问者IP |
| browse | 否 | String(30) | 访问者浏览器 |
| os | 否 | String(30) | 访问者操作系统 |
<br  />

##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "magazine_id":3,
        "url":"www.ddd.com",
        "device":"phone",
        "ip":"127.0.0.1",
        "browse":"uc",
        "os":"android",
        "deleted":1,
        "shop_id":30,
        "created":1441090605,
        "modified":1441090605,
        "id":"1"
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

