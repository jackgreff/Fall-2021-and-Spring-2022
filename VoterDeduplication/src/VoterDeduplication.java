import com.opencsv.CSVReaderHeaderAware;
import com.opencsv.exceptions.CsvException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

/**
 * Takes a file and removes duplicates in 3 different ways; also provides different information about sort
 */
public class VoterDeduplication {
    ArrayList<Voter> withDupes = new ArrayList<>();
    ArrayList<Voter> withoutDupes = new ArrayList<>(withDupes);
    ArrayList<Voter> onlyDupes = new ArrayList<>();
    int withoutSize = 0;//needed for hash function since it doesn't use withoutDupes, otherwise could use withoutDupes.size() in getter


    /**
     * Constructor; creates the list with duplicates and makes it ready for sorting
     * @param myFile: file to be sorted
     * @throws CsvException: trouble getting entries in file;
     */
    VoterDeduplication(String myFile) throws CsvException {
        try {
            CSVReaderHeaderAware reader = new CSVReaderHeaderAware(new FileReader(myFile));
            ArrayList<String[]> voters = new ArrayList<>(reader.readAll());//lines from each file (each a candidate)
            reader.close();

            for (String[] voter : voters) {//create a candidate from each line, adds to heap
                Voter myVoter = new Voter(voter);
                withDupes.add(myVoter);
            }


        } catch (IOException e) {System.out.println("   ******* Oops, something went wrong when opening the vote file :-(");e.printStackTrace();
        } catch (CsvException e) {System.out.println("   ******* Oops, something went wrong when extracting CSV entries :-(");e.printStackTrace();}
    }

    /**
     * Compares all pairs and if a pair is equal, we don't add the term to the non-duplicate list
     * @return: a list of the duplicates
     */
    ArrayList<Voter> allPairsDeduplication(){
        reset();//if other functions were run and global variables were changed, resets them
        withoutDupes.clear();//Set to start as withDupes, cleared for terms to be added;
        boolean wasIn = false;//boolean used to detect if it was already in
        for (int i = 0; i < withDupes.size(); i++){//for each voter,
            Voter voter = withDupes.get(i);
            for (int j= i + 1; j < withDupes.size(); j++){//compare with every voter after (no need to compare before since current item would've been deleted)
                Voter otherVoter = withDupes.get(j);//the compared voter
                if (voter.compareTo(otherVoter) == 0) {wasIn = true; break;}//if equal, signal it shouldn't be added
            }
            if (!wasIn){withoutDupes.add(voter);//if not in add to withoutDupes
            }else{onlyDupes.add(voter);}//else add to onlyDupes

            wasIn = false;//reset wasIn for each original item
        }
        withoutSize = withoutDupes.size();//set size

        return onlyDupes;
    }

    /**
     * Sorts the list and moves any terms that match the next term into the only duplicates list
     * @return the list with all duplicates
     */
    ArrayList<Voter> sortAndRemoveDeduplication(){
        reset();
       Collections.sort(withoutDupes);
       int numDeleted = 0;//counts number of deleted, so it can correctly calculate indexes when an item is deleted

        for (int voterIndex = 0; voterIndex < withoutDupes.size()-1+numDeleted; voterIndex++) {//-1 until end of list
            Voter currentVoter = withoutDupes.get(voterIndex-numDeleted);// current adjusted voter = original current count - number deleted (all before current item)
            Voter nextVoter = withoutDupes.get(voterIndex-numDeleted+1);//next after current voter

            if(currentVoter.compareTo(nextVoter) == 0){//if equal, remove
                withoutDupes.remove(currentVoter);
                onlyDupes.add(currentVoter);//add to only dupes as well
                numDeleted++;//adjusts counter for indexing
            }

       }
        withoutSize = withoutDupes.size();//need to set size of function; reset when next function called
        return onlyDupes;
    }

    /**
     * Maps all voters in a hash map, with the values of each key being how often they appear
     * @return: a list of all duplicates
     */
    ArrayList<Voter> hashMapDeduplication() {
        reset();
        HashMap<String, Integer> map = new HashMap<>();//initiate hash
        for (Voter voter : withoutDupes) {//check every voter
            if (map.containsKey(voter.toString())) {//if already in list
                int currSize = map.get(voter.toString());//will be size of already listed key
                map.replace(voter.toString(), currSize + 1);//increases by 1
                onlyDupes.add(voter);//adds repeat to repeat lists
            } else {
                map.put(voter.toString(), 1);//if not already in, add
            }
        }
        withoutSize = map.size();//need to set variable for get function below

        return onlyDupes;

    }

    /**
     * Getter methods for size
     * @return: returns the size of the desires list
     */
    public int getOriginalSize() {return withDupes.size();}//will always be the same
    public int getDeDupedSize(){return withoutSize;}
    public int getOnlyDupesSize(){return onlyDupes.size();}

    /**
     * Getters for the 3 main lists
     * @return: the desired list
     */
    public ArrayList<Voter> getOnlyDupes() {return onlyDupes;}
    public ArrayList<Voter> getWithDupes() {return withDupes;}
    public ArrayList<Voter> getWithoutDupes() {return withoutDupes;}

    /**
     * Resets deduplicated list and duplicates list so another method can sort/create them
     */
    public void reset(){withoutDupes = new ArrayList<>(withDupes); onlyDupes.clear();}
}
