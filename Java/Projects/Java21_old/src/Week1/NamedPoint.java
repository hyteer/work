package Week1;
import java.awt.Point;

class NamedPoint extends Point{
   String name;
   
   NamedPoint(int x, int y, String name) {
       super(x,y);
       this.name = name;
   }
   
   public static void main(String[] args) {
       NamedPoint np = new NamedPoint(11,22,"Point A");
       System.out.println("x is: " +np.x);
       System.out.println("y is: " + np.y);
       System.out.println("name is: " + np.name);
   }
}