/**
 * Interface (which serves as an outline) for linked Queue
 * @param <E>:type of items in queue
 */
public interface Queue<E> {//SAME FUNCTION COMMENTS AS LINKED QUEUE
    void enqueue(E e);
    E dequeue( );
    E first( );
    int size( );
    boolean isEmpty( );
}
