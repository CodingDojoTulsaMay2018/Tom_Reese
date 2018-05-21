// Get 1 to 255 - Write a function that returns an array with all the numbers from 1 to 255.

function one255(){
    var x = [];
    var i = 1;
    var j = 256;
        while(i<j){
            x.push(i);
            i++;
        }
    console.log(x);
}

one255();

// Get even 1000 - Write a function that would get the sum of all the even numbers from 1 to 1000.  You may use a modulus operator for this exercise.

function sumEven(){
var sum = 0;
var i = 1;
var j = 1001;
    while(i<j){
        if( i % 2===0){
            sum+=i;
            i++;
        }
        else{
            i++;
        }
    }
console.log(sum);
}

sumEven();

// Sum odd 5000 - Write a function that returns the sum of all the odd numbers from 1 to 5000. (e.g. 1+3+5+...+4997+4999).

function sumOdd(){
var sum = 0;
for(var i = 1; i < 5001; i++){
    if( i % 2 !== 0){
        sum+=i;
    }
}
console.log(sum);
}

sumOdd();

// Iterate an array - Write a function that returns the sum of all the values within an array. (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14).

function iterArr(x){
    var i = 0;
    var j = x.length;
    var w = 0;
    while(i<j){
        w+=x[i];
        i++;
    }
    console.log(w);
}

iterArr([1,2,3,4,5]);

// Find max - Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for [-3,3,5,7] max is 7)

function findMax(x){
    var i = 0;
    var j = x.length;
    var w = x[0];
    while(i<j){
        if(x[i] > w){
            w = x[i];
            i++;
        }
        i++;
    }
    console.log(w);
}

findMax([3,9,1,6,25,8,1,0,9]);

// Find average - Given an array with multiple values, write a function that returns the average of the values in the array. (e.g. for [1,3,5,7,20] average is 7.2)

function findAvg(x){
    var i = 0;
    var j = x.length;
    var w = 0;
    while(i<j){
        w+=x[i];
        i++;
    }
    console.log(w/j);
}

findAvg([1,3,5,7,20]);

// Array odd - Write a function that would return an array of all the odd numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method.

function allOdd(){
var a = [];
for(var i = 1; i < 51; i++){
    if( i % 2 !== 0){
        a.push(i);
    }
}
console.log(a);
}

allOdd();

// Greater than Y - Given value of Y, write a function that takes an array and returns the number of values that are greater than Y. For example if arr = [1, 3, 5, 7] and Y = 3, your function will return 2. (There are two values in the array greater than 3, which are 5, 7).

function greaterY(x,y){
    var i = 0;
    var j = x.length;
    var a = 0;
    while(i<j){
        if(x[i]>y){
            a++;
        }
        i++;
    }
    console.log(a);
}

greaterY([1,3,5,7], 3);

// Squares - Given an array with multiple values, write a function that replaces each value in the array with the product of the original value squared by itself. (e.g. [1,5,10,-2] will become [1,25,100,4])

function sqIt(x){
    var i = 0;
    var j = x.length;
    while(i<j){
        x[i] = x[i]*x[i];
        i++;
    }
    console.log(x);
}

sqIt([1,5,10,-2]);

// Negatives - Given an array with multiple values, write a function that replaces any negative numbers within the array with the value of 0. When the program is done the array should contain no negative values. (e.g. [1,5,10,-2] will become [1,5,10,0])

function remNeg(x){
    var i = 0;
    var j = x.length;
    while(i<j){
        if(x[i] < 0){
            x[i]=0;
            i++;
        }
        i++;
    }
    console.log(x);
}

remNeg([1,-5,3,10,-2]);

// Max/Min/Avg - Given an array with multiple values, write a function that returns a new array that only contains the maximum, minimum, and average values of the original array. (e.g. [1,5,10,-2] will return [10,-2,3.5])

function minMaxAvg(x){
    var i = 0;
    var m = x[0];
    var n = x[0];
    var s = 0;
    var j = x.length;
    while(i<j){
        if(x[i] > m){
            m = x[i];
        }
        if(x[i] < n){
            n = x[i];
        }
        s+=x[i];
        i++;
    }
    var a = s/j;
    var t = [m,n,a];
    console.log(t);
}

minMaxAvg([1,2,3,4,5]);

// Swap Values - Write a function that will swap the first and last values of any given array. The default minimum length of the array is 2. (e.g. [1,5,10,-2] will become [-2,5,10,1]).

function swapVal(x){
temp = x[0];
x[0] = x[x.length-1];
x[x.length-1] = temp;
console.log(x);
}

swapVal([1,5,10,-2]);

// Number to String - Write a function that takes an array of numbers and replaces any negative values within the array with the string 'Dojo'. For example if array = [-1,-3,2], your function will return ['Dojo','Dojo',2].

function numString(x){
    var i = 0;
    var j = x.length;
    while(i<j){
        if(x[i] < 0){
            x[i]= "Dojo";
        }
        i++;
    }
    console.log(x);
}

numString([-1,-3,2]);