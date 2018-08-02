class Node{
    constructor(val){
        this.value = val;
        this.left = null;
        this.right = null;
    }
}
var root = this.root
function findDepth(node){
    left = 1;
    right = 1;
    if (!node){
        return 0;
    }
    else {
        left = findDepth(node.left)
        right = findDepth(node.right)
    if(left > right){
        return left+1
    }
    else {
        return right+1
    }
}
}
root = new Node(1)
root.left = new Node(2)
root.right = new Node(3)
root.left.left = new Node(4)
root.left.right = new Node(5)
console.log(findDepth(root))