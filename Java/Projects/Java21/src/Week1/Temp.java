/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Week1;
import java.awt.Point;
/**
 *
 * @author Administrator
 */
public class Temp {
    public static void main(String[] args) {
        String s,s2;
        s = "item";
        s2 = s.valueOf(550);
        System.out.println(s2);
        s2 = String.valueOf("Silly");
        System.out.println(s2);
        
        // 判断对象所属的类
        System.out.println("Class of s: " + s.getClass());
        System.out.println("Class name of s: " + s.getClass().getName());
        
        boolean check1 ="Silly" instanceof String;
        Point pt = new Point(11, 12);
        boolean check2 = pt instanceof Point;
        System.out.println("check1： " + check1);
        
        
    }
}
