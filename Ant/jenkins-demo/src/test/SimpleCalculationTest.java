
import static org.junit.Assert.*;
import org.junit.Test;

public class SimpleCalculationTest {

    SimpleCalculation sc = new SimpleCalculation();
    
    @Test
    public void AddTest() {
        
        int c = sc.Add(3, 5);    
        
        assertEquals(8, c);        
    }
    
    @Test
    public void SubtrationTest() {
        
        int c = sc.Subtration(20, 5);    
        
        assertEquals(15, c);        
    }
}