using System;
using System.Collections.Generic;


namespace WizNinSam {

public class Ninja : Human
{
    public Ninja(string person = "",int dex=3) : base(){
        name = person;
        dexterity = dex;
    }

    public void getaway(object enemy){
        health -= 15;
    }

    public void steal(object enemy){
        Human target = enemy as Human;
        target.health -= 10;
        health += 10;
    }
    
}

}

