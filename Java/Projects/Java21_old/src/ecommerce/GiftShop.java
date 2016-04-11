/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ecommerce;

/**
 *
 * @author Administrator
 */
public class GiftShop {
    public static void main(String[] args) {
        Storefront store = new Storefront();
        store.addItem("C01", "MUG", "9.99", "150");
        store.addItem("CO2", "LG MUG", "12.99", "82");
        store.addItem("C03", "MOUSEPAD", "10.49", "800");
        store.addItem("DO1", "T SHIRT", "16.99", "90");
        store.sort();
        
        for (int i=0; i<store.getSize(); i++) {
            Item show = (Item)store.getItem(i);
            System.out.println("\nItem ID: " + show.getId() +
                    "\nName:" + show.getName() +
                    "\nRetail Price:$" + show.getRetail() +
                    "\nPrice:$" + show.getPrice() +
                    "\nQuantity:" + show.getQuantity());
        }
    }
}
