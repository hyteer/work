var http = require('http');
var soap = require('soap');

var myService = {
      MyService: {
          MyPort: {
              MyFunction: function(args) {
                  return {
                      name: args.name
                  };
              },
 
              // This is how to define an asynchronous function. 
              MyAsyncFunction: function(args, callback) {
                  // do some work 
                  callback({
                      name: args.name
                  });
              },
 
              // This is how to receive incoming headers 
              HeadersAwareFunction: function(args, cb, headers) {
                  return {
                      name: headers.Token
                  };
              },
 
              // You can also inspect the original `req` 
              reallyDeatailedFunction: function(args, cb, headers, req) {
                  console.log('SOAP `reallyDeatailedFunction` request from ' + req.connection.remoteAddress);
                  return {
                      name: headers.Token
                  };
              }
          }
      }
  };
 
  var xml = require('fs').readFileSync('../Res/myService.wsdl', 'utf8'),
      server = http.createServer(function(request,response) {
          response.end("404: Not Found: " + request.url);
      });
 
  server.listen(8000);
  soap.listen(server, '/wsdl', myService, xml);
  console.log('Soap Server listen on: 8000');