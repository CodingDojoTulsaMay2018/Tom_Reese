const mongoose = require("mongoose");
const User = mongoose.model("User");

module.exports = {
    index: (req, res) => {
        User.find({},(err,user)=>{
        res.json(user);
        })
    }, 
    new: (req, res) => {
        const user = new User({name:req.params.name});
        user.save(function(err){
                res.redirect('/');
            });
    },
    remove: (req, res) => {
        User.findOne({name:req.params.name}, (err, user)=>{
            user.remove()
            res.redirect('/');
                });
    },
    show: (req, res) => {
        User.findOne({name:req.params.name}, (err, user)=>{
            res.json(user);
                });
    }
}