const mongoose = require("mongoose");
const User = mongoose.model("User");

module.exports = {
    index: (req, res) => {
        User.find({},(err,user)=>{
        res.json(user);
        })
    }, 
    new: (req, res) => {
        User.create(req.body , (err,user) =>{;
        if(err){
            res.json(err)}
            else{
            res.json(user);
            }
        });
        
    },
    rate: (req, res) => {
        User.findBy(req.params.id, (err, user)=>{
            if(err){
                res.json(err)}
            else{
                user.rating.push(req.body)
                user.save()
                res.json({success: true});
                }
            })
    },
    remove: (req, res) => {
        User.findByIdAndRemove(req.params.id, (err)=>{
            if(err){
                res.json(err)}
            else{
                res.json({success: true});
                }
            })
    },
    show: (req, res) => {
        User.findOne({user:req.params.id}, (err, user)=>{
            if(err){
                res.json(err)}
            else{
                res.json(user);     
            }
        });
            },
    update: (req, res) => {
        User.findByIdAndUpdate(req.params.id, {$set: req.body}, (err, user)=>{
            if(err){
                res.json(err)}
            else{
                res.json(user);
                }
        })
    }
}