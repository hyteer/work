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
public class Pointsetter {
    public static void main(String[] args) {
        Point location = new Point(4,13);
        
        System.out.println("Starting location: ");
        System.out.println("X equals " + location.x);
        System.out.println("Y equals " + location.y);
        
        System.out.println("\nMoving to (7, 6)");
        location.x = 7;
        location.y = 6;
        
        System.out.println("\nEnding location:");
        System.out.println("X equals " + location.x);
        System.out.println("Y equals " + location.y);
        
    }
}
