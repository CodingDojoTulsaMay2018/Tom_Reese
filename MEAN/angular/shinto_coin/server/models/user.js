const mongoose = require("mongoose");

const UserSchema = new mongoose.Schema({
    coins: {type: Number, required: [true, "Title field is required"], min:0}, 
   }, {timestamps: true})


mongoose.model('User', UserSchema);
