using System;
using System.Collections.Generic;

namespace phone
{
    class Program
    {
        static void Main(string[] args)
        {
            Galaxy s8 = new Galaxy("s8", 100, "T-Mobile", "Dooooo do dooooooooooo doo");
            Nokia elevenhudred = new Nokia("1100", 60, "Metro PCS", "Ring ding dong Ringa ding ding dong");

            s8.DisplayInfo();
            System.Console.WriteLine(s8.Ring());
        }
    }
}
