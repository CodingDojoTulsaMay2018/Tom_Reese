function bracesvalid(str){
    let check = [];
    let key = {
        "}" : "{",
        "]" : "[",
        ")" : "("};
        for(let i = 0; i < str.length; i++){
            if(str[i] === "{" ||str[i] === "[" ||str[i] === "("){
                check.unshift(str[i])
            }            
            if(str[i] === "}"){
                if((check[0]) == key["}"]){
                    check.shift();
                    continue;}
                return false;
            }
            if(str[i] === "]"){
                if((check[0]) == key["]"]){
                    check.shift();
                    continue;}
                return false;
            }
            if(str[i] === ")"){
                if((check[0]) == key[")"]){
                    check.shift();
                    continue;}
                return false;
            }
        }
if(check.length){
    return false;
}
return true
};




console.log(bracesvalid("rty{tyu[rty(erty)erty]rt}."))
console.log(bracesvalid("}rty{tyu}{rty(erty)erty]rt}."))