function BST(){
    this.root = null; 

BST.prototype.insert = function(val){
    console.log("Im inside here!");
    
    if(!this.root){
        this.root = Node(val);
    }
    console.log("past the root")
    var runner = this.root;
    if(runner.value > val){
        if(runner.left === null && val < runner.value){
            runner.left = new Node(val);
            return this
        }
        if(runner.right == null && val > runner.value){
            runner.right = new Node(val);
            return this
        }
        runner = runner.left
            if(runner.left === null && val < runner.value){
                runner.left = new Node(val);
                return this
            }
            if(runner.right === null && val > runner.value){
            runner.right = new Node(val);
            return this
        }
        console.log("going left first");  
        while(runner.left != null || runner.right != null){
            if(runner.value > val){
                runner = runner.left;
                continue;
            }
            if(runner.value < val){
                runner = runner.right;
                continue;
            }
    }
    };
    if(runner.value < val){
        console.log("going right first");        
        if(runner.left === null && val < runner.value){
            runner.left = new Node(val);
            return this
        }
        if(runner.right == null && val > runner.value){
            runner.right = new Node(val);
            return this
        }
        runner = runner.right;
        while(runner.left != null || runner.right != null){
            if(runner.value < val){
                runner = runner.right;
                continue;
            }
            if(runner.value > val){
                runner = runner.left;
                continue;
            }
        }
        if(runner.right === null && val > runner.value){
            runner.right = new Node(val);
            return this
        }
        if(runner.left === null && val < runner.value){
            runner.left = new Node(val);
            return this
        }
    }
    console.log("welp, you suck Tom!");
}
}

function Node(val){
    this.value = val;
    this.left = null;
    this.right = null;
    console.log("hello, I'm a new node! With a value of "+val);
    return this
    };


var first = new BST();     
first.root = new Node(30);
first.insert(11).insert(31).insert(45).insert(28).insert(32).insert(33).insert(34).insert(01).insert(02); 
console.log(first);