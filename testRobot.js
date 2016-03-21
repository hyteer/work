var http = require('http');
var express = require('express');
var app = express();

app.post('/SayHello',function(req,res){
	res.send('Test response by YT');
	console.log(res.body);
})

app.listen(8088,function(){
	console.log('test Robot listen on: 8088');
})
