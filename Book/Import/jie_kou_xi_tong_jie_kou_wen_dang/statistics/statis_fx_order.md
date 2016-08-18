# 推广统计

## __推广员统计总数(门店/员工/代理商)__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/statistics/count-fx-member
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| shop_count_type|否|Integer(4)|1为统计全部的，2为只统计直营店的,默认是2|
| shop_sub_id|否|Integer(11)|分店id|
| staff_id|否|Integer(11)|员工id，0为统计所有员工的推广员数，否则统计单个员工的推广员数|
| agent_ids|否|Array|代理商id数组|
| start|否|Integer(11)|下单开始时间，包括当前值|
| end|否|Integer(11)|下单截止时间，包括当前值|
| kind|是|Integer(4)|1为统计门店推广员，2为统计员工的，3为统计代理商|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": 2
}
```
<br  />


## __推广订单统计总数或是收益统计数(门店/员工/代理商/推广员)__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/statistics/count-fx-order
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| shop_count_type|否|Integer(4)|1为统计全部的，2为只统计直营店的,默认是2|
| shop_sub_id|否|Integer(11)|分店id|
| staff_id|否|Integer(11)|员工id,不传或0则统计所有员工的推广订单|
| agent_ids|否|Array|代理商id数组,不传或0则统计所有代理商的推广订单|
| mid|否|Integer(11)|分销员id|
| start|否|Integer(11)|下单开始时间，包括当前值|
| end|否|Integer(11)|下单截止时间，包括当前值|
| kind|是|Integer(4)|1为统计门店的，2为统计员工的，3为统计代理商，4为统计推广员|
| sum|否|Integer(4)|如果值设为1，则统计收益总数，否则统计订单总数|

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": 2
}
```
<br  />


## __按组进行推广订单统计(门店/员工/代理商/推广员)__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/statistics/group-count-fx-order
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| shop_count_type|否|Integer(4)|1为统计全部的，2为只统计直营店的,默认是2|
| shop_sub_id|否|Integer(11)|分店id|
| staff_id|否|Integer(11)|员工id|
| agent_ids|否|Array|代理商id数组|
| mid|否|Integer(11)|分销员id|
| group|是|Integer(4)|1为按终端店，2为按员工，3为按代理商，4为按推广员|
| start|否|Integer(11)|下单开始时间，包括当前值|
| end|否|Integer(11)|下单截止时间，包括当前值|
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": [
      {
        "num":2,
        "brokerage_all":78,
        "id":31
      }
    ]
}
```
<br  />


## __代理商推广明细列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/statistics/fx-order-list-by-agent
<br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id|是|Integer(11)|商铺id|
| agent_ids|是|Array|代理商id数组|
| staff_id|否|Integer(11)|员工id|
| shop_sub_id|否|Integer(11)|门店id|
| fx_member_id|否|Integer(11)|分销员id|
| createStart|否|Integer(11)|下单开始时间，包括当前值|
| createEnd|否|Integer(11)|下单截止时间，包括当前值|
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": [
        {
            "id": 230,
            "order_no": "1000005010115072302071169689",
            "uid": 171,
            "user_name": "312321",
            "ip": null,
            "total_price": 45000,
            "delivery_fee": 0,
            "discount": 0,
            "should_pay": 45000,
            "payed": 0,
            "qr_discount": 0,
            "point_discount": 0,
            "seller_cut": 0,
            "card_name": null,
            "card_id": null,
            "red_packet_id": 0,
            "activity_id": null,
            "is_income": null,
            "order_status": 3,
            "refund_status": 0,
            "deliver_status": 1,
            "after_sales_status": 2,
            "order_type": 1,
            "seller_mark": null,
            "customer_mark": null,
            "r_points": 0,
            "send_points": 0,
            "shop_staff_id": 1,
            "pickup_code": null,
            "pos_pin_code": null,
            "shop_id": 5,
            "shop_sub_id": 43,
            "share_message_id": null,
            "pickup_type": 1,
            "pickup_shop_sub_id": null,
            "pickup_date": null,
            "express_type": null,
            "express_no": null,
            "agent_path": null,
            "agent_id": 8,
            "fx_member_id": null,
            "is_cod": 1,
            "created": 1437632591,
            "modified": 1437632804,
            "shopAgent": {
                "id": 8,
                "pid": 0,
                "user_name": "123123",
                "password": "21218cca77804d2ba1922c33e0151105",
                "real_name": "66666a",
                "role_id": 2,
                "mobile": "13812345678",
                "email": "yuan@snsshop.cn",
                "shop_sub_id": 43,
                "shop_id": 5,
                "last_login": 1431939834,
                "agent_name": "0122",
                "path": "",
                "area": "福建",
                "level": 1,
                "is_default": 1,
                "created": 1431939834,
                "modified": 1439454997,
                "deleted": 1
            },
            "orderDelivery": [ ],
            "orderPayInfos": [
                {
                    "id": 149,
                    "order_id": 230,
                    "pay_type": 3,
                    "amount": 45000,
                    "uid": null,
                    "user_name": null,
                    "pay_status": 1,
                    "trade_no": null,
                    "created": 1437632804,
                    "modified": 1437632804
                }
            ],
            "fxOrder": {
                "id": 21,
                "order_id": 230,
                "product_count": null,
                "fx_product_count": null,
                "total_price": null,
                "fx_total_price": null,
                "brokerage": null,
                "status": 1,
                "mid": null,
                "member_name": null,
                "uid": null,
                "user_name": null,
                "shop_id": null,
                "shop_sub_id": null,
                "created": null,
                "modified": null
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
<br  />

