import com.opencsv.CSVReader;
import com.opencsv.CSVReaderHeaderAware;
import com.opencsv.exceptions.CsvException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

/**
 * Given gender, name, and file, will find and store information
 */
public class NameData{

    //important variables that I will almost always need, set in constructor
    String name;
    String fileName;
    Boolean isMale = true;
    ArrayList<String[]> myEntries;
    int myNumber = 0;

    /**
     * Sets important variables, like name, gender, file name,
     * @param inpIsMale: gender, either -m or -f
     * @param inpName: name of baby
     * @param inpFilename: file name, ex: names2017.csv
     * @throws CsvException//errors caused by csv reader
     * @throws IOException//error caused by csv reader
     */
    public NameData(String inpIsMale, String inpName, String inpFilename) throws CsvException, IOException {
        //sets gender. Important for unisex names like sam, adrian, etc,
        if (inpIsMale.equals("-m")){
            isMale = true;
        }else if (inpIsMale.equals("-f")){
            isMale = false;
        }

        fileName = inpFilename;
        //sets the first letter to uppercase ex: mary -> Mary
        String currentName= Character.toUpperCase(inpName.charAt(0))+"";//will be adding to here
        for(int i=1; i<=inpName.length()-1; i++) {//adds everything except first letter
            name = currentName +inpName.charAt(i);
        }

        CSVReader reader = new CSVReader(new FileReader(fileName)); //read csv
        myEntries = new ArrayList<String[]>(reader.readAll());//add csv into string list array
        reader.close();

        for (String[] line : myEntries) {//finds the initial amount of occurrences of the name. when adding again, just sets number
            if (line[1].equals(name) && isMale.equals(true)) {//male
                myNumber = Integer.valueOf(line[2]);
            } else if (line[3].equals(name) && isMale.equals(false)) {//female
                myNumber = Integer.valueOf(line[4]);
            }
        }
    }
    //setters replace values with inputs
    public void setName(String setTheName){this.name = setTheName;}
    public void setFile(String theFileName){this.fileName = theFileName;}
    public void setSex(String theFileName){this.fileName = theFileName;}
    public void setNumber(int newNumber){ myNumber = myNumber + newNumber;}//setting here doesn't replace, but adds

    //getters, returns their respective values
    public String getName(){return this.name;}
    public String getFile(){return this.fileName;}
    public boolean getSex(){return this.isMale;}
    public int getNumber(){return this.myNumber;}

    /**
     * gets total names in the file
     * @return total names in file
     */
    public int getTotalNames(){
        int totalNames = 0;
        for (String[] line : myEntries) {
            if (isMale == true){ totalNames += Integer.parseInt(line[2]);}//adds all male names
             if (isMale == false){totalNames += Integer.parseInt(line[4]);}//adds all female names
        }
        return totalNames;
    }

    /**
     * sends name and appearances when asked to be printed
     * @return string with info
     */
    public String toString(){
        for (String[] line: myEntries){
            if (line[1].equals(name) && isMale == true) {//male
                return name+" appears "+myNumber+" times";
            }else if (line[3].equals(name) && isMale == false) {//male
                return name+" appears "+myNumber+" times";
            }
        }
        return name +" does not appear in the list";
    }

    //do not actually use. It's right, but the built-in function is just simpler and more useful

    /**
     * Compares name in this name data with another name data instance's name
     * @param compName name data instance to be comparison
     * @return returns an integer representing if its greater than or less than the input
     */
    public int compareTo(NameData compName){
        if (name.compareTo(compName.getName()) > 0){//the original is less than the comparison
            return 1;
        }if (name.compareTo(compName.getName()) < 0){//the original is greater than the comparison
            return -1;
        }else{//equal
            return 0;
        }
    }

}