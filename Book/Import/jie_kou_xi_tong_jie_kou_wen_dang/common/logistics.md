请求地址：/common/find-logistics
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| 无需参数 |  |  |  | |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":[
        {
            "apicode": "ems",
            "text": "中国邮政EMS",
            "key": 1
        },
        {
            "apicode": "shentong",
            "text": "申通快递",
            "key": 2
        },
    ]
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
