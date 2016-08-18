# 打印机设备
## __同步初始打印机设备信息__
* **注意：这里仅仅是同步信息，不是走接口同步，即由boss后台分配一天机器后需同步这台机器的信息（初始）**

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/sync-printer-clients
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| pin_code|是|varchar(50)|pin_code码|
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









## __编辑打印机__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/update-printer-clients
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| id | 是 | Integer(11) | 设备id |
| factory | 是 | Integer(4) | 打印机厂商：1为微信创 |
| printer_template_id | 是 | Integer(11) | 模板id |
| client_type | 是 | Integer(4) | 设备类型,1:V-box四格版,2:V-box巨屏版,3:M-box双屏A版,4:M-box双屏B版,5:M-box三屏A版,6:M-box三屏B版 |
| print_type | 是 | Integer(4) | 打印类型(1明信卡;2文字卡;3小广告卡;4广告卡) |
| user_limit | 是 | varchar(100) | 用户限制（json） |
| device_limit | 是 | varchar(100) | 设备限制（json） |
| wx_qrcode | 是 | varchar(250) | 微信二维码图片地址 |
| wx_qrscene | 是 | varchar(10) | 带参数二维码值 |
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














## __获取打印机回复信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/find-printer-responses
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| factory | 是 | Integer(4) | 打印机厂商：1为微信创 |
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







## __编辑打印机回复信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/edit-printer-responses
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| factory | 是 | Integer(4) | 打印机厂商：1为微信创 |
| welcome_word|是|varchar(255)|回复：欢迎语|
| input_code|是|varchar(255)|回复：输入验证码提示语|
| input_error|是|varchar(255)|回复：验证码错误提示语|
| input_img|是|varchar(255)|回复：发送图文提醒|
| printing|是|varchar(255)|回复：等待打印提示语|
| app_error|是|varchar(255)|回复：图片上传错误提示语|
| out_msg|是|varchar(255)|回复：退出打印提示|
| user_limit_msg|是|varchar(255)|回复：达到用户打印限制|
| device_limit_msg|是|varchar(255)|回复：达到设备打印限制|
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












## __获取某个键的打印机回复信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/get-printer-response-value
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| factory | 是 | Integer(4) | 打印机厂商：1为微信创 |
| key|是|varchar(50)|需要查询的键值，例如input_code，input_error|
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data":"请输入微信验证码"
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />







## __设备绑定模板__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/bind-printer-templates
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| id | 是 | Integer(11) | 设备id |
| printer_template_id | 是 | Integer(11) | 模板id |
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







## __检测打印限制__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/check-user-print-limit
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| open_id|是|varchar(28)|openid|
| printer_client_id | 是 | Integer(11) | 设备id |
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







