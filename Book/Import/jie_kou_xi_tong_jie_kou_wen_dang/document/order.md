## __添加普通订单__
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
|tag_id|否|Integer(11)|标签表外键|
|file_cdn_path|是|varchar(250)|文件路径cdn路径|
|file_type|是|Integer(11)|文件类型（1.图片、2.语音、3.音乐 、4.视频、5.word、6.excel）|
|shop_id|是|Integer(11)|商家id|
|shop_sub_id|是|Integer(11)|店铺id|
<br  />
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

