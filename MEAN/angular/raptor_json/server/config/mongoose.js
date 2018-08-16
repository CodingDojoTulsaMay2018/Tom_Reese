const mongoose = require("mongoose");
const path = require("path");
const fs = require("fs");
mongoose.Promise = global.Promise;

mongoose.connect("mongodb://localhost:27017/raptors_json", { useNewUrlParser: true });

var models_path = path.join(__dirname, './../models');

fs.readdirSync(models_path).forEach(function(file) {
  if(file.indexOf('.js') >= 0) {
    require(models_path + '/' + file);
   }
}) 