/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ytest;
import javax.swing.JFrame;
/**
 *
 * @author Administrator
 */
public class SwingTest {
    static final int WIDTH = 300;
    static final int HEIGHT = 200;
    public static void main(String[] args) {
        JFrame jf = new JFrame("hello swing");
        jf.setSize(WIDTH, HEIGHT);
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jf.setVisible(true);
    }
}
