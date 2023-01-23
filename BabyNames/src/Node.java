/**
 * A doubly linked list node made of a nameData
 * @param <NameData> the name data that makes up node
 */
public class Node<NameData> {
    private NameData element;          // reference to the element stored at this node
    private Node<NameData> prev;       // reference to the previous node in the list
    private Node<NameData> next;       // reference to the subsequent node in the list

    /**
     * Constructor, constructs node
     * @param e element of node
     * @param p previous node
     * @param n next node
     */
    public Node(NameData e, Node<NameData> p, Node<NameData> n) {
        element = e;
        prev = p;
        next = n;
    }
    public NameData getElement( ) { return element; }//get element
    public Node<NameData> getPrev( ) { return prev; }//get previous
    public Node<NameData> getNext( ) { return next; }//get next
    public void setPrev(Node<NameData> p) { prev = p; }//set previous
    public void setNext(Node<NameData> n) { next = n; }//set next
    public String toString(){//prints the element when asked
        return element.toString();
    }
}