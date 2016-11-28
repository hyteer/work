-- --------------------------------------------------------
-- 主机:                           10.100.100.84
-- 服务器版本:                        5.6.21-log - Source distribution
-- 服务器操作系统:                      Linux
-- HeidiSQL 版本:                  9.2.0.4947
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 导出 shop_db 的数据库结构
CREATE DATABASE IF NOT EXISTS `shop_db` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `shop_db`;


-- 导出  表 shop_db.bill_history 结构
CREATE TABLE IF NOT EXISTS `bill_history` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `type` varchar(5) NOT NULL DEFAULT 'ch' COMMENT 'bm：银行 ch：渠道 mch：商户',
  `accountid` int(11) unsigned NOT NULL COMMENT '账号ID，与type对应',
  `billtype` tinyint(1) unsigned NOT NULL COMMENT '账单类型 1 所有 2 交易账单 3 退款账单',
  `filepath` varchar(200) NOT NULL COMMENT '生成账单文件地址',
  `filename` varchar(50) NOT NULL COMMENT '生成账单文件名',
  `start_date` date NOT NULL COMMENT '开始日期',
  `end_date` date NOT NULL COMMENT '结束日期',
  `status` tinyint(1) NOT NULL DEFAULT '-1' COMMENT '-1 处理中 1 已生成',
  `writetime` int(10) unsigned NOT NULL COMMENT '生成时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='对账单生成历史';

-- 数据导出被取消选择。


-- 导出  表 shop_db.bm 结构
CREATE TABLE IF NOT EXISTS `bm` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `login_name` varchar(20) NOT NULL COMMENT '登录名',
  `login_pwd` varchar(32) NOT NULL COMMENT '登录密码',
  `pwd_salt` varchar(6) NOT NULL COMMENT '盐加密',
  `name` varchar(50) NOT NULL DEFAULT '' COMMENT '机构名称',
  `addr` varchar(50) NOT NULL DEFAULT '' COMMENT '地址',
  `headman` varchar(10) NOT NULL COMMENT '负责人',
  `headman_mobile` varchar(11) NOT NULL COMMENT '负责人手机号码',
  `email` varchar(50) NOT NULL DEFAULT '' COMMENT '邮箱',
  `login_error_count` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '登录错误次数',
  `login_error_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '上次登录错误时间',
  `bm_bank_cardno` varchar(50) NOT NULL DEFAULT '' COMMENT '银行端银行卡号',
  `service_bank_cardno` varchar(50) NOT NULL DEFAULT '' COMMENT '技术服务端银行卡号',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='银行管理账号';

-- 数据导出被取消选择。


-- 导出  表 shop_db.channel 结构
CREATE TABLE IF NOT EXISTS `channel` (
  `channelid` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '渠道id',
  `channel_name` varchar(50) NOT NULL COMMENT '渠道名称',
  `channel_sname` varchar(50) DEFAULT '' COMMENT '渠道简称',
  `industry_type` int(11) unsigned DEFAULT '0' COMMENT '行业类别id',
  `channel_type` tinyint(1) unsigned DEFAULT '1' COMMENT '1：渠道商 2：大客户',
  `parentid` int(11) unsigned DEFAULT '0' COMMENT '父渠道ID，如果有值则为子渠道',
  `levels` tinyint(2) unsigned DEFAULT '1' COMMENT '渠道层级',
  `login_pwd` varchar(32) NOT NULL COMMENT '密码(md5密码)',
  `pwd_salt` varchar(6) NOT NULL COMMENT '盐加密',
  `invite_no` varchar(50) DEFAULT '' COMMENT '邀请码',
  `flag` tinyint(1) unsigned DEFAULT '2' COMMENT '渠道来源 1：内部 2：外部',
  `prov` varchar(6) DEFAULT '' COMMENT '所在省',
  `city` varchar(6) DEFAULT '' COMMENT '所在市',
  `dist` varchar(6) DEFAULT '' COMMENT '所在区、县',
  `addr` varchar(50) DEFAULT '' COMMENT '详细地址',
  `headman` varchar(10) DEFAULT '' COMMENT '负责人',
  `headman_idnum` varchar(18) DEFAULT '' COMMENT '负责人身份证',
  `headman_mobile` varchar(11) DEFAULT '' COMMENT '负责人手机',
  `businesslicence` varchar(32) DEFAULT '' COMMENT '营业执照编码',
  `business_pic` varchar(255) DEFAULT '' COMMENT '营业执照片',
  `email` varchar(50) NOT NULL COMMENT '邮箱',
  `tel` varchar(20) DEFAULT '' COMMENT '电话',
  `homepage` varchar(50) DEFAULT '' COMMENT '网址',
  `audit` varchar(50) DEFAULT '' COMMENT '审核人',
  `audit_time` int(10) unsigned DEFAULT '0' COMMENT '审核时间',
  `audit_remark` varchar(50) DEFAULT '' COMMENT '审核备注',
  `writetime` int(10) unsigned NOT NULL COMMENT '录入时间',
  `login_error_count` tinyint(1) unsigned DEFAULT '0' COMMENT '登录错误次数',
  `login_error_time` int(11) unsigned DEFAULT '0' COMMENT '上次登录错误时间',
  `status` tinyint(1) NOT NULL DEFAULT '2' COMMENT '状态 -1 禁用 1 正常 2 审核中 -2 审核不通过',
  PRIMARY KEY (`channelid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='渠道表';

-- 数据导出被取消选择。


-- 导出  表 shop_db.channel_daystat 结构
CREATE TABLE IF NOT EXISTS `channel_daystat` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `channelid` int(11) unsigned NOT NULL COMMENT '渠道ID',
  `ispay` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '0：未结算 1：已经结算',
  `trade_count` bigint(20) unsigned DEFAULT '0' COMMENT '交易总笔数',
  `trade_amount` bigint(20) unsigned DEFAULT '0' COMMENT '交易总金额(分)',
  `refund_count` bigint(20) unsigned DEFAULT '0' COMMENT '退款总笔数',
  `refund_amount` bigint(20) unsigned DEFAULT '0' COMMENT '退款总额(分)',
  `trade_netamount` bigint(20) DEFAULT '0' COMMENT '交易总净额',
  `channel_profit` bigint(20) unsigned DEFAULT '0' COMMENT '渠道佣金',
  `refund_channel_profit` bigint(20) unsigned DEFAULT '0' COMMENT '渠道佣金退款',
  `needpay_amount` bigint(20) DEFAULT '0' COMMENT '待结算金额',
  `paytime` int(10) unsigned DEFAULT '0' COMMENT '结算时间',
  `pre_paydate` date NOT NULL COMMENT '预打款日期，打款以此为准，针对不同T+N',
  `dateflag` date NOT NULL COMMENT '统计日期（统计某天的交易订单）',
  `writetime` int(10) unsigned NOT NULL COMMENT '写入时间',
  `lastupdatetime` int(10) unsigned NOT NULL COMMENT '最后更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='渠道每天统计表';

-- 数据导出被取消选择。


-- 导出  表 shop_db.channel_levels 结构
CREATE TABLE IF NOT EXISTS `channel_levels` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `queryid` int(11) unsigned NOT NULL COMMENT '查询用渠道ID',
  `channelid` int(11) unsigned NOT NULL COMMENT '当前渠道ID（包含本身和上级）',
  `levels` tinyint(2) unsigned NOT NULL DEFAULT '1' COMMENT '渠道层级',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='渠道层级';

