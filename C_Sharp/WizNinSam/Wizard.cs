using System;
using System.Collections.Generic;


namespace WizNinSam {

public class Wizard : Human
{
    public Wizard(string person = "",int intel = 25, int hp = 50) : base(){
        name = person;
        intelligence = intel;
        health = hp;
    }
    public void heal()
    {
        health+=10;
    }

    public void fireball(object enemy){
        Human target = enemy as Human;
        Random rand = new Random();
        int damage = rand.Next(20,51);
        target.health -= damage;
    }
    
}

}

