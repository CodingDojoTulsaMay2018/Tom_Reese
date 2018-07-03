using System;
using System.Collections.Generic;

namespace classes
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Vehicle myCar = new Vehicle(3);
            Vehicle myBike = new Vehicle(1);
            System.Console.WriteLine(myCar.numPassengers);
            myCar.Move(4.5);
            myBike.Move(1.3);
            Console.WriteLine("My vehicle can hold " + myCar.numPassengers + " people");
        }
    }
}
