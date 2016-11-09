
package org.me.cal;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlType;


/**
 * <p>add complex type的 Java 类。
 * 
 * <p>以下模式片段指定包含在此类中的预期内容。
 * 
 * <pre>
 * &lt;complexType name="add"&gt;
 *   &lt;complexContent&gt;
 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType"&gt;
 *       &lt;sequence&gt;
 *         &lt;element name="i" type="{http://www.w3.org/2001/XMLSchema}int"/&gt;
 *         &lt;element name="j" type="{http://www.w3.org/2001/XMLSchema}int"/&gt;
 *       &lt;/sequence&gt;
 *     &lt;/restriction&gt;
 *   &lt;/complexContent&gt;
 * &lt;/complexType&gt;
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "add", propOrder = {
    "i",
    "j"
})
public class Add {

    protected int i;
    protected int j;

    /**
     * 获取i属性的值。
     * 
     */
    public int getI() {
        return i;
    }

    /**
     * 设置i属性的值。
     * 
     */
    public void setI(int value) {
        this.i = value;
    }

    /**
     * 获取j属性的值。
     * 
     */
    public int getJ() {
        return j;
    }

    /**
     * 设置j属性的值。
     * 
     */
    public void setJ(int value) {
        this.j = value;
    }

}
