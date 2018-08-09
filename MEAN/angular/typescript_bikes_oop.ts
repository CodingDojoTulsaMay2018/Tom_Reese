// Using the TypeScript Playground tool, create a new class called Bike with the following properties/attributes:

// price
// max_speed
// miles
// Create 3 instances of the Bike class.

// Use the constructor() function to specify the price and max_speed of each instance (e.g. let bike1 = new Bike(200, "25mph"); also write the code so that the initial miles is set to be 0 whenever a new instance is created.

// Add the following functions to this class:

// displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
// ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
// reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
// Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().

// What would you do to prevent the instance from having negative miles?

// Which methods can return this in order to allow chaining methods?

// For assignment submission, upload a ".ts" file with the contents of the TypeScript Playground.

class Bike {
    fullName: string;
    constructor(
        public price: number,
        public max_speed: string,
        public miles = 0) { }
    displayInfo(){
        console.log(`${this.price},${this.max_speed},${this.miles}`)
    }
    ride(){
        console.log("Riding")
        this.miles += 10
        console.log(this.miles)   
        return this  
        }
    reverse(){
        console.log("Riding")
        this.miles -= 5
        if(this.miles < 0){
            this.miles = 0;
            return this
        }
        console.log(this.miles)
        return this
    } 
    }

    const bike1 = new Bike(500,"twenty-fivemph");
    const bike2 = new Bike(700,"thirty-fivemph");
    const bike3 = new Bike(900,"forty-fivemph");

    bike1.ride().ride().ride().displayInfo()
    bike2.ride().ride().reverse().reverse().displayInfo()
    bike3.reverse().reverse().reverse().displayInfo()

