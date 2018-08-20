const mongoose = require("mongoose");

const RatingSchema = new mongoose.Schema({
    stars: {type: Number, required: [true, "Title field is required"], min:1, max:5}, 
    comment: {type: String, required: [true, "Completed field is required"], minlength:2, maxlength:100}, 
   }, {timestamps: true})


const FrisbeeSchema = new mongoose.Schema({
    type: {type: String, required: [true, "Title field is required"], minlength:2, maxlength:32}, 
    image: {type: String, required: [true, "Completed field is required"], minlength:2, maxlength:255}, 
    rating: [RatingSchema]
   }, {timestamps: true})

mongoose.model('Frisbee', FrisbeeSchema);
mongoose.model('Rating', RatingSchema);