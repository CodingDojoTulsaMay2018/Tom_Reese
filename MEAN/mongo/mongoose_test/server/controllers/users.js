const mongoose = require("mongoose");
const User = mongoose.model("user");

module.exports = {
    index: (req, res) => {
        User.find({}, (err, usersFromDB)=>{
            if(err) {
                console.log(err);
                console.log("2");
            } else {
                console.log(usersFromDB);
                console.log("2");
                res.render("index", {users: usersFromDB});
            }
        })
        console.log("1");
    }, 
    create: (req, res) => {
        const user = new User();
        user.age = 21;
        user.save((err)=>{
            if(err){
                console.log(err);
            }
            res.redirect("/");
        });
    }
}