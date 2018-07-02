using System;
using System.Collections.Generic;

namespace multiplication
{
    class Program
    {
        static void Main(string[] args)
        {

            int[,,] arrayMul = new int[10,1,10];

            for(int idx = 0; idx < (arrayMul.Length/10);idx++){
                for(int x = 0; x < arrayMul.Length/10;x++){
                    arrayMul[idx,0,x] = ((idx+1) * (x+1));
                }
                Console.WriteLine("{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}","[" + arrayMul[idx,0,0] + ",",arrayMul[idx,0,1] + ",",arrayMul[idx,0,2] + ",",arrayMul[idx,0,3] + ",",arrayMul[idx,0,4] + ",",arrayMul[idx,0,5] + ",",arrayMul[idx,0,6] + ",",arrayMul[idx,0,7] + ",",arrayMul[idx,0,8] + ",",arrayMul[idx,0,9] + "]");
            }

        }
    }
}

