const mongoose = require("mongoose");
var uniqueValidator = require('mongoose-unique-validator');


const AuthorSchema = new mongoose.Schema({
    name: {
        type: String, 
        // unique: true,
        required: [true, "Name field is required"], 
        minlength:[2, "Name must be longer than 15 chars!"], 
        maxlength:[64, "Name must be shorter than 15 chars!"]}
   }, {timestamps: true})


   AuthorSchema.pre('findOneAndUpdate', function(next) {
    this.options.runValidators = true;
    next();
  });

mongoose.model('Author', AuthorSchema);
// AuthorSchema.plugin(uniqueValidator, {message: "Author name must be unique"});

// function _calculateAge(birthday) { // birthday is a date
//     var ageDifMs = Date.now() - birthday.getTime();
//     var ageDate = new Date(ageDifMs); // miliseconds from epoch
//     var diff = Math.abs(ageDate.getUTCFullYear() - 1970)
//     if(diff > 17 && diff < 120){
//         return true
//     }
//     return false
// }


//below is if I need to stuff db values into another db, like putting comments into a message

// const CommentSchema = new mongoose.Schema({
//     name: {type: String, required: [true, "Comment name field is required"], minlength:2}, 
//     comment: {type: String, required: [true, "Comment text field is required"], minlength:2}    
// }, {timestamps: true})

// mongoose.model('Comment', CommentSchema);

// const PostSchema = new mongoose.Schema({
//     name: {type: String, required: [true, "Post name field is required"], minlength:2}, 
//     post: {type: String, required: [true, "Post text field is required"], minlength:2},
//     _comments: [{ type : Schema.Types.ObjectId, ref: 'Comment' }]
//     }, {timestamps: true})

// mongoose.model('Post', PostSchema);