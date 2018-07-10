using System;
using System.Collections.Generic;
using System.Collections;
using System.Linq;
using JsonData;

namespace ConsoleApplication
{
    public class Program
    {
        public static void Main(string[] args)
        {
            //Collections to work with
            List<Artist> Artists = JsonToFile<Artist>.ReadJson();
            List<Group> Groups = JsonToFile<Group>.ReadJson();
            System.Console.WriteLine(Artists);
            //========================================================
            //Solve all of the prompts below using various LINQ queries
            //========================================================

            //There is only one artist in this collection from Mount Vernon, what is their name and age?
var mvartist = Artists.Where(a => a.Hometown =="Mount Vernon");

foreach (var item in mvartist)
{
    System.Console.WriteLine(item.RealName);
    System.Console.WriteLine(item.Age);   
}
        

            //Who is the youngest artist in our collection of artists?
var young = Artists.OrderByDescending(a => a.Age).Last();
System.Console.WriteLine(young.Age);
System.Console.WriteLine(young.RealName);

            //Display all artists with 'William' somewhere in their real name
var willy = Artists.Where(a => a.RealName.Contains("William"));
foreach(var art in willy){
    System.Console.WriteLine(art.RealName);
}
            //Display the 3 oldest artist from Atlanta
var old = Artists.OrderByDescending(a => a.Age).Where(b => b.Hometown == "Atlanta").Take(3);
foreach(var i in old){
    System.Console.WriteLine(i.ArtistName+" is old!");
    System.Console.WriteLine(i.Age);
}
            // (Optional) Display the Group Name of all groups that have members that are not from New York City

var nyc = 
(from g in Groups
join a in Artists
on g.Id equals a.GroupId
where (a.Hometown != "New York City")
select new {g.GroupName}).Distinct();

// var nyc = nyc.Select(x=> x.GroupName).Distinct();

foreach(var i in nyc){
System.Console.WriteLine(i.GroupName);
}

            //(Optional) Display the artist names of all members of the group 'Wu-Tang Clan'

var wtc = 
from g in Groups
join a in Artists
on g.Id equals a.GroupId
select new {gName = g.GroupName, aName = a.ArtistName};

foreach(var i in wtc){
    if(i.gName == "Wu-Tang Clan"){
    System.Console.WriteLine(i.aName+" is in Wu-Tang Clan");

    }
}
        }
    }
}
