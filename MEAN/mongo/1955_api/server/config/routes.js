const users = require("./../controllers/users");

module.exports = (app) => {
    app.get("/", users.index),
    app.get("/new/:name", users.new),
    app.get("/remove/:name", users.remove),
    app.get("/:name", users.show)
}