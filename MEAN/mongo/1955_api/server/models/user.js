const mongoose = require("mongoose");

const UserSchema = new mongoose.Schema({
    name: {type: String, required: [true, "Name field is required"], minlength:2}, 
   }, {timestamps: true})

mongoose.model('User', UserSchema);