const mongoose = require("mongoose");
const Schema = mongoose.Schema

const CommentSchema = new mongoose.Schema({
    name: {type: String, required: [true, "Comment name field is required"], minlength:2}, 
    comment: {type: String, required: [true, "Comment text field is required"], minlength:2},
    _post: { type : Schema.Types.ObjectId, ref: 'Post' }
    
}, {timestamps: true})

mongoose.model('Comment', CommentSchema);

const PostSchema = new mongoose.Schema({
    name: {type: String, required: [true, "Post name field is required"], minlength:2}, 
    post: {type: String, required: [true, "Post text field is required"], minlength:2},
    _comments: [{ type : Schema.Types.ObjectId, ref: 'Comment' }]
    }, {timestamps: true})

mongoose.model('Post', PostSchema);