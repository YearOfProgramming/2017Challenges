/**
 * Created by slandau on 1/11/17.
 */
public class Reverse<T> {
    public Node root = null;
    public int size = 0;

    private class Node {
        public T data;
        public Node next;

        public Node(T data) {
            this.data = data;
        }
    }

    public void append(T data) {
        if (size == 0) {
            root = new Node(data);
        } else {
            Node temp = root;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = new Node(data);
        }
        size++;
    }

    public void reverse() {
        if (size == 1) {
            // do nothing
        } else {
            Node prev = null;
            Node cur = root;
            Node next = root.next;
            while (next != null) {
                cur.next = prev;
                prev = cur;
                cur = next;
                next = next.next;
            }
            cur.next = prev;
            root = cur;
        }

    }

    public void print() {
        Node temp = root;
        while (temp != null) {
            System.out.println(temp.data);
            temp = temp.next;
        }
    }


    public static void main(String[] args) {
        Reverse<Integer> a = new Reverse<>();
        a.append(1);
        a.append(2);
        a.append(3);
        a.print();
        a.reverse();
        a.print();
    }

}
