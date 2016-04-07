/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ytest;

/**
 *
 * @author Administrator
 */
public class Format {
    public static void main(String[] args) {
        int balance = 50012;
        System.out.format("Balance: $%,d%n", balance);
        
        double pi = Math.PI;
        System.out.format("PI: %.11f%n", pi);
        
    }
}
