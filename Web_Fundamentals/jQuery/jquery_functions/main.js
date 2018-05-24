$(document).ready(function(){
    console.log( "ready!" );

    $( ".click" ).click(function() {
        console.log("clicked click;")
        alert( "experience++" );
      });

      $( ".hide" ).click(function() {
        console.log("clicked hide");
        $( "#hide-b" ).hide();
      });
     
      $( ".show" ).click(function() {
        console.log("clicked show");
        $( "#hide-b" ).show();
      });

      $( ".toggle" ).click(function() {
        console.log("clicked toggle");
        $( ".toghead" ).toggle();
      });


      $( ".slide-up" ).click(function() {
        console.log("clicked slide up");  
        $( "#slided" ).slideUp( "slow", function() {
          // Animation complete.
        });
      });

      $( ".slide-down" ).click(function() {
        console.log("clicked slide down");
        $( "#slided" ).slideDown( "slow", function() {
          // Animation complete.
        });
      });

      $( ".slide-toggle" ).click(function() {
        console.log("clicked slide toggle"); 
        $( ".explain-slide-toggle-test" ).slideToggle( "slow", function() {
          // Animation complete.
        });
      });

      $( ".fade-out" ).click(function() {
        console.log("clicked fade out");
        $( ".fade-out-explained" ).fadeOut( "slow", function() {
          // Animation complete.
        });
      });

      $( ".fade-in" ).click(function() {
        console.log("clicked fade in");
        $( ".fade-out-explained" ).fadeIn( "slow", function() {
          // Animation complete
        });
      });

      $( ".add-class" ).click(function() {
        console.log("clicked added class");
        $( ".tester" ).addClass( "big-blue" );
      });

      $( ".before" ).click(function() {
        console.log("clicked added text");
        $( ".before-text" ).before( "Tribbles!" )
      });

      $( ".after" ).click(function() {
        console.log("clicked added text");
        $( ".after-text" ).after( "Tribbles!" );
      });

      $( ".append" ).click(function() {
        console.log("clicked append");
        $( ".append-test" ).append( $( "<div class='big-blue'><em> You did it!</em></div>" ) );
      });

       
    $( ".html" ).click(function() {
        console.log("clicked change html");
        $( ".breaking-internet" ).html(
            "<div class='big-blue'>Great Job! You just broke the internet!</div>"
        );
    });

    $( ".attr" ).click(function() {
        console.log("clicked on attribute");
        $( ".pagani" ).attr( "width", "60%", "height", "60%" );
    });

    
    $( ".val" ).click(function() {
    console.log("clicked on val");
    $( ".input-area" ).show();
    $( ".input-area" ).keyup(function() {
        var value = $( this ).val();
        $( ".user-input" ).text( value );
        })
        .keyup();  
    });
    
    $( ".text" ).click(function() {
        console.log("clicked on text");
        $( ".input-text-test" ).text( "Thanos won." );
    });

    $( ".data" ).click(function() {
        console.log("clicked on data");
        $( ".button-show" ).show();
        $( ".heros" ).click(function() {
            console.log("clicked on a hero");
            var value;
            switch ( $( ".heros" ).index( this ) ) {
              case 0 :
                $( ".heros" ).data( "Superman" );
                value = "totally lame, and obvious.  Just like you.";
              break;
              case 1 :
                $( ".heros" ).data( "Batman" );
                value = "He's rich, you're poor.  No one is going to help you.";
                break;
              case 2 :
                $( ".heros" ).data( "Wolverine" );
                value = "You win the internet";
                break;
                case 3 :
                $( ".heros" ).data( "Wolverine" );
                value = "Did you even watch Infinity War???";
                break;
            }
            $( ".answer" ).text( "" + value );
          }); 
        });

    // $( ".val" ).click(function() {
    //     console.log("clicked on val");
       

    // });
  



});



