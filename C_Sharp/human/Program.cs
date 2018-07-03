using System;
using System.Collections.Generic;


namespace human
{
    class Program
    {
        static void Main(string[] args)
        {
            Human weakling = new Human("Glassjaw Joe",1,1,7,50);
            System.Console.WriteLine("A new challenger, {0}, has arrived to the fight! {0} brings in {1} strength, {2} intelligence, {3} dexterity, and has {4}  health.",weakling.Name, weakling.Strength, weakling.Intelligence, weakling.Dexterity, weakling.Health);

            Human tank = new Human("Butter Bean",7,1,1,100);

            tank.Attack(tank,weakling);          tank.Attack(tank,weakling);
        }
    }
}
