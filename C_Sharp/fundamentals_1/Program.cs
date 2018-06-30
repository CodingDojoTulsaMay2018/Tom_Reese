using System;

namespace fundamentals_1
{
    class Program
    {
        static void Main(string[] args)
        {
            // for(int i = 0; i < 256; i++) {
            //     Console.WriteLine(i);
            // }

// int t = 1;
//             while (t < 101) {
//                 if(t % 3 == 0 && t % 5 == 0){
//                     t++;
//                     continue;
//                 } 
//                 if(t % 3 == 0 || t % 5 == 0){
//                     Console.WriteLine(t);
//                     t++;
//                 }
//                 if(t % 3 == 0 || t % 5 == 0){
//                     Console.WriteLine(t);
//                     t++;
//                 }
//                 t++;
//             }
// string buzz = "Buzz";
// string fizz = "Fizz";
// int t = 1;
//                   while (t < 101) {
//                 if(t % 3 == 0 && t % 5 == 0){
//                     Console.WriteLine(fizz+buzz);
//                     t++;
//                 } 
//                 if(t % 3 == 0){
//                     Console.WriteLine(fizz);
//                     t++;
//                 }
//                 if(t % 5 == 0){
//                     Console.WriteLine(buzz);
//                     t++;
//                 }
//                 Console.WriteLine(t);
//                 t++;
//             }

            string buzz = "Buzz";
string fizz = "Fizz";

    for(int t = 1;t < 101; t++) {
        int f = t / 3;
        int b = t / 5;
        if((f*3)-t == 0 && (b*5)-t == 0){
            Console.WriteLine(fizz+buzz);
            continue;
        }
        if(f*3-t == 0){
            Console.WriteLine(fizz);
            continue;
        }
        if((b*5)-t == 0){
            Console.WriteLine(buzz);
            continue;
                } 
                Console.WriteLine(t);
            }
        }
        }  
}
