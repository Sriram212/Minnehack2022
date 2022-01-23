const http = require('http');

// include the express modules
var express = require("express");

// create an express application
var app = express();
const url = require('url');

// helps in extracting the body portion of an incoming request stream
var bodyparser = require('body-parser');

// fs module - provides an API for interacting with the file system
var fs = require("fs");

// apply the body-parser middleware to all incoming requests
app.use(bodyparser());

const hostname = '127.0.0.1';
const port = 9007;


// server listens on port 9007 for incoming connections
app.listen(9007, () => console.log('Listening on port 9007!'));

app.use("/client/", express.static(__dirname + '/client'));

// function to return the welcome page
app.get('/',function(req, res) {
	res.sendFile(__dirname + '/client/index.html');
});

// function to return the bailey page
app.get('/bailey',function(req, res) {
	res.sendFile(__dirname + '/client/bailey.html');
});
// function to return the amazon page
app.get('/amazon',function(req, res) {
	res.sendFile(__dirname + '/client/amazon.html');
});

// function to return the amazon page
app.get('/amazonText',function(req, res) {
	fs.readFile("../Amazon.html", "utf-8", (err, data) => {
		res.send(data)
	})
});

// function to return the amazon page
app.get('/google',function(req, res) {
	res.sendFile(__dirname + '/client/google.html');
});

// function to return the amazon page
app.get('/googleText',function(req, res) {
	fs.readFile("../Google.html", "utf-8", (err, data) => {
		res.send(data)
	})
});
