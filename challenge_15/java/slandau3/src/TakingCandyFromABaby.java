/**
 * Created by slandau on 1/12/17.
 */

/**
 * @author Steven Landau
 * @description A circularly linked list with the a function that
 * determines who the survivor is when the little fucks start stealing candy
 * from each other.
 */
public class TakingCandyFromABaby<T> {
    private int size = 0; // The size of circularly LL
    public Node root = null;  // The root node of the LL

    /**
     * The acutal node class which will hold the data
     * and a reference to the next node.
     */
    private class Node {
        public Node next = null;
        public T data = null;

        public Node(T data) {
            this.data = data;
        }
    }

    // Increments size of the list
    private void incrementSize() {
        this.size++;
    }

    // Decrement size of the list
    private void decrementSize() {
        this.size--;
    }

    /**
     * Appends a node to the last index of the list.
     * @param data the data the new node will contain
     * @return nothing
     */
    public void append(T data) {
        if (size == 0) {
            this.root = new Node(data);
        } else {
            Node temp = this.root;
            int cur = 1; // Begin at 1 since we have
            // already checked the root node.
            while (cur != size) {
                temp = temp.next;
                cur++;
            }
            temp.next = new Node(data);
            temp.next.next = this.root;
        }
        incrementSize();
    }

    // Prints the entire circularly linked list
    public void printList() {
        if (this.size == 0) {
            System.out.println(this.root.data);
        } else {
            Node temp = this.root.next;
            System.out.println(this.root.data);
            while (temp != this.root) {
                System.out.println(temp.data);
                temp = temp.next;
            }
        }
    }

    /**
     * Function to remove a node from the circularly linked list.
     * @param data of the node
     * @exception DataNotFoundException if the data has not been found in the linked List
     * @return nothing
     */
    public void removeNode(T data) {
        if (this.root.data == data) {
            // We need to redirect the pointers to the root in two places.
            Node temp = root;
            while (temp.next.data != data) {
                temp = temp.next;
            }
            this.root = this.root.next; // Set root to the next node
            temp.next = temp.next.next; // and set the node after the temp (the previous root) to
            // the next next node.
            decrementSize();
        } else {

            int moves = 1; // begin counting at 1 since we already checked the root

            Node temp = this.root;
            while (moves <= this.size) {
                if (temp.next.data == data) {
                    temp.next = temp.next.next;
                    decrementSize();
                    return;
                }
                moves++;
                temp = temp.next;
            }
            // If we got here, then the data is not in the list
            throw new IndexOutOfBoundsException(data + " not found in the linked list");
        }
    }

    /**
     * Function to begin the fuckery. The list is destroyed in the process.
     * This function will remove every second node.
     * @exception NotEnoughKids if there are not enough kids to steal from.
     * @return The data of the surviving fuck.
     */
    public T beginTheft() { // this destroys the list
        if (size == 1 || size == 0) {
            // A child cannot steel from themself
            throw new NotEnoughKids("Not enough kids to steal from :(");
        } else {
            int current = 1; // Begin at 1 because we are looking at the first kids
            // If you wish to change this to 0 then you will need to do current % 1 below.
            while(size > 1) {
                // If we are at a second kid, steel from him and make him run away crying.
                if (current % 2 == 0) {
                    removeNode(root.data);
                }
                root = root.next; // move on to the (new) next kid.
                current++;
            }
            return root.data;
        }
    }

    public static void main(String[] args) {
        TakingCandyFromABaby<Integer> a = new TakingCandyFromABaby<>();
        a.append(1);
        a.append(2);
        a.append(3);
        a.append(4);
        //a.removeNode(1);
        //a.removeNode(3);
        //a.printList();
        System.out.println(a.beginTheft());
    }
}

// Custom exception to be used when there are not enough kids to
// perform an action.
class NotEnoughKids extends RuntimeException {
    public NotEnoughKids(String message) {
        super(message);
    }
}

// Custom exception to be used when data given via a parameter, does not exist in the list.
class DataNotFoundException extends RuntimeException {
    public DataNotFoundException(String message) {
        super(message);
    }
}