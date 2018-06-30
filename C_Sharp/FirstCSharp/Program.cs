using System;

namespace FirstCSharp
{
    class Program
    {
        static void Main(string[] args)
        {

for(int val = 0; val < 10; val++)
{
        Random rand  = new Random();
    //This will print the same generated value each time!!!
    Console.WriteLine(rand.Next(2,8));
}


        }
    }
}
