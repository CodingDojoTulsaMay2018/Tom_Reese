using System;
using System.Collections.Generic;

namespace human {
    public class Human {
        public string Name { get; set; }
        public int Strength { get; set; } = 3;
        public int Intelligence { get; set; } = 3;
        public int Dexterity { get; set; } = 3;
        public int Health { get; set; } = 100;

        public Human(string name, int strength, int intelligence, int dexterity, int health) {
            Name = name;
            Strength = strength;
            Intelligence = intelligence;
            Dexterity = dexterity;
            Health = health;
        }

        public void Attack(object attacker, object victim){
            if(victim is Human){
            var vic = (Human)victim;
            var atk = (Human)attacker;
            System.Console.WriteLine("{0} got attacked by {2}!!! He has {1} health!", vic.Name, vic.Health, atk.Name);
            var damage = atk.Strength * 5;
            vic.Health-= damage;
            if(vic.Health < 1){
                System.Console.WriteLine("{0} is dead!!!",vic.Name);
                vic.Health=0;
            }
            else {System.Console.WriteLine("{0} has {1} health left...", vic.Name, vic.Health);}
            }
            else{System.Console.WriteLine("You can't attack aliens!");}
        }

        // public int Move(double miles, bool km)
        // {
        //     // Convert the KM measurement to miles
        //     if (km == true)
        //     {
        //         miles = miles * 0.62;
        //     }
        //     return Move(miles);
        // }
    }
}