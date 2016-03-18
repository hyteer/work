var http = require('http');
var express    = require('express');        // call express
var app        = express();                 // define our app using express
var bodyParser = require('body-parser');

// configure app to use bodyParser()
// this will let us get the data from a POST
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(bodyParser());

  var data = '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/03/addressing"><soap:Header><wsa:Action></wsa:Action><wsa:MessageID>uuid:1881ca14-135a-4dae-a950-f6b02a69c144</wsa:MessageID><wsa:ReplyTo><wsa:Address>http://schemas.xmlsoap.org/ws/2004/03/addressing/role/anonymous</wsa:Address></wsa:ReplyTo><wsa:To>http://172.25.2.61:50021/yysqz/services/ElectronInvoiceSer</wsa:To></soap:Header><soap:Body><electronInvoice xmlns="http://unientry.sn.tradeswitch.unicom.com"><xml>&lt;ElectronInvoiceInput&gt;&lt;UNI_BSS_HEAD&gt;&lt;ORIG_DOMAIN&gt;PTIS&lt;/ORIG_DOMAIN&gt;&lt;SERVICE_NAME&gt;ElectronInvoiceSer&lt;/SERVICE_NAME&gt;&lt;OPERATE_NAME&gt;electronInvoice&lt;/OPERATE_NAME&gt;&lt;ACTION_CODE&gt;0&lt;/ACTION_CODE&gt;&lt;ACTION_RELATION&gt;0&lt;/ACTION_RELATION&gt;&lt;ROUTING&gt;&lt;ROUTE_TYPE&gt;36&lt;/ROUTE_TYPE&gt;&lt;ROUTE_VALUE&gt;18674453342&lt;/ROUTE_VALUE&gt;&lt;/ROUTING&gt;&lt;PROC_ID&gt;seq00001&lt;/PROC_ID&gt;&lt;TRANS_IDO&gt;seq00001&lt;/TRANS_IDO&gt;&lt;TRANS_IDH&gt;&lt;/TRANS_IDH&gt;&lt;PROCESS_TIME&gt;201603111704001&lt;/PROCESS_TIME&gt;&lt;RESPONSE&gt;&lt;RSP_TYPE&gt;&lt;/RSP_TYPE&gt;&lt;RSP_CODE&gt;&lt;/RSP_CODE&gt;&lt;RSP_DESC&gt;&lt;/RSP_DESC&gt;&lt;/RESPONSE&gt;&lt;COM_BUS_INFO&gt;&lt;OPER_ID&gt;yanff&lt;/OPER_ID&gt;&lt;PROVINCE_CODE&gt;0002&lt;/PROVINCE_CODE&gt;&lt;EPARCHY_CODE&gt;地市代码表&lt;/EPARCHY_CODE&gt;&lt;CITY_CODE&gt;区县编码&lt;/CITY_CODE&gt;&lt;CHANNEL_ID&gt;渠道编码&lt;/CHANNEL_ID&gt;&lt;ACCESS_TYPE&gt;1&lt;/ACCESS_TYPE&gt;&lt;ORDER_TYPE&gt;1&lt;/ORDER_TYPE&gt;&lt;/COM_BUS_INFO&gt;&lt;SP_RESERVE&gt;&lt;TRANS_IDC&gt;ECIP0002seq00001&lt;/TRANS_IDC&gt;&lt;CUTOFFDAY&gt;20080608&lt;/CUTOFFDAY&gt;&lt;OSNDUNS&gt;0002&lt;/OSNDUNS&gt;&lt;HSNDUNS&gt;1100&lt;/HSNDUNS&gt;&lt;CONV_ID&gt;ECIP0002seq00001200806081200111&lt;/CONV_ID&gt;&lt;/SP_RESERVE&gt;&lt;TEST_FLAG&gt;0&lt;/TEST_FLAG&gt;&lt;MSG_SENDER&gt;1100&lt;/MSG_SENDER&gt;&lt;MSG_RECEIVER&gt;1101&lt;/MSG_RECEIVER&gt;&lt;/UNI_BSS_HEAD&gt;&lt;UNI_BSS_BODY&gt;&lt;ELECTRON_INVOICE_REQ&gt;&lt;INVOICE_REQ_ID&gt;lyl{lsh}&lt;/INVOICE_REQ_ID&gt;&lt;MAKE_INVOICE_TYPE&gt;0&lt;/MAKE_INVOICE_TYPE&gt;&lt;SELLER_TAXPAYER_ID&gt;440300568519737&lt;/SELLER_TAXPAYER_ID&gt;&lt;SELLER_NAME&gt;电子发票测试&lt;/SELLER_NAME&gt;&lt;SELLER_ADD&gt;深圳市南山区南海大道1057号科技大厦二期A栋601房&lt;/SELLER_ADD&gt;&lt;SELLER_PHONE&gt;0755-26027907&lt;/SELLER_PHONE&gt;&lt;SELLER_BANK_ACCOUNT&gt;31001669701052502638&lt;/SELLER_BANK_ACCOUNT&gt;&lt;BUYER_TAXPAYER_ID&gt;&lt;/BUYER_TAXPAYER_ID&gt;&lt;BUYER_NAME&gt;张三&lt;/BUYER_NAME&gt;&lt;BUYER_ADD&gt;深圳市南山区深南大道1057号科技大厦二期A栋6888房&lt;/BUYER_ADD&gt;&lt;BUYER_BANK_ACCOUNT&gt;98888888701052502638&lt;/BUYER_BANK_ACCOUNT&gt;&lt;BUYER_PHONE&gt;18888888888&lt;/BUYER_PHONE&gt;&lt;BUYER_EMAIL&gt;test@fapiao.com&lt;/BUYER_EMAIL&gt;&lt;WRITE_MANAGER&gt;admin&lt;/WRITE_MANAGER&gt;&lt;RECE_FEE_MANAGER&gt;admin&lt;/RECE_FEE_MANAGER&gt;&lt;CHECK_MANAGER&gt;admin&lt;/CHECK_MANAGER&gt;&lt;ORG_INVOICE_CODE&gt;&lt;/ORG_INVOICE_CODE&gt;&lt;ORG_INVOICE_NUM&gt;&lt;/ORG_INVOICE_NUM&gt;&lt;TOTAL_PRICE_TAX&gt;117&lt;/TOTAL_PRICE_TAX&gt;&lt;TOTAL_FEE&gt;100&lt;/TOTAL_FEE&gt;&lt;TOTAL_TAX_PAY&gt;17&lt;/TOTAL_TAX_PAY&gt;&lt;PROJECT_INFO&gt;&lt;INVOICE_COMPANY_NATURE&gt;0&lt;/INVOICE_COMPANY_NATURE&gt;&lt;PROJECT_NAME&gt;洗衣粉&lt;/PROJECT_NAME&gt;&lt;UNIT&gt;袋&lt;/UNIT&gt;&lt;MODEL&gt;500克&lt;/MODEL&gt;&lt;PROJECT_COUNT&gt;1&lt;/PROJECT_COUNT&gt;&lt;PROJECT_UNIT_PRICE&gt;100&lt;/PROJECT_UNIT_PRICE&gt;&lt;PROJECT_FEE&gt;100&lt;/PROJECT_FEE&gt;&lt;TAX_RATE&gt;0.17&lt;/TAX_RATE&gt;&lt;TAX_PAY&gt;17&lt;/TAX_PAY&gt;&lt;/PROJECT_INFO&gt;&lt;PARA&gt;&lt;PARA_ID&gt;保留字段ID&lt;/PARA_ID&gt;&lt;PARA_VALUE&gt;保留字段值&lt;/PARA_VALUE&gt;&lt;/PARA&gt;&lt;/ELECTRON_INVOICE_REQ&gt;&lt;/UNI_BSS_BODY&gt;&lt;UNI_BSS_ATTACHED&gt;&lt;MEDIA_INFO&gt;&lt;/MEDIA_INFO&gt;&lt;/UNI_BSS_ATTACHED&gt;&lt;/ElectronInvoiceInput&gt;</xml></electronInvoice></soap:Body></soap:Envelope>';

  var options = {
     host: '172.25.2.61', port:50021,
	 path: '/yysqz/services/ElectronInvoiceSer',
     method: 'POST',
     headers: {
    'Content-Type': 'text/xml',
    'Content-Length': data.length
    }
  };

  var req = http.request(options, function(res)
  {
      res.setEncoding('utf8');
      res.on('data', function (chunk) {
     console.log("body: " + chunk);
   });
  });
  req.write(data);
  req.end();