-- 数据导出被取消选择。


-- 导出  表 shop_db.channel_paysetting 结构
CREATE TABLE IF NOT EXISTS `channel_paysetting` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `channelid` int(11) unsigned NOT NULL COMMENT '渠道id',
  `trade_type` varchar(16) NOT NULL DEFAULT 'WXPAY.JSAPI' COMMENT '支付类型',
  `calc_rate` int(5) unsigned NOT NULL COMMENT '结算费率（万分）',
  `writetime` int(10) unsigned NOT NULL COMMENT '写入时间',
  `status` tinyint(1) NOT NULL DEFAULT '2' COMMENT '状态 -1 禁用 1 正常 2 审核中 -2 审核不通过',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='渠道结算费率配置';

-- 数据导出被取消选择。


-- 导出  表 shop_db.channel_rates 结构
CREATE TABLE IF NOT EXISTS `channel_rates` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `trade_type` varchar(16) NOT NULL DEFAULT 'WXPAY.JSAPI' COMMENT '支付类型',
  `queryid` int(11) unsigned NOT NULL COMMENT '查询用渠道ID',
  `query_calc_rate` int(5) unsigned NOT NULL COMMENT '查询渠道费率',
  `channelid` int(11) unsigned NOT NULL COMMENT '当前渠道ID（包含本身和上级）',
  `calc_rate` int(5) unsigned NOT NULL COMMENT '当前渠道结算费率（万分）',
  `levels` tinyint(2) unsigned NOT NULL DEFAULT '1' COMMENT '当前渠道等级',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='渠道结算费率及上级结算费率';

-- 数据导出被取消选择。


-- 导出  表 shop_db.channel_stat 结构
CREATE TABLE IF NOT EXISTS `channel_stat` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `channelid` int(11) unsigned NOT NULL COMMENT '渠道id',
  `trade_count` bigint(20) unsigned DEFAULT '0' COMMENT '交易总笔数',
  `trade_amount` bigint(20) unsigned DEFAULT '0' COMMENT '交易总金额(分)',
  `refund_count` bigint(20) unsigned DEFAULT '0' COMMENT '退款总笔数',
  `refund_amount` bigint(20) unsigned DEFAULT '0' COMMENT '退款总额(分)',
  `trade_netamount` bigint(20) DEFAULT '0' COMMENT '交易总净额',
  `channel_profit` bigint(20) DEFAULT '0' COMMENT '渠道佣金',
  `refund_channel_profit` bigint(20) unsigned DEFAULT '0' COMMENT '渠道佣金退款',
  `total_amount` bigint(20) DEFAULT '0' COMMENT '总共所得',
  `needpay_amount` bigint(20) DEFAULT '0' COMMENT '待结算金额',
  `payed_amount` bigint(20) unsigned DEFAULT '0' COMMENT '已结金额',
  `lastupdatetime` int(10) unsigned NOT NULL COMMENT '最后更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='渠道总统计表';

-- 数据导出被取消选择。


