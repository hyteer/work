package org.me.cal;

import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.ejb.Stateless;

/**
 *
 * @author hyteer
 */
@WebService(serviceName = "CalWS")
@Stateless()
public class CalFull {
  //加法
  @WebMethod(operationName = "plus")
  public float plus(@WebParam(name = "x")float x, @WebParam(name = "y")float y) {
    return x + y;
  }
  //减法
  @WebMethod(operationName = "minus")
  public float minus(@WebParam(name = "x")float x, @WebParam(name = "y")float y) {
    return x - y;
  }
  //乘法
  @WebMethod(operationName = "multiply")
  public float multiply(@WebParam(name = "x")float x, @WebParam(name = "y")float y) {
    return x * y;
  }
  //除法
  @WebMethod(operationName = "divide")
  public float divide(@WebParam(name = "x")float x, @WebParam(name = "y")float y) {
    if(y!=0)
    {
      return x / y;
    }
    else
      return -1;
  }
}