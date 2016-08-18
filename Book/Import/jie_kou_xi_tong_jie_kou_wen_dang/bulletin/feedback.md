
## __创建反馈__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/bulletin/create-feedback
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| title | 是 | String(250) | 标题 |
| feedback_type_id | 是 | Integer(11) |  反馈分类id |
| shop_id | 是 | Integer(11) |  商户id |
| creator | 是 | String(20) | 创建者（员工ID） |
| issue| 是 | String | 内容 |
| issue_img| 否 | String | 用户上传反馈问题图片（多个逗号分隔） |
| mobile| 否 | String | 意见反馈人手机号 |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "replied": 2,
    "shop_id": 30,
    "title": "1606301",
    "feedback_type_id": 10,
    "creator": "369",
    "mobile": "13800138000",
    "issue": "1111",
    "issue_img": "1",
    "created": 1467219630,
    "deleted": 1,
    "id": 69
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __修改反馈__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/bulletin/update-feedback
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 反馈id |
| title | 是 | String(250) | 标题 |
| shop_id | 是 | Integer(11) |  商户id |
| creator | 是 | String(20) | 创建者 |
| issue| 是 | String | 内容 |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "shop_id": "5",
        "creator": "xxx",
        "issue": "s;dfj;lksdnfksdnfk",
        "created": 1437618649,
        "deleted": 1,
        "id": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取反馈详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/bulletin/get-feedback
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 反馈id |
| shop_id | 是 | Integer(11) |  商户id |
| creator | 否 | String(20) | 创建者 |
| deleted | 否 | Integer(11) | 状态 |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 1,
        "shop_id": 5,
        "creator": "xxx",
        "issue": "s;dfj;sdfsdfsafdsf",
        "created": 1437618649,
        "deleted": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取反馈列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/bulletin/find-feedback
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) |  商户id |
| creator | 否 | String(20) | 创建者 |
| deleted | 否 | Integer(11) | 状态 |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": [
        {
            "id": 1,
            "shop_id": 5,
            "creator": "xxx",
            "issue": "s;dfj;sdfsdfsafdsf",
            "created": 1437618649,
            "deleted": 1
        }
    ],
    "page": {
        "per_page": 20,
        "total_count": 1,
        "current_page": 0,
        "total_page": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __创建反馈回复__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/bulletin/create-feedback-reply
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| pid | 是 | Integer(11) |  回复的reply的id（当回复feedback时pid=0，其他的为相应feedback-reply的id） |
| feedback_id | 是 | Integer(11) |  反馈id |
| reply_type | 是 | Integer(11) | 回复类型（1.商家回复、2.管理员回复）  |
| shop_id | 是 | Integer(11) |  商户id |
| creator | 是 | String(20) | 创建者 |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "replied": 2,
        "pid": 0,
        "feedback_id": "1",
        "reply": "j;sdjf;lksdjkl;fkjdf",
        "is_reply": 2,
        "shop_id": 5,
        "creator": "xxx2",
        "created": 1437621301,
        "deleted": 1,
        "id": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __修改反馈回复__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/bulletin/update-feedback-reply
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 反馈回复id |
| shop_id | 是 | Integer(11) |  商户id |
| creator | 是 | String(20) | 创建者 |
| reply| 是 | String | 内容 |

<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 4,
        "pid": 0,
        "feedback_id": 1,
        "reply": "商户回复edit",
        "reply_type": 2,
        "replied": 1,
        "shop_id": 5,
        "creator": "xxx1",
        "created": 1437622645,
        "deleted": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取反馈回复详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/bulletin/get-feedback-reply
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 反馈回复id |
| pid | 是 | Integer(11) |  父级id |
| replied | 是 | Integer(11) | 是否已回复(1.是、2.否)  |
| feedback_id | 是 | Integer(11) |  反馈id |
| reply_type | 是 | Integer(11) | 回复类型（1.商家回复、2.管理员回复）  |
| shop_id | 是 | Integer(11) |  商户id |
| creator | 是 | String(20) | 创建者 |
| deleted | 否 | Integer(11) | 状态 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 4,
        "pid": 0,
        "feedback_id": 1,
        "reply": "商户回复edit",
        "reply_type": 2,
        "replied": 1,
        "shop_id": 5,
        "creator": "xxx1",
        "created": 1437622645,
        "deleted": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取反馈回复列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/bulletin/find-feedback
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| pid | 是 | Integer(11) |  父级id |
| replied | 是 | Integer(11) | 是否已回复(1.是、2.否)  |
| feedback_id | 是 | Integer(11) |  反馈id |
| reply_type | 是 | Integer(11) | 回复类型（1.商家回复、2.管理员回复）  |
| shop_id | 是 | Integer(11) |  商户id |
| creator | 是 | String(20) | 创建者 |
| deleted | 否 | Integer(11) | 状态 |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": [
        {
            "id": 4,
            "pid": 0,
            "feedback_id": 1,
            "reply": "商户回复edit",
            "reply_type": 2,
            "replied": 1,
            "shop_id": 5,
            "creator": "xxx1",
            "created": 1437622645,
            "deleted": 1
        },
        {
            "id": 5,
            "pid": 4,
            "feedback_id": 1,
            "reply": "商户回复",
            "reply_type": 1,
            "replied": 2,
            "shop_id": 5,
            "creator": "xxx1",
            "created": 1437623353,
            "deleted": 1
        }
    ],
    "page": {
        "per_page": 20,
        "total_count": 2,
        "current_page": 0,
        "total_page": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __创建意见反馈类型__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/bulletin/create-feedback-type
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| name | 是 | String(100) | 帮助类型名称 |
| type | 是 | Integer(11) | 类型：1微商户后台 2APP |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 10,
        "name": "闪退",
        "type": 2,
        "created": 1467211886,
        "modified": 1467211886
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __修改意见反馈类型__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/bulletin/update-feedback-type
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 帮助类型id |
| name | 否 | String(100) | 帮助类型名称 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 10,
        "name": "闪现",
        "type": 2,
        "created": 1467211886,
        "modified": 1467217678
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取反馈类型明细__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/bulletin/get-feedback-type
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 帮助类型id |
| name | 否 | String(100) | 帮助类型名称 |
<br  /><br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 1,
        "name": "商品",
        "created": 123456,
        "modified": 123456
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取帮助类型列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/bulletin/find-feedback-type
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| name | 否 | String(100) | 帮助类型名称 |
| type | 否 | Integer(11) | 类型：1微商户后台 2APP |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
  "errcode": 0,
  "errmsg": "ok",
  "data": [
    {
      "id": 10,
      "name": "闪退",
      "type": 2,
      "created": 1467211886,
      "modified": 1467211886
    },
    {
      "id": 11,
      "name": "卡顿",
      "type": 2,
      "created": 1467211886,
      "modified": 1467211886
    },
    {
      "id": 12,
      "name": "黑屏",
      "type": 2,
      "created": 1467211886,
      "modified": 1467211886
    },
    {
      "id": 13,
      "name": "死机",
      "type": 2,
      "created": 1467211886,
      "modified": 1467211886
    },
    {
      "id": 14,
      "name": "界面错位",
      "type": 2,
      "created": 1467211886,
      "modified": 1467211886
    },
    {
      "id": 15,
      "name": "消息推送",
      "type": 2,
      "created": 1467211886,
      "modified": 1467211886
    },
    {
      "id": 16,
      "name": "业绩统计",
      "type": 2,
      "created": 1467211886,
      "modified": 1467211886
    },
    {
      "id": 17,
      "name": "版本更新",
      "type": 2,
      "created": 1467211886,
      "modified": 1467211886
    },
    {
      "id": 18,
      "name": "其他",
      "type": 2,
      "created": 1467211886,
      "modified": 1467211886
    }
  ],
  "page": {
    "per_page": 20,
    "total_count": 9,
    "current_page": 0,
    "total_page": 1
  }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
