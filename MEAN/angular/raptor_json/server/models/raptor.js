const mongoose = require("mongoose");

const RaptorSchema = new mongoose.Schema({
    name: {
        type: String, 
        required: [true, "Name field is required"], 
        minlength:2,
        maxlength:64}, 
    ability: {
        type: String, 
        required: [true, "Ability field is required"], minlength:2,
        maxlength:64}
   }, {timestamps: true})

   RaptorSchema.pre('findOneAndUpdate', function(next) {
    this.options.runValidators = true;
    next();
  });

mongoose.model('Raptor', RaptorSchema);