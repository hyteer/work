# 打印机素材
## __创建素材__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/create-printer-materials
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| title|是|varchar(40)|标题|
| material_url|是|varchar(180)|素材图片url地址|
| shop_id|是|Integer(11)|商铺id|
| shop_sub_id|否|Integer(11)|分店id|
| type|是|Integer(4)|素材类型：1为图片;2为视频|
| factory | 是 | Integer(4) | 打印机厂商：1为微信创 |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": "0",
    "errmsg": "ok",
    "data": {
      "type": "1",
      "factory": "1",
      "shop_sub_id": "0",
      "shop_id": "32",
      "title": "2",
      "material_url": "http://imgcache.vikduo.com/static/4776c56e652ed34ffb587ef61a585226.png",
      "api_material_title": "5fe61e95-995d-4fdf-a5a7-4dd81de5b123",
      "api_material_id": "13",
      "modified": "1441164845",
      "created": "1441164845",
      "id": "2"
    }
  }
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  /><br  /><br  />
## __删除素材__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/del-printer-materials
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|素材id|
| shop_id|是|Integer(11)|商铺id|


<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": "0",
    "errmsg": "ok",
    "data": ""
  }
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  /><br  /><br  />
## __获取素材列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/get-printer-materials
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| factory | 是 | Integer(4) | 打印机厂商：1为微信创 |
| shop_sub_id|否|Integer(11)|分店id|
| type|否|Integer(4)|素材类型：1为图片;2为视频|
| title|否|varchar(40)|标题|


<br  />
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
          "title": "1",
          "api_material_title": "0190746f-191c-1e2c-345f-a0e8cd31599b",
          "material_url": "http://imgcache.vikduo.com/static/4776c56e652ed34ffb587ef61a585226.png",
          "api_material_id": "12",
          "type": "1",
          "factory": "1",
          "created": "1441164067",
          "modified": "1441164067",
          "shop_id": "32",
          "shop_sub_id": "0"
        },
        {
          "id": "2",
          "title": "2",
          "api_material_title": "5fe61e95-995d-4fdf-a5a7-4dd81de5b123",
          "material_url": "http://imgcache.vikduo.com/static/4776c56e652ed34ffb587ef61a585226.png",
          "api_material_id": "13",
          "type": "1",
          "factory": "1",
          "created": "1441164845",
          "modified": "1441164845",
          "shop_id": "32",
          "shop_sub_id": "0"
        }
      ]
    },
    "page": {
      "per_page": "20",
      "total_count": "2",
      "current_page": "0",
      "total_page": "1"
    }
  }
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  /><br  /><br  />

