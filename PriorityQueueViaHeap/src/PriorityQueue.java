import java.util.ArrayList;

/**
 * Priority Queue Implemented in arrayHeap (NOTHING CHANGED SO NO COMMENTS)
 * @param <E>: Type in queue
 */
public interface PriorityQueue<E extends Comparable<E>> {
    void insert(E element);

    E max();

    E removeMax();

    int size();

    boolean isEmpty();
}


