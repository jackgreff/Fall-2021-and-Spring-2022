/**
 * Jack Greff
 * Lab 6: Priority Queue Via Heap
 * 4/13/22Z
 */

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

import com.opencsv.CSVReaderHeaderAware;
import com.opencsv.exceptions.CsvException;

public class Main {
    /**
     * Main files; runs examples and if files are inputed, they will be sorted
     */
    public static void main(String[] args) throws CsvException {

        System.out.println("Put your main program here (note TODO items in source code below this print).");
    	// TODO: first create tests for your ArrayHeap class (in a separate method below).

        // TODO: then read in the polling data from the given file (just one) and create
		// a heap of candidates to be sorted by their polling numbers

        // For reference, here's an example of opening one of the polling data files:
        try {
            if (args.length != 0) {
                //EXAMPLE 4
                ArrayHeap<Candidate> candidateHeap = new ArrayHeap<Candidate>();
                CSVReaderHeaderAware reader = null;
                ArrayList<String[]> candidates = null;
                ArrayList<Candidate> sortCandidates = candidateHeap.arrayList;//will be and stay empty (candidateHeap never changed)

                for (String arg : args) {//for each file do the following:
                    //read file
                    //We need an arrayList of type candidate to initiate sortCandidates below;
                    reader = new CSVReaderHeaderAware(new FileReader(arg));
                    candidates = new ArrayList<String[]>(reader.readAll());//lines from each file (each a candidate)
                    reader.close();

                    for (String candidate[] : candidates) {//create a candidate from each line, adds to heap
                        Candidate myCandidate = new Candidate(candidate);
                        sortCandidates.add(myCandidate);
                    }

                    ArrayList<Candidate> sortedArray = candidateHeap.sort(sortCandidates);//need any heap to use sort
                    for (Candidate i: sortedArray){
                        System.out.println(i);
                    }
//                    System.out.println(sortedArray);
                }
            }

            //EXAMPLE 1
            Integer[] arr = {-2,3,9,-7,1,2,6,-3};
            ArrayHeap<Integer> numberHeap = new ArrayHeap<Integer>();
            for(Integer i: arr){numberHeap.insert(i);}
            System.out.println(numberHeap);

            //EXAMPLE 2
            ArrayHeap<Character> letterHeap = new ArrayHeap<Character>();
            letterHeap.insert('A');
            letterHeap.insert('C');
            letterHeap.insert('G');
            letterHeap.insert('B');
            letterHeap.insert('D');
            letterHeap.insert('G'); // inserting again, will still both copies
            letterHeap.insert('F');
            letterHeap.insert('E');
            letterHeap.insert('H');
            letterHeap.insert('I');
            System.out.println("size:" + letterHeap.size());
            System.out.println(letterHeap);
//            letterHeap.removeMax();
//            System.out.println(letterHeap);

            //EXAMPLE 3
            ArrayList<Integer> array = new ArrayList<Integer>(Arrays.asList(arr));
            // make a new heap out of the array
            ArrayHeap<Integer> heap = new ArrayHeap<Integer>();
            ArrayList<Integer> sortedArray = heap.sort(array);
            System.out.println("Sorted: "+sortedArray + "\n");
            System.out.println(heap);




        } catch (IOException e) {
            System.out.println("Oops, something went wrong when opening the poll data");
            e.printStackTrace();
        }
    }
}
