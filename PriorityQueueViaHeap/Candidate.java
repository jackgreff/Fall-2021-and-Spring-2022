/**
 * Candidate with certain data and methods stored
 */
public class Candidate implements Comparable<Candidate> {
    String wholeName = "";
    String lastName  = "";
    double percent = 0;

    /**
     * Takes a line and sets global variables
     * @param candidate: a line with candidate information
     */
    public Candidate(String[] candidate){
        lastName = candidate[0];
        wholeName = candidate[1];
        percent = Double.parseDouble(candidate[2]);
    }

    /**
     * What will be printed when demanded
     * @return: print statement
     */
    public String toString() {
        return wholeName+":"+percent;
    }

    /**
     * When comparing candidates, compare their percentages, if equal by last name
     */
    public int compareTo(Candidate candidate) {
        if (percent != candidate.percent){
            if (percent > candidate.percent){return 1;}
            else{return -1;}
        }else{
            return lastName.compareTo(candidate.lastName);

        }
    }
}
