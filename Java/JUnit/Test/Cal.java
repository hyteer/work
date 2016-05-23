
public class Cal {
  public int evaluate(String expression) {
    int sum = 0;
    for (String summand: expression.split("\\+"))
      sum += Integer.valueOf(summand);
    return sum;
  }
  public int evaluate2(String expression) {
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
  
  public static void main(String[] args){
	  Cal mycal = new Cal();
	  int sum = mycal.evaluate("3+4+5");
	  System.out.println("Sum: " + sum);
	  int result = mycal.multiply(5,6);
	  System.out.println("Result: " + result);
	  System.out.println("Max: " + mycal.getMax(11,22));
	  
  }
}