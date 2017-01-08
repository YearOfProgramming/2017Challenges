This uses arrays as tree nodes.  The first element is the value in the node.
The second and third elements are the left and right children.
To reverse a tree, reverse_tree swaps a node's children, then that function is recursively called on both children.
data, left_child, right_child, is_empty, not_empty, set_left_child, and set_right_child 
are helper functions that operate on tree nodes.
leaf is a helper function that creates a tree node with a value and two empty arrays, representing it having no children.