-- 导出  表 shop_db.industry_type 结构
CREATE TABLE IF NOT EXISTS `industry_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL COMMENT '行业名称',
  `parentid` int(11) NOT NULL DEFAULT '0' COMMENT '上级ID',
  `writetime` int(10) NOT NULL COMMENT '入库时间',
  `levels` tinyint(1) unsigned NOT NULL DEFAULT '1' COMMENT '层级',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='行业类型配置表';

-- 数据导出被取消选择。


-- 导出  表 shop_db.orders 结构
CREATE TABLE IF NOT EXISTS `orders` (
  `order_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `out_trade_no` varchar(50) NOT NULL COMMENT '第三方订单号',
  `mch_id` int(11) unsigned NOT NULL COMMENT '系统商户号',
  `channelid` int(11) unsigned NOT NULL COMMENT '上级渠道id',
  `order_no` varchar(50) NOT NULL COMMENT '平台订单号',
  `pay_channel` varchar(16) NOT NULL COMMENT '支付渠道 WXPAY ALIPAY SQPAY',
  `transaction_id` varchar(50) DEFAULT '' COMMENT '支付单号',
  `trade_type` varchar(16) NOT NULL DEFAULT 'WXPAY.JSAPI' COMMENT '支付类型',
  `sub_openid` varchar(32) DEFAULT '' COMMENT '第三方微信openid',
  `sub_mch_id` varchar(20) DEFAULT NULL COMMENT '第三方微信商户号（商户识别码）',
  `bank_type` varchar(16) DEFAULT '' COMMENT '银行类型，采用字符串类型的银行标识',
  `sub_is_subscribe` varchar(1) DEFAULT '' COMMENT '用户是否关注子公众账号，Y-关注，N-未关注，仅在公众账号类型支付有效',
  `cashierid` int(11) unsigned DEFAULT '0' COMMENT '收银员id',
  `salesid` int(11) unsigned DEFAULT '0' COMMENT '业务员id',
  `fee_type` varchar(20) DEFAULT 'CNY' COMMENT '标价币种，默认CNY',
  `total_fee` int(11) unsigned NOT NULL COMMENT '交易总金额',
  `cash_fee` int(11) DEFAULT '0' COMMENT '现金金额',
  `coupon_fee` int(11) DEFAULT '0' COMMENT '代金券金额',
  `refund_fee` int(11) unsigned DEFAULT '0' COMMENT '已退款金额',
  `refund_batch` tinyint(2) unsigned DEFAULT '0' COMMENT '已退款总次数',
  `refund_cash_fee` int(11) unsigned DEFAULT '0' COMMENT '已现在金额',
  `refund_coupon_fee` int(11) unsigned DEFAULT '0' COMMENT '已优惠券金额',
  `body` varchar(50) NOT NULL DEFAULT '' COMMENT '支付body',
  `attach` varchar(200) DEFAULT '' COMMENT '第三方附加数据',
  `order_status` tinyint(1) unsigned NOT NULL DEFAULT '1' COMMENT '1：未支付 2：已支付 3：已关闭 4：部分退款 5：完全退款',
  `settle_status` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '是否已结算',
  `shop_calc_rate` int(5) unsigned NOT NULL COMMENT '商户结算费率（万分，总扣除）',
  `shop_amount` int(11) unsigned NOT NULL COMMENT '商户可得，待结算给商户金额',
  `payment_profit_rate` int(5) unsigned NOT NULL COMMENT '支付手续费率（万分，利润）',
  `payment_profit` int(11) unsigned NOT NULL COMMENT '支付手续费',
  `channel_profit_rate` int(5) unsigned NOT NULL COMMENT '渠道总佣金费率（万分，利润）',
  `channel_profit` int(11) unsigned NOT NULL COMMENT '渠道总佣金金额',
  `service_profit_rate` int(5) unsigned NOT NULL COMMENT '技术服务费率（万分，利润）',
  `service_profit` int(11) unsigned NOT NULL COMMENT '技术服务费',
  `bm_profit_rate` int(5) unsigned NOT NULL COMMENT '机构清分手续费率（万分，利润）',
  `bm_profit` int(11) unsigned NOT NULL COMMENT '机构清分手续费',
  `total_commission` int(11) unsigned NOT NULL COMMENT '总手续费',
  `device_info` varchar(50) DEFAULT '' COMMENT '终端设备号(门店号或收银设备ID)，注意：PC网页或公众号内支付请传"WEB"',
  `device_type` varchar(50) DEFAULT '' COMMENT '设备类型',
  `spbill_create_ip` varchar(15) NOT NULL COMMENT '第三方终端ip',
  `notify_url` varchar(200) DEFAULT '' COMMENT '第三方支付回调地址',
  `return_url` varchar(200) DEFAULT '' COMMENT '第三方支付跳转地址',
  `order_from` varchar(10) DEFAULT '' COMMENT '订单生成来源',
  `writetime` int(10) unsigned NOT NULL COMMENT '下单时间',
  `lastupdatetime` int(10) unsigned DEFAULT '0' COMMENT '最后更新时间',
  `paytime` int(10) unsigned DEFAULT '0' COMMENT '支付成功时间',
  `refundtime` int(10) unsigned DEFAULT '0' COMMENT '退款成功时间（完全退款）',
  PRIMARY KEY (`order_id`,`writetime`),
  KEY `mch_id` (`mch_id`),
  KEY `channelid_paytime` (`channelid`,`paytime`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单表'
/*!50100 PARTITION BY RANGE (writetime)
(PARTITION d20161122 VALUES LESS THAN (1479830400) ENGINE = InnoDB,
 PARTITION d20161123 VALUES LESS THAN (1479916800) ENGINE = InnoDB,
 PARTITION d20161124 VALUES LESS THAN (1480003200) ENGINE = InnoDB,
 PARTITION d20161125 VALUES LESS THAN (1480089600) ENGINE = InnoDB,
 PARTITION d20161126 VALUES LESS THAN (1480176000) ENGINE = InnoDB,
 PARTITION d20161127 VALUES LESS THAN (1480262400) ENGINE = InnoDB,
 PARTITION d20161128 VALUES LESS THAN (1480348800) ENGINE = InnoDB,
 PARTITION d20161129 VALUES LESS THAN (1480435200) ENGINE = InnoDB,
 PARTITION d20161130 VALUES LESS THAN (1480521600) ENGINE = InnoDB,
 PARTITION d20161201 VALUES LESS THAN (1480608000) ENGINE = InnoDB,
 PARTITION d20161202 VALUES LESS THAN (1480694400) ENGINE = InnoDB,
 PARTITION d20161203 VALUES LESS THAN (1480780800) ENGINE = InnoDB,
 PARTITION d20161204 VALUES LESS THAN (1480867200) ENGINE = InnoDB,
 PARTITION d20161205 VALUES LESS THAN (1480953600) ENGINE = InnoDB,
 PARTITION d20161206 VALUES LESS THAN (1481040000) ENGINE = InnoDB,
 PARTITION d20161207 VALUES LESS THAN (1481126400) ENGINE = InnoDB,
 PARTITION d20161208 VALUES LESS THAN (1481212800) ENGINE = InnoDB,
 PARTITION d20161209 VALUES LESS THAN (1481299200) ENGINE = InnoDB,
 PARTITION d20161210 VALUES LESS THAN (1481385600) ENGINE = InnoDB,
 PARTITION d20161211 VALUES LESS THAN (1481472000) ENGINE = InnoDB,
 PARTITION d20161212 VALUES LESS THAN (1481558400) ENGINE = InnoDB,
 PARTITION d20161213 VALUES LESS THAN (1481644800) ENGINE = InnoDB,
 PARTITION d20161214 VALUES LESS THAN (1481731200) ENGINE = InnoDB,
 PARTITION d20161215 VALUES LESS THAN (1481817600) ENGINE = InnoDB,
 PARTITION d20161216 VALUES LESS THAN (1481904000) ENGINE = InnoDB,
 PARTITION d20161217 VALUES LESS THAN (1481990400) ENGINE = InnoDB,
 PARTITION d20161218 VALUES LESS THAN (1482076800) ENGINE = InnoDB,
 PARTITION d20161219 VALUES LESS THAN (1482163200) ENGINE = InnoDB,
 PARTITION d20161220 VALUES LESS THAN (1482249600) ENGINE = InnoDB,
 PARTITION d20161221 VALUES LESS THAN (1482336000) ENGINE = InnoDB,
 PARTITION d20161222 VALUES LESS THAN (1482422400) ENGINE = InnoDB,
 PARTITION d20161223 VALUES LESS THAN (1482508800) ENGINE = InnoDB,
 PARTITION d20161224 VALUES LESS THAN (1482595200) ENGINE = InnoDB,
 PARTITION d20161225 VALUES LESS THAN (1482681600) ENGINE = InnoDB,
 PARTITION d20161226 VALUES LESS THAN (1482768000) ENGINE = InnoDB,
 PARTITION d20161227 VALUES LESS THAN (1482854400) ENGINE = InnoDB,
 PARTITION d20161228 VALUES LESS THAN (1482940800) ENGINE = InnoDB,
 PARTITION d20161229 VALUES LESS THAN (1483027200) ENGINE = InnoDB,
 PARTITION d20161230 VALUES LESS THAN (1483113600) ENGINE = InnoDB,
 PARTITION d20161231 VALUES LESS THAN (1483200000) ENGINE = InnoDB,
 PARTITION d20170101 VALUES LESS THAN (1483286400) ENGINE = InnoDB,
 PARTITION d20170102 VALUES LESS THAN (1483372800) ENGINE = InnoDB,
 PARTITION d20170103 VALUES LESS THAN (1483459200) ENGINE = InnoDB,
 PARTITION d20170104 VALUES LESS THAN (1483545600) ENGINE = InnoDB,
 PARTITION d20170105 VALUES LESS THAN (1483632000) ENGINE = InnoDB,
 PARTITION d20170106 VALUES LESS THAN (1483718400) ENGINE = InnoDB,
 PARTITION d20170107 VALUES LESS THAN (1483804800) ENGINE = InnoDB,
 PARTITION d20170108 VALUES LESS THAN (1483891200) ENGINE = InnoDB,
 PARTITION d20170109 VALUES LESS THAN (1483977600) ENGINE = InnoDB,
 PARTITION d20170110 VALUES LESS THAN (1484064000) ENGINE = InnoDB,
 PARTITION d20170111 VALUES LESS THAN (1484150400) ENGINE = InnoDB,
 PARTITION d20170112 VALUES LESS THAN (1484236800) ENGINE = InnoDB,
 PARTITION d20170113 VALUES LESS THAN (1484323200) ENGINE = InnoDB,
 PARTITION d20170114 VALUES LESS THAN (1484409600) ENGINE = InnoDB,
 PARTITION d20170115 VALUES LESS THAN (1484496000) ENGINE = InnoDB,
 PARTITION d20170116 VALUES LESS THAN (1484582400) ENGINE = InnoDB,
 PARTITION d20170117 VALUES LESS THAN (1484668800) ENGINE = InnoDB,
 PARTITION d20170118 VALUES LESS THAN (1484755200) ENGINE = InnoDB,
 PARTITION d20170119 VALUES LESS THAN (1484841600) ENGINE = InnoDB,
 PARTITION d20170120 VALUES LESS THAN (1484928000) ENGINE = InnoDB,
 PARTITION d20170121 VALUES LESS THAN (1485014400) ENGINE = InnoDB,
 PARTITION d20170122 VALUES LESS THAN (1485100800) ENGINE = InnoDB,
 PARTITION d20170123 VALUES LESS THAN (1485187200) ENGINE = InnoDB,
 PARTITION d20170124 VALUES LESS THAN (1485273600) ENGINE = InnoDB,
 PARTITION d20170125 VALUES LESS THAN (1485360000) ENGINE = InnoDB,
 PARTITION d20170126 VALUES LESS THAN (1485446400) ENGINE = InnoDB,
 PARTITION d20170127 VALUES LESS THAN (1485532800) ENGINE = InnoDB) */;

-- 数据导出被取消选择。


-- 导出  表 shop_db.orders_channels 结构
CREATE TABLE IF NOT EXISTS `orders_channels` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `mch_id` int(11) unsigned NOT NULL COMMENT '系统商户号',
  `order_no` varchar(50) NOT NULL COMMENT '平台订单号',
  `trade_type` varchar(16) NOT NULL DEFAULT 'WXPAY.JSAPI' COMMENT '支付类型',
  `channelid` int(11) unsigned NOT NULL COMMENT '渠道ID',
  `total_fee` int(11) unsigned NOT NULL COMMENT '交易总金额',
  `channel_calc_rate` int(5) unsigned NOT NULL COMMENT '该渠道结算费率（万分）',
  `channel_profit_rate` int(5) unsigned NOT NULL COMMENT '该渠道佣金费率（万分）',
  `channel_profit` int(11) unsigned NOT NULL COMMENT '该渠道佣金金额',
  `paytime` int(10) unsigned DEFAULT '0' COMMENT '支付成功时间',
  `writetime` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '订单创建时间',
  PRIMARY KEY (`id`,`writetime`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单与多级渠道关联表'
/*!50100 PARTITION BY RANGE (writetime)
(PARTITION d20161117 VALUES LESS THAN (1479398400) ENGINE = InnoDB,
 PARTITION d20161118 VALUES LESS THAN (1479484800) ENGINE = InnoDB,
 PARTITION d20161119 VALUES LESS THAN (1479571200) ENGINE = InnoDB,
 PARTITION d20161120 VALUES LESS THAN (1479657600) ENGINE = InnoDB,
 PARTITION d20161121 VALUES LESS THAN (1479744000) ENGINE = InnoDB,
 PARTITION d20161122 VALUES LESS THAN (1479830400) ENGINE = InnoDB,
 PARTITION d20161123 VALUES LESS THAN (1479916800) ENGINE = InnoDB,
 PARTITION d20161124 VALUES LESS THAN (1480003200) ENGINE = InnoDB,
 PARTITION d20161125 VALUES LESS THAN (1480089600) ENGINE = InnoDB,
 PARTITION d20161126 VALUES LESS THAN (1480176000) ENGINE = InnoDB,
 PARTITION d20161127 VALUES LESS THAN (1480262400) ENGINE = InnoDB,
 PARTITION d20161128 VALUES LESS THAN (1480348800) ENGINE = InnoDB,
 PARTITION d20161129 VALUES LESS THAN (1480435200) ENGINE = InnoDB,
 PARTITION d20161130 VALUES LESS THAN (1480521600) ENGINE = InnoDB,
 PARTITION d20161201 VALUES LESS THAN (1480608000) ENGINE = InnoDB,
 PARTITION d20161202 VALUES LESS THAN (1480694400) ENGINE = InnoDB,
 PARTITION d20161203 VALUES LESS THAN (1480780800) ENGINE = InnoDB,
 PARTITION d20161204 VALUES LESS THAN (1480867200) ENGINE = InnoDB,
 PARTITION d20161205 VALUES LESS THAN (1480953600) ENGINE = InnoDB,
 PARTITION d20161206 VALUES LESS THAN (1481040000) ENGINE = InnoDB,
 PARTITION d20161207 VALUES LESS THAN (1481126400) ENGINE = InnoDB,
 PARTITION d20161208 VALUES LESS THAN (1481212800) ENGINE = InnoDB,
 PARTITION d20161209 VALUES LESS THAN (1481299200) ENGINE = InnoDB,
 PARTITION d20161210 VALUES LESS THAN (1481385600) ENGINE = InnoDB,
 PARTITION d20161211 VALUES LESS THAN (1481472000) ENGINE = InnoDB,
 PARTITION d20161212 VALUES LESS THAN (1481558400) ENGINE = InnoDB,
 PARTITION d20161213 VALUES LESS THAN (1481644800) ENGINE = InnoDB,
 PARTITION d20161214 VALUES LESS THAN (1481731200) ENGINE = InnoDB,
 PARTITION d20161215 VALUES LESS THAN (1481817600) ENGINE = InnoDB,
 PARTITION d20161216 VALUES LESS THAN (1481904000) ENGINE = InnoDB,
 PARTITION d20161217 VALUES LESS THAN (1481990400) ENGINE = InnoDB,
 PARTITION d20161218 VALUES LESS THAN (1482076800) ENGINE = InnoDB,
 PARTITION d20161219 VALUES LESS THAN (1482163200) ENGINE = InnoDB,
 PARTITION d20161220 VALUES LESS THAN (1482249600) ENGINE = InnoDB,
 PARTITION d20161221 VALUES LESS THAN (1482336000) ENGINE = InnoDB,
 PARTITION d20161222 VALUES LESS THAN (1482422400) ENGINE = InnoDB,
 PARTITION d20161223 VALUES LESS THAN (1482508800) ENGINE = InnoDB,
 PARTITION d20161224 VALUES LESS THAN (1482595200) ENGINE = InnoDB,
 PARTITION d20161225 VALUES LESS THAN (1482681600) ENGINE = InnoDB,
 PARTITION d20161226 VALUES LESS THAN (1482768000) ENGINE = InnoDB,
 PARTITION d20161227 VALUES LESS THAN (1482854400) ENGINE = InnoDB,
 PARTITION d20161228 VALUES LESS THAN (1482940800) ENGINE = InnoDB,
 PARTITION d20161229 VALUES LESS THAN (1483027200) ENGINE = InnoDB,
 PARTITION d20161230 VALUES LESS THAN (1483113600) ENGINE = InnoDB,
 PARTITION d20161231 VALUES LESS THAN (1483200000) ENGINE = InnoDB,
 PARTITION d20170101 VALUES LESS THAN (1483286400) ENGINE = InnoDB,
 PARTITION d20170102 VALUES LESS THAN (1483372800) ENGINE = InnoDB,
 PARTITION d20170103 VALUES LESS THAN (1483459200) ENGINE = InnoDB,
 PARTITION d20170104 VALUES LESS THAN (1483545600) ENGINE = InnoDB,
 PARTITION d20170105 VALUES LESS THAN (1483632000) ENGINE = InnoDB,
 PARTITION d20170106 VALUES LESS THAN (1483718400) ENGINE = InnoDB,
 PARTITION d20170107 VALUES LESS THAN (1483804800) ENGINE = InnoDB,
 PARTITION d20170108 VALUES LESS THAN (1483891200) ENGINE = InnoDB,
 PARTITION d20170109 VALUES LESS THAN (1483977600) ENGINE = InnoDB,
 PARTITION d20170110 VALUES LESS THAN (1484064000) ENGINE = InnoDB,
 PARTITION d20170111 VALUES LESS THAN (1484150400) ENGINE = InnoDB,
 PARTITION d20170112 VALUES LESS THAN (1484236800) ENGINE = InnoDB,
 PARTITION d20170113 VALUES LESS THAN (1484323200) ENGINE = InnoDB,
 PARTITION d20170114 VALUES LESS THAN (1484409600) ENGINE = InnoDB,
 PARTITION d20170115 VALUES LESS THAN (1484496000) ENGINE = InnoDB,
 PARTITION d20170116 VALUES LESS THAN (1484582400) ENGINE = InnoDB,
 PARTITION d20170117 VALUES LESS THAN (1484668800) ENGINE = InnoDB,
 PARTITION d20170118 VALUES LESS THAN (1484755200) ENGINE = InnoDB,
 PARTITION d20170119 VALUES LESS THAN (1484841600) ENGINE = InnoDB,
 PARTITION d20170120 VALUES LESS THAN (1484928000) ENGINE = InnoDB,
 PARTITION d20170121 VALUES LESS THAN (1485014400) ENGINE = InnoDB,
 PARTITION d20170122 VALUES LESS THAN (1485100800) ENGINE = InnoDB,
 PARTITION d20170123 VALUES LESS THAN (1485187200) ENGINE = InnoDB,
 PARTITION d20170124 VALUES LESS THAN (1485273600) ENGINE = InnoDB,
 PARTITION d20170125 VALUES LESS THAN (1485360000) ENGINE = InnoDB,
 PARTITION d20170126 VALUES LESS THAN (1485446400) ENGINE = InnoDB,
 PARTITION d20170127 VALUES LESS THAN (1485532800) ENGINE = InnoDB) */;

-- 数据导出被取消选择。


-- 导出  表 shop_db.orders_refund 结构
CREATE TABLE IF NOT EXISTS `orders_refund` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `mch_id` int(11) unsigned NOT NULL COMMENT '系统商户号',
  `channelid` int(11) unsigned NOT NULL COMMENT '渠道id',
  `salesid` int(11) unsigned DEFAULT '0' COMMENT '业务员id',
  `cashierid` int(11) unsigned DEFAULT '0' COMMENT '收银员id',
  `pay_channel` varchar(16) NOT NULL COMMENT '支付渠道 WXPAY ALIPAY SQPAY',
  `trade_type` varchar(16) NOT NULL DEFAULT 'WXPAY.JSAPI' COMMENT '支付类型',
  `batch_no` tinyint(2) unsigned DEFAULT '1' COMMENT '退款批次号，从1开始',
  `order_no` varchar(50) NOT NULL COMMENT '订单号',
  `refund_no` varchar(50) NOT NULL COMMENT '平台退款单号',
  `out_refund_no` varchar(50) NOT NULL COMMENT '第三方退款单号',
  `refund_id` varchar(50) DEFAULT '' COMMENT '微信退款单号',
  `refund_fee` int(11) unsigned NOT NULL COMMENT '退款金额',
  `total_fee` int(11) unsigned NOT NULL COMMENT '交易总金额',
  `refund_payment_profit` int(11) unsigned NOT NULL COMMENT '支付手续费退款',
  `refund_channel_profit` int(11) unsigned NOT NULL COMMENT '总渠道佣金退款',
  `refund_service_profit` int(11) unsigned NOT NULL COMMENT '技术服务费退款',
  `refund_bm_profit` int(11) unsigned NOT NULL COMMENT '机构清分服务费退款',
  `refund_shop_amount` int(11) unsigned NOT NULL COMMENT '商家所得退款',
  `refund_total_commission` int(11) unsigned NOT NULL COMMENT '总手续费退款',
  `is_all_refund` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '是否全额退款',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1 申请退款 2 微信退款申请成功 -2 审核不通过 3 退款成功 -3 退款失败 4 退款处理中 5 转入代发',
  `writetime` int(10) unsigned NOT NULL COMMENT '申请退款时间',
  `refundtime` int(10) unsigned DEFAULT '0' COMMENT '退款成功时间',
  `refund_from` tinyint(1) unsigned DEFAULT '1' COMMENT '退款请求来源 1 接口 2 平台',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单退款表';

-- 数据导出被取消选择。


-- 导出  表 shop_db.rate_change 结构
CREATE TABLE IF NOT EXISTS `rate_change` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `type` varchar(10) NOT NULL DEFAULT '0' COMMENT 'bm 机构 ch 渠道 mch 商户',
  `accountid` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '账号ID',
  `trade_type` varchar(16) NOT NULL DEFAULT '' COMMENT '支付类型',
  `from` int(5) unsigned NOT NULL DEFAULT '0' COMMENT '从费率X',
  `to` int(5) unsigned NOT NULL DEFAULT '0' COMMENT '改为费率X',
  `status` tinyint(1) NOT NULL DEFAULT '-1' COMMENT '-1 待更新 1 更新成功 -2 更新失败 -3 取消更新',
  `writetime` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '申请时间',
  `updatedate` date NOT NULL COMMENT '预更新日期',
  `updatetime` int(10) unsigned DEFAULT '0' COMMENT '更新时间',
  `extend1` bigint(20) unsigned DEFAULT '0' COMMENT 'bm:service_rate,ch:parent_channelid,mch:channelid',
  `extend2` bigint(20) unsigned DEFAULT '0' COMMENT 'bm:bm_rate,mch:min_amount',
  `extend3` bigint(20) unsigned DEFAULT '0' COMMENT 'mch:max_amount',
  `extend4` bigint(20) unsigned DEFAULT '0' COMMENT 'mch:day_amount',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='费率更新记录';

-- 数据导出被取消选择。


-- 导出  表 shop_db.refund_channels 结构
CREATE TABLE IF NOT EXISTS `refund_channels` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `mch_id` int(11) unsigned NOT NULL COMMENT '系统商户号',
  `refund_no` varchar(50) NOT NULL COMMENT '平台退款单号',
  `trade_type` varchar(16) NOT NULL DEFAULT 'WXPAY.JSAPI' COMMENT '支付类型',
  `channelid` int(11) unsigned NOT NULL COMMENT '渠道ID',
  `refund_fee` int(11) unsigned NOT NULL COMMENT '退款金额',
  `refund_channel_profit` int(11) unsigned NOT NULL COMMENT '该渠道佣金退款',
  `refundtime` int(10) unsigned DEFAULT '0' COMMENT '退款成功时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单退款与多级渠道佣金';

-- 数据导出被取消选择。


-- 导出  表 shop_db.roles 结构
CREATE TABLE IF NOT EXISTS `roles` (
  `roleid` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '权限组id',
  `rolename` varchar(10) NOT NULL COMMENT '权限组名称',
  `type` varchar(5) NOT NULL DEFAULT 'bm' COMMENT 'bm：银行 ch：渠道 mch：商户',
  `parentid` int(11) unsigned NOT NULL COMMENT '父用户id，与type联合',
  `remark` varchar(50) DEFAULT '' COMMENT '备注',
  `creator_id` int(11) unsigned NOT NULL COMMENT '创建者id',
  `creator` varchar(20) NOT NULL COMMENT '创建者用户名',
  `rights` varchar(3200) NOT NULL COMMENT '权限内容 （''all''为所有权限）',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1：启用 -1：停用',
  `writetime` int(10) unsigned NOT NULL COMMENT '入库时间',
  PRIMARY KEY (`roleid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='权限组，针对与子用户';

-- 数据导出被取消选择。


-- 导出  表 shop_db.salesman_daystat 结构
CREATE TABLE IF NOT EXISTS `salesman_daystat` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `salesid` int(11) unsigned NOT NULL COMMENT '业务员id，即子账号id',
  `trade_count` bigint(20) unsigned DEFAULT '0' COMMENT '交易总笔数',
  `trade_amount` bigint(20) unsigned DEFAULT '0' COMMENT '交易总金额(分)',
  `refund_count` bigint(20) unsigned DEFAULT '0' COMMENT '退款总笔数',
  `refund_amount` bigint(20) unsigned DEFAULT '0' COMMENT '退款总额(分)',
  `trade_netamount` bigint(20) DEFAULT '0' COMMENT '交易总净额',
  `channel_profit` bigint(20) DEFAULT '0' COMMENT '佣金净收入',
  `dateflag` date NOT NULL COMMENT '统计日期',
  `writetime` int(10) unsigned NOT NULL COMMENT '写入时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='业务员按天统计';

-- 数据导出被取消选择。


-- 导出  表 shop_db.salesman_stat 结构
CREATE TABLE IF NOT EXISTS `salesman_stat` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `salesid` int(11) unsigned NOT NULL COMMENT '业务员id，即子账号id',
  `trade_count` bigint(20) unsigned DEFAULT '0' COMMENT '交易总笔数',
  `trade_amount` bigint(20) unsigned DEFAULT '0' COMMENT '交易总金额(分)',
  `refund_count` bigint(20) unsigned DEFAULT '0' COMMENT '退款总笔数',
  `refund_amount` bigint(20) unsigned DEFAULT '0' COMMENT '退款总额(分)',
  `trade_netamount` bigint(20) DEFAULT '0' COMMENT '交易总净额',
  `channel_profit` bigint(20) DEFAULT '0' COMMENT '佣金净收入',
  `lastupdatetime` int(10) unsigned NOT NULL COMMENT '最后统计的截止时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='业务员总统计';

-- 数据导出被取消选择。


-- 导出  表 shop_db.settlelog 结构
CREATE TABLE IF NOT EXISTS `settlelog` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `type` varchar(5) NOT NULL DEFAULT 'ch' COMMENT 'bm：银行 ch：渠道 mch：商户',
  `accountid` int(11) unsigned NOT NULL COMMENT '商户或渠道id',
  `trade_count` bigint(20) unsigned DEFAULT '0' COMMENT '交易总笔数',
  `trade_amount` bigint(20) unsigned DEFAULT '0' COMMENT '交易总金额(分)',
  `bank_cardno` varchar(50) NOT NULL COMMENT '结算银行卡号',
  `payed_amount` bigint(20) unsigned DEFAULT '0' COMMENT '结算金额（分）',
  `status` tinyint(1) DEFAULT '-1' COMMENT '-1 待结算 1 已结算',
  `paydate` date NOT NULL COMMENT '结算日期（实际打款时间）',
  `dateflag` date NOT NULL COMMENT '交易日期（一般是昨天）',
  `writetime` int(10) unsigned NOT NULL COMMENT '写入时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='结算表';

-- 数据导出被取消选择。


-- 导出  表 shop_db.settlesetting 结构
CREATE TABLE IF NOT EXISTS `settlesetting` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `type` varchar(5) NOT NULL DEFAULT 'mch' COMMENT 'bm：银行 ch：渠道 mch：商户',
  `accountid` int(11) unsigned NOT NULL COMMENT '商户或渠道id',
  `bank_cardno` varchar(32) NOT NULL COMMENT '银行卡号',
  `bank_owner` varchar(50) NOT NULL COMMENT '开户人',
  `bank_type` varchar(20) NOT NULL COMMENT '开户银行编码',
  `bank_branch` varchar(20) NOT NULL COMMENT '银行支行',
  `branch_no` varchar(32) DEFAULT '' COMMENT '网点号',
  `mobile` varchar(11) DEFAULT '' COMMENT '手机号码',
  `prov` varchar(6) DEFAULT '' COMMENT '支行所在省',
  `city` varchar(6) DEFAULT '' COMMENT '支行所在市',
  `card_no` varchar(32) DEFAULT '' COMMENT '身份证号码',
  `card_pic` varchar(255) DEFAULT '' COMMENT '身份证正反照片',
  `bank_card_pic` varchar(255) DEFAULT '' COMMENT '银行卡照片',
  `cycle_payday` tinyint(2) unsigned DEFAULT '1' COMMENT '打款周期（天），T+N，0为手动提现',
  `is_public` tinyint(1) unsigned DEFAULT '1' COMMENT '结算类型 1对公还是对私(0)银行卡号',
  `writetime` int(10) unsigned NOT NULL COMMENT '入库时间',
  `lastupdatetime` int(10) unsigned DEFAULT '0' COMMENT '最后更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='商户+渠道结算信息配置';

-- 数据导出被取消选择。


-- 导出  表 shop_db.shops 结构
CREATE TABLE IF NOT EXISTS `shops` (
  `mch_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '商户号',
  `mch_key` varchar(32) NOT NULL COMMENT '商户KEY',
  `login_pwd` varchar(32) NOT NULL COMMENT '登录密码',
  `pwd_salt` varchar(6) NOT NULL COMMENT '盐加密',
  `channelid` int(11) unsigned NOT NULL COMMENT '所属渠道',
  `sub_mch_id` varchar(20) DEFAULT '' COMMENT '支付商户号',
  `shop_name` varchar(50) NOT NULL COMMENT '商户名称',
  `shop_sname` varchar(50) DEFAULT '' COMMENT '商户简称',
  `salesid` int(11) unsigned DEFAULT '0' COMMENT '所属业务员',
  `currency_type` tinyint(2) unsigned DEFAULT '1' COMMENT '币种 1：人民币（预删除）',
  `account_type` tinyint(1) unsigned DEFAULT '1' COMMENT '账户类型 1 企业 2 个人',
  `business_type` tinyint(1) unsigned DEFAULT '1' COMMENT '商户类型 1 大客户 2 普通商户 3 直营商户 4 加盟商户',
  `industry_type` int(11) unsigned DEFAULT '0' COMMENT '行业类别ID',
  `creator` varchar(20) DEFAULT '' COMMENT '创建人',
  `creator_id` int(11) unsigned DEFAULT '0' COMMENT '创建者id',
  `prov` varchar(6) DEFAULT '' COMMENT '省份',
  `city` varchar(6) DEFAULT '' COMMENT '城市',
  `dist` varchar(6) DEFAULT '' COMMENT '所在区、县',
  `addr` varchar(50) DEFAULT '' COMMENT '具体地址',
  `email` varchar(50) NOT NULL COMMENT '邮箱',
  `tel` varchar(20) DEFAULT '' COMMENT '电话',
  `homepage` varchar(50) DEFAULT '' COMMENT '网址',
  `headman` varchar(10) DEFAULT '' COMMENT '负责人',
  `headman_idnum` varchar(18) DEFAULT '' COMMENT '负责人身份证号码',
  `headman_mobile` varchar(11) DEFAULT '' COMMENT '负责人手机号码',
  `businesslicence` varchar(32) DEFAULT '' COMMENT '营业执照编码或身份证号',
  `business_pic` varchar(255) DEFAULT '' COMMENT '营业执照片或身份证照片',
  `status` tinyint(1) NOT NULL DEFAULT '0' COMMENT '状态 -1 禁用 1 正常 2 审核中 -2 审核不通过',
  `audit` varchar(20) DEFAULT '' COMMENT '审核人',
  `audit_time` int(10) unsigned DEFAULT '0' COMMENT '审核时间',
  `audit_remark` varchar(50) DEFAULT '' COMMENT '审核备注',
  `writetime` int(10) unsigned NOT NULL COMMENT '入库时间',
  `login_error_count` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '登录错误次数',
  `login_error_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '上次登录错误时间',
  `data_from` tinyint(2) unsigned DEFAULT '1' COMMENT '数据录入来源',
  PRIMARY KEY (`mch_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='商户表';

-- 数据导出被取消选择。


-- 导出  表 shop_db.shop_daystat 结构
CREATE TABLE IF NOT EXISTS `shop_daystat` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `mch_id` int(11) unsigned NOT NULL COMMENT '商户号',
  `channelid` int(11) unsigned NOT NULL COMMENT '所属渠道',
  `ispay` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '0：未结算 1：已经结算',
  `trade_count` bigint(20) unsigned DEFAULT '0' COMMENT '交易总笔数',
  `trade_amount` bigint(20) unsigned DEFAULT '0' COMMENT '交易总金额(分)',
  `refund_count` bigint(20) unsigned DEFAULT '0' COMMENT '退款总笔数',
  `refund_amount` bigint(20) unsigned DEFAULT '0' COMMENT '退款总额(分)',
  `trade_netamount` bigint(20) DEFAULT '0' COMMENT '交易总净额',
  `total_commission` bigint(20) DEFAULT '0' COMMENT '总手续费',
  `needpay_amount` bigint(20) DEFAULT '0' COMMENT '待结算金额',
  `paytime` int(10) unsigned DEFAULT '0' COMMENT '结算时间',
  `pre_paydate` date NOT NULL COMMENT '预打款日期，打款以此为准，针对不同T+N',
  `dateflag` date NOT NULL COMMENT '统计日期（统计某天的交易订单）',
  `writetime` int(10) unsigned NOT NULL COMMENT '写入时间',
  `lastupdatetime` int(10) unsigned NOT NULL COMMENT '最后更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='商家每日统计表';

-- 数据导出被取消选择。


-- 导出  表 shop_db.shop_paysetting 结构
CREATE TABLE IF NOT EXISTS `shop_paysetting` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `mch_id` int(11) unsigned NOT NULL COMMENT '商家号',
  `sub_appid` varchar(20) DEFAULT '' COMMENT '第三方APPID',
  `sub_appsecret` varchar(32) DEFAULT '' COMMENT '第三方APPSECRET',
  `calc_rate` int(5) unsigned NOT NULL COMMENT '结算费率（万分比）',
  `trade_type` varchar(16) NOT NULL DEFAULT 'WXPAY.JSAPI' COMMENT '支付类型',
  `min_amount` int(11) unsigned DEFAULT '0' COMMENT '单笔最小金额',
  `max_amount` int(11) unsigned DEFAULT '0' COMMENT '单笔最大金额',
  `day_amount` int(11) unsigned DEFAULT '0' COMMENT '每日最大金额',
  `writetime` int(10) unsigned NOT NULL COMMENT '入库时间',
  `status` tinyint(1) NOT NULL DEFAULT '2' COMMENT '状态 -1 禁用 1 正常 2 审核中 -2 审核不通过',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='商家结算费率及支付信息配置';

-- 数据导出被取消选择。


-- 导出  表 shop_db.shop_rates 结构
CREATE TABLE IF NOT EXISTS `shop_rates` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `mch_id` int(11) unsigned NOT NULL,
  `trade_type` varchar(16) NOT NULL DEFAULT 'WXPAY.JSAPI' COMMENT '支付类型',
  `calc_rate` int(5) unsigned NOT NULL COMMENT '商户结算费率（万分比）',
  `channelid` int(11) unsigned NOT NULL COMMENT '渠道ID',
  `channel_calc_rate` int(5) unsigned NOT NULL COMMENT '该渠道结算费率（万分）',
  `levels` tinyint(2) unsigned NOT NULL DEFAULT '1' COMMENT '渠道等级',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='商户对应渠道费率';

-- 数据导出被取消选择。


-- 导出  表 shop_db.shop_stat 结构
CREATE TABLE IF NOT EXISTS `shop_stat` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `mch_id` int(11) unsigned NOT NULL COMMENT '商户号',
  `trade_count` bigint(20) unsigned DEFAULT '0' COMMENT '交易总笔数',
  `trade_amount` bigint(20) unsigned DEFAULT '0' COMMENT '交易总金额(分)',
  `refund_count` bigint(20) unsigned DEFAULT '0' COMMENT '退款总笔数',
  `refund_amount` bigint(20) unsigned DEFAULT '0' COMMENT '退款总额(分)',
  `trade_netamount` bigint(20) DEFAULT '0' COMMENT '交易总净额',
  `total_commission` bigint(20) DEFAULT '0' COMMENT '总手续费',
  `total_amount` bigint(20) DEFAULT '0' COMMENT '总共所得',
  `needpay_amount` bigint(20) DEFAULT '0' COMMENT '当前待结算金额（大于一定值结算）',
  `payed_amount` bigint(20) unsigned DEFAULT '0' COMMENT '已结算金额',
  `lastupdatetime` int(10) unsigned NOT NULL COMMENT '最后更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='商家统计总表';

-- 数据导出被取消选择。


-- 导出  表 shop_db.subusers 结构
CREATE TABLE IF NOT EXISTS `subusers` (
  `subuserid` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '子用户id',
  `type` varchar(5) NOT NULL DEFAULT 'bm' COMMENT 'bm：银行 ch：渠道 mch：商户',
  `account_type` tinyint(1) unsigned NOT NULL DEFAULT '1' COMMENT '1：子账号 2： 业务员 3： 收银员',
  `parentid` int(11) unsigned NOT NULL COMMENT '父用户id，与typeid联合',
  `login_name` varchar(20) NOT NULL COMMENT '登录名',
  `login_pwd` varchar(32) NOT NULL COMMENT '登录密码',
  `pwd_salt` varchar(6) NOT NULL COMMENT '盐加密',
  `realname` varchar(10) NOT NULL COMMENT '员工姓名',
  `people_code` varchar(32) DEFAULT '' COMMENT '员工编号',
  `gender` tinyint(1) DEFAULT '1' COMMENT '性别 1 男 2 女',
  `mobile` varchar(11) DEFAULT '' COMMENT '手机号码',
  `email` varchar(50) DEFAULT '' COMMENT '邮箱',
  `idnum` varchar(18) DEFAULT '' COMMENT '身份证号',
  `department` varchar(10) DEFAULT '' COMMENT '部门名称',
  `resign` varchar(10) DEFAULT '' COMMENT '职务',
  `remark` varchar(50) DEFAULT '' COMMENT '备注',
  `superior` int(11) unsigned DEFAULT '0' COMMENT '所属员工id',
  `creator_id` int(11) unsigned NOT NULL COMMENT '创建者id',
  `creator` varchar(20) NOT NULL COMMENT '创建者用户名',
  `roleid` int(11) unsigned NOT NULL COMMENT '权限组id',
  `login_error_count` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '登录错误次数',
  `login_error_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '上次登录错误时间',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1：启用 -1：禁用',
  `writetime` int(10) unsigned NOT NULL COMMENT '入库时间',
  PRIMARY KEY (`subuserid`),
  UNIQUE KEY `login_name` (`login_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='子用户';

-- 数据导出被取消选择。


-- 导出  表 shop_db.sys_daystat 结构
CREATE TABLE IF NOT EXISTS `sys_daystat` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `trade_count` bigint(20) unsigned DEFAULT '0' COMMENT '交易总笔数',
  `trade_amount` bigint(20) unsigned DEFAULT '0' COMMENT '交易总金额(分)',
  `refund_count` bigint(20) unsigned DEFAULT '0' COMMENT '退款总笔数',
  `refund_amount` bigint(20) unsigned DEFAULT '0' COMMENT '退款总额(分)',
  `trade_netamount` bigint(20) DEFAULT '0' COMMENT '交易总净额',
  `total_commission` bigint(20) DEFAULT '0' COMMENT '总手续费',
  `payment_profit` bigint(20) DEFAULT '0' COMMENT '支付手续费',
  `refund_payment_profit` bigint(20) unsigned DEFAULT '0' COMMENT '支付手续费退款',
  `service_profit` bigint(20) DEFAULT '0' COMMENT '技术服务费',
  `refund_service_profit` bigint(20) unsigned DEFAULT '0' COMMENT '技术服务费退款',
  `channel_profit` bigint(20) DEFAULT '0' COMMENT '渠道佣金',
  `refund_channel_profit` bigint(20) unsigned DEFAULT '0' COMMENT '渠道佣金退款',
  `bm_profit` bigint(20) DEFAULT '0' COMMENT '机构清分手续费',
  `refund_bm_profit` bigint(20) unsigned DEFAULT '0' COMMENT '机构清分手续费退款',
  `needpay_serv_amount` bigint(20) DEFAULT '0' COMMENT '待结算金额（至技术服务方）',
  `needpay_bm_amount` bigint(20) DEFAULT '0' COMMENT '待结算金额（至银行机构方）',
  `ispay_serv` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '结算给技术服务方 0：未结算 1：已经结算',
  `ispay_bm` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '结算给银行机构方 0：未结算 1：已经结算',
  `paytime_serv` int(10) unsigned DEFAULT '0' COMMENT '结算时间给技术服务方',
  `paytime_bm` int(10) unsigned DEFAULT '0' COMMENT '结算时间给银行机构方',
  `pre_paydate` date NOT NULL COMMENT '预打款日期，打款以此为准，针对不同T+N',
  `dateflag` date NOT NULL COMMENT '统计日期',
  `writetime` int(10) unsigned NOT NULL COMMENT '写入时间',
  `lastupdatetime` int(10) unsigned NOT NULL COMMENT '最后更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='系统每日统计表';

-- 数据导出被取消选择。


-- 导出  表 shop_db.sys_stat 结构
CREATE TABLE IF NOT EXISTS `sys_stat` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `trade_count` bigint(20) unsigned DEFAULT '0' COMMENT '交易总笔数',
  `trade_amount` bigint(20) unsigned DEFAULT '0' COMMENT '交易总金额(分)',
  `refund_count` bigint(20) unsigned DEFAULT '0' COMMENT '退款总笔数',
  `refund_amount` bigint(20) unsigned DEFAULT '0' COMMENT '退款总额(分)',
  `trade_netamount` bigint(20) DEFAULT '0' COMMENT '交易总净额',
  `total_commission` bigint(20) DEFAULT '0' COMMENT '总手续费',
  `payment_profit` bigint(20) DEFAULT '0' COMMENT '支付手续费',
  `refund_payment_profit` bigint(20) unsigned DEFAULT '0' COMMENT '支付手续费退款',
  `service_profit` bigint(20) DEFAULT '0' COMMENT '技术服务费',
  `refund_service_profit` bigint(20) unsigned DEFAULT '0' COMMENT '技术服务费退款',
  `channel_profit` bigint(20) DEFAULT '0' COMMENT '渠道佣金',
  `refund_channel_profit` bigint(20) unsigned DEFAULT '0' COMMENT '渠道佣金退款',
  `bm_profit` bigint(20) DEFAULT '0' COMMENT '机构清分手续费',
  `refund_bm_profit` bigint(20) unsigned DEFAULT '0' COMMENT '机构清分手续费退款',
  `total_serv_amount` bigint(20) DEFAULT '0' COMMENT '总共所得（技术服务方）',
  `total_bm_amount` bigint(20) DEFAULT '0' COMMENT '总共所得（银行机构方）',
  `needpay_serv_amount` bigint(20) DEFAULT '0' COMMENT '待结算金额（技术服务方）',
  `needpay_bm_amount` bigint(20) DEFAULT '0' COMMENT '待结算金额（银行机构方）',
  `payed_serv_amount` bigint(20) unsigned DEFAULT '0' COMMENT '已结金额（技术服务方）',
  `payed_bm_amount` bigint(20) unsigned DEFAULT '0' COMMENT '已结金额（银行机构方）',
  `lastupdatetime` int(10) unsigned NOT NULL COMMENT '最后更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='系统总统计表';

-- 数据导出被取消选择。


-- 导出  表 shop_db.trade_type 结构
CREATE TABLE IF NOT EXISTS `trade_type` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `pay_channel` varchar(16) NOT NULL DEFAULT 'WXPAY' COMMENT '支付渠道 WXPAY ALIPAY SQPAY',
  `trade_type` varchar(16) NOT NULL DEFAULT 'WXPAY.JSAPI' COMMENT '支付类型 WXPAY.JSAPI  WXPAY.NATIVE WXPAY.APP WXPAY.MICROPAY',
  `pay_service` varchar(50) NOT NULL DEFAULT 'JSAPI' COMMENT '针对支付渠道的支付服务类型 JSAPI APP等',
  `calc_rate` int(5) unsigned NOT NULL DEFAULT '0' COMMENT '与支付渠道的结算费率，即手续费，万分比',
  `service_rate` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '剩余利润之技术服务利润百分比',
  `bm_rate` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '剩余利润之银行清分费率百分比',
  `desc` varchar(16) NOT NULL DEFAULT '' COMMENT '支付类型描述',
  `writetime` int(10) unsigned NOT NULL COMMENT '写入时间',
  `lastupdatetime` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '更新时间',
  `status` tinyint(1) DEFAULT '1' COMMENT '状态 -1 禁用 1 正常',
  PRIMARY KEY (`id`),
  UNIQUE KEY `trade_type` (`trade_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='支付渠道配置';

-- 数据导出被取消选择。
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
