## __创建用户__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/create
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| wxUser.open_id | 是 | Integer(11) | 微信open_id |
| userInfo.mobile | 否 | String(20) | 手机号 |
| userInfo.nickname | 是 | String(45) | 昵称 |
| userInfo.sex | 否 | Integer(3) | 性别（1：男，2：女，3：未知） |
| userInfo.province | 否 | String(30) | 所在省 |
| userInfo.city | 否 | String(30) | 所在市 |
| userInfo.country | 否 | String(50) | 所在国家 |
| userInfo.headimgurl | 否 | String(250) | 头像 |
| userInfo.shop_id | 是 | Integer(11) | 商家id |
| userInfo.shop_sub_id | 否 | Integer(11) | 商铺id |
| userInfo.belong_to_staff_id | 否 | Integer(11) | 归属员工id |
| userInfo.staff_id | 否 | Integer(11) | 绑定员工id |
| userInfo.group_id | 否 | Integer(11) | 分组id |
| userInfo.password | 否 | String(100) | 密码 |
| userInfo.type | 否 | Integer(3) | 类型（1：会员 2：粉丝）|
| userInfo.status | 否 | Integer(3) | 状态（1：正常，2：被冻结） |
| userInfo.member_refer | 否 | Integer(4) | 用户来源（1.关注、2.扫码、3.链接） |
| userInfo.scene_id | 否 | Integer(11) | 二维码参数id |
| userInfo.mpath | 否 | String(50) | 多级分销归属路径 |
| userInfo.mid | 否 | Integer(11) | 多级分销归属 |
| userInfo.sign_days | 否 | Integer(11) | 连续签到天数 |
| userInfo.sign_time | 否 | Integer(11) | 上次签到时间 |
| userInfo.is_subscribe | 否 | Integer(3) | 是否关注（1.是、2否 ）|
| userInfo.level_id | 否 | Integer(11) | 用户等级 |
| userInfo.point | 否 | Integer(11) | 会员积分 |
| userInfo.wsh_code | 否 | String(20) | 用户自定义用户名，可用于登陆 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "userInfo":{
            "sex":3,
            "shop_id":30,
            "shop_sub_id":187,
            "staff_id":0,
            "belong_to_staff_id":0,
            "login_count":0,
            "lastlogintime":0,
            "type":2,
            "status":1,
            "mid":0,
            "agent_id":0,
            "sign_days":0,
            "sign_time":0,
            "is_subscribe":1,
            "group_id":0,
            "point":0,
            "nickname":"ohei",
            "agent_path":null,
            "created":1440559519,
            "modified":1440559519,
            "deleted":1,
            "id":457
        },
        "WxUser":{
            "shop_sub_id":187,
            "open_id":"asfasdfasdf",
            "user_id":457,
            "shop_id":30,
            "id":75
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取用户列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/find-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| agent_id | 否 | Integer(11) | 代理商id |
| agent_path | 否 | Varchar(255) | 代理商路径 |
| nickname | 否 | Varchar(45) | 昵称 |
| group_id | 否 | Integer(11) | 分组id |
| createStart | 否 | Integer(11) | 搜索用户创建起始时间 |
| createEnd | 否 | Integer(11) | 搜索用户创建结束时间 |
| modifyStart | 否 | Integer(11) | 搜索用户最后修改起始时间 |
| modifyEnd | 否 | Integer(11) | 搜索用户最后修改结束时间 |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| ids | 否 | Array | 需要查找的id列表 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":[
        {
            "id":457,
            "mobile":null,
            "nickname":"ohei",
            "sex":3,
            "province":null,
            "city":null,
            "country":null,
            "headimgurl":null,
            "shop_id":30,
            "shop_sub_id":187,
            "staff_id":0,
            "belong_to_staff_id":0,
            "login_count":0,
            "lastloginip":null,
            "lastlogintime":0,
            "password":null,
            "type":2,
            "status":1,
            "member_refer":null,
            "scene_id":null,
            "mpath":null,
            "mid":0,
            "agent_id":0,
            "agent_path":null,
            "sign_days":0,
            "sign_time":0,
            "is_subscribe":1,
            "group_id":0,
            "level_id":null,
            "point":0,
            "wsh_code":null,
            "created":1440559519,
            "modified":1440559519,
            "deleted":1
        }
    ],
    "page":{
        "per_page":10,
        "total_count":1,
        "current_page":0,
        "total_page":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取用户信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/get
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| user_id | 是 | Integer(11) | 用户id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":457,
        "mobile":null,
        "nickname":"ohei",
        "sex":3,
        "province":null,
        "city":null,
        "country":null,
        "headimgurl":null,
        "shop_id":30,
        "shop_sub_id":187,
        "staff_id":0,
        "belong_to_staff_id":0,
        "login_count":0,
        "lastloginip":null,
        "lastlogintime":0,
        "password":null,
        "type":2,
        "status":1,
        "member_refer":null,
        "scene_id":null,
        "mpath":null,
        "mid":0,
        "agent_id":0,
        "agent_path":null,
        "sign_days":0,
        "sign_time":0,
        "is_subscribe":1,
        "group_id":0,
        "level_id":null,
        "point":0,
        "wsh_code":null,
        "created":1440559519,
        "modified":1440559519,
        "deleted":1,
        "fxMember":[

        ],
        "shopStaff":[

        ],
        "wxUsers":{
            "id":75,
            "open_id":"asfasdfasdf",
            "user_id":457,
            "shop_id":30,
            "shop_sub_id":187
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __修改用户分组__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/to-update
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| group_id | 是 | Integer(11) | 分组id |
| user_id | 是 | Integer(11) | 用户id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":457,
        "mobile":null,
        "nickname":"ohei",
        "sex":3,
        "province":null,
        "city":null,
        "country":null,
        "headimgurl":null,
        "shop_id":30,
        "shop_sub_id":187,
        "staff_id":0,
        "belong_to_staff_id":0,
        "login_count":0,
        "lastloginip":null,
        "lastlogintime":0,
        "password":null,
        "type":2,
        "status":1,
        "member_refer":null,
        "scene_id":null,
        "mpath":null,
        "mid":0,
        "agent_id":0,
        "agent_path":null,
        "sign_days":0,
        "sign_time":0,
        "is_subscribe":1,
        "group_id":11,
        "level_id":null,
        "point":0,
        "wsh_code":null,
        "created":1440559519,
        "modified":1440560711,
        "deleted":1,
        "wxUsers":{
            "id":75,
            "open_id":"asfasdfasdf",
            "user_id":457,
            "shop_id":30,
            "shop_sub_id":187
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __修改用户登陆信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/update-login
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| user_id | 是 | Integer(11) | 用户id |
| lastlogintime | 是 | Integer(11) | 登陆时间 |
| lastloginip | 否 | string | 登陆ip |
| login_count | 否 | Integer(11) | 登陆次数 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":457,
        "mobile":null,
        "nickname":"ohei",
        "sex":3,
        "province":null,
        "city":null,
        "country":null,
        "headimgurl":null,
        "shop_id":30,
        "shop_sub_id":187,
        "staff_id":0,
        "belong_to_staff_id":0,
        "login_count":1,
        "lastloginip":null,
        "lastlogintime":1436543468,
        "password":null,
        "type":2,
        "status":1,
        "member_refer":null,
        "scene_id":null,
        "mpath":null,
        "mid":0,
        "agent_id":0,
        "agent_path":null,
        "sign_days":0,
        "sign_time":0,
        "is_subscribe":1,
        "group_id":11,
        "level_id":null,
        "point":0,
        "wsh_code":null,
        "created":1440559519,
        "modified":1440568130,
        "deleted":1,
        "wxUsers":{
            "id":75,
            "open_id":"asfasdfasdf",
            "user_id":457,
            "shop_id":30,
            "shop_sub_id":187
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __修改用户分销员归属__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/update-mid
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| user_id | 是 | Integer(11) | 用户id |
| mid | 是 | Integer(11) | 分销员id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":457,
        "mobile":null,
        "nickname":"ohei",
        "sex":3,
        "province":null,
        "city":null,
        "country":null,
        "headimgurl":null,
        "shop_id":30,
        "shop_sub_id":187,
        "staff_id":0,
        "belong_to_staff_id":0,
        "login_count":1,
        "lastloginip":null,
        "lastlogintime":1436543468,
        "password":null,
        "type":2,
        "status":1,
        "member_refer":null,
        "scene_id":null,
        "mpath":null,
        "mid":35,
        "agent_id":0,
        "agent_path":null,
        "sign_days":0,
        "sign_time":0,
        "is_subscribe":1,
        "group_id":11,
        "level_id":null,
        "point":0,
        "wsh_code":null,
        "created":1440559519,
        "modified":1440568130,
        "deleted":1,
        "wxUsers":{
            "id":75,
            "open_id":"asfasdfasdf",
            "user_id":457,
            "shop_id":30,
            "shop_sub_id":187
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __通过openid获取用户__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/get-by-open-id
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| open_id | 是 | Varchar(100) | 微信open_id |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":75,
        "open_id":"asfasdfasdf",
        "user_id":457,
        "shop_id":30,
        "shop_sub_id":187,
        "userInfo":{
            "id":457,
            "mobile":null,
            "nickname":"ohei",
            "sex":3,
            "province":null,
            "city":null,
            "country":null,
            "headimgurl":null,
            "shop_id":30,
            "shop_sub_id":187,
            "staff_id":0,
            "belong_to_staff_id":0,
            "login_count":1,
            "lastloginip":null,
            "lastlogintime":1436543468,
            "password":null,
            "type":2,
            "status":1,
            "member_refer":null,
            "scene_id":null,
            "mpath":null,
            "mid":35,
            "agent_id":0,
            "agent_path":null,
            "sign_days":0,
            "sign_time":0,
            "is_subscribe":1,
            "group_id":11,
            "level_id":null,
            "point":0,
            "wsh_code":null,
            "created":1440559519,
            "modified":1440568406,
            "deleted":1,
            "fxMember":[

            ]
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __关注用户__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/subscribe
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| open_id | 是 | Varchar(100) | 微信open_id |
| mobile | 否 | String(20) | 手机号 |
| nickname | 否 | String(45) | 昵称 |
| sex | 否 | Integer(3) | 性别（1：男，2：女，3：未知） |
| province | 否 | String(30) | 所在省 |
| city | 否 | String(30) | 所在市 |
| country | 否 | String(50) | 所在国家 |
| headimgurl | 否 | String(250) | 头像 |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| staff_id | 否 | Integer(11) | 员工id |
| group_id | 否 | Integer(11) | 分组id |
| password | 否 | String(100) | 密码 |
| type | 否 | Integer(3) | 类型（1：会员 2：粉丝）|
| status | 否 | Integer(3) | 状态（1：正常，2：被冻结） |
| scene_id | 否 | Integer(11) | 二维码参数id |
| mpath | 否 | String(50) | 多级分销归属路径 |
| mid | 否 | Integer(11) | 多级分销归属 |
| level_id | 否 | Integer(11) | 用户等级 |
| point | 否 | Integer(11) | 会员积分 |
| wsh_code | 否 | String(20) | 用户自定义用户名，可用于登陆 |
| lastloginip | 否 | String | 最后登录ip |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "WxUser":{
            "id":75,
            "open_id":"asfasdfasdf",
            "user_id":457,
            "shop_id":30,
            "shop_sub_id":187,
            "userInfo":{
                "id":457,
                "mobile":null,
                "nickname":"ohei",
                "sex":3,
                "province":null,
                "city":null,
                "country":null,
                "headimgurl":null,
                "shop_id":30,
                "shop_sub_id":187,
                "staff_id":0,
                "belong_to_staff_id":0,
                "login_count":1,
                "lastloginip":null,
                "lastlogintime":1436543468,
                "password":null,
                "type":2,
                "status":1,
                "member_refer":null,
                "scene_id":null,
                "mpath":null,
                "mid":35,
                "agent_id":0,
                "agent_path":null,
                "sign_days":0,
                "sign_time":0,
                "is_subscribe":1,
                "group_id":11,
                "level_id":null,
                "point":0,
                "wsh_code":null,
                "created":1440559519,
                "modified":1440569128,
                "deleted":1
            }
        },
        "userInfo":{
            "id":457,
            "mobile":null,
            "nickname":"ohei",
            "sex":3,
            "province":null,
            "city":null,
            "country":null,
            "headimgurl":null,
            "shop_id":30,
            "shop_sub_id":187,
            "staff_id":0,
            "belong_to_staff_id":0,
            "login_count":1,
            "lastloginip":null,
            "lastlogintime":1436543468,
            "password":null,
            "type":2,
            "status":1,
            "member_refer":null,
            "scene_id":null,
            "mpath":null,
            "mid":35,
            "agent_id":0,
            "agent_path":null,
            "sign_days":0,
            "sign_time":0,
            "is_subscribe":1,
            "group_id":11,
            "level_id":null,
            "point":0,
            "wsh_code":null,
            "created":1440559519,
            "modified":1440569128,
            "deleted":1
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __取消关注__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/cancel-subscribe
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| open_id | 是 | Varchar(100) | 微信open_id |
| shop_id | 是 | Integer(11) | 商家id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "WxUser":{
            "id":75,
            "open_id":"asfasdfasdf",
            "user_id":457,
            "shop_id":30,
            "shop_sub_id":187,
            "userInfo":{
                "id":457,
                "mobile":null,
                "nickname":"ohei",
                "sex":3,
                "province":null,
                "city":null,
                "country":null,
                "headimgurl":null,
                "shop_id":30,
                "shop_sub_id":187,
                "staff_id":0,
                "belong_to_staff_id":0,
                "login_count":1,
                "lastloginip":null,
                "lastlogintime":1436543468,
                "password":null,
                "type":2,
                "status":1,
                "member_refer":null,
                "scene_id":null,
                "mpath":null,
                "mid":35,
                "agent_id":0,
                "agent_path":null,
                "sign_days":0,
                "sign_time":0,
                "is_subscribe":2,
                "group_id":11,
                "level_id":null,
                "point":0,
                "wsh_code":null,
                "created":1440559519,
                "modified":1440569128,
                "deleted":1
            }
        },
        "userInfo":{
            "id":457,
            "mobile":null,
            "nickname":"ohei",
            "sex":3,
            "province":null,
            "city":null,
            "country":null,
            "headimgurl":null,
            "shop_id":30,
            "shop_sub_id":187,
            "staff_id":0,
            "belong_to_staff_id":0,
            "login_count":1,
            "lastloginip":null,
            "lastlogintime":1436543468,
            "password":null,
            "type":2,
            "status":1,
            "member_refer":null,
            "scene_id":null,
            "mpath":null,
            "mid":35,
            "agent_id":0,
            "agent_path":null,
            "sign_days":0,
            "sign_time":0,
            "is_subscribe":2,
            "group_id":11,
            "level_id":null,
            "point":0,
            "wsh_code":null,
            "created":1440559519,
            "modified":1440569128,
            "deleted":1
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __用户积分流水列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/find-point-log
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| uid | 否 | Integer(11) | 用户id |
| type | 否 | Integer(11) | 积分类型（1.消费赠送、2.消费抵扣现金、3.积分兑换、4.签到赠送、5.抽奖赠送 ）|
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":[
        {
            "id":142,
            "uid":454,
            "points":222,
            "change":222,
            "source":"抽奖活动",
            "shop_id":30,
            "shop_sub_id":0,
            "type":5,
            "created":1440499232
        },
        {
            "id":141,
            "uid":454,
            "points":0,
            "change":222,
            "source":"抽奖活动",
            "shop_id":30,
            "shop_sub_id":0,
            "type":5,
            "created":1440491443
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

## __用户积分流水明细__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/get-point-log
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 积分流水id |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| uid | 否 | Integer(11) | 用户id |
| type | 否 | Integer(11) | 积分类型（1.消费赠送、2.消费抵扣现金、3.积分兑换、4.签到赠送、5.抽奖赠送 ）|
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":141,
        "uid":454,
        "points":0,
        "change":222,
        "source":"抽奖活动",
        "shop_id":30,
        "shop_sub_id":0,
        "type":5,
        "created":1440491443
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __补全用户归属信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/to-update-belong
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| user_id | 是 | Integer(11) | 用户id |
| shop_id | 是 | Integer(11) | 店铺id |
| ids | 否 | Array | 用户id列表 |
| agent_id | 否 | Integer(11) | 代理商id |
| agent_path | 否 | varchar(255) | 代理商路径，如：/26/ |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| belong_to_staff_id | 否 | Integer(11) | 用户归属员工id |
| mid | 否 | Integer(11) | 多级分销归属 |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "id": 824,
    "mobile": null,
    "nickname": "Oh Wennio Chien",
    "sex": 2,
    "province": "首尔",
    "city": null,
    "country": "韩国",
    "headimgurl": "http://wx.qlogo.cn/mmopen/3U3X9zfvGnH6y6GPuxa6Ziat6JheAy4xAVhVJgJmPD2hiaEic7XF6ib4hzIa6JK6EuT1c8G37B17OxjgMia8ibAA9E1z2iafljOBtOD/0",
    "shop_id": 30,
    "shop_sub_id": "205",
    "staff_id": 0,
    "belong_to_staff_id": "",
    "login_count": 0,
    "lastloginip": null,
    "lastlogintime": 0,
    "password": null,
    "type": 2,
    "status": 1,
    "member_refer": null,
    "scene_id": null,
    "mpath": null,
    "mid": "",
    "agent_id": 26,
    "agent_path": "/26/",
    "sign_days": 0,
    "sign_time": 0,
    "is_subscribe": 1,
    "group_id": 1,
    "level_id": null,
    "point": 0,
    "wsh_code": null,
    "created": 1452612741,
    "modified": 1453171447,
    "deleted": 1,
    "wxUsers": {
      "id": 317,
      "open_id": "obUMWuJt9V-Jsqdth87uU5NgTOuU",
      "user_id": 824,
      "shop_id": 30,
      "shop_sub_id": 0
    }
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

