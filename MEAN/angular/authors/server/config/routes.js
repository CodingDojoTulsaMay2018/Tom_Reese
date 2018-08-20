const author = require("./../controllers/authors");
const path = require('path');


module.exports = (app) => {
    console.log("in the routes...."),
    
    app.get("/author", author.index),
    app.post("/author", author.new),
    app.post("/author/:id", author.rate),
    app.get("/author/:id", author.show),
    app.put("/author/:id", author.update),
    app.delete("/author/:id", author.remove),
    app.all("*", (req,res,next) => {
        res.sendFile(path.resolve("./public/dist/public/index.html"))
      });
}