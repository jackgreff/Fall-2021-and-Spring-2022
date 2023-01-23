/**
 * Creates a Queue that is a linked list (GOTTEN FROM SLIDES, SO NO COMMENTS)
 * @param <E>: type of the nodes linked
 */
public class LinkedStack<E> implements Stack<E> {
    private SinglyLinkedList<E> list;

    public LinkedStack() {list =  new SinglyLinkedList<>();} // new stack relies on the initially empty list
    public int size() { return list.size( ); }//returns size
    public boolean isEmpty() { return list.isEmpty( ); }//returns boolean if empty
    public E peek() { return list.first( ); }//checks first term
    public void push(E element) { list.addFirst(element); }//adds new term to stack
    public E pop() { return list.removeFirst( ); }//removes first term, also returns it
    public String toString(){return list.toString();}//when printing stack
}
