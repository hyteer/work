
## __创建杂志表单__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/create-magazine-form
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| magazine_id | 是 | Integer(11) | 杂志id |
| title | 是 | String(30) | 表单名称 |
| content | 是 | Text | 表单内容json |
| button | 是 | String(15) | 表单按钮名称 |
<br  /><br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "magazine_id":3,
        "title":"表单2",
        "shop_id":30,
        "content":"asfafdfasdfasdf",
        "button":"提交",
        "created":1441160406,
        "modified":1441160406,
        "deleted":1,
        "id":"2"
    }
}
```

错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取杂志表单列表__


##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/find-magazine-form
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| magazine_id | 否 | Integer(11) | 杂志id |
| title | 否 | String(30) | 表单名称 |
| createStart | 否 | Integer(11) | 表单创建起始时间 |
| createEnd | 否 | Integer(11) | 表单创建结束时间 |
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
            "id":"1",
            "magazine_id":"3",
            "title":"表单1",
            "content":"asfafdfasdfasdf",
            "button":"提交",
            "shop_id":"30",
            "created":"1441160354",
            "modified":"1441160354",
            "deleted":"1",
            "num":"0",
            "magazine_name":"棒棒哒"
        },
        {
            "id":"2",
            "magazine_id":"3",
            "title":"表单2222",
            "content":"asfafdfasdfasdf22222",
            "button":"提交",
            "shop_id":"30",
            "created":"1441160406",
            "modified":"1441160744",
            "deleted":"1",
            "num":"0",
            "magazine_name":"棒棒哒"
        }
    ],
    "page":{
        "per_page":20,
        "total_count":2,
        "current_page":0,
        "total_page":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __获取杂志表单详情__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/get-magazine-form
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 表单id |
| shop_id | 是 | Integer(11) | 店铺id |
| magazine_id | 否 | Integer(11) | 杂志id |
<br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":"1",
        "magazine_id":"3",
        "title":"表单1",
        "content":"asfafdfasdfasdf",
        "button":"提交",
        "shop_id":"30",
        "created":"1441160354",
        "modified":1441160354,
        "deleted":1,
        "magazine":{
            "id":"3",
            "name":"棒棒哒",
            "category_id":"1",
            "type":1,
            "share_message_id":944,
            "face_document_id":346,
            "music_document_id":347,
            "pv":10,
            "version":"2.1.7",
            "shop_id":"30",
            "created":1441077746,
            "modified":1441090113,
            "deleted":1
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __修改杂志表单__

##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/update-magazine-form
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| id | 是 | Integer(11) | 表单id |
| title | 否 | String(30) | 表单名称 |
| content | 否 | Text | 表单内容json |
| button | 否 | String(15) | 表单按钮名称 |
<br  />



##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":"2",
        "magazine_id":"3",
        "title":"表单2222",
        "content":"asfafdfasdfasdf22222",
        "button":"提交",
        "shop_id":30,
        "created":"1441160406",
        "modified":1441160744,
        "deleted":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __删除杂志表单__


##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/del-magazine-form
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 表单id |
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


## __创建用户表单报名记录__


##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/create-magazine-form-join
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| magazine_form_id | 是 | Integer(11) | 表单id |
| shop_id | 是 | Integer(11) | 店铺id |
| uid | 是 | Integer(11) | 用户id |
| content | 是 | Text | 报名内容json |
<br  />

##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "magazine_form_id":1,
        "uid":457,
        "valid":1,
        "shop_id":30,
        "content":"iggghjjh",
        "created":1441162056,
        "modified":1441162056,
        "deleted":1,
        "id":"1"
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __修改用户表单报名记录__


##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/update-magazine-form-join
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 报名记录id |
| shop_id | 是 | Integer(11) | 店铺id |
| content | 是 | Text | 报名内容json |
<br  />

##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":"1",
        "magazine_form_id":"1",
        "content":"iggghjjhdfghsdfhsfgh",
        "uid":"457",
        "valid":1,
        "shop_id":30,
        "created":"1441162056",
        "modified":1441162428,
        "deleted":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __审核用户表单报名记录__


##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/examine-magazine-form-join
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 报名记录id |
| shop_id | 是 | Integer(11) | 店铺id |
| valid | 是 | Integer(4) | 是否有效 2有效,3无效 |
<br  />

##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":"1",
        "magazine_form_id":"1",
        "content":"iggghjjhdfghsdfhsfgh",
        "uid":"457",
        "valid":2,
        "shop_id":30,
        "created":"1441162056",
        "modified":1441162983,
        "deleted":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取用户表单报名记录详情__


##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/get-magazine-form-join
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 报名记录id |
| shop_id | 是 | Integer(11) | 店铺id |
| magazine_form_id | 否 | Integer(11) | 表单id |
<br  />

##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
        "id":"1",
        "magazine_form_id":"1",
        "content":"iggghjjhdfghsdfhsfgh",
        "uid":"457",
        "valid":2,
        "shop_id":30,
        "created":"1441162056",
        "modified":1441162983,
        "deleted":1,
        "magazineForm":{
            "id":"1",
            "magazine_id":"3",
            "title":"表单1",
            "content":"asfafdfasdfasdf",
            "button":"提交",
            "shop_id":"30",
            "created":"1441160354",
            "modified":1441160354,
            "deleted":1
        }
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取用户表单报名记录列表__


##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/find-magazine-form-join
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| magazine_form_id | 否 | Integer(11) | 表单id |
| uid | 否 | Integer(11) | 用户id |
| valid | 否 | Integer(4) | 是否有效 1未审核,2有效,3无效 |
| createStart | 否 | Integer(11) | 报名起始时间 |
| createEnd | 否 | Integer(11) | 报名结束时间 |
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
            "id":"1",
            "magazine_form_id":"1",
            "content":"iggghjjhdfghsdfhsfgh",
            "uid":"457",
            "valid":2,
            "shop_id":30,
            "created":"1441162056",
            "modified":1441163229,
            "deleted":1,
            "magazineForm":{
                "id":"1",
                "magazine_id":"3",
                "title":"表单1",
                "content":"asfafdfasdfasdf",
                "button":"提交",
                "shop_id":"30",
                "created":"1441160354",
                "modified":1441160354,
                "deleted":1,
                "magazine":{
                    "id":"3",
                    "name":"棒棒哒",
                    "category_id":"1",
                    "type":1,
                    "share_message_id":944,
                    "face_document_id":346,
                    "music_document_id":347,
                    "pv":10,
                    "version":"2.1.7",
                    "shop_id":"30",
                    "created":1441077746,
                    "modified":1441090113,
                    "deleted":1
                }
            }
        }
    ],
    "page":{
        "per_page":20,
        "total_count":1,
        "current_page":0,
        "total_page":1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />



## __删除用户表单报名记录__


##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/magazine/del-magazine-form-join
<br  /><br  />

##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 报名记录id |
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
