/**
 * Linked list comprised of NameData nodes
 */
public class DoublyLinkedList {
    //important nodes
    private Node<NameData> header;             // header sentinel
    private Node<NameData> trailer;            // trailer sentinel
    private int size;               // number of elements in the list

    /**
     * Constructor, just needs to be initiated. will create header and trailer immediately
     */
    public DoublyLinkedList( ) {
        header = new Node<NameData>(null, null, null);        // create header
        trailer = new Node<NameData>(null, header, null);        // trailer is preceded by header
        header.setNext(trailer);                                // header is followed by trailer
        size = 0;
    }

    // access methods
    public int size( ) { return size; }
    public boolean isEmpty( ) { return size == 0; }
    public Node<NameData> getHeader(){return header;}
    public Node<NameData> getTrailer(){return trailer;}

    /**
     * gives you the first item
     * @return first item in list
     */
    public NameData first( ) {
        if (isEmpty( ))
            return null;
        return header.getNext( ).getElement( );  // first element is beyond header
    }

    /**
     * gives you the last item
     * @return the last item in list
     */
    public NameData last( ) {
        if (isEmpty( ))
            return null;
        return trailer.getPrev( ).getElement( );  // last element is before trailer
    }

    // private update methods
    private void addBetween(NameData e, Node<NameData> predecessor, Node<NameData> successor) { // create and link a new node
        Node<NameData> newest = new Node<>(e, predecessor, successor);
        predecessor.setNext(newest);
        successor.setPrev(newest);
        size++;
    }
    //removes node
    private NameData remove(Node<NameData> node) {
        Node<NameData> predecessor = node.getPrev( );
        Node<NameData> successor = node.getNext( );
        predecessor.setNext(successor);
        successor.setPrev(predecessor);
        size--;
        return node.getElement( );
    }

    // public update methods
    public void addFirst(NameData e) {
        addBetween(e, header, header.getNext( ));  // place just after the header
    }
    //adds last
    public void addLast(NameData e) {
        addBetween(e, trailer.getPrev( ), trailer); // place just before the trailer
    }
    //removes first
    public NameData removeFirst( ) {
        if (isEmpty( )) return null;    // nothing to remove
        return remove(header.getNext( ));    // first element is beyond header
    }
    //removes last
    public NameData removeLast( ) {
        if (isEmpty( )) return null;                // nothing to remove
        return remove(trailer.getPrev( ));        // last element is before trailer
    }

    /**
     * inserts new node into an alphabetical list
     * @param inputName a name data instance that is transformed into a node and places it
     */
    void insertAlpha(NameData inputName){
        Node<NameData> inputNode = new Node(inputName,null,null);
        Node<NameData> loopNode = header.getNext();//will be inserting

        if (size == 0) {
            addFirst(inputNode.getElement());
        }
        else{
            while (true){
                if (loopNode == trailer.getPrev()){
                    addLast(inputName);
                    break;
                }
                String a = loopNode.getElement().getName();
                String b = inputNode.getElement().getName();
                float comparison = (float) a.compareTo(b);
                if (comparison < 0) {
                    loopNode = loopNode.getNext();
                }else if (comparison > 0 || loopNode == trailer.getPrev()){
                    addBetween(inputNode.getElement(), loopNode.getPrev(), loopNode);
                    break;
                }else{
                    loopNode.getElement().setNumber(inputNode.getElement().getNumber());
                    break;

                }
            }

        }
    }

    /**
     * finds name data of a name in list
     * @param name name to be found
     * @return name data instance
     */
    NameData fetch(String name){
        Node<NameData> currNode = getHeader().getNext();
        int count = 0;
        while (!currNode.getElement().getName().equals(name)){
            count+=1;
            currNode = currNode.getNext();
        }
        return currNode.getElement();
    }

    /**
     * name to be found
     * @param name name to be found
     * @return placement in list
     */
    int findPosition(String name){
        Node<NameData> currNode = getHeader().getNext();
        int count = 0;
        while (!currNode.getElement().getName().equals(name)){
            count+=1;
            currNode = currNode.getNext();
        }
        return count;

    }

    /**
     * toString method for the Doubly Linked List class
     * @return a string containing the data in the nodes of the list
     */
    public String toString(){
        if (isEmpty()){
            return "List is Empty";
        }
        Node<NameData> curr = header.getNext();               // Start with the node after the header
        String str = curr.toString();                  // Using toString from the Node Class
        while (curr.getNext() != trailer){             // Keep hoping until the next node is the trailer
            curr = curr.getNext();
            str = str + " -> " + curr.toString();      // Using toString from the Node Class
        }
        return str;
    }
}

