package Volcano;


import Volcano.VolcanoRobot;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Administrator
 */
public class VolcanoApp {
    public static void main(String[] args) {
        VolcanoRobot dante = new VolcanoRobot();
        dante.status = "exploring";
        dante.speed = 2;
        dante.temperature = 510;
        
        dante.showAttributes();
        System.out.println("Increasing speed to 3.");
        dante.speed = 3;
        dante.showAttributes();
        System.out.println("Changing temperature to 670.");
        dante.temperature = 670;
        dante.showAttributes();
        System.out.println("Checking the temperature.");
        dante.checkTemperature();
        dante.showAttributes();
        
        VolcanoRobot virgil = new VolcanoRobot();
        virgil.status = "flying...";
        virgil.speed = 2;
        virgil.temperature = 300;
        
        virgil.showAttributes();
        System.out.println("There's an accident...");
        virgil.temperature = 808;
        virgil.showAttributes();
        System.out.println("Checking status...");
        virgil.checkTemperature();
        virgil.showAttributes();
        
    }
}
