package ytest;
import java.io.FileOutputStream;
import java.io.IOException;
import com.lowagie.text.*;
import com.lowagie.text.pdf.PdfWriter;


public class GenPDF {
    static String pdfstr = "";
    static String pdf = "Hello! \nThis is a test for demostrate generating PDF file.+"
                + "\nIt's a test programe write by YT...";

public GenPDF(String[] args) {
    System.out.println("pdfstr.length:"+ pdfstr.length());
    System.out.println("args[0]:"+ args[0]);
    if (args.length > 0) {
        for (int i=0; pdfstr.length()<500000; i++){
          // if (pdfstr.length() <=500000) {
               //pdfstr = args[0];
              pdfstr += args[0];
              // System.out.println("pdfstr:"+ pdfstr);
          // }
        
        }
       /*
        pdfstr = args[0];
        pdfstr+= args[0];*/
        System.out.println("pdfstr.length:"+ pdfstr.length());
    } else {
        pdfstr = "No content...";
    }
    System.out.println("Pdf:" + pdfstr);
    System.out.println("Silly".length());
}
    
public static void main(String[] args) {
    
    GenPDF pdftest = new GenPDF(args);
    
    // 创建一个Document对象
    Document document = new Document();
    //String pdfcon = pdfstr;
    try 
    {
        // 生成名为 HelloWorld.pdf 的文档
        PdfWriter.getInstance(document, new FileOutputStream("GenPDF-Test.pdf"));
        // 添加PDF文档的一些信息
        document.addTitle("A demostration.");
        document.addAuthor("Bruno Lowagie");
        document.addSubject("This example explains how to add metadata.");
        document.addKeywords("iText, Hello World, step 3, metadata");
        document.addCreator("My program using iText");
        // 打开文档，将要写入内容
        document.open();
        // 插入一个段落
        
        if(document.add(new Paragraph(pdfstr))) {
            System.out.println("Generate PDF sucessful...");
        }
        

    } catch (DocumentException de) 
    {
        System.err.println(de.getMessage());
    }
    catch (IOException ioe) 
    {
        System.err.println(ioe.getMessage());
    }
    // 关闭打开的文档
    
    document.close();
}
}