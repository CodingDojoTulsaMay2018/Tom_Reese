var mongoose = require("mongoose")
const Schema = mongoose.Schema




const UserSchema = new Schema({
    first_name:{type: String, validate: firstNameValidator},
    last_name:{type: String, required: true, validate: lastNameValidator},
    password:{type: String, required: true},
    email:{type: String, required: true, validate: emailValidator},
    birthday: {type: String, required: [true, "Birthday field is required"], minlength:2}    
}, {timestamps: true})



mongoose.model('User', UserSchema);

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

