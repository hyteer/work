/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ytest;
import org.apache.commons.codec.binary.Base64;
/**
 *
 * @author Administrator
 */
public class CharCoding {
    
    //*****加密方法******
    public static String encodeBase64(String message){
        // 加密方法
        byte[] result = Base64.encodeBase64(message.getBytes());
        return new String(result);
    }
    //*******************
     
    
    
    public static void main(String[] args) throws Exception{
        String charset = "UTF-8";
        String org = "<REQUEST_COMMON_FPKJ class='REQUEST_COMMON_FPKJ'><BY6></BY6><BY5></BY5><GMF_MC>柳絮浩</GMF_MC><BY4></BY4><XSF_NSRSBH>330203954230624</XSF_NSRSBH><XSF_DZDH>宁波市高新区凌云路98号,0574-27821213</XSF_DZDH><BY3></BY3><BY2></BY2><BY1>1</BY1><JSHJ>117</JSHJ><EWM><![CDATA[]]></EWM><BZ>机器编号:499099915432</BZ><KPRQ>20160222164757</KPRQ><JQBH>499099900038</JQBH><GMF_NSRSBH></GMF_NSRSBH><JYM>09193963768980293853</JYM><GMF_SJH>15920066345,18964787876</GMF_SJH><FPT_ZH></FPT_ZH><FP_MW><![CDATA[03/7>2445855/8<2<248-1<08/29+/8+1*5/5+06*5/8-118*13901896</7>2445855/8<2<231>3+-982/389<5**>>*01+54119-9/902/4<6]]></FP_MW><FPFM>12340000000160190121</FPFM><HYLX>0</HYLX><KPLX>0</KPLX><KPR>AI_QA_KQ</KPR><SKR></SKR><FHR></FHR><XSF_YHZH>610118191919191919</XSF_YHZH><FP_HM>60190121</FP_HM><FPQQLSH>lyl12345678909876543212</FPQQLSH><FP_DM>123400000001</FP_DM><GMF_DZDH></GMF_DZDH><GMF_DZYX>fengfan_yan@139.com</GMF_DZYX><XSF_MC>中国联合网络通信有限公司宁波市分公司</XSF_MC><HJJE>100</HJJE><YFP_DM></YFP_DM><HJSE>*</HJSE><BY7></BY7><YFP_HM></YFP_HM><BY8></BY8><BY9></BY9><BY10></BY10><GMF_YHZH></GMF_YHZH><COMMON_FPKJ_XMXXS class='COMMON_FPKJ_XMXX' size='1'><COMMON_FPKJ_XMXX><BY6></BY6><BY5></BY5><BY4></BY4><SE>*</SE><BY3></BY3><BY2></BY2><BY1></BY1><GGXH></GGXH><SL>*</SL><XMSL></XMSL><DW></DW><FPHXZ>0</FPHXZ><XMDJ></XMDJ><XMMC><![CDATA[普通资金]]></XMMC><XMJE>1</XMJE></COMMON_FPKJ_XMXX></COMMON_FPKJ_XMXXS></REQUEST_COMMON_FPKJ>";

        String str = "FDKjfk中午";
		 byte[] bs = str.getBytes("utf-8");
		 System.out.println("转换前:"+str);
		   //用新的字符编码生成字符串
		  System.out.println(new String(bs, "GB2312")); 
                  
        byte[] b_utf8 = "这是一个测试".getBytes("UTF-8"); 
        byte[] b_gbk = "这是一个测试".getBytes("GBK");
        byte[] b_gb2312 = "这是一个测试".getBytes("GB2312"); 
        
        byte[] b1_utf8 = org.getBytes("UTF-8");
        byte[] b1_gb2312 = org.getBytes("GB2312");
        
        
        
        System.out.println(b1_utf8.length);
        System.out.println(b_gbk.toString());
        System.out.println(b1_gb2312.length);
        
        String str1 = new String(b1_utf8,charset);
        
        System.out.println("Byte-utf8: " + b1_utf8.toString());
       
               
        
        //printbyte("gb2312:", _b2);
        
        
        
        
    }
    
}
