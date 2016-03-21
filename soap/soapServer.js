var express = require("express");
var app = express();
var data='<?xml version="1.0"?><soap:Envelope xmlns:soap="http://www.w3.org/2001/12/soap-envelope" soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding"><soap:Body xmlns:m="http://www.example.org/stock"><m:GetStockPriceResponse><m:Price>34.5</m:Price></m:GetStockPriceResponse></soap:Body></soap:Envelope>';

console.log(data);

app.get('/Dynamic', function(req, response) {
response.contentType('application/xml');
console.log('listening');
response.send(data);
});
console.log('server will be listening on: 1360' );
app.listen(1360);