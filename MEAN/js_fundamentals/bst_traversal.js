class Node{
    constructor(val){
        this.value = val;
        this.left = null;
        this.right = null;
    }
}
var root = this.root
function inOrder(root){
    if (root){
        inOrder(root.left)
        console.log(root.value)
        inOrder(root.right)
    }
}
function preOrder(root){
    if (root){
        console.log(root.value)
        preOrder(root.left)
        preOrder(root.right)
    }
}
function postOrder(root){
    if (root){
        postOrder(root.right)
        postOrder(root.left)
        console.log(root.value)
    }
}
root = new Node(1)
root.left = new Node(2)
root.right = new Node(3)
root.left.left = new Node(4)
root.left.right = new Node(5)
console.log(inOrder(root))
console.log(preOrder(root))
console.log(postOrder(root))