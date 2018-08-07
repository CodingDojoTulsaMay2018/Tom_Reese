const mongoose = require("mongoose");
const Raptor = mongoose.model("Raptor");
mongoose.Promise = global.Promise;


module.exports = {
    index: (req, res) => {
        Raptor.find({}, (err, raptorsFromDB)=>{
            if(err) {
                console.log(err);
            } else {
                res.render("index", {raptors: raptorsFromDB});
            }
        })
    },
    
    create: (req, res) => {
        const raptor = new Raptor(req.body);
        raptor.save(function(err){
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

    newRap: (req, res) => {
        res.render("raptors");
    }, 
    
    showRap: (req, res) => {
        Raptor.findOne({_id:req.params.id}, (err, raptorsFromDB)=>{
            if(err) {
            console.log(err);
        } else {
            console.log(raptorsFromDB);
            res.render("show", {raptor: raptorsFromDB});
        }
    });
}, 

edit: (req, res) => {
    Raptor.findOne({_id:req.params.id}, (err, raptorsFromDB)=>{
        if(err) {
            console.log("error while editing raptor: ", err);
        } else {
            console.log(raptorsFromDB);
            res.render('edit', {raptor: raptorsFromDB});
        }
    });
},  

update: (req, res) => {
    Raptor.update({_id: req.params.id}, req.body, (err, raptorsFromDB) => {
        if(err) {
            console.log(err);
        } else {
            console.log(raptorsFromDB);
            res.redirect(`/raptors/${req.params.id}`);
        }
    });
},

delete: (req, res) => {
    Raptor.remove({_id: req.params.id}, (err, raptorsFromDB) => {
        if(err) {
            console.log("error while deleting raptor: ", err);
        } else {
            console.log(raptorsFromDB);
            res.redirect('/');
        }
    });
},
}
                                // create: (req, res) => {
                                //     const raptor = new Raptor(req.body);
                                //     raptor.save(function(err){
                                //         if(err){
                                //             console.log("We have an error!", err)
                                //             for(var key in err.errors){
                                //                 req.flash('registration', err.errors[key].message);
                                //             }
                                //             res.redirect('/');
                                //         }
                                //         else {
                                //             res.redirect('/');
                                //         }
                                //     });
                                // },
                                // show: (req, res) => {
                                //     Raptor.find({}, (err, raptorsFromDB)=>{
                                //         if(err) {
                                //             console.log(err);
                                //             console.log("there has been an error at the raptor show");
                                //         } else {
                                //             console.log(raptorsFromDB);
                                //             console.log("good to go for a new raptor");
                                //             res.render("raptors", {raptors: raptorsFromDB});
                                //         }
                                //     }).sort({createdAt: -1})
                                //     console.log("show went on with nothing happening...");
                                // }
                                // }