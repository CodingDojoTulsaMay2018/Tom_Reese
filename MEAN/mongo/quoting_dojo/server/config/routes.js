const quotes = require("./../controllers/quotes");

module.exports = (app) => {
    app.get("/", quotes.index),
    app.post("/quotes", quotes.create)
    app.get("/quotes", quotes.show)
}