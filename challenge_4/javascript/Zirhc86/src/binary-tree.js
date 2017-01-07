
// Binary tree node structure
var Node = function(value) {
	this.value = value;
	this.left = null;
	this.right = null;
};



function reverseTree(node) {
	// Checks for the next node/s down the tree, then recursively 
	// call reverseTree()
	
	if(node.left || node.right) {

		if(node.left){
			reverseTree(node.left);
		}
		if(node.right) {
			reverseTree(node.right);
		}	
                // Swaps child nodes around only 
		// on nodes that have at least
	 	// one !null child
		var temp;
		temp = node.left;
		node.left = node.right;
		node.right = temp;
	}
}


// Builds a string containing the values from an 'inorder' traversal of the tree
function printInOrder(tree) {
    var p = '';
    getOrder(tree);

    function getOrder(root) {
	    if(root){
			getOrder(root.left);
			p += p ?  ", " + root.value : root.value;
			getOrder(root.right);
	    }	
    }  

    return p;
	
}
// Declare and builds a tree
var test = new Node(1);
test.left = new Node(2);
test.left.left = new Node(3);
test.left.right = new Node(4);
test.right = new Node(5);
test.right.left = new Node(6);
test.right.right = new Node(7);
test.right.right.right = new Node(8);
test.right.right.right.right = new Node(9);

console.log("Tree before reversal:")
console.log(printInOrder(test));
reverseTree(test);
console.log("After reversal:");
console.log(printInOrder(test));
