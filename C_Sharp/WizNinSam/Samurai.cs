using System;
using System.Collections.Generic;


namespace WizNinSam {

public class Samurai : Human{
    public int SamCount = 0;
    public Samurai(string person = "",int hp=200) : base(){
        name = person;
        health = hp;
        SamCount++;
    }

    public void death_blow(object enemy){
        Human target = enemy as Human;
        if(target.health < 50){
            target.health = 0;
        }
    }

    public void mediate(){
        health = 200;       
    }

    public void how_many(){
        System.Console.WriteLine(SamCount);       
    }
    
}

}