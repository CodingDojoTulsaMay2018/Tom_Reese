const raptors = require("./../controllers/raptors");

module.exports = (app) => {
    app.get("/", raptors.index),
    app.post("/create", raptors.create) 
    app.get("/raptors/new", raptors.newRap)
    app.get('/raptors/:id', raptors.showRap)
    app.get('/edit/:id', raptors.edit)
    app.post('/raptors/:id', raptors.update)
    app.get('/destroy/:id', raptors.delete) 
}