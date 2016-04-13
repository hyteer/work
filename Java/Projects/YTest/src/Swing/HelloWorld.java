/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Swing;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
// This is a Login class, can be designed as a container inheriting class
/**
 *
 * @author Administrator
 */
public class HelloWorld extends JPanel{
    static final int WIDTH=300;
    static final int HEIGHT=150;
    JFrame loginframe;
    // 按网格组布局排列组件
    
    public void add(Component c, GridBagConstraints constraints, int x, int y,
             int w, int h) {
        constraints.gridx = x;
        constraints.gridy = y;
        constraints.gridwidth = w;
        constraints.gridheight = h;
        add(c, constraints);
    }
    // Constructor
    HelloWorld() {
        loginframe = new JFrame("Welcome to java's world!");
        loginframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        GridBagLayout lay = new GridBagLayout();
        setLayout(lay);
        loginframe.add(this, BorderLayout.WEST);
        loginframe.setSize(WIDTH, HEIGHT);
        Toolkit kit = Toolkit.getDefaultToolkit();
        Dimension screenSize = kit.getScreenSize();
        int width = screenSize.width;
        int height = screenSize.height;
        int x = (width-WIDTH)/2;
        int y = (height-HEIGHT)/2;
        loginframe.setLocation(x,y);
        JButton ok = new JButton("Login");
        JButton cancel = new JButton("Cancel");
        JLabel title = new JLabel("Welcome to Swing's world!");
        JLabel name = new JLabel("User ID");
        JLabel password = new JLabel("Password");
        final JTextField nameinput = new JTextField(15);
        final JTextField passwordinput = new JTextField(15);
        GridBagConstraints constraints = new GridBagConstraints();
        constraints.fill = GridBagConstraints.NONE;
        constraints.anchor = GridBagConstraints.EAST;
        constraints.weightx = 3;
        constraints.weighty = 4;
        add(title,constraints,0,0,4,1);
        add(name,constraints,0,1,1,1);
        add(password,constraints,0,2,1,1);
        add(nameinput,constraints,2,1,1,1);
        add(passwordinput,constraints,2,2,1,1);
        add(ok,constraints,0,3,1,1);
        add(cancel,constraints,2,3,1,1);
        loginframe.setResizable(false);
        loginframe.setVisible(true);
        
        
    }
    public static void main(String[] args) {
        HelloWorld hell = new HelloWorld();
    }
}
