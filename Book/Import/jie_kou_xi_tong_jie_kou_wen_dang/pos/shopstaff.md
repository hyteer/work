## __pos员工登录__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/staff/shop-staff-login
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| pin_code | 是 | String(32) | pin_code |
| user_name | 是 | String(20) | 登录用户名 |
| password | 是 | String(32) | 登录密码 |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok"
    "data": {
        "id":132 , "user_name":"14321372134720" , "password":"68a91563789fc74109b0ddb5f50939ac" , "real_name":"范德萨发松岛枫" , "role_id":"123123" , "mobile":"1321213" , "email":"213145" , "shop_sub_id":"48" , "shop_id":"5" , "ewm_img":"4564646" , "scene_id":"5416546" , "last_login":0 , "path":"14654165416" , "created":1432374621 , "modified":1432374621 , "deleted":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
