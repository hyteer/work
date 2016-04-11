package Week1;
import java.awt.Point;

class Box {
    int x1 = 0;
    int y1 = 0;
    int x2 = 0;
    int y2 = 0;
    
    Box buildBox(int x1,int y1,int x2,int y2) {
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2;
        return this;
    }
    
    Box buildBox(Point topLeft, Point rightBottom) {
       
        x1 = topLeft.x;
        y1 = topLeft.y;
        x2 = rightBottom.x;
        y2 = rightBottom.y;
        return this;
        ///*** Below is another way to implement
        //return buildBox(topLeft.x, topLeft.y, rightBottom.x, rightBottom.y);
        //*****/
    }
    
    Box buildBox(Point topLeft,int w,int h) {
        x1 = topLeft.x;
        y1 = topLeft.y;
        x2 = (x1 + w);
        y2 = (y1 + h);
        return this;
    }
    
    void printBox(){
        System.out.println("Box: <" + x1 + "," + y1 +"," + x2 + "," + y2 + ">");
    }
    
    public static void main(String[] args) {
        Box rect1 = new Box();
        System.out.println("Calling buildBox with coordinates(25,25)and (50,50):");
        rect1.buildBox(25,25,50,50);
        rect1.printBox();
        
        Box rect2 = new Box();
        System.out.println("Calling with points (10,10) and (20,20):");
        rect2.buildBox(new Point(10,10), new Point(20,20));
        rect2.printBox();
        
        Box rect3 = new Box();
        System.out.println("Calling with point(10,10), width 50 and height 50:");
        rect3.buildBox(new Point(10,10), 50,50);
        rect3.printBox();
        
    }
}