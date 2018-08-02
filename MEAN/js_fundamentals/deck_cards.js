var x = require('underscore');

class Card{

    constructor(suitType,stringValue,cardValue){
    this.suitType = ["Hearts", "Clubs", "Diamonds", "Spades"];
    this.stringValue = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    this.cardValue = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    }

    showCard(card){
        
        console.log(this.value);
        return this
        }
    
}

class Deck extends Card{

    constructor(){
        super()
        this.deckArray = [];
        this.deck = function(){
            
            for(let j=0;j<this.suitType.length;j++)
            {
                for(let i=0;i<this.stringValue.length;i++)
                {
                    let suits = this.suitType[j]
                    let strings = this.stringValue[i]
                    let ints = i+1
                    let card = [suits,strings,ints]
                    this.deckArray.push(card)
                    // console.log(deckArray);   
                }
            }
            // var deckArray = new Deck
            return this.deckArray
        }
    }

        shuffle(cards) {
            console.log(cards+"*************************************************************");
            var newcards = x.shuffle(cards); 
            console.log(newcards);
            
            // return newcards;
          }
    }




    //   reset(arr){
    //       arr.

    //   }


var deck1 = new Deck;
deck1.deck()
// console.log(deck1);
// console.log(deck1.stringValue.length)
console.log(deck1.deckArray);
deck1.shuffle(deck1.deckArray)

// deck1.shuffle(deck1.deckArray)
// deck1.deckArray = deck1.shuffle(deck1.deckArray)
// console.log(deck1.deckArray);


// console.log(deck1.shuffle(this.cards));
// console.log(deck1.card);