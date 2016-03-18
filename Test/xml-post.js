var http=require('http');
var qs=require('querystring');
 
//var post_data={a:123,time:new Date().getTime()};//这是需要提交的数据
var content='<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/03/addressing"><soap:Header><wsa:Action></wsa:Action><wsa:MessageID>uuid:1881ca14-135a-4dae-a950-f6b02a69c144</wsa:MessageID><wsa:ReplyTo><wsa:Address>http://schemas.xmlsoap.org/ws/2004/03/addressing/role/anonymous</wsa:Address></wsa:ReplyTo><wsa:To>http://172.25.2.61:50021/yysqz/services/ElectronInvoiceSer</wsa:To></soap:Header><soap:Body><electronInvoice xmlns="http://unientry.sn.tradeswitch.unicom.com"><xml>&lt;ElectronInvoiceInput&gt;&lt;UNI_BSS_HEAD&gt;&lt;ORIG_DOMAIN&gt;PTIS&lt;/ORIG_DOMAIN&gt;&lt;SERVICE_NAME&gt;ElectronInvoiceSer&lt;/SERVICE_NAME&gt;&lt;OPERATE_NAME&gt;electronInvoice&lt;/OPERATE_NAME&gt;&lt;ACTION_CODE&gt;0&lt;/ACTION_CODE&gt;&lt;ACTION_RELATION&gt;0&lt;/ACTION_RELATION&gt;&lt;ROUTING&gt;&lt;ROUTE_TYPE&gt;36&lt;/ROUTE_TYPE&gt;&lt;ROUTE_VALUE&gt;18674453342&lt;/ROUTE_VALUE&gt;&lt;/ROUTING&gt;&lt;PROC_ID&gt;seq00001&lt;/PROC_ID&gt;&lt;TRANS_IDO&gt;seq00001&lt;/TRANS_IDO&gt;&lt;TRANS_IDH&gt;&lt;/TRANS_IDH&gt;&lt;PROCESS_TIME&gt;201603111704001&lt;/PROCESS_TIME&gt;&lt;RESPONSE&gt;&lt;RSP_TYPE&gt;&lt;/RSP_TYPE&gt;&lt;RSP_CODE&gt;&lt;/RSP_CODE&gt;&lt;RSP_DESC&gt;&lt;/RSP_DESC&gt;&lt;/RESPONSE&gt;&lt;COM_BUS_INFO&gt;&lt;OPER_ID&gt;yanff&lt;/OPER_ID&gt;&lt;PROVINCE_CODE&gt;0002&lt;/PROVINCE_CODE&gt;&lt;EPARCHY_CODE&gt;地市代码表&lt;/EPARCHY_CODE&gt;&lt;CITY_CODE&gt;区县编码&lt;/CITY_CODE&gt;&lt;CHANNEL_ID&gt;渠道编码&lt;/CHANNEL_ID&gt;&lt;ACCESS_TYPE&gt;1&lt;/ACCESS_TYPE&gt;&lt;ORDER_TYPE&gt;1&lt;/ORDER_TYPE&gt;&lt;/COM_BUS_INFO&gt;&lt;SP_RESERVE&gt;&lt;TRANS_IDC&gt;ECIP0002seq00001&lt;/TRANS_IDC&gt;&lt;CUTOFFDAY&gt;20080608&lt;/CUTOFFDAY&gt;&lt;OSNDUNS&gt;0002&lt;/OSNDUNS&gt;&lt;HSNDUNS&gt;1100&lt;/HSNDUNS&gt;&lt;CONV_ID&gt;ECIP0002seq00001200806081200111&lt;/CONV_ID&gt;&lt;/SP_RESERVE&gt;&lt;TEST_FLAG&gt;0&lt;/TEST_FLAG&gt;&lt;MSG_SENDER&gt;1100&lt;/MSG_SENDER&gt;&lt;MSG_RECEIVER&gt;1101&lt;/MSG_RECEIVER&gt;&lt;/UNI_BSS_HEAD&gt;&lt;UNI_BSS_BODY&gt;&lt;ELECTRON_INVOICE_REQ&gt;&lt;INVOICE_REQ_ID&gt;lyl{lsh}&lt;/INVOICE_REQ_ID&gt;&lt;MAKE_INVOICE_TYPE&gt;0&lt;/MAKE_INVOICE_TYPE&gt;&lt;SELLER_TAXPAYER_ID&gt;440300568519737&lt;/SELLER_TAXPAYER_ID&gt;&lt;SELLER_NAME&gt;电子发票测试&lt;/SELLER_NAME&gt;&lt;SELLER_ADD&gt;深圳市南山区南海大道1057号科技大厦二期A栋601房&lt;/SELLER_ADD&gt;&lt;SELLER_PHONE&gt;0755-26027907&lt;/SELLER_PHONE&gt;&lt;SELLER_BANK_ACCOUNT&gt;31001669701052502638&lt;/SELLER_BANK_ACCOUNT&gt;&lt;BUYER_TAXPAYER_ID&gt;&lt;/BUYER_TAXPAYER_ID&gt;&lt;BUYER_NAME&gt;张三&lt;/BUYER_NAME&gt;&lt;BUYER_ADD&gt;深圳市南山区深南大道1057号科技大厦二期A栋6888房&lt;/BUYER_ADD&gt;&lt;BUYER_BANK_ACCOUNT&gt;98888888701052502638&lt;/BUYER_BANK_ACCOUNT&gt;&lt;BUYER_PHONE&gt;18888888888&lt;/BUYER_PHONE&gt;&lt;BUYER_EMAIL&gt;test@fapiao.com&lt;/BUYER_EMAIL&gt;&lt;WRITE_MANAGER&gt;admin&lt;/WRITE_MANAGER&gt;&lt;RECE_FEE_MANAGER&gt;admin&lt;/RECE_FEE_MANAGER&gt;&lt;CHECK_MANAGER&gt;admin&lt;/CHECK_MANAGER&gt;&lt;ORG_INVOICE_CODE&gt;&lt;/ORG_INVOICE_CODE&gt;&lt;ORG_INVOICE_NUM&gt;&lt;/ORG_INVOICE_NUM&gt;&lt;TOTAL_PRICE_TAX&gt;117&lt;/TOTAL_PRICE_TAX&gt;&lt;TOTAL_FEE&gt;100&lt;/TOTAL_FEE&gt;&lt;TOTAL_TAX_PAY&gt;17&lt;/TOTAL_TAX_PAY&gt;&lt;PROJECT_INFO&gt;&lt;INVOICE_COMPANY_NATURE&gt;0&lt;/INVOICE_COMPANY_NATURE&gt;&lt;PROJECT_NAME&gt;洗衣粉&lt;/PROJECT_NAME&gt;&lt;UNIT&gt;袋&lt;/UNIT&gt;&lt;MODEL&gt;500克&lt;/MODEL&gt;&lt;PROJECT_COUNT&gt;1&lt;/PROJECT_COUNT&gt;&lt;PROJECT_UNIT_PRICE&gt;100&lt;/PROJECT_UNIT_PRICE&gt;&lt;PROJECT_FEE&gt;100&lt;/PROJECT_FEE&gt;&lt;TAX_RATE&gt;0.17&lt;/TAX_RATE&gt;&lt;TAX_PAY&gt;17&lt;/TAX_PAY&gt;&lt;/PROJECT_INFO&gt;&lt;PARA&gt;&lt;PARA_ID&gt;保留字段ID&lt;/PARA_ID&gt;&lt;PARA_VALUE&gt;保留字段值&lt;/PARA_VALUE&gt;&lt;/PARA&gt;&lt;/ELECTRON_INVOICE_REQ&gt;&lt;/UNI_BSS_BODY&gt;&lt;UNI_BSS_ATTACHED&gt;&lt;MEDIA_INFO&gt;&lt;/MEDIA_INFO&gt;&lt;/UNI_BSS_ATTACHED&gt;&lt;/ElectronInvoiceInput&gt;</xml></electronInvoice></soap:Body></soap:Envelope>';
//var content='<ElectronInvoiceInput><UNI_BSS_HEAD><ORIG_DOMAIN>PTIS</ORIG_DOMAIN><SERVICE_NAME>ElectronInvoiceSer</SERVICE_NAME><OPERATE_NAME>electronInvoice</OPERATE_NAME><ACTION_CODE>0</ACTION_CODE><ACTION_RELATION>0</ACTION_RELATION><ROUTING><ROUTE_TYPE>36</ROUTE_TYPE><ROUTE_VALUE>18674453342</ROUTE_VALUE></ROUTING><PROC_ID>seq00001</PROC_ID><TRANS_IDO>seq00001</TRANS_IDO><TRANS_IDH></TRANS_IDH><PROCESS_TIME>201603111704001</PROCESS_TIME><RESPONSE><RSP_TYPE></RSP_TYPE><RSP_CODE></RSP_CODE><RSP_DESC></RSP_DESC></RESPONSE><COM_BUS_INFO><OPER_ID>yanff</OPER_ID><PROVINCE_CODE>0002</PROVINCE_CODE><EPARCHY_CODE>地市代码表</EPARCHY_CODE><CITY_CODE>区县编码</CITY_CODE><CHANNEL_ID>渠道编码</CHANNEL_ID><ACCESS_TYPE>1</ACCESS_TYPE><ORDER_TYPE>1</ORDER_TYPE></COM_BUS_INFO><SP_RESERVE><TRANS_IDC>ECIP0002seq00001</TRANS_IDC><CUTOFFDAY>20080608</CUTOFFDAY><OSNDUNS>0002</OSNDUNS><HSNDUNS>1100</HSNDUNS><CONV_ID>ECIP0002seq00001200806081200111</CONV_ID></SP_RESERVE><TEST_FLAG>0</TEST_FLAG><MSG_SENDER>1100</MSG_SENDER><MSG_RECEIVER>1101</MSG_RECEIVER></UNI_BSS_HEAD><UNI_BSS_BODY><ELECTRON_INVOICE_REQ><INVOICE_REQ_ID>lyl{lsh}</INVOICE_REQ_ID><MAKE_INVOICE_TYPE>0</MAKE_INVOICE_TYPE><SELLER_TAXPAYER_ID>440300568519737</SELLER_TAXPAYER_ID><SELLER_NAME>电子发票测试-LR</SELLER_NAME><SELLER_ADD>深圳市南山区南海大道1057号科技大厦二期A栋601房</SELLER_ADD><SELLER_PHONE>0755-26027907</SELLER_PHONE><SELLER_BANK_ACCOUNT>31001669701052502638</SELLER_BANK_ACCOUNT><BUYER_TAXPAYER_ID></BUYER_TAXPAYER_ID><BUYER_NAME>张三</BUYER_NAME><BUYER_ADD>深圳市南山区深南大道1057号科技大厦二期A栋6888房</BUYER_ADD><BUYER_BANK_ACCOUNT>98888888701052502638</BUYER_BANK_ACCOUNT><BUYER_PHONE>18888888888</BUYER_PHONE><BUYER_EMAIL>test@fapiao.com</BUYER_EMAIL><WRITE_MANAGER>admin</WRITE_MANAGER><RECE_FEE_MANAGER>admin</RECE_FEE_MANAGER><CHECK_MANAGER>admin</CHECK_MANAGER><ORG_INVOICE_CODE></ORG_INVOICE_CODE><ORG_INVOICE_NUM></ORG_INVOICE_NUM><TOTAL_PRICE_TAX>117</TOTAL_PRICE_TAX><TOTAL_FEE>100</TOTAL_FEE><TOTAL_TAX_PAY>17</TOTAL_TAX_PAY><PROJECT_INFO><INVOICE_COMPANY_NATURE>0</INVOICE_COMPANY_NATURE><PROJECT_NAME>洗衣粉</PROJECT_NAME><UNIT>袋</UNIT><MODEL>500克</MODEL><PROJECT_COUNT>1</PROJECT_COUNT><PROJECT_UNIT_PRICE>100</PROJECT_UNIT_PRICE><PROJECT_FEE>100</PROJECT_FEE><TAX_RATE>0.17</TAX_RATE><TAX_PAY>17</TAX_PAY></PROJECT_INFO><PARA><PARA_ID>保留字段ID</PARA_ID><PARA_VALUE>保留字段值</PARA_VALUE></PARA></ELECTRON_INVOICE_REQ></UNI_BSS_BODY><UNI_BSS_ATTACHED><MEDIA_INFO></MEDIA_INFO></UNI_BSS_ATTACHED></ElectronInvoiceInput>';
//var content=qs.stringify(post_data);
 
var options = {
  host: '127.0.0.1',
  port: 8888,
  path: 'http://172.25.2.61:50021/yysqz/services/ElectronInvoiceSer',
 // path: '/yysqz/services/ElectronInvoiceSer',
  method: 'POST',
  headers:{
  'Content-Type':'text/xml;charset=utf-8',
  'Content-Length':content.length,
  'SOAPAction':'""',
  'Connection': 'Keep-Alive',
  'Accept-Encoding': 'gzip,deflate',
  'User-Agent': 'Apache-HttpClient/4.1.1 (java 1.5)'
  }
};
console.log("post options:\n",options);
console.log("content:",content);
console.log("\n");
 
var req = http.request(options, function(res) {
  console.log("statusCode: ", res.statusCode);
  console.log("headers: ", res.headers);
  var _data='';
  res.on('data', function(chunk){
     _data += chunk;
  });
  res.on('end', function(){
     console.log("\n--->>\nresult:",_data)
   });
});
 
req.write(content);
req.end();