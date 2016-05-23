import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class CalculatorTest {
  @Test
  public void evaluatesExpression() {
    Calculator calculator = new Calculator();
    int sum = calculator.evaluate("1+2+3");
    assertEquals(6, sum);
  }
  @Test
  public void evaluatesExpression2() {
    Calculator calculator = new Calculator();
    int sum = calculator.evaluate2("11+12+13");
    assertEquals(36, sum);
  }
  @Test
  public void evaluatesMultiply() {
	  Calculator calculator = new Calculator();
	  int result = calculator.multiply(5,6);
	  assertEquals(30, result);
  }
  @Test
  public void evaluatesGetMax() {
	  Calculator cal = new Calculator();
	  int max = cal.getMax(13,33);
	  assertEquals(33,max);
  }
}