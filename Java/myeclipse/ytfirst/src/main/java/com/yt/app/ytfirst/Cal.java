package com.yt.app.ytfirst;

public class Cal {
	  public int plus(String expression) {
	    int sum = 0;
	    for (String summand: expression.split("\\+"))
	      sum += Integer.valueOf(summand);
	    return sum;
	  }
	  public int plus2(String expression) {
	    int sum = 0;
	    for (String summand: expression.split("\\+"))
	      sum += Integer.valueOf(summand);
	    return sum;
	  }
	  public int multiply(int a,int b){
		  int result = 0;
		  result = a*b;
		  return result;
	  }
	  public int getMax(int a, int b) {
		  int max = a>b?a:b;
		  return max;
		  
	  }
	  
	  
	}