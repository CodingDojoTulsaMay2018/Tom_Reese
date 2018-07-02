using System;
using System.Collections.Generic;


namespace box_unbox
{
    class Program
    {
        static void Main(string[] args)
        {
            List<object> boxes = new List<object>();
            boxes.Add(7);
            boxes.Add(-1);
            boxes.Add(28);
            boxes.Add(true);
            boxes.Add("chair");
            int sum = 0;
            foreach(object i in boxes){
                if(i is int){
                    sum += (int)i;
                }
            }
        System.Console.WriteLine(sum);
        }
    }
}
