const mongoose = require("mongoose");
const User = mongoose.model("User");
mongoose.Promise = global.Promise;
const bcrypt = require('bcrypt');


module.exports = {
    index: (req, res) => {
        res.render("index");
            },
    
    users: (req, res) => {
        console.log("creating a new post");
        
        const user = new User(req.body);
        user.save(function(err){
            if(err){
                console.log("This error was thrown: ", err);
                for(var key in err.errors){
                    req.flash('registration', err.errors[key].message);
                }
                res.redirect('/');
            }
            else {
                res.redirect('/');
            }
        });
    },

    sessions: (req, res) => {
        console.log("creating a new comment");
        User.findOne({_id: req.params.id},(err,post) =>{
            if(err){
                console.log(err);
            }
            else{        
            res.redirect('/');
                }
            })
            }
}

// bcrypt.hash('password_from_form', 10)
// .then(hashed_password => {
	 
// })
// .catch(error => {
	 
// });


// bcrypt.compare('password_from_form', 'stored_hashed_password')
// .then( result => {
	 
// })
// .catch( error => {
	 
// })