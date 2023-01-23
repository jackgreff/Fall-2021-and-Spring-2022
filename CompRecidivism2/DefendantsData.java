import java.util.ArrayList;
//import propublica.datadesign.Defendant;

/**
 * This class provides calculates information on COMPAS system
 * @author jgreff
 */
public class DefendantsData {

    //variables used to calculate false scores
    private double highNoReoffendWhite;
    private double highNoReoffendBlack;

    private double lowReoffendWhite;
    private double lowReoffendBlack;

    private double reoffendWhite;
    private double reoffendBlack;
    private double noReoffendWhite;
    private double noReoffendBlack;

    //uses above variables to calculate the percent of false positives and negatives for each race
    private double falsePositiveBlack;
    private double falsePositiveWhite;
    private double falseNegativeBlack;
    private double falseNegativeWhite;

    ArrayList<Defendant> defendants = new ArrayList<Defendant>();//will contain defendant classes, added in constructor

    /**
     * puts multiple defendants information into an array list
     * @param data:String list with a single defendants information
     */
    DefendantsData(ArrayList<String[]> data) {
        for (String[] person : data) {
            Defendant a = new Defendant(person);
            defendants.add(a);//creates defendants and adds them to array list
        }
    }

    /**
     * sorts through each defendant and if their information matches any of the categories adds 1 to the counter
     */
    public void readData() {
        for (Defendant d : defendants) {//for each defendant
            if (d.isHighRisk() && !d.hasReoffended() && d.isWhite()) {//number of high score, didn't reoffend, and white
                highNoReoffendWhite += 1.0;
            } else if (d.isHighRisk() && !d.hasReoffended() && d.isBlack()) {//number of high score, didnt reoffend, and black
                highNoReoffendBlack += 1.0;
            } else if (d.isLowRisk() && d.hasReoffended() && d.isWhite()) {//number of low score, reoffend, and white
                lowReoffendWhite += 1.0;
            } else if (d.isLowRisk() && d.hasReoffended() && d.isBlack()) {//number of low score, reoffend, and black
                lowReoffendBlack += 1.0;
            }

            if (d.hasReoffended() && d.isWhite()) {//counts number of whites who reoffend
                reoffendWhite += 1;
            } else if (d.hasReoffended() && d.isBlack()) {//counts number of blacks who reoffend
                reoffendBlack += 1;
            } else if (!d.hasReoffended() && d.isWhite()) {//counts number of whites who didn't reoffend
                noReoffendWhite += 1;
            } else if (!d.hasReoffended() && d.isBlack()) {//counts number of blacks who didn't reoffend
                noReoffendBlack += 1;
            }

            this.falsePositiveBlack = highNoReoffendBlack / noReoffendBlack;//percent of blacks who were assigned high risk, but weren't
            this.falsePositiveWhite = highNoReoffendWhite / noReoffendWhite;//percent of whites who were assigned high risk, but weren't
            this.falseNegativeBlack = lowReoffendBlack / reoffendBlack;//percent of black who were assigned low risk and reoffended
            this.falseNegativeWhite = lowReoffendWhite / reoffendWhite;//percent of whites who were assigned low risk and reoffended


        }
    }

    /**
     * prints table of false positive and negative COMPAS scores for whites and blacks in a percent
     */
    public void printTable(){
        PropublicaDataTable t = new PropublicaDataTable(falsePositiveWhite,falsePositiveBlack,falseNegativeWhite,falseNegativeBlack);//enters information into table
        System.out.println(t.toString());//prints it
}





}
