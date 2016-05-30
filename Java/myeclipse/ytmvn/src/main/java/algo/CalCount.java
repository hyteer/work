package algo;


import java.util.Calendar;
/**
 * 功能概述：计算指定年月的天数和周数<br>
 * 创建时间：2010-5-17 下午05:25:58<br>
 * 
 */
public class CalCount{
    public static void countcal(int year, int month) {
        Calendar c = Calendar.getInstance();
        c.set(Calendar.YEAR, year); // 2010年
        c.set(Calendar.MONTH, month); // 6 月
        System.out.println("------------" + c.get(Calendar.YEAR) + "年" + (c.get(Calendar.MONTH) + 1) + "月的天数和周数-------------");
        System.out.println("天数：" + c.getActualMaximum(Calendar.DAY_OF_MONTH));
        System.out.println("周数：" + c.getActualMaximum(Calendar.WEEK_OF_MONTH));
    }
    
    /*
    public static void main(String[] args){
    	countcal(2010,6);
    }
    */
}

