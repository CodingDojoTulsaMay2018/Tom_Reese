const user = require("./../controllers/users");

module.exports = (app) => {
    app.get("/user", user.index),
    app.post("/user", user.new),
    app.post("/user/:id", user.rate),
    app.get("/user/:id", user.show),
    app.put("/user/:id", user.update),
    app.delete("/user/:id", user.remove)
}