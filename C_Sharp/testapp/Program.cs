using System;
using System.Collections.Generic;


namespace testapp
{
    class Program
    {
        static void Main(string[] args)
        {

Dictionary<string,string> profile = new Dictionary<string,string>();
//Almost all the methods that exists with Lists are the same with Dictionaries
profile.Add("Name", "Speros");
profile.Add("Language", "PHP");
profile.Add("Location", "Greece");
Console.WriteLine("Instructor Profile");
Console.WriteLine("Name - " + profile["Name"]);
Console.WriteLine("From - " + profile["Location"]);
Console.WriteLine("Favorite Language - " + profile["Language"]);
foreach (KeyValuePair<string,string> entry in profile)
{
 Console.WriteLine(entry.Key + " - " + entry.Value);
}
//The var keyword takes the place of a type in type-inference
foreach (var entry in profile)
{
 Console.WriteLine(entry.Key + " - " + entry.Value);
}


        }
    }
}
