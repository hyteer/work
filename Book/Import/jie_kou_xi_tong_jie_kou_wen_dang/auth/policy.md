## __获取权限策略列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/find-policy
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php

```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __获取权限策略详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/auth/get-policy
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id|是|Integer(11)|策略ID|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 1,
        "name": "policy1",
        "remark": "mark"
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
