// class Card{

//     constructor(suitType,stringVal,cardValue){
//     this.suitType = ["Hearts", "Clubs", "Diamonds", "Spades"];
//     this.stringValue = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
//     this.cardValue = [1,2,3,4,5,6,7,8,9,10,11,12,13]
//     }

//     showCard(card){
        
//         console.log(this.value);
//         return this
//         }
    
// }

class Deck{

    constructor(){
        this.deckArray = []
        let suit = ["Hearts","Clubs","Diamonds","Spades"]
        let stringValue = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
        this.buildDeck= function(){
            for(let j=0;j<suit.length;j++)
            {
                for(let i=0;i<stringValue.length;i++)
                {
                    let suits = suit[j]
                    let stringVal = stringValue[i]
                    let intVal = i+1
                    let card = new Cards(suits,stringVal,intVal)
                    console.log(card);

                    this.deckArray.push(card)
                }

            }
        }
        // shuffle(cards) {
        //     console.log(this.cards);
            
        //     var copy = [], n = this.length, i;
        //     while (n) {
        //       i = Math.floor(Math.random() * this.length);
        //       if (i in this) {
        //         copy.push(this[i]);
        //         delete this[i];
        //         n--;
        //       }
        //     }  
        //     return copy;
        //   }
    }






}



    //   reset(arr){
    //       arr.

    //   }
}

var deck1 = new Deck;
console.log(deck1);
console.log(deck1.stringValue.length)
console.log(deck1.deck());
// console.log(deck1.shuffle(this.cards));
console.log(deck1.cards);


