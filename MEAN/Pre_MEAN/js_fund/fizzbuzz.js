function fizzbuzz(num){
    if(!Number.isInteger(num) || num < 0){
        return ("you must enter a valid positive integer")
    }
    var str = ""
    for(var i = 1; i <= num; i++){
        if( i == num){
            if((i % 3 ==0) && (i % 5 ==0)){
                str += ("and FizzBuzz.")
                break;
            }
            if(i % 3 ==0){
                str += ("and Fizz.")
                break;
            }
            if(i % 5 ==0){
                str += ("and Buzz.")
                break;
            }
            else{
                str+=("and "+i+".")
                break;
            }
        }
        if((i % 3 ==0) && (i % 5 ==0)){
            str += ("FizzBuzz"+", ")
            continue;
        }
        if(i % 3 ==0){
            str += ("Fizz"+", ")
            continue;
        }
        if(i % 5 ==0){
            str += ("Buzz"+", ")
            continue;
        }
        else{
            str+=(i+", ")
        }
    }
    return str;
}

console.log(fizzbuzz(16))