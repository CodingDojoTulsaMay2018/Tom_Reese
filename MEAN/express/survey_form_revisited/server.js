const express = require("express");
var session = require('express-session');
var app = express();
// var ses = express-session();
const path = require("path");
const bodyParser = require('body-parser');
const server = app.listen(8000, function() {
const io = require('socket.io')(server);

io.on('connection', function (socket) { //2
  socket.on('formsubmit', function (data) { //4
  console.log(data);
  socket.emit('greeting', { msg: data});
  var num = Math.floor((Math.random() * 1000) + 1)
  socket.emit('number', { num: num});
  ;});})


});


app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "./static")));
app.use(session({
  secret: 'keyboardkitteh',
  resave: false,
  saveUninitialized: true,
  cookie: { maxAge: 60000 }
}))

console.log("listening on port 8000");

app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
require("./server/config/routes")(app);
