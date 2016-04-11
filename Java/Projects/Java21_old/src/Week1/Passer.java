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
public class Passer {
    
    void toUpperCase(String[] text) {
        for (int i=0; i<text.length; i++){
            text[i] = text[i].toUpperCase();
        }
    }
    
    public static void main(String[] args) {
        Passer passer = new Passer();
        passer.toUpperCase(args);
        for (int i=0; i<args.length; i++) {
            System.out.print(args[i] + " ");
        }
        System.out.println("\n---The End---");
        System.out.println(System.currentTimeMillis()); // Just for testing
    }
}
