const mongoose = require("mongoose");

const UserSchema = new mongoose.Schema({
    name: {type: String, required: [true, "Name field is required"]}, 
    age: Number
   }, {timestamps: true})

mongoose.model('user', UserSchema);