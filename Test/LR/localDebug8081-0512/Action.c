Action()
{

        web_add_header("Content-Type","text/xml; charset=utf-8");
        web_add_header("Accept","application/soap+xml, application/dime,multipart/related, text/*");
        web_add_header("Cache-Control","no-cache");
        web_add_header("Pragma","no-cache");
        web_add_header("SOAPAction","AgentServer");
   
        web_custom_request("AgentServer",
        "URL=http://localhost:8081",
        "Method=POST",
        "Resource=0",
        "RecContentType=text/xml",
        "Mode=HTML",
        "EncType=text/xml; charset=utf-8",
        "Body=<?xml version=\"1.0\"encoding=\"UTF-8\" standalone=\"no\"?>"
        "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:ns=\"ns:fwbs\">"
                        "<soapenv:Header></soapenv:Header>"
                        "<soapenv:Body>"
                                "<ns:agentPay>"
                                        "<feetype>13</feetype>"
                                        "<tlrno>0394</tlrno>"
                                        "<custno>45113904</custno>"
                                        "<hbrno>10004</hbrno>"
                                        "<channel>selfHelp</channel>"
                                        "<qfbs>1</qfbs>"
                                        "<txamt>702.00</txamt>"
                                        "<cashflg>1</cashflg>"
                                        "<actno>6223920001101146592</actno>"
                                        "<NotCheckPasswd>1</NotCheckPasswd>"
                                        "<TXTYPE>0</TXTYPE>"
                                        "<passwd></passwd>"
                                "</ns:agentPay>"
                        "</soapenv:Body>"
                "</soapenv:Envelope>",
                LAST);
		


	return 0;
}
