var mongoose = require("mongoose")
const Schema = mongoose.Schema
var uniqueValidator = require('mongoose-unique-validator');



const UserSchema = new Schema({
    first_name:{type: String, 
        required: [true, "First name field is required"], 
        minlength:2,
        maxlength: 32},
    last_name:{type: String,
        required: [true, "Last name field is required"], 
        minlength:2,
        maxlength: 32
    },
    password:{type: String, 
        required: [true, "Password field is required"], 
        minlength:2,
        maxlength: 32
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
        required: [true, "Birthday field is required"]}    
}, {timestamps: true})



function _calculateAge(birthday) { // birthday is a date
    var ageDifMs = Date.now() - birthday.getTime();
    var ageDate = new Date(ageDifMs); // miliseconds from epoch
    var diff = Math.abs(ageDate.getUTCFullYear() - 1970)
    if(diff > 17 && diff < 120){
        return true
    }
    return false
}

mongoose.model('User', UserSchema);
UserSchema.plugin(uniqueValidator, {message: "Email must be unique"});





























// var validate = require('mongoose-validator');
// var uniqueValidator = require('mongoose-unique-validator');
// var firstNameValidator = [
//     validate({
//       validator: 'isLength',
//       arguments: [3, 50],
//       message: 'First name should be between {ARGS[0]} and {ARGS[1]} characters',
//     }),
//     validate({
//       validator: 'isAlpha',
//       passIfEmpty: true,
//       message: 'First name should contain alpha characters only',
//     }),
//   ]

//   var lastNameValidator = [
//     validate({
//       validator: 'isLength',
//       arguments: [3, 50],
//       message: 'First name should be between {ARGS[0]} and {ARGS[1]} characters',
//     }),
//     validate({
//       validator: 'isAlpha',
//       passIfEmpty: false,
//       message: 'First name should contain alpha characters only',
//     }),
//   ]

//   var emailValidator = [
//     validate({
//       validator: 'isEmail',
//       passIfEmpty: false,
//       message: 'Email must be in valid format, and cannot be empty',
//     })
//   ]

