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

    this.punch = function(enemy){
        if(enemy instanceof Ninja){
            enemy.health -= 5;
            console.log(`${enemy.name} took it to the face!  Black eye cost them 5 health!  Their health is now ${enemy.health}.`);
        }
        console.log("You can't punch this thing man!")
    };
    this.kick = function(enemy){
        if(enemy instanceof Ninja){
            enemy.health -= 15;
            console.log(`${enemy.name} took it to the knee!  A snapped ACL cost them 15 health!  Their health is now ${enemy.health}.`);
        }
        console.log("You can't punch this thing man!");
}
}

var ninja1 = new Ninja("Hyabusa");
var ninja2 = new Ninja("Paula Deen");

ninja1.sayName();
ninja1.drinkSake();
ninja1.showStats();
console.log(ninja1);
ninja1.punch(ninja2);
ninja2.kick(ninja1);
ninja2.kick(ninja1);
