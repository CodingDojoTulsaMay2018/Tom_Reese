function a(){
  return 35;
}
console.log(a())

//nothing *2

function a(){
  return 4;
}
console.log(a()+a());

// 4,4,8


function a(b){
  return b;
}
console.log(a(2)+a(4));

// 2,4,6

function a(b){
      console.log(b);
      return b*3;
  }
  console.log(a(3));

// 3,9

function a(b){
    return b*4;
    console.log(b);
 }
 console.log(a(10));

// 40

 function a(b){
  if(b<10) {
      return 2;
  }
    else     {
      return 4;
  }
  console.log(b);
}
console.log(a(15));

// 2

function a(b,c){
  return b*c;
}
console.log(10,3);
console.log( a(3,10) );

// 30,30,30

function a(b){
  for(i=0; i<10; i++){
      console.log(i);
  }
  return i;
}
console.log(3);
console.log(4);

// 0,1,2,3,4,5,6,7,8,9,9  0,1,2,3,4,5,6,7,8,9,9

function a(){
  for(i=0; i<10; i++){
      i = i +2;
      console.log(i);
  }
}
a();

// 2,4,6,8,10

function a(b,c){
  for(i=b; i<c; i++) {
     console.log(i);
 }
 returncopy b*c;
}
a(0,10);
console.log(a(0,10

// 0,1,2,3,4,5,6,7,8,9   0,1,2,3,4,5,6,7,8,9  0,1,2,3,4,5,6,7,8,9  0

  function a(){
    for(i=0; i<10; i++){
       for(j=0; j<10; j++){
           console.log(j);
       }
       console.log(i);
    }
}

// nothing


function a(){
  for(i=0; i<10; i++){
      for(j=0; j<10; j++){
          console.log(i,j);
      }
  console.log(j,i);
}

// error:syntax

z = 10;
function a(){
    z = 15;
    console.log(z);
}
console.log(z);

// 10

z = 10;
function a(){
        z = 15;
        console.log(z);
}
a();
console.log(z);

// 15,10


z = 10;
function a(){
    z = 15;
    console.log(z);
    return z;
}
z = a();
console.log(z);

// 15/15