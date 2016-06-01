package algo;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class MyCalendar {

    /**
     * @param args
     * @throws ParseException
     */
	/*
	public static void main(String[] args)
    {
         Date earlydate = new Date();   
         Date latedate = new Date();   
         DateFormat df = DateFormat.getDateInstance();   
         try {   
             earlydate = df.parse("2016-03-01");   
             latedate = df.parse("2016-05-30");   
         } catch (ParseException e) {   
               e.printStackTrace();   
           }   
          int days = daysBetween(earlydate,latedate);   
          System.out.println(days);   
    }
    */

/**
     * 
     * @param date1 <String>
     * @param date2 <String>
     * @return int
     * @throws ParseException
     */
    public static final int daysBetween(Date early, Date late) { 
        
        java.util.Calendar calst = java.util.Calendar.getInstance();   
        java.util.Calendar caled = java.util.Calendar.getInstance();   
        calst.setTime(early);   
         caled.setTime(late);   
         //设置时间为0时   
         calst.set(java.util.Calendar.HOUR_OF_DAY, 0);   
         calst.set(java.util.Calendar.MINUTE, 0);   
         calst.set(java.util.Calendar.SECOND, 0);   
         caled.set(java.util.Calendar.HOUR_OF_DAY, 0);   
         caled.set(java.util.Calendar.MINUTE, 0);   
         caled.set(java.util.Calendar.SECOND, 0);   
        //得到两个日期相差的天数   
         int days = ((int) (caled.getTime().getTime() / 1000) - (int) (calst   
                .getTime().getTime() / 1000)) / 3600 / 24;   
         
        return days;   
   } 

}