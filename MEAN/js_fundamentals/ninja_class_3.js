class Ninja{

    constructor(name){
    this.name = name;
    this.health = 100;
    this.speed = 3;
    this.strength = 3;
    }

    drinkSake() {
        this.health += 10;
        console.log(`You drank some local booze! Your current health is ${this.health}`);
        return this
    };
  
    showStats(){
        console.log(`Your health is ${this.health}, your speed is ${this.speed}, your strength is ${this.strength}, and your name is ${this.name}.`)
        return this
    };
    sayName() {
      console.log(this.name);
      return this
    }; 

    punch(enemy){
        if(enemy instanceof Ninja){
            enemy.health -= 5;
            console.log(`${enemy.name} took it to the face!  Black eye cost them 5 health!  Their health is now ${enemy.health}.`);
            return this
        }
        console.log("You can't punch this thing man!")
        return this
    };
    kick(enemy){
        if(enemy instanceof Ninja){
            enemy.health -= 15;
            console.log(`${enemy.name} took it to the knee!  A snapped ACL cost them 15 health!  Their health is now ${enemy.health}.`);
            return this
        }
        console.log("You can't kickthis thing man!");
        return this
}
}


class Sensei extends Ninja {
    constructor(name) {
        super(name);
        this.health = 100;
        this.speed = 10;
        this.strength = 10;
        this.wisdom = 10;
    }
    speakWisdom() {
        super.drinkSake();
        console.log("How many cows can you fit in dutch oven?  Depends.");
        return this
    }
}


var ninja1 = new Ninja("Hyabusa");
var ninja2 = new Ninja("Paula Deen");

ninja1.sayName();
ninja1.drinkSake();
ninja1.showStats();
ninja1.punch(ninja2);
ninja2.kick(ninja1);
ninja2.kick(ninja1);
ninja1.drinkSake();
const superSensei = new Sensei("Master Splinter");
superSensei.speakWisdom();
superSensei.showStats();