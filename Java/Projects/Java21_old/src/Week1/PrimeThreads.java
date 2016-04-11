/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Week1;

/**
 *
 * @author Administrator
 */
public class PrimeThreads {
    public static void main(String[] args) {
        PrimeThreads pt = new PrimeThreads(args);
    }
    
    public PrimeThreads(String[] args) {
        PrimeFinder[] finder = new PrimeFinder[args.length];
        for (int i=0; i<args.length; i++) {
            try {
                long count = Long.parseLong(args[i]);
                finder[i] = new PrimeFinder(count);
                System.out.println("Looking for prime " + count);                
            } catch (NumberFormatException nfe) {
                System.out.println("Error:" + nfe.getMessage());
            }
        }
        boolean complete = false;
        while (!complete) {
            complete = true;
            for (int j=0; j<finder.length; j++) {
                if (finder[j] == null) continue;
                if (!finder[j].finished) {
                    complete = false;
                } else {
                    displayResult(finder[j]);
                    finder[j] = null;
                }
            }
            try {
                Thread.sleep(1000);
            } catch (InterruptedException ie) {
                // do nothing
            }
        }
    }
    
    private void displayResult(PrimeFinder finder) {
        System.out.println("Prime " + finder.target + " is " + finder.prime);
    }
}
