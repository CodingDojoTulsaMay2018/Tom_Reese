// Given an array and a value Y, count and print the number of array values greater than Y.

function greaterY(arr, y){
  var i = 0;
  var sum = 0;
  var l = arr.length;
  while(i < l){
    if(arr[i] > y){
      sum++;
      i++;
    }
    else{
      i++;
    }
  }
  console.log(sum);
}

greaterY([2,3,4,5,6],2);
greaterY([2,3,-6],0);

// Given an array, print the max, min and average values for that array.

function maxMinAvg(arr){
var max = arr[0];
var min = arr[0];
var sum = 0;
var i = 0;
var j = arr.length;
while(i< j){
  if (arr[i] > max){
    max = arr[i];
  }
  if(arr[i] < min){
    min = arr[i];
  }
  sum+=arr[i];
  i++;
}
var avg = sum/j;
var arr = [max, min, avg];
console.log(arr);
}

maxMinAvg([1,2,3,4,5,6,7,8,9]);
maxMinAvg([5,5,5,5]);
maxMinAvg([-1,-1,7,7]);
maxMinAvg([8,-1,7,7]);

// Given an array of numbers, create a function that returns a new array where negative values were replaced with the string ‘Dojo’.   For example, replaceNegatives( [1,2,-3,-5,5]) should return [1,2, "Dojo", "Dojo", 5].

function dojoN(x){
  var i = 0;
  var j = x.length;
  while(i < j){
    if(x[i] < 0){
      x[i] = "Dojo";
    }
    i++;
  }
  console.log(x);
}

dojoN([-1,3,-1,4]);
dojoN([-1,3,-1,0,-99999,0.5]);

// Given array, and indices start and end, remove vals in that index range, working in-place (hence shortening the array).  For example, removeVals([20,30,40,50,60,70],2,4) should return [20,30,70].

// function removeVals(x,a,b){
//   if(x.length-1 < a || x.length-1 < b){
//     console.log ("null");
//     return;
//   }
//   if(a>b){
//     console.log("invalid input, first parameter must be smaller than second parameter")
//     return;
//   }
//   var q = [];
//   var w = x[a];
//   var e = x[b];
//   for(var i = 0; i < x.length; i++){
//    if(x[i] >= w && x[i] <= e || x[i] >= e && x[i] <= w){
//      continue;
//    }
//    else{
//      q.push(x[i]);
//    }
//  }
//  console.log(q);
// }

// function splice(arr, lowIdx, highExc) { 
//   if (lowIdx < 0 || highExc > arr.length || highExc <= lowIdx || (highExc - lowIdx) > arr.length) 
//   {return null; }
//   else { 
//     for (var i = lowIdx, j = 0; i < highExc; i++, j++) {
//       arr[j] = arr[i]; }
//       arr.length = highExc - lowIdx; return arr}; }

console.log(removeInner([0,1,2,3,4,5],2,4));

function removeInner(x, a,b) {
  if (a < 0 || b > x.length - 1 || (b - a) >= x.length - 1) {
      return null;
    } 
  else {
    for (var i = a, j = b + 1; j < x.length; i++, j++) {
      console.log(j,a,x)  ;
      x[i] = x[j];} 
        x.length -= b - a + 1;} 
return x; }