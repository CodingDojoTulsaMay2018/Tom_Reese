const frisbees = require("./../controllers/frisbees");

module.exports = (app) => {
    app.get("/frisbees", frisbees.index),
    app.post("/frisbees", frisbees.new),
    app.post("/frisbees/:id", frisbees.rate),
    app.get("/frisbees/:id", frisbees.show),
    app.put("/frisbees/:id", frisbees.update),
    app.delete("/frisbees/:id", frisbees.remove)
}