/**
 *takes a string list and allows you access to change and read important information
 */
public class Defendant {

    //creating enums
    enum chargeDegree {m, f};//types of charges: misdemeanor and felony
    enum sex {male, female};//types of gender
    enum race {caucasian, africanAmerican,hispanic,asian,other};//types of race
    enum decileRating {low, medium, high};//types of rating
    enum recivisimDegree {m1, m2, f1, f2, f3,noDegree};//types of degree of recidivism

    //string variables, don't make sense as enums (large variety)
    private String charge; //charge ie. burglary
    private String recidCharge; //recidivism charge

    //int variables, don't make sense as enums (easier as ints)
    private int decileScore;//1-10, how likely to reoffend
    private int recidivism;//1 is reoffended, 0 is did not

    //creating our variables from enums
    private chargeDegree currentChargeDegree;
    private sex currentSex;
    private race currentRace;
    private decileRating currentDecileRating;
    private recivisimDegree currentRecivisimDegree;


    /**
     * the following classes convert string to the type of enum. Easy for both initialization and the setter
     * @param a input as a string
     * @returnrace  input as an enum
     */
    public race enumToRace(String a){
        //SAME FOR THE OTHER METHODS
        if (a.equals("Caucasian")){return race.caucasian;}//given the race, converts to the coinciding enum
        else if (a.equals("African-American")){return race.africanAmerican;}
        else if (a.equals("Hispanic")){return race.hispanic;}
        else if (a.equals("Asian")){return race.asian;}
        else {return race.other;}//last one is else so there is something guaranteed to be returned
    }
    public sex enumToSex(String a){//converts sex to enum
        if (a.equals("Male")){return sex.male;}
        else {return sex.female;}
    }
    public chargeDegree enumToCD(String a){//converts charge degree to enum
        if (a.equals("M")){return chargeDegree.m;}
        else {return chargeDegree.f;}
    }
    public decileRating enumToDR(String a){//converts decile rating to enum
        if (a.equals("Low")){return decileRating.low;}
        else if (a.equals("Medium")){return decileRating.medium;}
        else {return decileRating.high;}
    }
    public recivisimDegree enumToRD(String a){//converts recidivism degree to enum
        if (a.equals("M1")){return recivisimDegree.m1;}
        else if (a.equals("M2")){return recivisimDegree.m2;}
        else if (a.equals("F1")){return recivisimDegree.f1;}
        else if (a.equals("F2")){return recivisimDegree.f2;}
        else if (a.equals("F3")){return recivisimDegree.f3;}
        else {return recivisimDegree.noDegree;}
    }


    /**
     * Sets variables to the correct data, and converts where needed
     * @param data data sorted
     */
    Defendant(String[] data) {
        //initializing variables from string array converted to correct type
        currentSex = enumToSex(data[0]);
        currentRace = enumToRace(data[1]);
        currentChargeDegree = enumToCD(data[2]);
        charge = data[3];//string, no fancy stuff needed
        decileScore = Integer.parseInt(data[4]);//integer converted
        currentDecileRating = enumToDR(data[5]);
        recidivism = Integer.parseInt(data[6]);
        recidCharge = data[7];
        currentRecivisimDegree = enumToRD(data[8]);
    }

    /**
     * Will give a line of summary about the defendant
     * @return a string with important information
     */
    public String toString(){
        if (recidCharge.equals("")){//if not reoffended
            return "A " +  currentRace.toString()+ " " +currentSex.toString() + " defendant was charged with " + charge + ". They were assigned a " + currentDecileRating.toString() + " a risk score of "+decileScore +". They did not reoffend.";
        }else{//if reoffended
            return "A " +  currentRace.toString()+ " " +currentSex.toString() + " defendant was charged with " + charge + ". They were assigned a " + currentDecileRating.toString() + " a risk score of "+decileScore +". They did reoffend, committing "+ recidCharge + " ("+currentRecivisimDegree+")";

        }
    }


    /**
     * change variables to the inputted values
     * @param settingSex: new value
     */
    public void setSex(String settingSex){this.currentSex=enumToSex(settingSex);};//EXAMPLE: input is converted and made to be current variable
    public void setRace(String settingRace){this.currentRace=enumToRace(settingRace);};
    public void setCharge(String settingCharge){this.charge=settingCharge;};
    public void setChargeDegree(String settingChargeD){this.currentChargeDegree=enumToCD(settingChargeD);};
    public void setDecileScore(int settingDS){this.decileScore=settingDS;};
    public void setDecileRating(String settingDR){this.currentDecileRating=enumToDR(settingDR);};
    public void setRecidivism(int settingRecid){this.recidivism=settingRecid;};
    public void setRecidivismCharge(String settingRecidCharge){this.recidCharge=settingRecidCharge;};
    public void setRecidivismDegree(String settingRecidDeg){this.currentRecivisimDegree=enumToRD(settingRecidDeg);};


    /**
     * gives the values of the desired variable
     * @return variable (as a string or number)
     */
    public String getSex(){return currentSex.toString();};//EXAMPLE: gives the sex when called
    public String getRace(){return currentRace.toString();};
    public String getCharge(){return charge;};
    public String getChargeDegree(){return currentChargeDegree.toString();};
    public int getDecileScore(){return decileScore;};
    public String getDecileRating(){return currentDecileRating.toString();};
    public int getRecidivism(){return recidivism;};
    public String getRecidivismCharge(){return recidCharge;};
    public String getRecidivismDegree(){return currentRecivisimDegree.toString();};


    /**
     * key booleans about the identity and actions of defendant
     * @return whether the defendant matches desired criteria
     */
    //says whether defendeant is white
    public boolean isWhite() {
        if (currentRace.equals(race.caucasian)) {return true;} //if true
        else {return false;}//if false
    }
    //says whether defendeant is black
    public boolean isBlack() {
        if (currentRace.equals(race.africanAmerican)) {return true;}
        else {return false;}
    }
    //says whether person reoffends
    public boolean hasReoffended() {
        if (recidivism == 1) {return true;}
        else {return false;}//make an else to throw an error
    }
    //says whether defendeant is high risk (which includes medium)
    public boolean isHighRisk() {
        if (currentDecileRating.equals(decileRating.high) || currentDecileRating.equals(decileRating.medium)) {return true;}
        else{return false;}
    }
    //says whether defendeant is low risk
    public boolean isLowRisk() {
        if (currentDecileRating.equals(decileRating.low)) {return true;}
        else {return false;}
    }

}