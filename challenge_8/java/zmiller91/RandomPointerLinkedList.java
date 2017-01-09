package zmiller91;
import java.util.HashMap;

/**
 * @author zmiller
 */
public class RandomPointerLinkedList {
    
    /**
     * Given a RandomPointerNode this method returns a deep copy 
     * 
     * @param ogNode - node to copy
     * @return deep copy
     */
    public static RandomPointerNode deepCopy(RandomPointerNode ogNode) {
        
        // Create the memory references
        RandomPointerNode ogHead = ogNode;
        RandomPointerNode cpHead = null;
        HashMap<RandomPointerNode, Integer> ogIndexes =  new HashMap<>();
        HashMap<Integer, RandomPointerNode> cpObjects = new HashMap<>();
        
        // Create a simple copy
        int count = 0;
        RandomPointerNode cpNode = null;
        while(ogNode != null) {
            count++;
            
            // Create and attach the copied node
            RandomPointerNode copy = new RandomPointerNode(prime(ogNode.data));
            if(cpHead == null) {
                cpHead = copy;
                cpNode = cpHead;
            } 
            else {
              cpNode.next = copy;
              cpNode = cpNode.next;
            }
            
            // Add the objects/indexes to the maps
            ogIndexes.put(ogNode, count);
            cpObjects.put(count, cpNode);
            ogNode = ogNode.next;
        }
        
        // Create the deep copy
        cpNode = cpHead;
        ogNode = ogHead;
        while(ogNode != null) {
            
            // Create and attach the copied node
            cpNode.random = cpObjects.get(ogIndexes.get(ogNode.random));
            cpNode = cpNode.next;
            ogNode = ogNode.next;
        }
        
        return cpHead;
    }
    
    /**
     * Test method for comparing two linked lists.
     * 
     * @param og - original list
     * @param cp - copied list
     * #return true if equal otherwise false
     */
    public static boolean equals(RandomPointerNode og, RandomPointerNode cp) {
        
        while(og != null) {
            if(cp == null) {
                return false;
            }
            
            // Values must be equal
            if(!prime(og.data).equals(cp.data)) {
                return false;
            }
            
            // If either next is null they must both be null
            if(og.next == null || cp.next == null) {
                return og.next == null && cp.next == null;
            }
            
            // If either random is null they must both be null
            if(og.random == null || cp.random == null) {
                return og.random == null && cp.random == null;
            }
            
            // Next values must be equal
            if(!prime(og.next.data).equals(cp.next.data)) {
                return false;
            }
            
            // Random values must be equal
            if(!prime(og.random.data).equals(cp.random.data)) {
                return false;
            }
            
            og = og.next;
            cp = cp.next;
        }
        
        // og is null, cp must be too
        return og == null && cp == null;
    }
    
    /**
     * Assert two RandomPointerNodes are deep copies
     * 
     * @param og
     * @param cp
     * @param message 
     */
    public static void assertEquals(RandomPointerNode og, RandomPointerNode cp, 
            String message) {
        if(!equals(og, cp)) {
            throw new AssertionError(message);
        }
    }
    /**
     * Convenience method for adding '
     * 
     * @param p
     * @return 
     */
    public static String prime(String p){
        return p + "'";
    }
    
    public static void main(String[] args) {
        
        // #1. The provided example
        RandomPointerNode three = new RandomPointerNode("3");
        RandomPointerNode five = new RandomPointerNode("5");
        RandomPointerNode one = new RandomPointerNode("1");
        RandomPointerNode two = new RandomPointerNode("2");
        RandomPointerNode four = new RandomPointerNode("4");
        
        one.next = two;
        one.random = three;
        two.next = three;
        two.random = one;
        three.next = four;
        three.random = five;
        four.next = five;
        four.random = three;
        five.random = two;
        
        assertEquals(one, deepCopy(one), "Test case 1 failed.");
        
        // #2. Null random node
        three = new RandomPointerNode("3");
        five = new RandomPointerNode("5");
        RandomPointerNode seven = new RandomPointerNode("7");
        
        seven.random = three;
        seven.next = five;
        five.next = three;
        three.random = five;
        
        assertEquals(seven, deepCopy(seven), "Test case 2 failed.");
        
        // #3. One element
        three = new RandomPointerNode("3");
        assertEquals(three, deepCopy(three), "Test case 3 failed.");
        
        // #4. Duplicate values, random value is itself, duplicate randoms
        one = new RandomPointerNode("1");
        three = new RandomPointerNode("3");
        RandomPointerNode one2 = new RandomPointerNode("1");
        
        one.next = three;
        one.random = one2;
        three.next = one2;
        three.random = three;
        one2.random = three;
        
        assertEquals(three, deepCopy(three), "Test case 4 failed.");
        
        // #5. Nothing but null
        assertEquals(null, deepCopy(null), "Test case 5 failed.");
    }
}
