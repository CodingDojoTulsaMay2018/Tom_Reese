using System;
using System.Collections.Generic;


namespace WizNinSam {

public class Human
{
    public string name { get; set; }
    public int health { get; set; }
    public int strength { get; set; }
    public int intelligence { get; set; }
    public int dexterity { get; set; }

    public Human(string person ="", int str=3, int intel=3, int dex=3, int hp=100)
    {
        name = person;
        health = hp;
        strength = str;
        intelligence = intel;
        dexterity = dex;
    }
    public void attack(object obj)
    {
        Human enemy = obj as Human;
        if(enemy == null)
        {
            Console.WriteLine("Failed Attack");
        }
        else
        {
            enemy.health -= strength * 5;
        }
    }
}

}
