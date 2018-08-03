const express = require("express");
var session = require('express-session');
var app = express();
// var ses = express-session();
const path = require("path");
const bodyParser = require('body-parser');
const server = app.listen(8000, function() {
console.log("listening on port 8000");
const io = require('socket.io')(server);

var count = 0;

io.on('connection', function (socket) {
  io.emit('update', {msg:count})
  console.log("back at server")
  
  socket.on('addsubmit', function() { //4
  console.log(count+" is the new count");
  count++
  io.emit('update', { msg: count});})

  socket.on('destroy', function() {
  count = 0;
  io.emit('update', { msg: count});
    ;})
  ;})
});

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "./static")));

// app.use(session({
//   secret: 'keyboardkitteh',
//   resave: false,
//   saveUninitialized: true,
//   cookie: { maxAge: 60000 }
// }))

app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
require("./server/config/routes")(app);
