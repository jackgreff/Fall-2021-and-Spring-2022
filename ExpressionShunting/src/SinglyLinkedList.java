public class SinglyLinkedList<E> {
    private Node<E> head;        // head node of the list (or null if empty)
    private Node<E> tail;        // last node of the list (or null if empty)
    private int size;               // number of nodes in the list

    public SinglyLinkedList() {    // constructs an initially empty list
        head = null;
        tail = null;
        size = 0;
    }

    public int size() {
        return size;
    }
    public boolean isEmpty() {
        return size == 0;
    }
    public E first( ) {
        if (isEmpty( )) return null;
        return head.getElement( );
    }

    public E last() {
        if (isEmpty( )) return null;
        return tail.getElement( );
    }

    public E getItem(int pos){
        if (pos < 0 || pos > this.size)
            return null;

        Node<E> desiredNode = head;
        for (int i = 0; i < pos; i++){
            desiredNode = desiredNode.getNext();
        }
        return desiredNode.getElement();
    }

    public void addFirst(E e) {
        Node<E> newest = new Node<E>(e, null);
        newest.setNext(head);
        head = newest;

        if (isEmpty())
            tail = head;

        size++;
    }
    public void addLast(E e) {
        Node<E> newest = new Node<E>(e, null);

        if (isEmpty())
            head = newest;
        else
            tail.setNext(newest);

        tail = newest;
        size++;
    }

    public E removeFirst() {
        if (isEmpty( ))
            return null;

        E answer = head.getElement( );
        head = head.getNext( );
        size--;

        if (size == 0)
            tail = null;

        return answer;
    }

    /**
     * This method removes an element (a node) from the list
     * @param pos the position of the element the user wants to remove
     */
    public void removeFrom(int pos) throws IndexOutOfBoundsException {
        if (pos < 0 || pos > size)
            throw new IndexOutOfBoundsException("Invalid position: " + pos);

        if (pos == 0){              // if position is 0, that's the same as removing the head
            this.removeFirst();
        } else{
            Node<E> curr = head;
            // if position is more than 0, you "walk" on the list until the node right before the node you
            // want to remove
            for (int i = 0; i < pos-1; i++){
                curr = curr.getNext();
            }

            // When you get to the node right before the node you want to remove, set its next node as the next of its
            // current next node. This will "skip" the node you wnat to remove
            curr.setNext(curr.getNext().getNext());
        }
    }

    public String toString() {
        if (isEmpty()){
            return "List is empty";
        }
        Node<E> curr = head;
        String str = head.toString();                   // Using toString from the Node Class
        while(curr.getNext() != null){
            curr = curr.getNext();
            str = str + " -> " + curr.toString();       // Using toString from the Node Class
        }
        return str;
    }
}
