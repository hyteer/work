package java21;
/****
 * 
 * @author YT
 */

class Averager {
    public static void main(String[] args) {
        int sum = 0;
        if (args.length > 0) {
            for (int i=0; i<args.length; i++) {
                sum+= Integer.parseInt(args[i]);
            }
            System.out.println("Sum is: " + sum);
            System.out.println("Average is: " + (float)sum/args.length);
        }
    }
}