const mongoose = require("mongoose");
const Quote = mongoose.model("Quote");

module.exports = {
    index: (req, res) => {
        res.render("index");
        console.log("at the index");
    }, 
    create: (req, res) => {
        const quote = new Quote(req.body);
        quote.save(function(err){
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
        Quote.find({}, (err, quotesFromDB)=>{
            if(err) {
                console.log(err);
                console.log("there has been an error at the quote show");
            } else {
                console.log(quotesFromDB);
                console.log("good to go for a new quote");
                res.render("quotes", {quotes: quotesFromDB});
            }
        }).sort({createdAt: -1})
        console.log("show went on with nothing happening...");
    }
}