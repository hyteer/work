## __新增众筹参与__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/create-collect-click
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
|collect_join_id|是|Integer(11)|众筹参与id|
| uid|是|Integer(11)|用户id|
| word|否|String(20)|手机号|
| name|是|String(10)|姓名|
| address|是|String(220)|住址|
| collect_product_id|是|Integer(11)|活动产品id|
| collect_redpacket_id|是|Integer(11)|活动关联的红包|
| collect_custom_gift_id|是|Integer(11)|用户自定义礼物|
| shop_id|是|Integer(11)|商家id|
| shop_sub_id|是|Integer(11)|店铺id|
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "uid": "157",
        "status": 2,
        "mobile": "15823568956",
        "name": "大幅减少地方",
        "address": "考虑国家实力可见弗兰克",
        "collect_product_id": "1",
        "collect_redpacket_id": "",
        "created": 1436944457,
        "collect_id": "7",
        "title": "呵呵",
        "collect_custom_gift_id": "",
        "shop_id": "5",
        "shop_sub_id": "43",
        "modified": 1436944457,
        "id": 1
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取众筹帮助列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/collect/find-collect-click
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| collect_id | 是 | Integer(11) | 众筹id |
| collect_join_id|是|Integer(11)|众筹参与id|
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
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
            "id": 2,
            "collect_id": 16,
            "collect_join_id": 9,
            "uid": 164,
            "num": 1,
            "word": "我为自己代言",
            "shop_id": 5,
            "shop_sub_id": 43,
            "created": 1437361763,
            "modified": 1437361763,
            "userInfo": {
                "id": 164,
                "mobile": null,
                "nickname": "晨晨Cathy",
                "sex": 2,
                "province": "湖北",
                "city": "武汉",
                "country": "中国",
                "headimgurl": "http://wx.qlogo.cn/mmopen/wmBXq89PkTDm6FniaicGFzA0tU2jQSSI7icbzWA1sia8EfQ9l00mMmJB4g8NoRvYaoLtSdM5S2gLuJl3ewOjnGaTlHeBtnVHtnYO/0",
                "shop_id": 5,
                "shop_sub_id": 43,
                "staff_id": 0,
                "login_count": 0,
                "lastloginip": null,
                "lastlogintime": 0,
                "password": null,
                "type": 2,
                "status": 1,
                "member_refer": null,
                "weixin": null,
                "scene_id": null,
                "mpath": null,
                "mid": null,
                "code": null,
                "sign_days": 0,
                "sign_time": 0,
                "is_subscribe": 1,
                "group_id": 1,
                "level_id": null,
                "point": null,
                "wsh_code": null,
                "created": 1437355566,
                "modified": 1437384715,
                "deleted": 1
            }
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
