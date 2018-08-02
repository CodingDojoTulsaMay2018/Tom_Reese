module.exports = app =>{
  app.get("/", (req, res)=> {

  res.render('index')})

  app.post("/submit", (req, res)=> {
  console.log("at process");
  req.session.name = req.body.name;
  req.session.dojo_location = req.body.dojo_location;
  req.session.fav_lang = req.body.fav_lang;
  req.session.comment = req.body.comment;
  res.redirect('results')})

  app.get("/results", (req, res)=> {
  console.log("at result");
  
    res.render('results', {session : req.session})})

}


