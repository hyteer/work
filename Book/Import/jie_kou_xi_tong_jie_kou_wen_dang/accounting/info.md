
## __创建账务配置信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/accounting/create-config
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| rec_bankacc | 是 | String(100) | 账号 |
| bank_type | 否 | String(20) | 银行编码 |
| rec_name | 是 | String(20) | 户名 |
| acc_type | 否 | Integer(3) | 账户类型（1：个人账户，：对公账户） |
| area | 否 | String(20) |  |
| city | 否 | String(20) |  |
| subbank_name | 否 | String(50) | 支行名称 |
| verify | 否 | Integer(3) | 审核状态（3：通过，4：不通过） |
| type | 是 | Integer(3) | 支付类型编号（1：银行卡，2：财付通，3：支付宝） |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取账务配置信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/accounting/get-config
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| config_id | 是 | Integer(11) | 配置id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __修改账务配置信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/accounting/update-config
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| config_id | 是 | Integer(11) | 配置id |
| rec_bankacc | 否 | String(100) | 账号 |
| bank_type | 否 | String(20) | 银行编码 |
| rec_name | 否 | String(20) | 户名 |
| acc_type | 否 | Integer(3) | 账户类型（1：个人账户，：对公账户） |
| area | 否 | String(20) |  |
| city | 否 | String(20) |  |
| subbank_name | 否 | String(50) | 支行名称 |
| verify | 否 | Integer(3) | 审核状态（3：通过，4：不通过） |
| type | 否 | Integer(3) | 支付类型编号（1：银行卡，2：财付通，3：支付宝） |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __获取账务余额__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/accounting/get-balance
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode":0,
    "errmsg":"ok",
    "data":{
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />


## __创建提现流水账__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/accounting/create
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| transtype_id | 是 | Integer(11) | 事务类型ID |
| obj | 是 | Integer(11) | 关联处理对象(0：无 1：订单 2：提现) |
| obj_id | 是 | Integer(11) | 商家id |
| code | 是 | String(32) | 流水号 |
| amount | 是 | Integer(11) | 记账金额，单位分 |
| fee | 否 | Integer(11) | 手续费，单位分 |
| balance | 是 | Integer(11) | 记账之后余额，单位分 |
| remark | 否 | String | 备注 |
| user_id | 否 | Integer(11) | 终端会员ID |
| user_nickname | 否 | String(50) | 终端会员昵称 |
| managers_id | 否 | Integer(50) | 操作人（boss） |
<br  />
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


## __获取提现流水账列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/accounting/find-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| date | 否 | datetime | 日志记录日期，日期格式（yyyy-mm-dd） |
| page | 否 | Integer(11) | 分页值 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
* **注意：sort排序可选字段['id']**

<br  />
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


## __获取提现流水账信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/accounting/get
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 是 | Integer(11) | 店铺id |
| accounting_id | 是 | Integer(11) | 账务id |
<br  />
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



