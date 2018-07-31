function Ninja(name) {
    this.health = 100;
    this.name = name;
    this.speed = 3;
    this.strength = 3;
    
    this.drinkSake = function() {
        this.health += 10;
        console.log("Your current health is "+this.heath);
    };
  
    this.showStats = function(){
        console.log(`Your health is ${this.health}, your speed is ${this.speed}, your strength is ${this.strength}, and your name is ${this.name}.`)
    };
    this.sayName = function() {
      console.log(name);
    }; 
}

var ninja1 = new Ninja("Hyabusa");
ninja1.sayName();
// -> "My ninja name is Hyabusa!"
ninja1.drinkSake();
ninja1.showStats();
// -> "Name: Hayabusa, Health: 100, Speed: 3, Strength: 3"
