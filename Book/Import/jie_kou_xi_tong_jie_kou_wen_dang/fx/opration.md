
## __获取分销员操作日志列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/find-operation-log-list
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| type | 否 | Integer(11) | 1.策略、2.分销员审核相关操作、3.分销员余额(提款)4.审核条件5.导入6.导出7.启用/禁用 |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
* **注意：sort排序可选字段['id']**

##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok"
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />

## __创建分销员操作日志__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/fx/create-fx-operation-log
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 店铺id |
| shop_sub_id | 否 | Integer(11) | 商铺id |
| type | 是 | Integer(11) | 1.策略、2.分销员审核相关操作、3.分销员余额(提款)4.审核条件5.导入6.导出7.启用/禁用 |
| content | 是 | Integer(11) | 内容 |
| operator | 是 | Integer(2) | 操作者 |
* **注意：sort排序可选字段['id']**

##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok"
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
