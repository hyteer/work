/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Yt;

/**
 *
 * @author Administrator
 */
public class List {
    String listType;
    String listColor;
    String listStatus;
    int listWidth;
    int listHeight;
    
    void setList(String newType, String newColor, int newWidth, int newHeight) {
        listType = newType;
        listColor = newColor;
        listWidth = newWidth;
        listHeight = newHeight;
    }
    
    void changeColor(String newColor) {
        listColor = newColor;
    }
    
    void showInfo() {
        System.out.println("List Type: " + listType);
        System.out.println("List Color: " + listColor);
        System.out.println("List Size: " + listWidth + "*" + listHeight);
    }


    public static void main( String[] args ) {
        List list1= new List();
        list1.setList("SimpleList", "Blue", 120, 12);
        list1.showInfo();
        System.out.println("Change color to White...");
        list1.changeColor("White");
        list1.showInfo();
        
        
    }
}