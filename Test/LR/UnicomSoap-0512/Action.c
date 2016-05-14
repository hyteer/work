Action()
{
	web_set_proxy("127.0.0.1:8888");  //Set Proxy for test
	
	web_add_header("Content-Type","text/xml; charset=utf-8");
	//web_add_header("Accept","application/soap+xml, application/dime,multipart/related, text/*");
	//web_add_header("Cache-Control","no-cache");
	//web_add_header("Pragma","no-cache");
	web_add_header("SOAPAction", "\"\"");

	web_custom_request("AgentServer",
	"URL=http://127.0.0.1:9091/yys-test-upload/services/ElectronInvoiceSer",
	"Method=POST",
	"Resource=0",
	"RecContentType=text/xml",
	//"Mode=HTML",
	"EncType=text/xml; charset=utf-8",
	"Body="
	"<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:unib=\"http://ws.chinaunicom.cn/ElectronInvoiceSer/unibssBody\" xmlns:unib1=\"http://ws.chinaunicom.cn/unibssHead\" xmlns:cre=\"http://ws.chinaunicom.cn/ElectronInvoiceSer/unibssBody/createElectronInvoiceReq\" xmlns:unib2=\""
	"http://ws.chinaunicom.cn/unibssAttached\">"
	   "<soapenv:Header/>"
	   "<soapenv:Body>"
		  "<unib:CREATE_ELECTRON_INVOICE_INPUT>"
			 "<unib1:UNI_BSS_HEAD>"
				"<unib1:ORIG_DOMAIN>PTIS</unib1:ORIG_DOMAIN>"
				"<unib1:SERVICE_NAME>ElectronInvoiceSer</unib1:SERVICE_NAME>"
				"<unib1:OPERATE_NAME>checkElectronInvoice</unib1:OPERATE_NAME>"
				"<unib1:ACTION_CODE>0</unib1:ACTION_CODE>"
				"<unib1:ACTION_RELATION>0</unib1:ACTION_RELATION>"
				"<unib1:ROUTING>"
				   "<unib1:ROUTE_TYPE>00</unib1:ROUTE_TYPE>"
				   "<unib1:ROUTE_VALUE>11</unib1:ROUTE_VALUE>"
				"</unib1:ROUTING>"
				"<unib1:PROC_ID>lyl001</unib1:PROC_ID>"
				"<unib1:TRANS_IDO>lyl001</unib1:TRANS_IDO>"
				"<!--Optional:-->"
				"<unib1:TRANS_IDH></unib1:TRANS_IDH>"
				"<unib1:PROCESS_TIME>20160512114537</unib1:PROCESS_TIME>"
				"<!--Optional:-->"
				"<unib1:RESPONSE>"
				   "<unib1:RSP_TYPE>1</unib1:RSP_TYPE>"
				   "<unib1:RSP_CODE>1111</unib1:RSP_CODE>"
				   "<unib1:RSP_DESC></unib1:RSP_DESC>"
				"</unib1:RESPONSE>"
				"<unib1:COM_BUS_INFO>"
				   "<unib1:OPER_ID>00029345sunhong</unib1:OPER_ID>"
				   "<!--Optional:-->"
				   "<unib1:PROVINCE_CODE>00</unib1:PROVINCE_CODE>"
				   "<!--Optional:-->"
				   "<unib1:EPARCHY_CODE>988988</unib1:EPARCHY_CODE>"
				   "<!--Optional:-->"
				   "<unib1:CITY_CODE></unib1:CITY_CODE>"
				   "<unib1:CHANNEL_ID></unib1:CHANNEL_ID>"
				   "<unib1:CHANNEL_TYPE>7777777</unib1:CHANNEL_TYPE>"
				   "<unib1:ACCESS_TYPE>11</unib1:ACCESS_TYPE>"
				   "<!--Optional:-->"
				   "<unib1:ORDER_TYPE>22</unib1:ORDER_TYPE>"
				"</unib1:COM_BUS_INFO>"
				"<!--Optional:-->"
				"<unib1:SP_RESERVE>"
				   "<!--Optional:-->"
				   "<unib1:TRANS_IDC>ECIP0002seq00001</unib1:TRANS_IDC>"
				   "<!--Optional:-->"
				   "<unib1:CUTOFFDAY>20080608</unib1:CUTOFFDAY>"
				   "<unib1:OSNDUNS>2222</unib1:OSNDUNS>"
				   "<!--Optional:-->"
				   "<unib1:HSNDUNS>1100</unib1:HSNDUNS>"
				   "<!--Optional:-->"
				   "<unib1:CONV_ID>ECIP0002seq00001200806081200111</unib1:CONV_ID>"
				"</unib1:SP_RESERVE>"
				"<unib1:TEST_FLAG>0</unib1:TEST_FLAG>"
				"<unib1:MSG_SENDER>1100</unib1:MSG_SENDER>"
				"<unib1:MSG_RECEIVER>1101</unib1:MSG_RECEIVER>"
			 "</unib1:UNI_BSS_HEAD>"
			 "<unib:UNI_BSS_BODY>"
				"<cre:CREATE_ELECTRON_INVOICE_REQ>"
				   "<cre:INVOICE_CODE>PFJFUVVFU1Q+PE9SSUdJTkFMPlBGSkZVVlZGVTFSZlEwOU5UVTlPWDBaUVMwb2dZMnhoYzNNOUoxSkZVVlZGVTFSZlEwOU5UVTlPWDBaUVMwb25QanhDV1RZK1BDOUNXVFkrUEVKWk5UNDhMMEpaTlQ0OFIwMUdYMDFEUHVhZnMrZTFydWExcVR3dlIwMUdYMDFEUGp4Q1dUUStQQzlDV1RRK1BGaFRSbDlPVTFKVFFrZytNek13T1RBeE56QTBOak01T0RRNVBDOVlVMFpmVGxOU1UwSklQanhZVTBaZlJGcEVTRDdscm9IbXM2TGx1SUxwcTVqbWxyRGxqTHJsaDR6a3VwSG90Njg1T09XUHR5d3dOVGMwTFRJM09ESXhNakV6UEM5WVUwWmZSRnBFU0Q0OFFsa3pQand2UWxrelBqeENXVEkrUEM5Q1dUSStQRUpaTVQ0eFBDOUNXVEUrUEVwVFNFbytNVEUzUEM5S1UwaEtQanhGVjAwK1BDRmJRMFJCVkVGYlhWMCtQQzlGVjAwK1BFSmFQdWFjdXVXWnFPZThsdVdQdHpvME9Ua3dPVGs1TVRVME16SThMMEphUGp4TFVGSlJQakl3TVRZd01qSXlNVFkwTnpVM1BDOUxVRkpSUGp4S1VVSklQalE1T1RBNU9Ua3dNREF6T0R3dlNsRkNTRDQ4UjAxR1gwNVRVbE5DU0Q0OEwwZE5SbDlPVTFKVFFrZytQRXBaVFQ0d09URTVNemsyTXpjMk9EazRNREk1TXpnMU16d3ZTbGxOUGp4SFRVWmZVMHBJUGpFMU9USXdNRFkyTXpRMUxERTRPVFkwTnpnM09EYzJQQzlIVFVaZlUwcElQanhHVUZSZldrZytQQzlHVUZSZldrZytQRVpRWDAxWFBqd2hXME5FUVZSQld6QXpMemMrTWpRME5UZzFOUzg0UERJOE1qUTRMVEU4TURndk1qa3JMemdyTVNvMUx6VXJNRFlxTlM4NExURXhPQ294TXprd01UZzVOand2Tno0eU5EUTFPRFUxTHpnOE1qd3lNekUrTXlzdE9UZ3lMek00T1R3MUtpbytQaW93TVNzMU5ERXhPUzA1THprd01pODBQRFpkWFQ0OEwwWlFYMDFYUGp4R1VFWk5QakV5TXpRd01EazBPRGN4TmpZd09UUTROekUyUEM5R1VFWk5QanhJV1V4WVBqQThMMGhaVEZnK1BFdFFURmcrTUR3dlMxQk1XRDQ4UzFCU1BrRkpYMUZCWDB0UlBDOUxVRkkrUEZOTFVqNDhMMU5MVWo0OFJraFNQand2UmtoU1BqeFlVMFpmV1VoYVNENDJNVEF4TVRneE9URTVNVGt4T1RFNU1UazhMMWhUUmw5WlNGcElQanhHVUY5SVRUNDJNRGswT0RjeE5qd3ZSbEJmU0UwK1BFWlFVVkZNVTBnK2JIbHNNVEl6TkRVMk56ZzVNRGs0TnpZMU5ETXlNVEk4TDBaUVVWRk1VMGcrUEVaUVgwUk5QakV5TXpRd01EazBPRGN4Tmp3dlJsQmZSRTArUEVkTlJsOUVXa1JJUGp3dlIwMUdYMFJhUkVnK1BFZE5SbDlFV2xsWVBtWmxibWRtWVc1ZmVXRnVRREV6T1M1amIyMDhMMGROUmw5RVdsbFlQanhZVTBaZlRVTSs1TGl0NVp1OTZJR1U1WkNJNTcyUjU3dWM2WUNhNUwraDVweUo2Wm1RNVlXczVZKzQ1YTZCNXJPaTViaUM1WWlHNVlXczVZKzRQQzlZVTBaZlRVTStQRWhLU2tVK01UQXdQQzlJU2twRlBqeFpSbEJmUkUwK1BDOVpSbEJmUkUwK1BFaEtVMFUrS2p3dlNFcFRSVDQ4UWxrM1Bqd3ZRbGszUGp4WlJsQmZTRTArUEM5WlJsQmZTRTArUEVKWk9ENDhMMEpaT0Q0OFFsazVQand2UWxrNVBqeENXVEV3UGp3dlFsa3hNRDQ4UjAxR1gxbElXa2crUEM5SFRVWmZXVWhhU0Q0OFEwOU5UVTlPWDBaUVMwcGZXRTFZV0ZNZ1kyeGhjM005SjBOUFRVMVBUbDlHVUV0S1gxaE5XRmduSUhOcGVtVTlKekVuUGp4RFQwMU5UMDVmUmxCTFNsOVlUVmhZUGp4Q1dUWStQQzlDV1RZK1BFSlpOVDQ4TDBKWk5UNDhRbGswUGp3dlFsazBQanhUUlQ0cVBDOVRSVDQ4UWxrelBqd3ZRbGt6UGp4Q1dUSStQQzlDV1RJK1BFSlpNVDQ4TDBKWk1UNDhSMGRZU0Q0OEwwZEhXRWcrUEZOTVBpbzhMMU5NUGp4WVRWTk1Qand2V0UxVFRENDhSRmMrUEM5RVZ6NDhSbEJJV0ZvK01Ed3ZSbEJJV0ZvK1BGaE5SRW8rUEM5WVRVUktQanhZVFUxRFBqd2hXME5FUVZSQlcrYVpydW1BbXVpMWhPbUhrVjFkUGp3dldFMU5RejQ4V0UxS1JUNHhQQzlZVFVwRlBqd3ZRMDlOVFU5T1gwWlFTMHBmV0UxWVdENDhMME5QVFUxUFRsOUdVRXRLWDFoTldGaFRQand2VWtWUlZVVlRWRjlEVDAxTlQwNWZSbEJMU2o0PTwvT1JJR0lOQUw+PFNFUklBTE5VTUJFUi8+PFNJR05BVFVSRS8+PC9SRVFVRVNUPg==</cre:INVOICE_CODE>"
				   "<!--Zero or more repetitions:-->"
				   "<cre:PARA>"
					  "<cre:PARA_ID></cre:PARA_ID>"
					  "<cre:PARA_VALUE></cre:PARA_VALUE>"
				   "</cre:PARA>"
				"</cre:CREATE_ELECTRON_INVOICE_REQ>"
			 "</unib:UNI_BSS_BODY>"
			 "<unib2:UNI_BSS_ATTACHED>"
				"<!--Optional:-->"
				"<unib2:MEDIA_INFO></unib2:MEDIA_INFO>"
			 "</unib2:UNI_BSS_ATTACHED>"
		  "</unib:CREATE_ELECTRON_INVOICE_INPUT>"
	   "</soapenv:Body>"
	"</soapenv:Envelope>",
			LAST);


	return 0;
}
