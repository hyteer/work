package com.yt.app.ytfirst;
import java.util.Calendar;

import algo.CalCount;;

/**
 * hyteer-first maven
 *
 */
public class App 
{
	
	
    public static void main( String[] args )
    {
    	
    	Cal cal = new Cal();

    	int plus = cal.plus("11+22+33");
    	int multi = cal.multiply(11, 8);
    	int max = cal.getMax(33, 121);
    	
        System.out.println( "Yt first maven!" );
        System.out.println("11+22+33=" + plus);
        System.out.println("11x8= " + multi);
        System.out.println("Max(33,121)= " + max);
        
        CalCount clc = new CalCount();
        clc.countcal(2016, 5);
        
        
        
        
        
    }
}
