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
public class RangeLister {
    
    // Method makeRange
    int[] makeRange(int lower, int upper) {
        int[] range = new int[(upper-lower) + 1];
        for (int i=0; i<range.length; i++) {
            range[i] = lower++;
        }
        return range;
    }
    
    public static void main(String[] args) {
        int[] range;
        RangeLister lister = new RangeLister();
        range = lister.makeRange(4, 13);
        System.out.print("The array: [ ");
        for (int i=0; i<range.length; i++) {
            System.out.print(range[i] + " ");
        }
        System.out.println("]");
    }
}
