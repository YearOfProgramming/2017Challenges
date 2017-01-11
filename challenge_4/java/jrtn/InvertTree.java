public class InvertTree {
    public static <T> Tree<T> invertTree(Tree<T> root) {
        if(root != null) {
            Tree<T> temp = root.left;
            root.left = invertTree(root.right);
            root.right = invertTree(temp);
        }        
        return root;
    }
}
