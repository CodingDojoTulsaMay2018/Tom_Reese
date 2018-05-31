$(document).ready(function(){
    
    var button = document.getElementById("counter"),
    count = 0;
    button.onclick = function() {
    count += 1;
    button.innerHTML = "Click me: " + count;
    };

    $('button').click(function(){  
    document.getElementById("poke").src = "https://pokeapi.co/media/img/"+count+".png";
    }) 
})
