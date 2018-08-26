const mongoose = require("mongoose");
const Task = mongoose.model("Task");
mongoose.Promise = global.Promise;

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
    rate: (req, res) => {
        Task.findBy(req.params.id, (err, task)=>{
            if(err){
                res.json(err)}
            else{
                task.rating.push(req.body)
                task.save()
                res.json({success: true});
                }
            })
    },

    //other method for rating...
//     rate: (req, res) => {
//         Restaurant.findOne({_id: req.params.id}, (err, rest)=>{
//             if(err){
//                 res.json(err)}
//             else{
//                 const review = new Rate({
//                     reviewer: req.body.reviewer,
//                     stars: req.body.stars,
//                     comment: req.body.comment
//                 });
//                 review.save(function(err){
//                     if(err){
//                         res.json(err)}
//                     else{
//                         rest._reviews.push(review)
//                         rest.save()
//                         res.json(rest);
//                     }}
//                 )
//             }
//     })
// },

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
        Product.findById(req.params.id)
        .then(result => res.json(result))
        .catch(err => res.json(err))  
            },

            //show ratings inside of an object
            // show: (req, res) => {
            //     Restaurant.findById(req.params.id).populate("_reviews").exec(function(err, postsFromDB){
            //         if(err) {
            //             console.log(err);
            //         } else {
            //             res.json(postsFromDB);
            //         }
            //     })},


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


//in case I need to use multiple db's, and validate errors


// const mongoose = require("mongoose");
// const Comment = mongoose.model("Comment");
// const Post = mongoose.model("Post");
// mongoose.Promise = global.Promise;


// module.exports = {
//     index: (req, res) => {
//         Post.find({}).populate("_comments").exec(function(err, postsFromDB){
//             if(err) {
//                 console.log(err);
//             } else {
//                 res.render("index", {posts: postsFromDB});
//             }
//         })
//     },
    
//     createPost: (req, res) => {
//         console.log("creating a new post");
        
//         const post = new Post(req.body);
//         post.save(function(err){
//             if(err){
//                 console.log("This error was thrown: ", err);
//                 for(var key in err.errors){
//                     req.flash('registration', err.errors[key].message);
//                 }
//                 res.redirect('/');
//             }
//             else {
//                 res.redirect('/');
//             }
//         });
//     },

//     createComment: (req, res) => {
//         console.log("creating a new comment");
//         Post.findOne({_id: req.params.id},(errorComment,post) =>{
//             if(errorComment){
//                 console.log(errorComment);
//             }
//             else{
//             const comment = new Comment({
//                 name: req.body.name,
//                 comment: req.body.comment,
//             });

//             comment.save(function(err){
//                 if(err){
//                     console.log("This error was thrown: ", err);
//                     for(var key in err.errors){
//                         req.flash('registration', err.errors[key].message);
//                     }
//                     res.redirect('/');
//                 }
//                 else {
//                     post._comments.push(comment)
//                     post.save()
//                     res.redirect('/');
//                 }
//             })
//         }
//     })
// }
// }