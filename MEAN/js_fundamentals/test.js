// function heapsort(heap){
    
//     heap.unshift(undefined)
//     console.log(heap)
//     for(var num in heap){
//         if(heap[num] < heap[num*2]){
//             var temp = heap[num]
//             heap[num] = heap[num*2]
//             heap[num*2] = temp;
//             num--;}
//         if(heap[num] < heap[(num*2)+1]){
//             var swap = heap[num]
//             heap[num] = heap[(num*2)+1]
//             heap[num*2+1] = swap;
//             num--;}
//         while(heap[num] > heap[num/2]){
//             var x = heap[num/2]
//             heap[num/2] = heap[num]
//             heap[num] = x;
//             num--;
//             num = num/2;}
//     }
//     console.log(heap)
// }

// heapsort([9,6,23,56,4,0,87,54,2,15,41,16,61,73,100])


//es6
class Dot {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
    // prototype method
    showLocation() {
        console.log(`This Dot is at x ${this.x} and y ${this.y}`);
    }
    // static method
    static getHelp() {
        console.log("This is a Dot class, for created Dots! A Dot takes x and y coordinates, type 'new Dot' to create one!");
    }
} 
const dot3 = new Dot(4, 2);
// we can see showLocation from our instance...
console.log(dot3.showLocation);
// but we can't see getHelp
console.log(dot3.getHelp);
// however we can call getHelp this way:
Dot.getHelp();




// parent Dot class
class Dot {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
    showLocation() {
        console.log(`This ${ this.constructor.name } is at x ${ this.x } and y ${ this.y }`);
    }
    // simple method in the parent class
    parentFunction(){
        return "This is coming from the parent!";
    }
}
// child Circle class
class Circle extends Dot {
    constructor(x, y, radius) {
        super(x, y);
        this.radius = radius;
    }
    // simple function in the child class
    childFunction() {
        // by using super, we can call the parent method
        const message = super.parentFunction();
        console.log(message);
    }
}
const circle = new Circle(1, 2, 3);
circle.childFunction();


//getters and setters
class Pizza {
    constructor(radius, slices) {
        this.radius = radius;
        this._slices = slices;
    }
    get slices () { 
        return this._slices; 
    }
    set slices (slices) { 
        this._slices = slices;
    }
};

//custom getters
class Circle{
    constructor(x, y, radius) {
        this.x = x;
        this.y = y;
        this.radius = radius;
    }
    get diameter() {
        return this.radius * 2;
    }
}



