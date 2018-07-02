using System;
using System.Collections.Generic;


namespace collections_practice
{
    class Program
    {
        static void Main(string[] args)
        {

int[] numArray = new int[10];

for(int idx = 0; idx < numArray.Length; idx++){
    numArray[idx] = idx;
        Console.WriteLine("The current number is {0}", numArray[idx]);

}
string[] names = new string[4] {"Tom", "Ryan", "Frank", "Troy"};


bool[] tfarray = new bool[10];

for(int i = 0; i < tfarray.Length; i++){
    if(i % 2 == 0){
        tfarray[i] = true;
        Console.WriteLine(tfarray[i]);
        continue;
    }
    tfarray [i] = false;
    Console.WriteLine(tfarray[i]);
}

List<string> flavors = new List<string>();

flavors.Add("chocolate");
flavors.Add("vanilla bean");
flavors.Add("lemon biscoff");
flavors.Add("cappucino chip");
flavors.Add("mint chocolate chip");
flavors.Add("double fudge brownie");
flavors.Add("green tea");


Console.WriteLine("We currently know of {0} flavors in Tom's wishlist.", flavors.Count);

Console.WriteLine(flavors[2]);
flavors.Remove("lemon biscoff");
Console.WriteLine(flavors.Count);


// Create a Dictionary that will store both string keys as well as string values

Dictionary<string,string> name = new Dictionary<string,string>();
//Almost all the methods that exists with Lists are the same with Dictionaries
name.Add("Tom",null);
name.Add("Ryan",null);
name.Add("Frank",null);
name.Add("Troy",null);

Random rand = new Random();
name["Tom"] = flavors[rand.Next(0,5)];
name["Ryan"] = flavors[rand.Next(0,5)];
name["Troy"] = flavors[rand.Next(0,5)];
name["Frank"] = flavors[rand.Next(0,5)];

//The var keyword takes the place of a type in type-inference
foreach (var entry in name)
{
 Console.WriteLine(entry.Key + " - " + entry.Value);
}



// For each name key, select a random flavor from the flavor list above and store it as the value
// Loop through the Dictionary and print out each user's name and their associated ice cream flavor.



        }
    }
}
