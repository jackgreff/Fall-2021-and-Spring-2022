import org.junit.Test;

import static org.junit.Assert.*;
import static org.junit.jupiter.api.Assertions.assertEquals;


// Test from the .md file is given below

class BinarySearchTreeTest {
    public static void main(String[] args) {
        testInteger(null); // need to replace this with a tree, e.g., new LinkedBinarySearchTree<Integer>());
        testCharacter(null); // same here, but <Character>
    }

    @Test
    private static void testInteger(BinarySearchTree<Integer> initiallyEmptyIntTree) {
        if (initiallyEmptyIntTree == null) {
            System.out.println("testCharacter: need to create a tree for testing!");
        }
        assert(initiallyEmptyIntTree != null);        // If we wanted to run this without changing the object we were passed, we would copy:
        //      BinarySearchTree<Integer> intTree = initiallyEmptyIntTree.deepCopy();
        // But, since the assignment doesn't require "deepCopy", we'll make this method private,
        //   and only call it when we don't subsequently care about the BST we pass it,
        //   and then just change the original tree:
        BinarySearchTree<Integer> intTree = initiallyEmptyIntTree;  // intTree now "paired with" the original tree
        assert(intTree.isEmpty());

        intTree.insert(8);
        intTree.insert(11);
        intTree.insert(5);
        intTree.insert(17);
        intTree.insert(1);
        intTree.insert(9);
        intTree.insert(3);
        System.out.println("Pre: "+intTree.toStringPreOrder());
        System.out.println("Pre: "+intTree.toStringPreOrder());
        System.out.println("Pre: "+intTree.toStringPreOrder());

        assertEquals("8 5 1 3 11 9 17", intTree.toStringPreOrder());
        assertEquals("1 3 5 8 9 11 17", intTree.toStringInOrder());
        assertEquals("3 1 5 9 17 11 8", intTree.toStringPostOrder());
    }


    @Test
    private static void testCharacter(BinarySearchTree<Character> initiallyEmptyCharacterTree) {
        // perhaps should have called this Kobayashi Maru?
        // See note in testInteger about "deepCopy"
        if (initiallyEmptyCharacterTree == null) {
            System.out.println("testCharacter: need to create a tree for testing!");
        }
        assert(initiallyEmptyCharacterTree != null);

        BinarySearchTree<Character> letterTree = initiallyEmptyCharacterTree;
        assert(letterTree.isEmpty());

        letterTree.insert('A');
        letterTree.insert('C');
        letterTree.insert('G');
        letterTree.insert('B');
        letterTree.insert('D');
        letterTree.insert('G'); // inserting again, should replace
        letterTree.insert('F');
        letterTree.insert('E');
        letterTree.insert('H');
        letterTree.insert('I');
        assertEquals(9, letterTree.size());
        assertEquals("A C B G D F E H I", letterTree.toStringPreOrder());
        assertEquals("A B C D E F G H I", letterTree.toStringInOrder());
        assertEquals("B E F D I H G C A", letterTree.toStringPostOrder());
    }
}