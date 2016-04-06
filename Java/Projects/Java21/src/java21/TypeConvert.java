/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package java21;

/**
 *
 * @author Administrator
 */
public class TypeConvert {
    public static void main(String[] args){
        Integer dataCount = new Integer(7801);
        int newCount = dataCount.intValue();
        
        System.out.println("newCount: " + newCount);
        
        String pennsylvania = "65000";
        int penn = Integer.parseInt(pennsylvania);
        System.out.println("penn: " + penn);
        
        //自动封装（autoboxing）和拆封（unboxing）
        Float f1 = new Float(12.5F);
        Float f2 = new Float(27.2F);
        System.out.println("Lower number: " + Math.min(f1, f2));
        
        
    }
}
