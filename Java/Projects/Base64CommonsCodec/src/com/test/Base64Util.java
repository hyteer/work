/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.test;

import org.apache.commons.codec.binary.Base64;

/**
 *
 * @author Administrator
 */
public class Base64Util {
    
    //*****加密方法******
    public static String encodeBase64(String message){
        // 加密方法
        byte[] result = Base64.encodeBase64(message.getBytes());
        return new String(result);
    }
    //*******************
    
    
    
    //******解密方法******
    public static String decodeBase64(String message){
        byte[] result = Base64.decodeBase64(message);
        return new String(result);
    }
    
    public static void main(String[] args){
        // TODO code application logic here
        //******Testing******
        String commonMessage = "Hello world";   //原始消息
        String encodeMessage = encodeBase64(commonMessage); //加密
        System.out.println("加密后为：" + encodeMessage);
        String decodeMessage = decodeBase64(encodeMessage); //解密
        System.out.println("解密后为：" + decodeMessage);
        
  
        
        
        
    }
}
