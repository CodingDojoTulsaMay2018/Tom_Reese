module.exports = app =>{
  app.get("/", (req, res)=> {
      res.render('index');
  })
  app.get("/remington", function (req, res){ 
    var cat = {name:"Remington", Img: "/images/cat.jpg", FavGame:"3-Gun", Age: 3, Secrets : ["I know when you sleep", "I laugh in the dark"]}
    res.render('details', {cats: cat});
    console.log(cat);
    
  })
  app.get("/chopper", function (req, res){ 
    var cat = {name:"Chopper", Img: "/images/cheetah.jpg", FavGame:"murdering rabbits", Age: 4, Secrets : ["I'm actually hungry right now", "Have you always looked this delicious?"]}
    res.render('details', {cats: cat});
  })
  app.get("/putin", function (req, res){ 
    var cat = {name:"Putin", Img: "/images/explode.jpg", FavGame:"Vodka", Age: 10, Secrets : ["In Russia, secrets know you", "Registered to vote in America of U-S"]}
    res.render('details', {cats: cat});
  })
}


