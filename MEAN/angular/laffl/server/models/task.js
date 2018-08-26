const mongoose = require("mongoose");
var uniqueValidator = require('mongoose-unique-validator');

const TaskSchema = new mongoose.Schema({
    title: {
        type: String, 
        required: [true, "Title field is required"], 
        minlength:[2, "Name must be longer than 15 chars!"], 
        maxlength:[15, "Name must be shorter than 15 chars!"]},
    description: {
        type: String, 
        required: [true, "Completed field is required"], 
        minlength:2,
        maxlength:[15, "Name must be shorter than 15 chars!"]},
    number: {
        type: Number, 
        required:[true, "How many tasks are left?"],
        min: -9999,
        max: 9999
    },
    password:{type: String, 
        required: [true, "Password field is required"], 
        minlength:[2, "Password must be longer than 15 chars!"],
        maxlength: [32, "Password must be shorter than 33 chars!"]
    },
    email: {
        type: String, 
        unique: true,
        required: [true, "Email is required."],
        validate: {
            validator: function(email) {
                return /^[a-zA-Z0-9.!#$%&’+\/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:.[a-zA-Z0-9-]+)$/.test(email)
            },
            message: 'Please enter a valid email.'
        }, 
        maxlength: [120, 'Email must be less than 120 characters.']
    },
    birthday: {type: Date,
        validate: {
            validator: function checkDates(value) {
               return _calculateAge(value)               
             },
             message: date => `Must be older than 18 to enter (or less than 120)!!!`
        },
        required: [true, "Birthday field is required"]},
    completed: {
        type: Boolean, 
        default: false}
   }, {timestamps: true})


mongoose.model('Task', TaskSchema);
TaskSchema.plugin(uniqueValidator, {message: "Email must be unique"});

function _calculateAge(birthday) { // birthday is a date
    var ageDifMs = Date.now() - birthday.getTime();
    var ageDate = new Date(ageDifMs); // miliseconds from epoch
    var diff = Math.abs(ageDate.getUTCFullYear() - 1970)
    if(diff > 17 && diff < 120){
        return true
    }
    return false
}


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