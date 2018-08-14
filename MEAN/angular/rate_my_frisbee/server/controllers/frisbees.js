const mongoose = require("mongoose");
const Frisbee = mongoose.model("Frisbee");
// const Rating = mongoose.model("Rating");

module.exports = {
    index: (req, res) => {
        Frisbee.find({},(err,frisbee)=>{
        res.json(frisbee);
        })
    }, 
    new: (req, res) => {
        Frisbee.create(req.body , (err,frisbee) =>{;
        if(err){
            res.json(err)}
            else{
            res.json(frisbee);
            }
        });
        
    },
    rate: (req, res) => {
        Frisbee.findBy(req.params.id, (err, frisbee)=>{
            if(err){
                res.json(err)}
            else{
                frisbee.rating.push(req.body)
                frisbee.save()
                res.json({success: true});
                }
            })
    },
    remove: (req, res) => {
        Frisbee.findByIdAndRemove(req.params.id, (err)=>{
            if(err){
                res.json(err)}
            else{
                res.json({success: true});
                }
            })
    },
    show: (req, res) => {
        Frisbee.findOne({frisbee:req.params.id}, (err, frisbee)=>{
            if(err){
                res.json(err)}
            else{
                res.json(frisbee);     
            }
        });
            },
    update: (req, res) => {
        Frisbee.findByIdAndUpdate(req.params.id, {$set: req.body}, (err, frisbee)=>{
            if(err){
                res.json(err)}
            else{
                res.json(frisbee);
                }
        })
    }
}