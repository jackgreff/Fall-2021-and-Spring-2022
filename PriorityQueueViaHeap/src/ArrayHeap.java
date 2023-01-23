import javax.xml.bind.Element;
        import java.util.ArrayList;
        import java.util.Collection;
        import java.util.Collections;

/**
 * A Max Heap, composed in an arraylist with features to change and append itself
 * @param <E>: Type in heap
 */
public class ArrayHeap<E extends Comparable<E>> implements PriorityQueue<E> {

    ArrayList<E> arrayList;//will be the list for heap

    /**
     * Constructor; initiates arraylist
     */
    public ArrayHeap() {this.arrayList = new ArrayList<E>();}

    /**
     * adds an element to the heap
     * @param element: element added to heap
     */
    public void insert(E element) {

        arrayList.add(element);//puts the element last in order and moves it up as it needs to be
        bubbleUp(arrayList.size()-1);//moves it up, or bubbles it up
    }

    /**
     * swaps elements in the heap if base is greater than parent
     * @param baseIndex: lower element index
     * @param parentIndex: parenet element index
     */
    public void swap(int baseIndex, int parentIndex){
        E oldBase = arrayList.get(baseIndex);
        E oldParent = arrayList.get(parentIndex);
        arrayList.set(baseIndex,oldParent);//parent moves to element
        arrayList.set(parentIndex, oldBase);//element replaces parent


    }

    /**
     * Calculates the index of the "parent" of the element
     * @param child: base element index
     * @return: parent index
     */
    public int parent(int child){
        int parentIndex = (child -1)/2;//assuming left branch
        if (child % 2 == 0) {parentIndex = (child -2)/2;}//change if right branch
        return parentIndex;
    }

    /**
     * moves an element up when its greater than its parent recursively until the parent is bigger or its at the top
     * @param elIndex: element bubbled up
     */
    public void bubbleUp(int elIndex){
        int parentIndex = parent(elIndex); //calculate parents
        if (elIndex != 0){//if at the top, do nothing
            int comparison = arrayList.get(elIndex).compareTo(arrayList.get(parentIndex));//checks if element is greater than parent
            if (comparison > 0){//if larger swap and see check again
                swap(elIndex,parentIndex);
                bubbleUp(parentIndex);
            }
        }
    }

    /**
     * Checks if element is smaller than either of its children; swaps with larger one
     * @param parentIndex: index of parent element
     */
    public void bubbleDown(int parentIndex){

        if(leftChild(parentIndex) <= size()-1 && rightChild(parentIndex) <= size()-1) {//if there is a child to compare
            int comparison = arrayList.get(leftChild(parentIndex)).compareTo(arrayList.get(rightChild(parentIndex)));
            if (comparison > 0) {//if left is bigger swap it there
                swap(leftChild(parentIndex), parentIndex);
                bubbleDown(leftChild(parentIndex));
            } else {//if right is bigger or they are equal, which won't matter.
                swap(rightChild(parentIndex), parentIndex);
                bubbleDown(rightChild(parentIndex));
            }
        }else if(leftChild(parentIndex) <= size()-1 && rightChild(parentIndex) > size()-1) {//if left is in there but not right
            if (arrayList.get(parentIndex).compareTo(arrayList.get(leftChild(parentIndex))) < 0){//if
                swap(leftChild(parentIndex), parentIndex);//if no right, there is no next row
            }
        }
    }

    /**
     * finds left child index (whether exists or not
     * @param parent: parent index
     * @return: left child index
     */
    public int leftChild(int parent){
        return 2*parent+1;
    }
    /**
     * finds right child index (whether exists or not
     * @param parent: parent index
     * @return: right child index
     */
    public int rightChild(int parent){
        return 2*parent+2;
    }

    /**
     * Gets max element in heap, which is the top
     * @return: biggest element
     */
    public E max() {
        if (!arrayList.isEmpty()) {return arrayList.get(0);}
        else {return null;}
    }

    /**
     * removes top elements, moves last element to top and sorts it (bubbles it down)
     * @return: top element removed
     */
    public E removeMax() {
        E oldRoot = arrayList.get(0);
        arrayList.set(0, arrayList.get(arrayList.size()-1));//replace first term with last one
        arrayList.remove(arrayList.size()-1);//remove last term

        bubbleDown(0);
        return oldRoot;
    }

    /**
     * Size of heap
     * @return size
     */
    public int size() {return arrayList.size();}

    /**
     * Checks if empty
     * @return boolean if true
     */
    public boolean isEmpty() {return arrayList.size() == 0;}

    /**
     * Since there is no easy way to get log two,created my own
     * @param number: number plugged into log 2
     * @return result
     */
    public double toLogTwo(int number){
        return Math.log(number)/Math.log(2);//property of logs
    }

    /**
     * Sorts a list and returns the version of a max heap
     * @param sortList: list to be sorted
     * @return: sorted version of list
     */
    public ArrayList<E> sort(ArrayList<E> sortList){
        ArrayHeap<E> m = new ArrayHeap<E>();
        for (E a: sortList){//create max heap
            m.insert(a);
        }
//        buildMaxHeap(addlist);
//        m.arrayList = addlist;
        int count = 0;
        for(E i: sortList){//remove max and add to sortList
            sortList.set(count,m.removeMax());
            count++;
        }

        return sortList;

//        Collections.sort(arrayList);
//        Collections.reverse(arrayList);
    }

    /**
     * Build a max heap and copies the arraylist to the input
     * @param buildList: arraylist
     */
    public void buildMaxHeap(ArrayList<E> buildList) {
        ArrayHeap<E> m = new ArrayHeap<E>();
        for (E a: buildList){
            m.insert(a);
        }
        buildList = m.arrayList;//changes list to heap


    }


    /**
     * Will print the list into a presentable heap
     * @return: heap
     */
    public String toString(){

        double levels = Math.floor(toLogTwo(arrayList.size()));//calculates number of levels

        String printLine = "";//what's returned

        for (int level = 0; level <= levels; level++){
            int init = (int) Math.pow(2,level) -1;//first term in row
            int end = 2* init;//last tern in row


            for (int index = init; index <= end && index <= arrayList.size()-1; index++){//for every item in the right range add to row
                printLine = printLine + arrayList.get(index)+ " ";

            }
            printLine = printLine + "\n";//add a /n so each line is a different level and returned as one string

        }

        return printLine;

    }
}