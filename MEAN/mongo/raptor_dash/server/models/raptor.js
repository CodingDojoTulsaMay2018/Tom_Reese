const mongoose = require("mongoose");

const RaptorSchema = new mongoose.Schema({
    name: {type: String, required: [true, "Name field is required"], minlength:2}, 
    ability: {type: String, required: [true, "Ability field is required"], minlength:2}
   }, {timestamps: true})

mongoose.model('Raptor', RaptorSchema);