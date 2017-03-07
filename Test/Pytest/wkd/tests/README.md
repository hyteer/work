# WKD测试用例

## 用例分类
用例分为API、UI、和Scene(业务场景)大部分。
* API用例

* UI用例

* Scene


## 命名规范
* 对象属性引用统一采用小写，如有多个单词组成，则单词之间需要用下划线分隔，例如：ui.weixin、api.market.second_kill_add
* 针对具体模块实例化时的引用路径在对象名之前只可通过属性引用，即对象名之前只有小写，例如：ui.weixin.Product(conf),错误的写法：ui.Weixin.Product(conf)
* 常量、配置字典采用全大写，例如：LOCATERS、MK_PARAM、TIME_OUT

## 用例编写指南

### 用例标记
除了系统自带的标记如“skipif”，另外还提供以下自定义标记：

* not_ready (注：此标记表示用例还未准备就绪，标记后在CI任务中不会运行)
* debug (注： 此标记可用于本地或CI运行调试）
* no_cycle (注：此标记表明该用例产生的数据无法回收，CI任务中将会控制该类用例的运行频率。)

### 用例作者
可以通过在测试用例类中增加 "AUTHOR" 变量声明此用例的作者。

例如：AUTHOR = 'YT'

(注：当前可声明的预定义作者为'YT','BW','XZ)

### 用例覆盖率
通过设置COVERAGE属性在测试类中声明该用例的覆盖率，如 COVERAGE=50，表明该用例类下所有用例已覆盖自身功能的50%

## 运行调试

### 运行可用参数
* --testenv
* --author (仅运行指定作者的用例，如：pytest --author "XZ")
* --dbg
