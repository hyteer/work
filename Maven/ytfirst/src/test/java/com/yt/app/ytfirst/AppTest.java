package com.yt.app.ytfirst;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

/**
 * Unit test for simple App.
 */
public class AppTest 
    extends TestCase
{
    /**
     * Create the test case
     *
     * @param testName name of the test case
     */
    public AppTest( String testName )
    {
        super( testName );
    }

    /**
     * @return the suite of tests being tested
     */
    public static Test suite()
    {
        return new TestSuite( AppTest.class );
    }

    /**
     * Rigourous Test :-)
     */
    public void testApp()
    {
        assertTrue( true );
    }
    public void testCalPlus()
    {
    	Cal cal = new Cal();
        int sum = cal.plus("1+2+3");
        assertEquals(6, sum);
        //assertTrue( true );
    }
    public void testCalMulti()
    {
    	Cal cal = new Cal();
        int multi = cal.multiply(12,20);
  	  assertEquals(240, multi);
    }
    public void testCalMax()
    {
    	Cal cal = new Cal();
        int max = cal.getMax(111, 212);
        assertEquals(212, max);
        //assertTrue( true );
    }
}
