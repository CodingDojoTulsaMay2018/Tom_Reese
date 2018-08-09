const express = require("express");
const path = require("path");
const bodyParser = require('body-parser');
const app = express();
const PORT = 5000;

app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, "./static")));
app.set("views", path.join(__dirname, "./views"));
app.set("view engine", "ejs");


require("./server/config/mongoose");
require("./server/config/routes")(app);

app.listen(PORT, ()=>{
    console.log(`Listening on port: ${PORT}!`);
})