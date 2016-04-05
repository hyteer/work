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
public class Variables {
    
    public static void main(String[] args) {
        final char UP = 'U';
        byte initialLevel = 12;
        short location = 13250;
        int score = 3500100;
        boolean  newGame = true;
        int jackpot = 3_500_000;
        
        System.out.println("Level: " + initialLevel);
        System.out.println("Up: " + UP);
        System.out.println("jackpot: " + jackpot);
        
        String example = "Socrates asked, \"Hemlock is posion?\"";
        String title = "Sams Teach Yourself Ruby on Rails in the John\u2122";
        
        System.out.println(example);
        System.out.println("Sincerely,\nMillard Fillmore\n");
        System.out.println(title);
        
        
        
        
    }
}
