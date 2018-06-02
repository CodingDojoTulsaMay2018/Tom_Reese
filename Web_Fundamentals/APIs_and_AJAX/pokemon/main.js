$(document).ready(function(){
    
    var count = 0;
    
    function bcounter(){
        if(button = document.getElementById("counter"),
        count = 0;
        button.onclick = function() {
        count += 1;
        button.innerHTML = "Forward: " + count;

        )

    };
    var 
    };


    var button = document.getElementById("counterneg"),
    count = 0;
    button.onclick = function() {
    count -= 1;
    button.innerHTML = "Backward: " + count;
    };

    // var button = document.getElementById("counter"),
    // count = 0;
    // button.onclick = function() {
    // count += 1;
    // button.innerHTML = "Forward: " + count;
    // };


    // var button = document.getElementById("counterneg"),
    // count = 0;
    // button.onclick = function() {
    // count -= 1;
    // button.innerHTML = "Backward: " + count;
    // };

    $('button').click(function(){  
    document.getElementById("poke").src = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"+count+".png";
    }) 
})
