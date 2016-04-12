/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Week2;
import java.util.*;
/**
 *
 * @author Administrator
 */
public class CodeKeeper {
    ArrayList list;
    String[] codes = { "alpha", "lambda", "gamma", "delta", "zeta" };
    
    public CodeKeeper(String[] userCodes) {
        list = new ArrayList();
        // load built-in codes
        for (int i=0; i<codes.length; i++) {
            addCode(codes[i]);
        }
        // load user codes
        for (int j=0; j<userCodes.length; j++) {
            addCode(userCodes[j]);
        }
        // display all codes
        for (Iterator ite = list.iterator(); ite.hasNext();) {
            String output = (String) ite.next();
            System.out.println(output);
        }
        
        for ( Object name: list) {
            System.out.println("|"+name);
        }
    }
    
    private void addCode(String code) {
        if (!list.contains(code)) {
            list.add(code);
        }
    }
    
    public static void main(String[] args) {
        CodeKeeper keeper = new CodeKeeper(args);
    }
}
