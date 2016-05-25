
import static org.junit.Assert.*;

import org.junit.Test;


public class ComplexCalculationTest {
    
    ComplexCalculation cc = new ComplexCalculation();
    
    @Test
    public void DivisionTest() {
        
        int c = cc.Division(100, 5);
        
        assertEquals(20, c);        
    }

    @Test
    public void MultiplyTest() {
        
        int c = cc.Multiply(100, 5);
        
        assertEquals(500, c);        
    }
}