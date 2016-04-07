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
public class StringChecker {
    
    public static void main(String[] args) {
        String str = "Would you like an apple pie with that?";
        System.out.println("The string is: " + str);
        System.out.println("Length of this string: " + str.length());
        System.out.println("The charactor at position 6: " + str.charAt(6));
        System.out.println("The charactor from 26 to 32: " + str.substring(26, 32));
        System.out.println("The index of the first 'a': " + str.indexOf('a'));
        System.out.println("The index of the begining of the substring \"apple\": "
        + str.indexOf("apple"));
        System.out.println("The string in uppercase: " + str.toUpperCase());
        
    }
}
