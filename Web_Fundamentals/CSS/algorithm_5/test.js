// Return the given array, after setting any negative values to zero.  For example resetNegatives( [1,2,-1, -3]) should return [1,2,0,0].

function noNEg(x) {
  var i = 0;
  var j = x.length;
  while (i<j) {
    if(x[i] < 0){
      x[i] = 0;
      i++;
    }
    else{
      i++;
      continue;
    }
  }
  console.log(x);
}

noNEg([0,-1,3,4,-2,-999,998]);


// Given an array, move all values forward by one index, dropping the first and leaving a ‘0’ value at the end.  For example moveForward( [1,2,3]) should return [2,3,0].


function moveOver(x){
x.shift();
x.push(0);
console.log(x);
}
moveOver([1,2,3]);

// Given an array, return an array with values in a reversed order.  For example, returnReversed([1,2,3]) should return [3,2,1].

function revOrd(x){
x.reverse(x);
console.log(x);
}

revOrd([1,2,3,4,5]);

function revOrd2(b){
  var p = [];
  var i = 0;
  var l = -1
  var sum = 0;
  var j = b.length;
  while (i<j) {
    p.push(j+l)
    l=l+(l);
    sum++;
  }
  console.log(p);
}


// revOrd2([1,2,3,4,5]);
// Create a function that changes a given array to list each original element twice, retaining original order.  Have the function return the new array.  For example repeatTwice( [4,”Ulysses”, 42, false] ) should return [4,4, “Ulysses”, “Ulysses”, 42, 42, false, false].

function twiceArr(x){
  var p = [];
  var i = 0;
  var j = x.length;
  while (i<j){
    p.push(x[i]);
    p.push(x[i]);
    i++;
  }
  console.log(p);
}

twiceArr([1,2,3, "done"]);

// Given an array and a value Y, count and print the number of array values greater than Y.

function greaterY(x,y){
  var i = 0;
  var j = x.length;
  var sum = 0;
  while(i<j){
    if(x[i] > y){
      sum++;
      i++;
    }
    else{
      i++;
    }
  }
  console.log(sum);
}

greaterY([0,-5,2,5,6,7,8,4,3,7,1,2,0],3);