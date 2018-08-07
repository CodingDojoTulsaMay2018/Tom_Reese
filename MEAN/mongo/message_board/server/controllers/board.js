const mongoose = require("mongoose");
const Comment = mongoose.model("Comment");
const Post = mongoose.model("Post");
mongoose.Promise = global.Promise;


module.exports = {
    index: (req, res) => {
        Post.find({}).populate("_comments").exec(function(err, postsFromDB){
            if(err) {
                console.log(err);
            } else {
                res.render("index", {posts: postsFromDB});
            }
        })
    },
    
    createPost: (req, res) => {
        console.log("creating a new post");
        
        const post = new Post(req.body);
        post.save(function(err){
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

    createComment: (req, res) => {
        console.log("creating a new comment");
        Post.findOne({_id: req.params.id},(errorComment,post) =>{
            if(errorComment){
                console.log(errorComment);
            }
            else{
            const comment = new Comment({
                name: req.body.name,
                comment: req.body.comment,
            });

            comment.save(function(err){
                if(err){
                    console.log("This error was thrown: ", err);
                    for(var key in err.errors){
                        req.flash('registration', err.errors[key].message);
                    }
                    res.redirect('/');
                }
                else {
                    post._comments.push(comment)
                    post.save()
                    res.redirect('/');
                }
            })
        }
    })
}
}