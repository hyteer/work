#include "replace.h"
#include "yt.h"
Action()
{

//	lr_start_transaction("kp");


	web_service_call( "StepName=electronInvoice_102",
		"SOAPMethod=ElectronInvoiceSer|ElectronInvoiceSerHttpPort|electronInvoice",
		"ResponseParam=response",
		"Service=ElectronInvoiceSer",
		"ExpectedResponse=SoapResult",
		"Snapshot=t1457769024.inf",
		BEGIN_ARGUMENTS,
		"xml=<ElectronInvoiceInput><UNI_BSS_HEAD><ORIG_DOMAIN>PTIS</ORIG_DOMAIN><SERVICE_NAME>ElectronInvoiceSer</SERVICE_NAME><OPERATE_NAME>electronInvoice</OPERATE_NAME><ACTION_CODE>0</ACTION_CODE><ACTION_RELATION>0</ACTION_RELATION><ROUTING><ROUTE_TYPE>36</ROUTE_TYPE><ROUTE_VALUE>18674453342</ROUTE_VALUE></ROUTING><PROC_ID>seq00001</PROC_ID><TRANS_IDO>seq00001</TRANS_IDO><TRANS_IDH></TRANS_IDH><PROCESS_TIME>201603111704001</PROCESS_TIME><RESPONSE><RSP_TYPE></RSP_TYPE><RSP_CODE></RSP_CODE><RSP_DESC></RSP_DESC></RESPONSE><COM_BUS_INFO><OPER_ID>yanff</OPER_ID><PROVINCE_CODE>0002</PROVINCE_CODE><EPARCHY_CODE>地市代码表</EPARCHY_CODE><CITY_CODE>区县编码</CITY_CODE><CHANNEL_ID>渠道编码</CHANNEL_ID><ACCESS_TYPE>1</ACCESS_TYPE><ORDER_TYPE>1</ORDER_TYPE></COM_BUS_INFO><SP_RESERVE><TRANS_IDC>ECIP0002seq00001</TRANS_IDC><CUTOFFDAY>20080608</CUTOFFDAY><OSNDUNS>0002</OSNDUNS><HSNDUNS>1100</HSNDUNS><CONV_ID>ECIP0002seq00001200806081200111</CONV_ID></SP_RESERVE><TEST_FLAG>0</TEST_FLAG><MSG_SENDER>1100</MSG_SENDER><MSG_RECEIVER>1101</MSG_RECEIVER></UNI_BSS_HEAD><UNI_BSS_BODY><ELECTRON_INVOICE_REQ><INVOICE_REQ_ID>lyl{lsh}</INVOICE_REQ_ID><MAKE_INVOICE_TYPE>0</MAKE_INVOICE_TYPE><SELLER_TAXPAYER_ID>440300568519737</SELLER_TAXPAYER_ID><SELLER_NAME>电子发票测试</SELLER_NAME><SELLER_ADD>深圳市南山区南海大道1057号科技大厦二期A栋601房</SELLER_ADD><SELLER_PHONE>0755-26027907</SELLER_PHONE><SELLER_BANK_ACCOUNT>31001669701052502638</SELLER_BANK_ACCOUNT><BUYER_TAXPAYER_ID></BUYER_TAXPAYER_ID><BUYER_NAME>张三</BUYER_NAME><BUYER_ADD>深圳市南山区深南大道1057号科技大厦二期A栋6888房</BUYER_ADD><BUYER_BANK_ACCOUNT>98888888701052502638</BUYER_BANK_ACCOUNT><BUYER_PHONE>18888888888</BUYER_PHONE><BUYER_EMAIL>test@fapiao.com</BUYER_EMAIL><WRITE_MANAGER>admin</WRITE_MANAGER><RECE_FEE_MANAGER>admin</RECE_FEE_MANAGER><CHECK_MANAGER>admin</CHECK_MANAGER><ORG_INVOICE_CODE></ORG_INVOICE_CODE><ORG_INVOICE_NUM></ORG_INVOICE_NUM><TOTAL_PRICE_TAX>117</TOTAL_PRICE_TAX><TOTAL_FEE>100</TOTAL_FEE><TOTAL_TAX_PAY>17</TOTAL_TAX_PAY><PROJECT_INFO><INVOICE_COMPANY_NATURE>0</INVOICE_COMPANY_NATURE><PROJECT_NAME>洗衣粉</PROJECT_NAME><UNIT>袋</UNIT><MODEL>500克</MODEL><PROJECT_COUNT>1</PROJECT_COUNT><PROJECT_UNIT_PRICE>100</PROJECT_UNIT_PRICE><PROJECT_FEE>100</PROJECT_FEE><TAX_RATE>0.17</TAX_RATE><TAX_PAY>17</TAX_PAY></PROJECT_INFO><PARA><PARA_ID>保留字段ID</PARA_ID><PARA_VALUE>保留字段值</PARA_VALUE></PARA></ELECTRON_INVOICE_REQ></UNI_BSS_BODY><UNI_BSS_ATTACHED><MEDIA_INFO></MEDIA_INFO></UNI_BSS_ATTACHED></ElectronInvoiceInput>",
		END_ARGUMENTS,
		BEGIN_RESULT,
		"out=Param_out",
		END_RESULT,
		LAST);

//	lr_save_string( lr_eval_string("{Param_out}"),"a" );
	//lr_output_message("Result-->:%s",lr_eval_string({Param_out})_)
	lr_output_message("【result】:%s", lr_eval_string("{Param_out}"));


	

	lr_save_string( lr_eval_string("{Param_out}"),"a" );
	lr_output_message("【String a is】:%s", lr_eval_string("{a}"));
	

	lr_replace("a","&lt;","<" );
	lr_replace( "a","&gt;",">" );
	lr_output_message("【#2 String a is】:%s", lr_eval_string("{a}"));

	//*********【lr_xml_get_values】Start Temp Test***********************

	yt="<employee><name>John Smith</name><cubicle>227</cubicle></employee>";

	lr_output_message("【Test-YT】:%s",yt);

     lr_save_string(yt, "XML_Input_Param"); // Save input as parameter

     lr_xml_get_values("XML={XML_Input_Param}",
          "ValueParam=OutputParam",
          "Query=/employee/name",
          LAST );

     lr_output_message(lr_eval_string("Query result = {OutputParam}"));

	 //************End Temp Test***********************

//*********【Electron Invoice】***********************

 
	xml_res="<ElectronInvoiceOutput><UNI_BSS_HEAD><ORIG_DOMAIN>PTIS</ORIG_DOMAIN><SERVICE_NAME>ElectronInvoiceSer</SERVICE_NAME><OPERATE_NAME>electronInvoice</OPERATE_NAME><ORIG_DOMAIN>PTIS</ORIG_DOMAIN><ACTION_CODE>1</ACTION_CODE><ACTION_RELATION>0</ACTION_RELATION><ROUTING><ROUTE_TYPE></ROUTE_TYPE><ROUTE_VALUE></ROUTE_VALUE></ROUTING><PROC_ID>seq00001</PROC_ID><TRANS_IDO>seq00001</TRANS_IDO><TRANS_IDH></TRANS_IDH><PROCESS_TIME>201603111704001</PROCESS_TIME><RESPONSE><RSP_TYPE></RSP_TYPE><RSP_CODE></RSP_CODE><RSP_DESC></RSP_DESC></RESPONSE><COM_BUS_INFO><OPER_ID></OPER_ID><PROVINCE_CODE></PROVINCE_CODE><EPARCHY_CODE></EPARCHY_CODE><CITY_CODE></CITY_CODE><CHANNEL_ID></CHANNEL_ID><ACCESS_TYPE></ACCESS_TYPE><ORDER_TYPE></ORDER_TYPE></COM_BUS_INFO><SP_RESERVE><TRANS_IDC></TRANS_IDC><CUTOFFDAY></CUTOFFDAY><OSNDUNS></OSNDUNS><HSNDUNS></HSNDUNS><CONV_ID></CONV_ID></SP_RESERVE><TEST_FLAG>0</TEST_FLAG><MSG_SENDER>1100</MSG_SENDER><MSG_RECEIVER>1101</MSG_RECEIVER></UNI_BSS_HEAD><UNI_BSS_BODY><ELECTRON_INVOICE_RSP><RESP_CODE>0000</RESP_CODE><RESP_DESC>成功</RESP_DESC><INVOICE_REQ_ID>lyl{lsh}</INVOICE_REQ_ID><INVOICE_INFO><INVOICE_CODE>000003521012</INVOICE_CODE><INVOICE_NUM>00407595</INVOICE_NUM><MAKE_INVOICE_TIME>20160316161526</MAKE_INVOICE_TIME><TAX_EQUIPMENT_NUM>499099900038</TAX_EQUIPMENT_NUM><TWO_DIMENSION_CODE><![CDATA[]]></TWO_DIMENSION_CODE><INVOICE_CIPHERTEXT><![CDATA[03-8-1/>-9+26-680/-0728>/6134/+49-80059042/*<348845/70-+9*-8-1/>-9+26-680/>3<<0-9838-36><692*201-54119*98874*036]]></INVOICE_CIPHERTEXT><INVOICE_CHECK_CODE>3543204179235341814398218</INVOICE_CHECK_CODE><INVOICE_URL><![CDATA[http://172.25.2.61:50023/download/downloadController/download?request=nvg6d5oscoMeZ2n91NYsIbL.ptK3sS1BmpwJYtYQKyo4mDnc5OyhlW1kqfLbuJ3C%5EbEheBefDa]]></INVOICE_URL></INVOICE_INFO><PARA><PARA_ID></PARA_ID><PARA_VALUE></PARA_VALUE></PARA></ELECTRON_INVOICE_RSP></UNI_BSS_BODY><UNI_BSS_ATTACHED><MEDIA_INFO></MEDIA_INFO></UNI_BSS_ATTACHED></ElectronInvoiceOutput>";
	//xml_res="<ElectronInvoiceOutput><UNI_BSS_HEAD><ORIG_DOMAIN>PTIS</ORIG_DOMAIN><SERVICE_NAME>电子发票系统</SERVICE_NAME><OPERATE_NAME>electronInvoice</OPERATE_NAME><ORIG_DOMAIN>PTIS</ORIG_DOMAIN><ACTION_CODE>1</ACTION_CODE><ACTION_RELATION>0</ACTION_RELATION><ROUTING><ROUTE_TYPE></ROUTE_TYPE><ROUTE_VALUE></ROUTE_VALUE></ROUTING><PROC_ID>seq00001</PROC_ID><TRANS_IDO>seq00001</TRANS_IDO><TRANS_IDH></TRANS_IDH><PROCESS_TIME>201603111704001</PROCESS_TIME><RESPONSE><RSP_TYPE></RSP_TYPE><RSP_CODE></RSP_CODE><RSP_DESC></RSP_DESC></RESPONSE><COM_BUS_INFO><OPER_ID></OPER_ID><PROVINCE_CODE></PROVINCE_CODE><EPARCHY_CODE></EPARCHY_CODE><CITY_CODE></CITY_CODE><CHANNEL_ID></CHANNEL_ID><ACCESS_TYPE></ACCESS_TYPE><ORDER_TYPE></ORDER_TYPE></COM_BUS_INFO><SP_RESERVE><TRANS_IDC></TRANS_IDC><CUTOFFDAY></CUTOFFDAY><OSNDUNS></OSNDUNS><HSNDUNS></HSNDUNS><CONV_ID></CONV_ID></SP_RESERVE><TEST_FLAG>0</TEST_FLAG><MSG_SENDER>1100</MSG_SENDER><MSG_RECEIVER>1101</MSG_RECEIVER></UNI_BSS_HEAD></ElectronInvoiceOutput>";
	  lr_convert_string_encoding(xml_res,LR_ENC_SYSTEM_LOCALE,LR_ENC_UTF8,"xml_input");
	lr_output_message("【Test-ElectronInoice】:%s",lr_eval_string("Query result = {xml_input}"));

    // lr_save_string(lr_eval_string("{xml_input}"),"XML_E_Invoice")); // Save input as parameter

    lr_xml_get_values("XML={xml_input}",
          "ValueParam=XML_Out",
          "Query=/ElectronInvoiceOutput/UNI_BSS_BODY/ELECTRON_INVOICE_RSP/RESP_CODE",
          LAST );
   /*  lr_xml_get_values("XML={xml_input}", 
              "ValueParam=XML_Out", 
              "Query=/ElectronInvoiceOutput/UNI_BSS_HEAD/SERVICE_NAME", 
              LAST);*/

     lr_output_message(lr_eval_string("Query result = {XML_Out}"));

	 //************ End ***********************


//	lr_output_message("result:%s", lr_eval_string("{a}"));

   //	lr_xml_get_values("XML={a}","FastQuery=/ElectronInvoiceOutput/UNI_BSS_BODY/ELECTRON_INVOICE_RSP/RESP_CODE", "ValueParam=strXml",LAST);
  //  lr_output_message("result:%s", lr_eval_string("{strXml}"));
/*

	if(atoi(lr_eval_string("{strXml}"))==0){
      lr_output_message("result:%s", "Success!-YT");
      
	lr_end_transaction("kp", LR_AUTO);

	}
	else{
      lr_error_message("result:%s", "交易失败");
      
	lr_end_transaction("kp", LR_AUTO);

	}
   */

	lr_output_message("Result: %s","Welldone!");

return 0;
}
