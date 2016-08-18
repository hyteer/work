
## __添加商品__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/create
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| product.product_category_id | 是 | String(1000) | 商品分类 |
| product.product_category_path | 是 | String(250) | procduct_category表path冗余 |
| product.product_kind_ids | 是 | String(50) | 产品规格.格式1,2,3,注意一定是以‘,’结尾 |
| product.name | 是 | String(100) | 标题 |
| product.subtitle | 否 | String(100) | 副标题 |
| product.keyword | 否 | String(200) | 商品关键字 |
| product.product_type | 是 | Integer(3) | 产品类型（1.实物、2.虚拟） |
| product.product_no | 否 | String(10) | 商品编号，商家自定义 |
| product.show_price | 是 | Integer(11) | 展示价。（根据策略获取） |
| product.prod_weight | 是 | Double(10,2) | 产品重量 |
| product.shop_id | 是 | Integer(11) | 商家id |
| product.shop_sub_id | 是 | Integer(11) | 店铺id |
| product.hits | 否 | Integer(11) | 点击数 |
| product.sales | 否 | Integer(11) | 销量 |
| product.status | 是 | Integer(3) | 商品状态（1.上架、2.下架） |
| product.postage_fee_type | 是 | Integer(3) | 邮费类型（1.使用模版、2.免邮） |
| product.quota | 否 | Integer(11) | 限购数量 |
| product.sort | 否 | Integer(11) | 排序，值越大越优先显示 |
| product.is_pre_sale | 否 | Integer(3) | 是否预售（1.是、2.否）|
| product.pre_sale_id | 否 | Integer(11) | 预售活动id |
| product.show_sale_num | 否 | Integer(3) | 是否展示销量（1.是、2。否） |
| product.covers_id | 否 | Integer(11) | 封面图id |
| productInfo.detail_pic | 是 | String(200) | 商品详情幻灯图 |
| productInfo.description | 是 | String(300) | 商品描述 |
| productInfo.detail | 是 | String | 商品内容 |
| skus.sku_no | 是 | String(20) | sku编号 |
| skus.name | 是 | String(100) | sku的名称 |
| skus.reserves | 是 | Integer(11) | 库存 |
| skus.freez_reserve | 否 | Integer(11) | 冻结库存 |
| skus.market_price | 是 | Integer(11) | 市场价 |
| skus.cost_price | 是 | Integer(11) | 成本价 |
| skus.retail_price | 是 | Integer(11) | 零售价 |
| skus.sales | 否 | Integer(11) | 销量 |
| skus.status | 是 | Integer(3) | 库存状态（1.上架、2.下架） |
| skus.barcode | 否 | String(20) | 条形码 |
| skus.barcode_pic | 否 | Integer(11) | 条形码图片id |
| skus.kind_ids | 是 | String(100) | 规格id列表。array |
| skus.kind_value_ids | 是 | String(100) | 规格值id列表。array |
| shareMessage.title | 是 | String(100) | 分享时的标题 |
| shareMessage.desc | 是 | String(100) | 分享时的摘要 |
| shareMessage.pic_id | 是 | Integer(11) | 分享时的缩略图 |
* **注意：skus为二维索引数组，如 $var = ['0'=>['id'=>1,'name'=>'mch']]**
* **注意：shareMessage未非必要，如无需设置，则勿提供shareMessage参数信息**
* **注意：skus.kind_ids和skus.kind_value_ids是一一对应的**

<br  /><br  />
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


## __获取商品列表__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/find-list
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| product_category_id | 否 | Integer(11) | 分类id |
| fx_product_filter | 否 | boolean | 是否过滤分销商品中已使用的 |
| name | 否 | String | 名称 |
| product_no | 否 | String | 商品编码 |
| keyword | 否 | String | 关键词 |
| subtitle | 否 | String | 副标题 |
| is_recommend | 否 | Integer(11) | 是否推荐商品（1.是、2.否） |
| status | 否 | Integer(4) | 状态 |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| ids | 否 | Array | 需要查找的id列表 |
| sale_scope | 否 | Array |  销售范围1.线上、2.线下、3.线上和线下 |
| postage_fee_type | 否 | Integer(11) |  关联邮费模板id |
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

## __获取商品列表及相关详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/find-product-with-other-info
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| shop_sub_id | 否 | Integer(11) | 店铺id |
| fx_product_filter | 否 | boolean | 是否过滤分销商品中已使用的 |
| product_category_id | 否 | Integer(11) | 分类id |
| name | 否 | String | 名称 |
| product_no | 否 | String | 商品编码 |
| keyword | 否 | String | 关键词 |
| subtitle | 否 | String | 副标题 |
| is_recommend | 否 | Integer(11) | 是否推荐商品（1.是、2.否） |
| status | 否 | Integer(4) | 状态 |
| page | 否 | Integer(11) | 分页值，第一页值为0 |
| count | 否 | Integer(2) | 列表个数，一次最多获取100个 |
| sortStr | 否 | Array | 排序方式 eg:['id'=>'desc'] |
| modifyStart | 否 | Integer(11) | 开始时间 |
| modifyEnd | 否 | Integer(11) | 结束时间 |
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


## __获取商品信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/get
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| product_id | 是 | Integer(11) | 商品id |
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

## __获取商品信息及相关详情__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/get-product-with-other-info
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| product_id | 是 | Integer(11) | 商品id |
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

