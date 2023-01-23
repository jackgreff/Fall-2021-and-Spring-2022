/**
 * Creates a Queue that is a linked list (GOTTEN FROM SLIDES, SO NO COMMENTS)
 * @param <E>: type of the nodes linked
 */
public class LinkedQueue<E> implements Queue<E> {
    private SinglyLinkedList<E> list;

    public LinkedQueue( ) {list = new SinglyLinkedList<>(); }// new queue relies on the initially empty list
    public int size( ) { return list.size( ); }//returns size of queue
    public boolean isEmpty( ) { return list.isEmpty( ); }//returns boolean if empty
    public void enqueue(E element) { list.addLast(element); }//add item to queue
    public E first( ) { return list.first( ); }//checks first term
    public E dequeue( ) { return list.removeFirst( ); }//removes first term, also returns it
    public String toString(){ return list.toString();}//when printing queue
}
