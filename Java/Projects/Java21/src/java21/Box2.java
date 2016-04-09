package java21;
import java.awt.Point;

class Box2 {
    
    int x1 = 0;
    int y1 = 0;
    int x2 = 0;
    int y2 = 0;
    
    Box2(int x1, int y1, int x2, int y2) {
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2;
    }
    
    Box2(Point topLeft, Point rightBottom) {
        this(topLeft.x, topLeft.y, rightBottom.x, rightBottom.y);
    }
    
    Box2(Point topLeft, int w, int h) {
        this(topLeft.x, topLeft.y, topLeft.x + w, topLeft.y + h);
    }
    
    void printBox(){
        System.out.println("Box:<" + x1 +"," + y1 +"," + x2 + "," + y2 + ">");
    }
    
    public static void main(String[] args) {
        Box2 rect = new Box2(10,10,20,20);
        System.out.println("Calling Box2 with coordinates:");
        rect.printBox();
        
        Box2 rect2 = new Box2(new Point(10,10), new Point(50,50));
        System.out.println("Calling Box2 with points:");
        rect2.printBox();
        
        rect = new Box2(new Point(11,11), 20, 40);
        System.out.println("Calling with 1 point, width and height:");
        rect.printBox();
    }
}