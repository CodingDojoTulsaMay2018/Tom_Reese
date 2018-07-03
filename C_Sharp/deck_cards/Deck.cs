using System;
using System.Collections.Generic;

namespace deck_cards {
    public class Deck {
        public List<Card> cards = new List<Card>();
        public List<string> cardType = new List<string>{"2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"};
        public List<string> suitType = new List<string>{"Clubs", "Spades", "Hearts", "Diamonds"};

        public Deck() {
            for(int i = 0; i < suitType.Count; i++){
                for(int j = 0; j < cardType.Count;j++){
                    var suit = suitType[i];
                    var stringVal = cardType[j];
                    var val = j+1;
                    Card unique = new Card(stringVal,suit, val);
                    cards.Add(unique);
                }

            }
        }

        public Card topmost(){
            Card topcard = cards[0];
            cards.RemoveAt(0);
            System.Console.WriteLine("*top card was..."+topcard.StringVal+" of "+topcard.Suit);
            return topcard;
        }

        public void reset(){
            cards.Clear();
            System.Console.WriteLine("***Gathering all the cards for a new game***");
            for(int i = 0; i < suitType.Count; i++){
                for(int j = 0; j < cardType.Count;j++){
                    var suit = suitType[i];
                    var stringVal = cardType[j];
                    var val = j+1;
                    Card unique = new Card(stringVal,suit, val);
                    cards.Add(unique);
                }
            }
        }

        public void shuffle(int num){   
            System.Console.WriteLine("***Shuffling the deck "+num+" times***");
            for(int x = num; x > 0; x--){
                for(var i = 0; i < cards.Count; i++){
                    Random rand = new Random();
                    var idx = rand.Next(cards.Count);
                    var temp = cards[idx];
                    cards[idx] = cards[i];
                    cards[i] = temp;
                    }
            }  
        }
    }
}