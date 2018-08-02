module.exports = app =>{
  app.get("/", (req, res)=> {
if('count' in req.session){
  req.session.count++
}
else{
  req.session.count = 1;
}
var sessx = {count: req.session.count}
  res.render('index', {session :sessx})})

  app.post("/add2", (req, Response)=> {
req.session.count++

    Response.redirect('/');
})
app.post("/destroy", (request, Response)=> {
  request.session.destroy()
  
      Response.redirect('/');
  })
  // app.get("/putin", function (req, res){ 
  //   var cat = {name:"Putin", Img: "/images/explode.jpg", FavGame:"Vodka", Age: 10, Secrets : ["In Russia, secrets know you", "Registered to vote in America of U-S"]}
  //   res.render('details', {cats: cat});
  // })
}


