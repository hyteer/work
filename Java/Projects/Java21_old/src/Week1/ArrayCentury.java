/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Week1;

/**
 *
 * @author Administrator
 */
public class ArrayCentury {
    // 声明一个三级数组用来存储一个世纪中的每一天的一个整数
    public static void main(String[] args) {
        int[][][] century = new int[100][52][7];
        System.out.println("Elements in the first dimension: " + century.length);
        System.out.println("Elements in the second dimension: " + century[0].length);
        System.out.println("Elements in the third dimension: " + century[0][0].length);
        
    }
}
