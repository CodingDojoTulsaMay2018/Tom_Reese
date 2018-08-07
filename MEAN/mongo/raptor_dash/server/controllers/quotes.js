const raptor = require("raptor");
const Quote = raptor.model("Raptor");

module.exports = {
    index: (req, res) => {
        res.render("index");
        console.log("at the index");
    }, 
    create: (req, res) => {
        const raptor = new Raptor(req.body);
        raptor.save(function(err){
            if(err){
                console.log("We have an error!", err)
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
    show: (req, res) => {
        Raptor.find({}, (err, raptorsFromDB)=>{
            if(err) {
                console.log(err);
                console.log("there has been an error at the raptor show");
            } else {
                console.log(raptorsFromDB);
                console.log("good to go for a new raptor");
                res.render("raptors", {raptors: raptorsFromDB});
            }
        }).sort({createdAt: -1})
        console.log("show went on with nothing happening...");
    }
}