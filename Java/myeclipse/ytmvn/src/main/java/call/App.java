package call;
import java.text.DateFormat;
import java.text.ParseException;
import java.util.Calendar;
import java.util.Date;

import com.yt.app.ytfirst.*;

import algo.CalCount;
import algo.*;

/**
 * hyteer-first maven
 *
 */
public class App 
{
	
	
    public static void main( String[] args )
    {
    	// Call ytfirst
    	Cal cal = new Cal();

    	int plus = cal.plus("11+22+33");
    	int multi = cal.multiply(11, 8);
    	int max = cal.getMax(33, 121);
    	
        System.out.println( "Yt first maven!" );
        System.out.println("11+22+33=" + plus);
        System.out.println("11x8= " + multi);
        System.out.println("Max(33,121)= " + max);
        
        // Call algo/CalCount
        CalCount clc = new CalCount();
        clc.countcal(2016, 5);
        
        // Call algo/MyCalendar
        MyCalendar mycal = new MyCalendar();
        Date earlydate = new Date();   
        Date latedate = new Date();   
        DateFormat df = DateFormat.getDateInstance();   
        try {   
            earlydate = df.parse("2016-03-01");   
            latedate = df.parse("2016-05-30");   
        } catch (ParseException e) {   
              e.printStackTrace();   
          }   
         int days = mycal.daysBetween(earlydate,latedate);   
         System.out.println(days+"天"); 
        
        
        
        
    }
}
