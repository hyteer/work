## __创建用户等级__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/create-level
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| name | 是 | String(50) | 等级名称 |
| level_exp | 是 | Integer(11) | 当前等级经验经验 |
| level_img_id | 是 | String(20) | 用户等级图标id,document_lib表外键 |
| user_level_policy_ids | 否 | String(50) | 等级对应的策略集 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "shop_sub_id":187,
        "name":"一级棒",
        "level_exp":10,
        "level_img_id":"346",
        "shop_id":30,
        "created":1440495629,
        "deleted":1,
        "id":3
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取用户等级列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/find-level-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| page | 否 | Integer(11) | 分页 |
| count | 否 | Integer(11) | 每页总数 |
| sortStr | 否 | Varchar(50) | 排序 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":[
        {
            "id":3,
            "name":"一级棒",
            "level_img_id":"346",
            "level_exp":10,
            "shop_id":30,
            "shop_sub_id":187,
            "created":1440495629,
            "user_level_policy_ids":null,
            "modified":null,
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

## __获取用户等级信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/get-level
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| level_id | 是 | Integer(11) | 等级id |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":3,
        "name":"一级棒",
        "level_img_id":"346",
        "level_exp":10,
        "shop_id":30,
        "shop_sub_id":187,
        "created":1440495629,
        "user_level_policy_ids":null,
        "modified":null,
        "deleted":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __修改用户等级信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/wxuser/update-level
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| level_id | 是 | Integer(11) | 等级id |
| name | 否 | String(50) | 等级名称 |
| level_exp | 否 | Integer(11) | 当前等级经验经验 |
| level_img_id | 否 | String(20) | 用户等级图标id,document_lib表外键 |
| user_level_policy_ids | 否 | String(50) | 等级对应的策略集 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":3,
        "name":"一级棒棒",
        "level_img_id":"347",
        "level_exp":20,
        "shop_id":30,
        "shop_sub_id":187,
        "created":1440495629,
        "user_level_policy_ids":null,
        "modified":1440497438,
        "deleted":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
