/**
 * Voter with certain data and methods stored
 */
public class Voter implements Comparable<Voter> {
    String firstName = "";
    String middleName = "";
    String lastName  = "";
    String birthday = "";

    /**
     * Takes a line and sets global variables
     * @param voter: a line with candidate information
     */
    public Voter(String[] voter){
        lastName = voter[3];
        firstName = voter[4];
        middleName = voter[5];
        birthday = voter[7];
    }

    /**
     * What will be printed when demanded
     * @return: print statement
     */
    public String toString() {return lastName+", "+firstName;}

    /**
     * Compares voters. Will sort by last name, then first name
     * @return: the result of the comparison (first or last name)
     */
    public int compareTo(Voter otherVoter) {return lastName.compareTo(otherVoter.lastName) * 100 + firstName.compareTo(otherVoter.firstName);}//if same will be 0
}
