/**
 * Node class taken from class (so no major comments)
 * @param <E> type of node
 */
public class Node<E> {
    private E element;          // reference to the element stored at this node
    private Node<E> next;       // reference to the subsequent node in the list

    public Node(E e, Node<E> n) {//constructing node
        element = e;
        next = n;
    }

    public E getElement( ) { return element; }//returns what's inside node
    public Node<E> getNext( ) { return next; }//checks what comes after
    public void setNext(Node<E> n) { next = n; }//changes what is next
    public String toString(){return element.toString();}//prints element
}