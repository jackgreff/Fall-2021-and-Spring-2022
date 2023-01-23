import com.opencsv.exceptions.CsvException;
/**
 * Jack Greff
 * CS106
 * Lab 7/Bonus Lab: Deduplicaton
 * 4/27/2022
 */

/**
 * Main parts of code, assembles, collects, and runs code
 */
public class Main {

    static final boolean CheckCVS = true;  // set to false if you don't want to bother with the CSV self-check

    /**
     * Main takes a file of voters as an argument, and compares the time it takes to deduplicate it in three methods
     * @param args: file
     */
    public static void main(String[] args) {
        if (CheckCVS) {
            try {
                //initiate file
                VoterDeduplication sortVoters = new VoterDeduplication(args[0]);

                //collect information about all pairs deduplication on file
                System.out.println("-All Pairs Deduplication:");
                long start1 = System.currentTimeMillis();
                sortVoters.allPairsDeduplication();
                System.out.println("Records given: "+ sortVoters.getOriginalSize());
                System.out.println("Deduplicated size: "+ sortVoters.getDeDupedSize());
                System.out.println("Duplicates found: "+sortVoters.getOnlyDupesSize());
                long finish1 = System.currentTimeMillis();
                long timeElapsed1 = finish1 - start1;
                System.out.println("Elapsed Time: "+ timeElapsed1+" milliseconds \n");

                //collect information about hash map deduplication on file
                System.out.println("-Hash Map Deduplication:");
                long start2 = System.currentTimeMillis();
                sortVoters.hashMapDeduplication();
                System.out.println("Records given: "+ sortVoters.getOriginalSize());
                System.out.println("Deduplicated size: "+ sortVoters.getDeDupedSize());
                System.out.println("Duplicates found: "+sortVoters.getOnlyDupesSize());
                long finish2 = System.currentTimeMillis();
                long timeElapsed2 = finish2 - start2;
                System.out.println("Elapsed Time: "+ timeElapsed2+" milliseconds \n");

                //collect information about sort and remove deduplication on file
                System.out.println("-Sort and Remove Deduplication:");
                long start3 = System.currentTimeMillis();
                sortVoters.sortAndRemoveDeduplication();
                System.out.println("Records given: "+ sortVoters.getOriginalSize());
                System.out.println("Deduplicated size: "+ sortVoters.getDeDupedSize());
                System.out.println("Duplicates found: "+sortVoters.getOnlyDupesSize());
                long finish3 = System.currentTimeMillis();
                long timeElapsed3 = finish3 - start3;
                System.out.println("Elapsed Time: "+ timeElapsed3+" milliseconds \n");
            } catch (CsvException e) {
                System.out.println("   ******* Oops, something went wrong when extracting CSV entries :-(");
                e.printStackTrace();
            }
        }
    }
}
