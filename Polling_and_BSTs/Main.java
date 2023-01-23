import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import com.opencsv.CSVReaderHeaderAware;
import com.opencsv.exceptions.CsvException;

public class Main {
    public static void main(String[] args) throws CsvException{
        try {
            if (args.length != 0) {
                LinkedBinarySearchTree<Candidate> candidateTree = new LinkedBinarySearchTree<Candidate>();

                CSVReaderHeaderAware reader = null;
                ArrayList<String[]> candidates = null;
                for (String arg : args) {//for each file do the following:
                    //read file
                    reader = new CSVReaderHeaderAware(new FileReader(arg));
                    candidates = new ArrayList<String[]>(reader.readAll());//lines from each file (each a candidate)
                    reader.close();

                    for (String candidate[] : candidates) {//create a candidate from each line, adds to tree
                        Candidate myCandidate = new Candidate(candidate);
                        candidateTree.insert(myCandidate);
                    }
                }
                System.out.println("Pre:  "+candidateTree.toStringPreOrder());
                System.out.println("In:   "+candidateTree.toStringInOrder());
                System.out.println("Post: "+candidateTree.toStringPostOrder());
            }







            LinkedBinarySearchTree<Integer> intTree = new LinkedBinarySearchTree<Integer>();
            intTree.insert(8);
            intTree.insert(11);
            intTree.insert(5);
            intTree.insert(17);
            intTree.insert(1);
            intTree.insert(9);
            intTree.insert(3);
            System.out.println("Pre:  "+intTree.toStringPreOrder());
            System.out.println("In:   "+intTree.toStringInOrder());
            System.out.println("Post: "+intTree.toStringPostOrder());

            BinarySearchTree<Character> letterTree = new LinkedBinarySearchTree<Character>();
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
            System.out.println("Size: " + letterTree.size());
            System.out.println("Pre:  "+letterTree.toStringPreOrder());
            System.out.println("In:   "+letterTree.toStringInOrder());
            System.out.println("Post: "+letterTree.toStringPostOrder());
        } catch (IOException e) {
            System.out.println("Oops, something went wrong when opening the poll data");
            e.printStackTrace();
        }

    }
}