## __走接口打印图片__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/do-print
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| printer_client_id | 是 | Integer(11) | 设备id |
| open_id|是|varchar(28)|openid|
| factory | 是 | Integer(4) | 打印机厂商：1为微信创 |
| pin_code | 是 |varchar(28)|打印机pincode|
| code | 是 |Integer(11)|打印验证码|
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
errcode：123204005表示验证码错误
```php
{
    "errcode": 0,
    "errmsg": "ok"
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />








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
<br  /><br  />









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
<br  /><br  />






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
<br  /><br  />



# 打印机模板
## __创建模板__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/create-printer-templates
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| title|是|varchar(50)|模板标题|
| material_urls|是|text|json格式，不同类型的设备参数不同。例如{"mainurls":"1;3","mainurls_type":"1","logourl":"4","newplayurls":"3","touchurl":"baidu.com"}，每个键对应的值是上传素材后，接口返回的id|
| material_api_ids|是|varchar(255)|使用到的所有素材上传到接口那边返回的id,以逗号隔开，以逗号开头,对应上面的值，则是,1,3,4,|
| shop_id|是|Integer(11)|商铺id|
| shop_sub_id|否|Integer(11)|分店id|
| type|是|Integer(4)|模板适用的设备类型，微信创（1巨屏版;2四格版;3双屏A版;4双屏B版;5三屏A版;6三屏B版）|
| factory | 是 | Integer(4) | 打印机厂商，1为微信创 |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
            "id": 1,
            "title": "模板1",
            "material_urls": "json格式",
            "type": 1,
            "shop_id": 30,
            "shop_sub_id": 0,
            "created": 1440829190,
            "factory": 1
        }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />














## __模板列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/find-printer-templates
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| title|否|varchar(50)|模板标题|
| shop_sub_id|否|Integer(11)|分店id|
| type|否|Integer(4)|模板适用的设备类型，微信创（1巨屏版;2四格版;3双屏A版;4双屏B版;5三屏A版;6三屏B版）|
| factory | 是 | Integer(4) | 打印机厂商，1为微信创 |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取2000个
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": "0",
    "errmsg": "ok",
    "data": [
         {
        "id": "1",
        "title": "测试模板1",
        "material_urls": "{\"mainurls\":\"12;13\",\"mainurls_type\":\"1\",\"logourl\":\"13\",\"newplayurls\":\"13\",\"touchurl\":\"baidu.com\"}",
        "material_api_ids": ",12,13,",
        "type": "1",
        "shop_id": "32",
        "shop_sub_id": "0",
        "created": "1441174563",
        "modified": "1441174563",
        "factory": "1",
        "api_template_id": "3",
        "api_template_title": "6dfa8a85-c5f5-9ab3-0cc4-0f424210e186"
      }
    ],
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








## __获取模板详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/get-printer-templates
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|模板id|
| shop_id|是|Integer(11)|商铺id|
| shop_sub_id|否|Integer(11)|分店id|
##### 返回说明
| 键 | 说明 |
| -- | -- |
| master|对应的模板详情数据|
| materials|模板里面使用到的素材列表|
| hasClient|该模板是否有设备在使用，1为是，0为没有|
| clientType|所有的设备类型列表|
| cateClientType|厂商设备类型分类列表|
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": "0",
    "errmsg": "ok",
    "data": {
      "master": {
        "id": "1",
        "title": "测试模板1",
        "material_urls": "{\"mainurls\":\"12;13\",\"mainurls_type\":\"1\",\"logourl\":\"13\",\"newplayurls\":\"13\",\"touchurl\":\"baidu.com\"}",
        "material_api_ids": ",12,13,",
        "type": "1",
        "shop_id": "32",
        "shop_sub_id": "0",
        "created": "1441174563",
        "modified": "1441174563",
        "factory": "1",
        "api_template_id": "3",
        "api_template_title": "6dfa8a85-c5f5-9ab3-0cc4-0f424210e186"
      },
      "materials":[
      },
      "hasClient": "0",
      "clientType": [
          {
            "id": "1",
            "name": "V-box巨屏版"
          },
          {
            "id": "2",
            "name": "V-box四格版"
          },
          {
            "id": "3",
            "name": "M-box双屏A版"
          },
          {
            "id": "4",
            "name": "M-box双屏B版"
          },
          {
            "id": "5",
            "name": "M-box三屏A版"
          },
          {
            "id": "6",
            "name": "M-box三屏B版"
          }
        ],
      "cateClientType": [
          {
            "name": "小打印机",
            "types": [
                "1",
                "2"
              ]
          },
          {
            "name": "大打印机",
            "types": [
                "3",
                "4",
                "5",
                "6"
              ]
          }
        ]
      }

  }
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __删除模板__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/del-printer-templates
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| id|是|Integer(11)|模板id|
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






## __修改模板__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/update-printer-templates
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|模板ID|
| title|是|varchar(50)|模板标题|
| material_urls|是|text|json格式，不同类型的设备参数不同。例如{"mainurls":"1;3","mainurls_type":"1","logourl":"4","newplayurls":"3","touchurl":"baidu.com"}，每个键对应的值是上传素材后，接口返回的id|
| material_api_ids|是|varchar(255)|使用到的所有素材上传到接口那边返回的id,以逗号隔开，以逗号开头,对应上面的值，则是,1,3,4,|
| shop_id|是|Integer(11)|商铺id|
| shop_sub_id|否|Integer(11)|分店id|
| type|是|Integer(4)|模板适用的设备类型，微信创（1巨屏版;2四格版;3双屏A版;4双屏B版;5三屏A版;6三屏B版）|
| factory | 是 | Integer(4) | 打印机厂商，1为微信创 |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
            "id": 1,
            "title": "模板1",
            "material_urls": "json格式",
            "type": 1,
            "shop_id": 30,
            "shop_sub_id": 0,
            "created": 1440829190,
            "factory": 1
        }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)












## __添加打印机统计数__
* **注意：目前打印机接口的统计是内部统计的，没走接口**

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/add-print-to-statistics
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| printer_client_id|是|Integer(11)|打印机设备id|
| s_date|否|date|日期，默认是当天，格式是2015-09-06|
| free_num|否|Integer(11)|免费打印数添加个数，默认为0|
| code_num|否|Integer(11)|付费码打印数添加个数，默认为0|
| code_amount|否|Integer(11)|付费码金额添加数,单位为分，默认为0|
| pay_num|否|Integer(11)|微信支付打印数添加个数，默认为0|
| pay_amount|否|Integer(11)|微信支付金额添加数,单位为分，默认为0|
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
     "data": {
      "id": "1",
      "s_date": "2015-09-06",
      "free_num": "4",
      "code_num": "0",
      "code_amount": "0",
      "pay_num": "0",
      "pay_amount": "0",
      "printer_client_id": "1"
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />









## __商家打印机统计数__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/count-printer-statistics
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| shop_sub_id|否|Integer(11)|分店id|
| printer_client_id|否|Integer(11)|打印机设备id|
| start|否|date|统计开始日期，包括当前值天，格式是2015-09-06|
| end|否|date|统计截止日期，包括当前值天，格式是2015-09-06|
| factory | 是 | Integer(4) | 打印机厂商，1为微信创 |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
     "data": {
      "free_num": "4",
      "code_num": "0",
      "pay_amount": "0",
      "pay_num": "0",
      "code_amount": "0"
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />








## __商家所有打印机日统计列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/shop-printer-statistics
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| shop_sub_id|否|Integer(11)|分店id|
| start|否|date|统计开始日期，包括当前值天，格式是2015-09-06|
| end|否|date|统计截止日期，包括当前值天，格式是2015-09-06|
| factory | 是 | Integer(4) | 打印机厂商，1为微信创 |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取2000个
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
     "data": [
     {
        "s_date": "2015-09-06",
        "free_num": "4",
        "code_num": "0",
        "pay_amount": "0",
        "pay_num": "0",
        "code_amount": "0"
      }
    ],
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









## __按商家打印机统计列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/client-printer-statistics
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| shop_sub_id|否|Integer(11)|分店id|
| keyword|否|string|搜索门店或设备号|
| s_date|否|date|仅统计当前日期，格式是2015-09-06|
| start|否|date|统计开始日期，包括当前值天，格式是2015-09-06|
| end|否|date|统计截止日期，包括当前值天，格式是2015-09-06|
| factory | 是 | Integer(4) | 打印机厂商，1为微信创 |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取2000个
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
     "data": [
       {
        "printer_client_id": "2",
        "device_code": "VD00315",
        "shop_name": "xx",
        "shop_sub_name": "
        ",
        "free_num": "4",
        "code_num": "0",
        "pay_amount": "0",
        "pay_num": "0",
        "code_amount": "0"
      }
    ],
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










## __设备日统计列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/find-printer-statistics
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| printer_client_id|是|Integer(11)|设备id|
| start|否|date|统计开始日期，包括当前值天，格式是2015-09-06|
| end|否|date|统计截止日期，包括当前值天，格式是2015-09-06|
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取2000个
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
     "data": [
     {
        "id": "1",
        "s_date": "2015-09-06",
        "free_num": "4",
        "code_num": "0",
        "code_amount": "0",
        "pay_num": "0",
        "pay_amount": "0",
        "printer_client_id": "2"
      }
    ],
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







## __创建打印机队列__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/create-printer-lists
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| shop_sub_id|否|Integer(11)|分店id|
| open_id|是|varchar(28)|open_id|
| printer_client_id|是|Integer(11)|设备id|
| type | 是 | Integer(4) | 队列类型，1为免费打印，2为微信支付 |
| status | 是 | varchar(20) | 队列状态，‘input_img’ 等待图片状态（初始状态）|
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
             "shop_id": "32",
              "shop_sub_id": "0",
              "type": "1",
              "deleted": "1",
              "open_id": "2321",
              "status": "input_img",
              "printer_client_id": "2",
              "created": "1441594637",
              "modified": "1441594637",
              "id": "2"
        }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />








## __修改打印机队列信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/update-printer-lists
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| id|是|Integer(11)|队列id|
| pic|否|varchar(255)|用户上传的图片地址|
| print_pic|否|varchar(255)|最终打印的图片地址|
| deleted | 否 | Integer(4) | 3表示队列完成 |
| status | 否 | varchar(20) | 队列状态，‘input_img’ 等待图片状态（初始状态），‘input_cut’询问裁剪状态，‘input_write’等待输入文字状态，‘input_code’等待验证码状态，‘input_code_running’正在处理状态，等待图片合成，‘finish’完成状态|
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
          "id": "1",
          "open_id": "232",
          "printer_client_id": "2",
          "shop_id": "32",
          "shop_sub_id": "0",
          "status": "input_img",
          "type": "1",
          "created": "1441594578",
          "modified": "1441594767",
          "pic": "http://www.yiichina.com/images/logo.png",
          "print_pic": "",
          "ext": "",
          "deleted": "1"
        }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />










## __获取打印机队列信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/printer/get-printer-lists
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| id|否|Integer(11)|队列id|
| open_id|否|varchar(28)|open_id|
| ext|否|varchar(255)|额外信息|
| print_pic|否|varchar(255)|最终打印的图片地址|
| printer_client_id | 否 | Integer(11) | 设备id |
| status | 是 | varchar(20) | 队列状态，‘input_img’ 等待图片状态（初始状态），‘input_cut’询问裁剪状态，‘input_write’等待输入文字状态，‘input_code’等待验证码状态，‘input_code_running’正在处理状态，等待图片合成，‘finish’完成状态|
| withClient | 否 | Integer(4) | 是否同时返回设备信息，1是，2不是，默认不是 |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": "0",
    "errmsg": "ok",
    "data": {
        "id": "1",
        "open_id": "232",
        "printer_client_id": "2",
        "shop_id": "32",
        "shop_sub_id": "0",
        "status": "input_img",
        "type": "1",
        "created": "1441594578",
        "modified": "1441594767",
        "pic": "http://www.yiichina.com/images/logo.png",
        "print_pic": "",
        "ext": " ",
        "deleted": "1",
        "printerClient": {
            "id": "2",
            "device_id": "1",
            "pin_code": "1408042015090110000800000142",
            "device_code": "VD00315",
            "title": " ",
            "user_limit": " ",
            "device_limit": " ",
            "bottom_img": "",
            "wx_qrcode": "",
            "wx_qrscene": " ",
            "printer_template_id": "3",
            "shop_id": "32",
            "shop_sub_id": "32",
            "created": "1441077954",
            "modified": "1441527651",
            "client_type": "1",
            "print_type": "1",
            "pay_type": "1",
            "ext": " ",
            "factory": "1",
            "sync": "1",
            "deleted": "1"
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


