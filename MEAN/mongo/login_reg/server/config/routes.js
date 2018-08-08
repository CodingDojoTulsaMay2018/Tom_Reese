const logreg = require("./../controllers/log_reg");

module.exports = (app) => {
    app.get("/", logreg.index),
    app.post("/sessions", logreg.sessions),
    app.post('/users', logreg.users)
}