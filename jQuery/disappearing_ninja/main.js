$(document).ready(function(){
    console.log( "ready!" );


    $( "img" ).click(function() {
    console.log("clicked hide");
    $( this ).hide();
    });
    
    $( "button" ).click(function() {
    console.log("clicked show");
    $( "img" ).show();
    });


});