## __修改商品信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/to-update
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| product.id | 是 | String(1000) | 商品id |
| product.product_category_id | 是 | String(1000) | 商品分类id |
| product.product_category_path | 否 | String(250) | procduct_category表path冗余 |
| product.product_kind_ids | 否 | String(50) | 产品规格.格式1,2,3,注意一定是以‘,’结尾 |
| product.name | 否 | String(100) | 标题 |
| product.subtitle | 否 | String(100) | 副标题 |
| product.keyword | 否 | String(200) | 商品关键字 |
| product.product_type | 否 | Integer(3) | 产品类型（1.实物、2.虚拟） |
| product.product_no | 否 | String(10) | 商品编号，商家自定义 |
| product.show_price | 否 | Integer(11) | 展示价。（根据策略获取） |
| product.prod_weight | 否 | Double(10,2) | 产品重量 |
| product.shop_id | 是 | Integer(11) | 商家id |
| product.shop_sub_id | 否 | Integer(11) | 店铺id |
| product.hits | 否 | Integer(11) | 点击数 |
| product.sales | 否 | Integer(11) | 销量 |
| product.status | 否 | Integer(3) | 商品状态（1.上架、2.下架） |
| product.postage_fee_type | 否 | Integer(3) | 邮费类型（1.使用模版、2.免邮） |
| product.quota | 否 | Integer(11) | 限购数量 |
| product.sort | 否 | Integer(11) | 排序，值越大越优先显示 |
| product.is_pre_sale | 否 | Integer(3) | 是否预售（1.是、2.否）|
| product.pre_sale_id | 否 | Integer(11) | 预售活动id |
| product.show_sale_num | 否 | Integer(3) | 是否展示销量（1.是、2。否） |
| product.covers_id | 否 | Integer(11) | 封面图id |
| productInfo.detail_pic | 否 | String(200) | 商品详情幻灯图 |
| productInfo.description | 否 | String(300) | 商品描述 |
| productInfo.detail | 否 | String | 商品内容 |
| skus.sku_no | 否 | String(20) | sku编号 |
| skus.name | 否 | String(100) | sku的名称 |
| skus.reserves | 否 | Integer(11) | 库存 |
| skus.freez_reserve | 否 | Integer(11) | 冻结库存 |
| skus.market_price | 否 | Integer(11) | 市场价 |
| skus.cost_price | 否 | Integer(11) | 成本价 |
| skus.retail_price | 否 | Integer(11) | 零售价 |
| skus.sales | 否 | Integer(11) | 销量 |
| skus.barcode | 否 | String(20) | 条形码 |
| skus.barcode_pic | 否 | Integer(11) | 条形码图片id |
| skus.kind_ids | 否 | String(100) | 规格id列表.array |
| skus.kind_value_ids | 否 | String(100) | 规格值id列表。array |
| shareMessage.title | 否 | String(100) | 分享时的标题 |
| shareMessage.desc | 否 | String(100) | 分享时的摘要 |
| shareMessage.pic_id | 否 | Integer(11) | 分享时的缩略图 |
* **注意：skus为二维索引数组，如 $var = ['0'=>['id'=>1,'name'=>'mch']]**
* **注意：shareMessage未非必要，如无需设置，则勿提供shareMessage参数信息**
* **注意：skus.kind_ids和skus.kind_value_ids是一一对应的**

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


## __删除商品信息__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/del
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| product_id | 是 | Integer(11) | 商品id |
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

## __商品下架__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/off-sale
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| ids | 是 | array | 商品id数组 |
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

## __商品上架__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/on-sale
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| ids | 是 | array | 商品id数组 |
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

## __商品批量删除__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/mult-del
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| ids | 是 | array | 商品id数组 |
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

## __商品批量修改分类__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/mult-update-product-category
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| ids | 是 | array | 商品id数组 |
| product_category_id | 是 | Integer(11) | 修改为的产品分类 |
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

## __设置商品为推荐__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/recommend-product
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| id | 是 | Integer(11) | 商品id |
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

## __取消商品推荐__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/un-recommend-product
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| shop_id | 是 | Integer(11) | 商家id |
| id | 是 | Integer(11) | 商品id |
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


## __修改商品sku__
##### 接口调用请求说明
请求方式：POST
<br  />
请求地址：/product/update-product-sku
<br  /><br  />
##### 参数说明
| 参数 | 是否必须 | 类型限制 | 说明 |
| -- | -- | -- | -- |
| id | 是 | Integer(11) | 商品skuid |
| shop_id | 是 | Integer(11) | 商家id |
| name | 否 | String(100) | 商品sku名称 |
| reserves | 否 | Integer(11) | 商品sku库存 |
| market_price | 否 | Integer(11) | 商品sku市场价 |
| retail_price | 否 | Integer(11) | 商品sku销售价 |
| sales | 否 | Integer(11) | 商品sku销量 |
| status | 否 | Integer(11) | 商品sku状态（1.上架、2.下架） |
| barcode | 否 | String(20) | 条形码 |
| sku_no | 否 | String(20) | 商家编码 |
* **注意：status 填写为1 时market_price/retail_price/reserves必填**

<br  />
##### 返回说明
正常情况下，会返回下述JSON数据包给开发者：
```php
{
    "errcode": 0,
    "errmsg": "ok",
    "data": {
        "id": 114708,
        "sku_no": "H02140043",
        "product_id": 17047,
        "name": "呷虾咪麻糬 手工花莲麻糬 无明胶无果胶 纯糯米制作 45g 红豆",
        "reserves": 458,
        "freez_reserve": 0,
        "market_price": 0,
        "cost_price": 0,
        "retail_price": 500,
        "sales": 1,
        "status": 1,
        "barcode": "H0214004",
        "barcode_pic": '',
        "shop_id": 514,
        "shop_sub_id": 0,
        "created": 1468220704,
        "modified": 1468220704
    }
}
```
错误时接口平台会返回错误码等信息，请参照：
[全局返回码说明](/error-code.html)
<br  /><br  />
