Action()
{


	web_service_call( "StepName=checkElectronInvoice_101",
		"SOAPMethod=ElectronInvoiceSer|ElectronInvoiceSerHttpPort|checkElectronInvoice",
		"ResponseParam=response",
		"Service=ElectronInvoiceSer",
		"ExpectedResponse=SoapResult",
		"Snapshot=t1457771428.inf",
		BEGIN_ARGUMENTS,
		"in0=<QryCdrOfVaInfoOutput><UNI_BSS_HEAD><ORIG_DOMAIN> PTIS</ORIG_DOMAIN><SERVICE_NAME>ElectronInvoiceSer</SERVICE_NAME><OPERATE_NAME>checkElectronInvoice</OPERATE_NAME><ACTION_CODE>0</ACTION_CODE><ACTION_RELATION>0</ACTION_RELATION><ROUTING> <ROUTE_TYPE>00</ROUTE_TYPE> <ROUTE_VALUE>11</ROUTE_VALUE></ROUTING><PROC_ID>lyl001</PROC_ID><TRANS_IDO> lyl001</TRANS_IDO><TRANS_IDH> </TRANS_IDH>  <PROCESS_TIME>200806081204</PROCESS_TIME><RESPONSE><RSP_TYPE></RSP_TYPE><RSP_CODE></RSP_CODE></RESPONSE><COM_BUS_INFO><OPER_ID>00029345sunhong</OPER_ID><PROVINCE_CODE>0011</PROVINCE_CODE></COM_BUS_INFO><SP_RESERVE><TRANS_IDC>ECIP0002seq00001</TRANS_IDC><CUTOFFDAY>20080608</CUTOFFDAY><OSNDUNS>0002</OSNDUNS><HSNDUNS>1100</HSNDUNS><CONV_ID>ECIP0002seq00001200806081200111</CONV_ID></SP_RESERVE><TEST_FLAG>0</TEST_FLAG><MSG_SENDER>1100</MSG_SENDER><MSG_RECEIVER>1101</MSG_RECEIVER></UNI_BSS_HEAD><UNI_BSS_BODY><CHECK_ELECTRON_INVOICE_REQ><INVOICE_CODE>000003521012</INVOICE_CODE><INVOICE_NUM>32080451</INVOICE_NUM><TOTAL_FEE>117</TOTAL_FEE><MAKE_INVOICE_DATE>20160312</MAKE_INVOICE_DATE><PARA></PARA><PARA_ID></PARA_ID><PARA_VALUE></PARA_VALUE></CHECK_ELECTRON_INVOICE_REQ></UNI_BSS_BODY><UNI_BSS_ATTACHED><MEDIA_INFO></MEDIA_INFO></UNI_BSS_ATTACHED></QryCdrOfVaInfoOutput>",
		END_ARGUMENTS,
		BEGIN_RESULT,
		"out=Param_out",
		END_RESULT,
		LAST);
   lr_output_message("result:%s",lr_eval_string("{Param_out}"));

	return 0;
}