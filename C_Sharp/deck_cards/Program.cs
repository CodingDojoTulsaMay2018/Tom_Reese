using System;
using System.Collections.Generic;

namespace deck_cards
{
    class Program
    {
        static void Main(string[] args)
        {
        Deck deck = new Deck();

        foreach(var i in deck.cards){
            System.Console.WriteLine(i.StringVal+" of "+i.Suit+" and int val is "+i.Val);
        }

        deck.shuffle(7);

        foreach(var i in deck.cards){
            System.Console.WriteLine(i.StringVal+" of "+i.Suit);
        }

        Player player1 = new Player("Drop Tables");
        
        player1.Draw(deck,4);

        foreach(var i in deck.cards){
            System.Console.WriteLine(i.StringVal+" of "+i.Suit);
        }

        foreach(var i in player1.Hand){
            System.Console.WriteLine(player1.Name+"'s hand includes a "+i.StringVal+" of "+i.Suit);
        }

        player1.Discard(5);
        player1.Discard(1);

        deck.topmost();
         foreach(var i in deck.cards){
            System.Console.WriteLine(i.StringVal+" of "+i.Suit);
        }

        deck.reset();
                 foreach(var i in deck.cards){
            System.Console.WriteLine(i.StringVal+" of "+i.Suit);
        }


        }
    }
}
