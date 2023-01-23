/**
 *Jack Greff
 * Lab 3
 * 3/17/22
 */
import com.opencsv.CSVReader;
import com.opencsv.exceptions.CsvException;

import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * takes a name and recognized csv files to see the popularity of a name
 * @args: List of names
 */
public class Main {
    public static void main(String[] args) throws CsvException, IOException {
        // Your main code goes here. Remember to create the NameData, Node and DoublyLinkedList classes in separate files
//        NameData nd = new NameData(args[0],args[1],args[2]);//creates the instance requested
        //sort inputs
        //get csvs to look at

        //will get all csv files known
        String[] csvArray = {"names1990.csv", "names1991.csv", "names1992.csv", "names1993.csv", "names1994.csv", "names1995.csv", "names1996.csv", "names1997.csv", "names1998.csv", "names1999.csv", "names2000.csv", "names2001.csv", "names2002.csv", "names2003.csv", "names2004.csv", "names2005.csv", "names2006.csv", "names2007.csv", "names2008.csv", "names2009.csv", "names2010.csv", "names2011.csv", "names2012.csv", "names2013.csv", "names2014.csv", "names2015.csv", "names2016.csv", "names2017.csv"};
        List<String> csvAsList = new ArrayList<String>(Arrays.asList(csvArray));//converts it to a list to use the .contain checker

        List<String> csvAsked = new ArrayList<String>();
        List<Boolean> addNames = new ArrayList<Boolean>();
        List<Boolean> addFiles = new ArrayList<Boolean>();
        for (String arg: args){
            if (csvAsList.contains(arg)){addFiles.add(true);}//adds all file names to a list to then check if empty
            if (arg.equals("-m") || arg.equals("-f")) {addNames.add(true);}//adds all  names to a list to then check if empty
        }
        try{Boolean testFiles = addFiles.get(0);//checks if list full of files is not empty
        }catch (Exception E){System.out.println(E + ": No data set to search on!");}//if empty produce this error
        try{Boolean testNames = addNames.get(0);//checks if list full of names is not empty
        }catch (Exception E){System.out.println(E + ": No names to look up!");}//if empty produce this error


        int index = 0;//index of args list
        for (String detectSex : args) {
            if (detectSex.equals("-f") || detectSex.equals("-m")) {//for each name
                String inputName = args[index + 1];
                int totalNamesM = 0;
                int totalNamesF = 0;
                int indAppearancesM = 0;
                int indAppearancesF = 0;

                DoublyLinkedList entireList = new DoublyLinkedList();//entire list with all names, numbers, etc
                //I DON'T NEED A SEPARATE MALE AND FEMALE LISTS, WILL SORT BELOW
                for (String file : args) {//for each file
                    if (csvAsList.contains(file)) {
                        csvAsked.add(file);
                        //adds every occurrence and total names, through nodes is not necessary or easier, though it could retrieve from there
                        NameData nameInfo = new NameData(detectSex, inputName, file);
                        if (detectSex.equals("-f")) {
                            totalNamesF += nameInfo.getTotalNames();
                            indAppearancesF += nameInfo.getNumber();
                        }
                        if (detectSex.equals("-m")) {
                            totalNamesM += nameInfo.getTotalNames();
                            indAppearancesM += nameInfo.getNumber();
                        }

                        //file-reader
                        CSVReader reader = new CSVReader(new FileReader(file)); //read csv
                        ArrayList<String[]> myEntries = new ArrayList<String[]>(reader.readAll());//add csv into string list array
                        reader.close();
                        //insert data into the larger list
                        if (detectSex.equals("-m")) {
                            for (String[] line : myEntries) {
                                NameData nd = new NameData(detectSex, line[1], file);//creates data class instance
                                entireList.insertAlpha(nd);//adds to the list
                            }
                        }else if (detectSex.equals("-f")) {
                            for (String[] line : myEntries) {
                                NameData nd = new NameData(detectSex, line[3], file);
                                entireList.insertAlpha(nd);
                            }
                        }
                    }
                }//finished searching files after this;

                //Have all data now, just need to print it
                if (indAppearancesF != 0 && indAppearancesM != 0) {//if name in list
                    if (detectSex.equals("-m")) {
                        float percent = (float) indAppearancesM / (float) totalNamesM;
                        System.out.println(inputName + ": " + indAppearancesM + " occurrences in " + totalNamesM + " names (" + percent + "%)");
                    } else if (detectSex.equals("-f")) {
                        float percent = (float) indAppearancesF / (float) totalNamesF;
                        System.out.println(inputName + ": " + indAppearancesF + " occurrences in " + totalNamesF + " names (" + percent + "%)");
                    }
                    System.out.println("Position of " + inputName + " in the Linked List: " + entireList.findPosition(inputName));
                }else {//if name in list
                    System.out.println("Name " + inputName + " not listed");
                }
            }
            index += 1;//need to keep track of index to
        }
    }
}






