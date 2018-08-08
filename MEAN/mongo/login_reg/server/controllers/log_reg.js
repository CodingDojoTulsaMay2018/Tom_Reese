const mongoose = require("mongoose");
const User = mongoose.model("User");
mongoose.Promise = global.Promise;
const bcrypt = require('bcrypt');


module.exports = {
    index: (req, res) => {
        res.render("index");
            },
    reg: (req, res) => {
        console.log("registering a new user");
        const newUser = new User(req.body);
        newUser.save(function(err){
            if(err){
                console.log("This error was thrown: ", err);
                for(var key in err.errors){
                    req.flash('registration', err.errors[key].message);
                }
                res.redirect('/');
            }
            else {
                console.log(newUser);
                newUser.password = bcrypt.hashSync(newUser.password, 10)
                newUser.save()
                res.redirect('/success');
            }
        });
    },
    
    log: (req, res) => {
        console.log("user is trying to log in");
        User.findOne({email: req.body.email},(err, user) =>{
            if(err){
                console.log(err);
                res.redirect('/');
            }
            if(user === null){
                console.log("User doesn't exist");
                res.redirect('/'); 
            }
            else{
                passwordIsValid = bcrypt.compareSync(req.body.password, user.password)
                if(passwordIsValid){
                    console.log(user.first_name);
                    res.redirect('/success'); 
                }
                else{
                    console.log("The password is incorrect")
                    res.redirect('/')
                }
            }
        })
    },
    
    success: (req, res) => {
        res.render("success");
            },
}
