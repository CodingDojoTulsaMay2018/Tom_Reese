const mongoose = require("mongoose");
// const Task = mongoose.model("Task");

module.exports = {
    index: (req, res) => {
        Task.find({},(err,task)=>{
        res.json(task);
        })
    }, 
    new: (req, res) => {
        Task.create(req.body , (err,task) =>{;
        if(err){
            res.json(err)}
            else{
            res.json(task);
            }
        });
        
    },
    remove: (req, res) => {
        Task.findByIdAndRemove(req.params.id, (err)=>{
            if(err){
                res.json(err)}
            else{
                res.json({success: true});
                }
            })
    },
    show: (req, res) => {
        Task.findOne({task:req.params.id}, (err, task)=>{
            res.json(task);
                });
    },
    update: (req, res) => {
        Task.findByIdAndUpdate(req.params.id, {$set: req.body}, (err, task)=>{
            if(err){
                res.json(err)}
            else{
                res.json(task);
                }
        })
    }
}