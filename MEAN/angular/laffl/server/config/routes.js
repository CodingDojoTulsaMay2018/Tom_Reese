const task = require("./../controllers/tasks");
const path = require('path');


module.exports = (app) => {
    app.get("/task", task.index),
    app.post("/task", task.new),
    app.post("/task/:id", task.rate),
    app.get("/task/:id", task.show),
    app.put("/task/:id", task.update),
    app.delete("/task/:id", task.remove),
    app.all("*", (req,res,next) => {
        res.sendFile(path.resolve("./public/dist/public/index.html"))
    });
}