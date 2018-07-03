using System;
using System.Collections.Generic;

namespace puzzles
{
    class Program
    {
        static int[] RandomArray(){
        Random rand = new Random();
        int[] ranArr = new int[10];
        int max = 0;
        int sum = 0;
        foreach(int i in ranArr){
            ranArr[i] = rand.Next(5,26);
            System.Console.WriteLine(ranArr[i]);
            if(ranArr[i] > max){
                max = ranArr[i];
            }
            sum+=ranArr[i];
        }
        System.Console.WriteLine(max+" is the max");
        System.Console.WriteLine(sum+" is the sum");
        return ranArr;
        }
        static string Tosscoin(){
        Random rand = new Random();
        int flip = rand.Next(1,3);
        System.Console.WriteLine(flip+" was the number");
        if(flip == 1){
        System.Console.WriteLine("Heads");
        }
        if(flip == 2){
        System.Console.WriteLine("Tails");
        }
        string flips = flip.ToString();
        return flips;
        }
        static double TossMultipleCoins(int num){
            double sum = 0;
            for(int i = num; i >0; i--){
                string flips = Tosscoin();
                    if(flips == "1"){
                        sum+=1;
                    }
                    System.Console.WriteLine(sum);
            }
            double cointosses = (sum/num)*100;
            System.Console.WriteLine("Heads was tossed "+cointosses+"% of the time");
            return cointosses; 
        }
        static string[] Names(){
            string[] peeps = new string[] {"Todd", "Tiffany", "Charlie", "Geneva", "Sydney"};
            for(int i = 0; i < peeps.Length; i++){
            Random rand = new Random();
            int idx = rand.Next(0,4);
            string temp = peeps[idx];
            peeps[idx] = peeps[i];
            peeps[i] = temp;
            }
            List<string> lenfive = new List<string>();
            foreach(var i in peeps){
            System.Console.WriteLine(i);
            if(i.Length > 4){
                lenfive.Add(i);
            }
            }
            foreach(var i in lenfive){
                System.Console.WriteLine(i);
            }
            return lenfive.ToArray();
        }
        static void Main(string[] args)
        {
        int[] ranArr = RandomArray();
        string flips = Tosscoin();
        double cointosses = TossMultipleCoins(5);
        string[] lenfive = Names();
        }
    }
}
