package propublica.datadesign;

//Jack Greff
//Lab 1
//2/10/22

//HEADER: main class assembles whole process, in this case getting information on a defendant
public class Main {
    // this should become the "Prediction Fails Differently for Black Defendants" table
 	public static PropublicaDataTable racialBiasTable = null;

    //main method
    public static void main( String[] args ) {

        //create class and print it
        String[] data = {"Male","Other","F","Aggravated Assault w/Firearm","1","Low","0","",""};
        Defendant d = new Defendant(data);
        System.out.println(d+"\n");

        //gets individual values
        System.out.println("Sex: " + d.getSex());
        System.out.println("Race: " + d.getRace());
        System.out.println("Charge: " + d.getCharge());
        System.out.println("Charge Degree: " + d.getChargeDegree());
        System.out.println("Decile Score: " + d.getDecileScore());
        System.out.println("Decile Rating: " + d.getDecileRating());
        System.out.println("Recidivism: " + d.getRecidivism());
        System.out.println("Recidivism Charge (if any): " + d.getRecidivismCharge());
        System.out.println("Recidivism Degree (if any): " + d.getRecidivismDegree());

        //change values
        d.setSex("Female");
        d.setRace("African-American");
        d.setCharge("Burglary");
        d.setChargeDegree("F2");
        d.setDecileScore(5);
        d.setDecileRating("medium");
        d.setRecidivism(1);
        d.setRecidivismCharge("Assault");
        d.setRecidivismDegree("M1");

        //see changes
        System.out.println("\n"+d);

        // TODO: For now, demonstrate the functionality of your "Defendant" class.
        // TODO: Eventually, set racialBiasTable to a new PropublicaDataTable with correct values.
    }
}
