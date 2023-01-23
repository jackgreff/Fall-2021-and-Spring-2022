/**
 * Interface (which serves as an outline) for linked Queue
 * @param <E>:type of items in stack
 */
public interface Stack<E> {//SAME FUNCTION COMMENTS AS LINKED QUEUE
    void push(E element);
    E pop();
    E peek();
    int size();
    boolean isEmpty();
}