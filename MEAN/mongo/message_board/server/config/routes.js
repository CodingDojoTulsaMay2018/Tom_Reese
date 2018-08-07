const board = require("./../controllers/board");

module.exports = (app) => {
    app.get("/", board.index),
    app.post("/createpost", board.createPost),
    app.post('/createcomment/:id', board.createComment)
}