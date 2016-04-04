/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package calws_client;

/**
 *
 * @author Administrator
 */
public class CalWS_Client {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        try {
            int i = 3;
            int j = 22;
            String name = "Tang";
            int result = add(i,j);
            String sayHello = hello(name);
            System.out.println("Result = " + result);
            System.out.println( "Say Hello: " + sayHello);
        } catch ( Exception ex) {
            System.out.println( "Exception: " + ex);
        }
        
    }

    private static int add(int i, int j) {
        org.me.cal.CalWS_Service service = new org.me.cal.CalWS_Service();
        org.me.cal.CalWS port = service.getCalWSPort();
        return port.add(i, j);
    }

    private static String hello(java.lang.String name) {
        org.me.cal.CalWS_Service service = new org.me.cal.CalWS_Service();
        org.me.cal.CalWS port = service.getCalWSPort();
        return port.hello(name);
    }
    
}
