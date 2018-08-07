const users = require("./../controllers/users");

module.exports = (app) => {
    app.get("/", users.index),
    app.get("/users", users.create)
}