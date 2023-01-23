/**
 * A Binary Search Tree that will have a left tree and a right tree. Has additional functions within it
 * @param <E>: The type of the data in each tree root
 */
public class LinkedBinarySearchTree<E extends Comparable<E>> implements BinarySearchTree<E> {
    private E data; // Root's element
    private LinkedBinarySearchTree<E> leftSubTree; // Reference to the left subtree
    private LinkedBinarySearchTree<E> rightSubTree; // Reference to the right subtree

    /**
     * An empty tree (no data provided)
     */
    public LinkedBinarySearchTree() {
        this.data = null;
        leftSubTree = null;
        rightSubTree = null;
    }

    /**
     * A tree with data inside
     * @param data : Data to be entered
     */
    public LinkedBinarySearchTree(E data) {
        this.data = data;
        leftSubTree = null;
        rightSubTree = null;
    }

    /**
     * gives root element
     * @return the root element
     */
    public E getRootElement() {
        return this.data;
    }


    /**
     * Will say if the tree has any data (true or false)
     * @return True or false on it being empty
     */
    public boolean isEmpty() {
        return data == null;
    }

    /**
     * Says size of tree
     * @return size of tree
     */
    public int size() {
        if (isEmpty())return 0;//if the tree is empty add nothing
        else{
            int theSize = 0;
            if (leftSubTree != null)theSize += leftSubTree.size();//add the length of left branches
            if (rightSubTree != null)theSize += rightSubTree.size();//add length of right branches
            return theSize + 1;//add one for the current tree (not zero since else statement)
        }

    }

    /**
     * Add a tree to the tree (will be in the right order)
     * @param datapoint: datapoint of new tree
     */
    public void insert(E datapoint){
        if (data == null){//if there is no data fill it
            this.data = datapoint;
        }else if (data.compareTo(datapoint) > 0) {//if it's less than current node
            if(leftSubTree == null){leftSubTree = new LinkedBinarySearchTree<E>(datapoint);}//if tree is nonexistent make a new one with the node
            else{leftSubTree.insert(datapoint);}//go into the left branch and resort it there
        }else if (data.compareTo(datapoint) < 0) {
            if(rightSubTree == null){rightSubTree = new LinkedBinarySearchTree<E>(datapoint);}//if tree is nonexistent make a new one with the node
            else{rightSubTree.insert(datapoint);}//go into the right branch and resort it there
        }else{
            this.data = datapoint;//if they are equal, replace new one
        }
    }

    /**
     * returns a tree's data in the order of current - left -  right
     * @return the preorder traversal of the tree
     */
    public String toStringPreOrder() {
        if (leftSubTree != null && rightSubTree != null){return data.toString() + " "+leftSubTree.toStringPreOrder() +" "+ rightSubTree.toStringPreOrder();//if all there, the order is current left right
        }else if (leftSubTree == null && rightSubTree != null){return data.toString()  +" "+ rightSubTree.toStringPreOrder();//if right missing, just take left and current
        } else if (leftSubTree != null && rightSubTree == null){return data.toString() + " "+leftSubTree.toStringPreOrder();//if left is missing, return right and current
        }else{return data.toString();}
    }
    /**
     * returns a tree's data in the order of left - current -  right
     * @return the inorder traversal of the tree
     */
    public String toStringInOrder(){//
        if (leftSubTree != null && rightSubTree != null){return leftSubTree.toStringInOrder() +" "+data.toString() +" "+ rightSubTree.toStringInOrder();//if all there, the order is  left current right
        }else if (leftSubTree == null && rightSubTree != null){return data.toString()  +" "+ rightSubTree.toStringInOrder();//if right missing, just take left and current
        } else if (leftSubTree != null && rightSubTree == null){return leftSubTree.toStringInOrder()+" "+data.toString();//if left is missing, return right and current
        }else{return data.toString();}

    }
    /**
     * returns a tree's data in the order of left - right -  current
     * @return the postorder traversal of the tree
     */
    public String toStringPostOrder(){//
        if (leftSubTree != null && rightSubTree != null){return leftSubTree.toStringPostOrder() +" "+ rightSubTree.toStringPostOrder() +" "+data.toString();//if all there, the order is left right current
        }else if (leftSubTree == null && rightSubTree != null){return  rightSubTree.toStringPostOrder() +" "+data.toString() ;//if right missing, just take left and current
        } else if (leftSubTree != null && rightSubTree == null){return leftSubTree.toStringPostOrder()+" "+data.toString();//if left is missing, return right and current
        }else{return data.toString();}
    }



}

