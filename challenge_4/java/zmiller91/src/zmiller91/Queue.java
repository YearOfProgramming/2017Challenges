package zmiller91;

import java.util.LinkedList;

/**
 * Generic Queue data structure. It's a wrapper to a linked list.
 * 
 * @author zmiller
 */
public class Queue<T> {
    
    LinkedList<T> queue = new LinkedList<>();
    public Queue() {}
    
    public void enqueue(T e) {
        queue.addLast(e);
    }
    
    public T dequeue() {
        return queue.removeFirst();
    }
    
    public boolean empty() {
        return queue.isEmpty();
    }
}
