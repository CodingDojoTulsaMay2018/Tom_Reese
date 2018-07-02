using System;
using System.Collections.Generic;

namespace basic_13
{
    class Program
    {
        static void LookArray(int[] arr){
            for(int i = 0; i < arr.Length; i++){
            System.Console.WriteLine(arr[i]);
            }
        }
        static void findMax(int[] arr){
            int max = arr[0];
            for(int i = 0; i < arr.Length; i++){
                if(arr[i]> max){
                    max=arr[i];
                }
            } 
        System.Console.WriteLine(max);
        }

        static void findAvg(double[] arr){
            double count = 0;
            for(int i = 0; i < arr.Length; i++){
                count+=arr[i];
                }
            System.Console.WriteLine(count/arr.Length);
            }
        
        static void GreaterY(int[] arr, int y){
            int count = 0;
            for(int i = 0; i < arr.Length; i++){
                if(arr[i] > y){
                    count++;
                }
            }
        System.Console.WriteLine(count);
        }

        static void Square(int[] arr){
            for(int i = 0; i < arr.Length; i++){
                arr[i] = arr[i]*arr[i];
                System.Console.WriteLine(arr[i]);
            }
        }

        static void removeNeg(int[] arr){
            for(int i = 0; i < arr.Length; i++){
                if(arr[i] < 0){
                    arr[i] = 0;
                }
                System.Console.WriteLine(arr[i]);
            }
        }

        static void MinMaxAvg(int[] arr){
            int max = arr[0];
            int min = arr[0];
            var sum = 0f;
            for(int i = 0; i < arr.Length; i++){
                if(arr[i] < min){
                    min = arr[i];
                }
                if(arr[i] > max){
                    max = arr[i];
                }
                sum+=arr[i];
            }
        System.Console.WriteLine(min+" is the min. "+max+" is the max. "+(sum/arr.Length)+" is the average.");
        }

        static void shiftArr(int[] arr){
            for(int i = 0; i < arr.Length-1; i++){
                int temp = arr[i+1];
                arr[i] = temp;
                System.Console.WriteLine(arr[i]);
                }
                arr[arr.Length-1] = 0;
            }

        static List<object> DojoNeg(int[] arr){
            List<object> answer = new List<object>();
            string dojo = "Dojo";
            for(int i = 0; i < arr.Length; i++){
                if(arr[i] < 0){
                    answer.Add(dojo);
                    continue;
                }
                answer.Add(arr[i]);
                // System.Console.WriteLine(arr[i]);
            }
            return answer;
        }
        static void Main(string[] args)
        {


// Print 1-255
for( int i = 1; i < 256; i++){
    System.Console.WriteLine(i);
}

// Print odd numbers between 1-255
for( int i = 1; i < 256; i++){
    if(i % 3 ==0){
System.Console.WriteLine(i);
    } 
}

// Print Sum
int count = 0;
for( int i = 1; i < 256; i++){
    count+=i;
System.Console.WriteLine("the current number is "+i+", and the current count is "+count);
}


// Iterating through an Array
int[] nums = {1,2,3,4,5,6,7};
LookArray(nums);

// Find Max
int[] maxs = {-5,-3,-7,-445,-8,-32,0,-55};
findMax(maxs);

// Get Average
double[] avg = {9,10};
findAvg(avg);

// Array with Odd Numbers
List<int> y = new List<int>(); 
for(int i = 1; i < 256; i++){
    if(i % 3 == 0){
        y.Add(i);
System.Console.WriteLine(i);        
    }
}
y.ToArray();

// Greater than Y
int[] grety = {4,8,4,6,7,8,9,4,3,4,7,0};
GreaterY(grety, 8);

// Square the Values
int[] sqr = {2,4,6,8};
Square(sqr);

// Eliminate Negative Numbers
int[] negs = {2,-4,6,-8};
removeNeg(negs);

// Min, Max, and Average
int[] mma = {1, 5, 10, -2};
MinMaxAvg(mma);

// Shifting the values in an array
int[] shf = {1, 5, 10, 7, -2};
shiftArr(shf);

// Number to String
int[] dojonegs = {-1, -3, 2};
List<object> answer = DojoNeg(dojonegs);
foreach(object i in answer){
    System.Console.WriteLine(i);
}
        }
    }
}

