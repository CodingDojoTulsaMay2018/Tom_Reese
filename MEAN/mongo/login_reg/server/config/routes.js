const logreg = require("./../controllers/log_reg");

module.exports = (app) => {
    app.get("/", logreg.index),
    app.post("/log", logreg.log),
    app.post('/reg', logreg.reg),
    app.get("/success", logreg.success)
}