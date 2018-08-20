const raptor = require("./../controllers/raptors");
const path = require('path');


module.exports = (app) => {

    app.get("/raptor", raptor.index),
    app.post("/raptor", raptor.new),
    app.post("/raptor/:id", raptor.rate),
    app.get("/raptor/:id", raptor.show),
    app.put("/raptor/:id", raptor.update),
    app.delete("/raptor/:id", raptor.remove),
    app.all("*", (req,res,next) => {
        res.sendFile(path.resolve("./public/dist/public/index.html"))
      });
}