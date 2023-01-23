//HEADER: defendant class assembles information of a defendant, allowing you to change and get information, as well as get important booleans
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


    //the following classes convert string to the type of enum. Easy for both initialization and the setters;
    public race enumToRace(String a){
        //SAME FOR THE OTHER METHODS
        if (a == "Caucasian"){return race.caucasian;}//given the race, converts to the coinciding enum
        else if (a == "African-American"){return race.africanAmerican;}
        else if (a == "Hispanic"){return race.hispanic;}
        else if (a == "Asian"){return race.asian;}
        else {return race.other;}//last one is else so there is something guaranteed to be returned
    }

    //converts sex to enum
    public sex enumToSex(String a){
        if (a == "Male"){return sex.male;}
        else {return sex.female;}
    }

    //converts charge degree to enum
    public chargeDegree enumToCD(String a){
        if (a == "M"){return chargeDegree.m;}
        else {return chargeDegree.f;}
    }

    //converts decile rating to enum
    public decileRating enumToDR(String a){
        if (a == "Low"){return decileRating.low;}
        else if (a == "Medium"){return decileRating.medium;}
        else {return decileRating.high;}
    }

    //converts recidivism degree to enum
    public recivisimDegree enumToRD(String a){
        if (a == "M1"){return recivisimDegree.m1;}
        else if (a == "M2"){return recivisimDegree.m2;}
        else if (a == "F1"){return recivisimDegree.f1;}
        else if (a == "F2"){return recivisimDegree.f2;}
        else if (a == "F3"){return recivisimDegree.f3;}
        else {return recivisimDegree.noDegree;}
    }


    //constructor
    Defendant(String[] data) {
        //initalizing variables from string array coverted to correct type
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

    //what will show when printed
    public String toString(){
        if (recidCharge == ""){//if not reoffended
            return "A " +  currentRace.toString()+ " " +currentSex.toString() + " defendant was charged with " + charge + ". They were assigned a " + currentDecileRating.toString() + " a risk score of "+decileScore +". They did not reoffend.";
        }else{//if reoffended
            return "A " +  currentRace.toString()+ " " +currentSex.toString() + " defendant was charged with " + charge + ". They were assigned a " + currentDecileRating.toString() + " a risk score of "+decileScore +". They did reoffend, committing "+ recidCharge + " ("+currentRecivisimDegree+")";

        }
    }


    //change inputs to the coinciding values
    public void setSex(String settingSex){this.currentSex=enumToSex(settingSex);};//EXAMPLE: input is converted and made to be current variable
    public void setRace(String settingRace){this.currentRace=enumToRace(settingRace);};
    public void setCharge(String settingCharge){this.charge=settingCharge;};
    public void setChargeDegree(String settingChargeD){this.currentChargeDegree=enumToCD(settingChargeD);};
    public void setDecileScore(int settingDS){this.decileScore=settingDS;};
    public void setDecileRating(String settingDR){this.currentDecileRating=enumToDR(settingDR);};
    public void setRecidivism(int settingRecid){this.recidivism=settingRecid;};
    public void setRecidivismCharge(String settingRecidCharge){this.recidCharge=settingRecidCharge;};
    public void setRecidivismDegree(String settingRecidDeg){this.currentRecivisimDegree=enumToRD(settingRecidDeg);};

    //gives the values
    public String getSex(){return currentSex.toString();};//EXAMPLE: gives the sex when called
    public String getRace(){return currentRace.toString();};
    public String getCharge(){return charge;};
    public String getChargeDegree(){return currentChargeDegree.toString();};
    public int getDecileScore(){return decileScore;};
    public String getDecileRating(){return currentDecileRating.toString();};
    public int getRecidivism(){return recidivism;};
    public String getRecidivismCharge(){return recidCharge;};
    public String getRecidivismDegree(){return currentRecivisimDegree.toString();};


    //says whether defendeant is white
    private boolean isWhite() {
        if (currentRace == race.caucasian) {return true;} //if true
        else {return false;}//if false
    }

    //says whether defendeant is black
    private boolean isBlack() {
        if (currentRace == race.africanAmerican) {return true;}
        else {return false;}

    }

    //says whether person reoffends
    private boolean hasReoffended() {
        if (recidivism == 1) {return true;}
        else {return false;}//make an else to throw an error
    }

    //says whether defendeant is high risk (which includes medium)
    private boolean isHighRisk() {
        if (currentDecileRating == decileRating.high || currentDecileRating == decileRating.medium) {return true;}
        else{return false;}

    }

    //says whether defendeant is low risk
    private boolean isLowRisk() {
        if (currentDecileRating == decileRating.low) {return true;}
        else {return false;}
    }

}