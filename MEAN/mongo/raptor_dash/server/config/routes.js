const raptors = require("./../controllers/raptors");

module.exports = (app) => {
    app.get("/", quotes.index),
    app.post("/raptors", raptors.create) 
    app.get("/raptors", raptors.show)
}