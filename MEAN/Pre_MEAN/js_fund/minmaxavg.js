function maxMinAvg(arr){
    var str = "";
    var max = -Infinity;
    var min = Infinity;
    var sum = 0;

    for(var i = 0; i < arr.length; i++){
        if(arr[i] > max){
            max = arr[i];
        }
        if(arr[i] < min){
            min = arr[i];
        }
        sum+=arr[i];
    }
    avg = sum/arr.length;
    return (str = ("Them min is "+min+", the max is "+max+", and the average is "+avg+"."))
}
console.log(maxMinAvg([1,2,3]));