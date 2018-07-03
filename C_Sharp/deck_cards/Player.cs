using System;
using System.Collections.Generic;

namespace deck_cards {
    public class Player {
        public string Name;
        public List<Card> Hand = new List<Card>();

        public Player(string name){
            Name = name;

        }
            public List<Card> Draw(Deck deck, int times){
            while (times > 0){
            Card draw = deck.cards[0];
            Hand.Add(draw);
            deck.cards.Remove(draw);
            System.Console.WriteLine(draw.StringVal+" of "+draw.Suit+" is the card that was drew.");
            times--;
            }
            return Hand;
            }

            public Card Discard(int num){
            
            if(num > Hand.Count){
                System.Console.WriteLine("Player can't remove that card!");
                return null;
            }
            Card Drop = Hand[num];
            Hand.Remove(Drop);
            System.Console.WriteLine(Drop.StringVal+" of "+Drop.Suit+" is the card that was removed!");
            return Drop;
            }

            }

        }
    