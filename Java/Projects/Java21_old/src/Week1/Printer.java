package Week1;

class Printer {
    int x = 0;
    int y = 1;
    
    void printMe() {
        System.out.println("x is " + x + ", y is " + y);
        System.out.println("I am an instance of the class " +
                this.getClass().getName());
    }
}

class SubPrinter extends Printer {
    int z = 3;
    
    @Override
    // 覆盖方法
             
     void printMe() {
         /*
        System.out.println("Below is  " + this.getClass().getName());
        System.out.println("x is " + x + ", y is " + y + ",z is " + z);
    */
    // 覆盖方法并调用原方法，再添加新行为
    //***
     super.printMe();
     System.out.println("z is: " + z);
     
    }
    
    public static void main(String[] args) {
        SubPrinter obj = new SubPrinter();
        obj.printMe();
    }
}