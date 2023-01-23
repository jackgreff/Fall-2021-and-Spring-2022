/**
 *Jack Greff
 * Lab 2
 * 2/20/22
 * NOTE: I could not find a place to use TRY/CATCH. If I could find a place I would, but there was no necessary place to use it
 */

//import propublica.datadesign.Defendant;

import com.opencsv.CSVReaderHeaderAware;
import com.opencsv.exceptions.CsvException;

import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

/**
 *Main class and main method convert the csv file into an an array of string lists, and then puts that into defendant data, which can then read and print table
 */
public class Main {
    public static void main( String[] args ) throws CsvException, IOException{//add throws to avoid certain exceptions
        CSVReaderHeaderAware reader = new CSVReaderHeaderAware(new FileReader("compas-scores.csv")); //read csv
        ArrayList<String[]> myEntries = new ArrayList<String[]>(reader.readAll());//add csv into string list array
        reader.close();

        DefendantsData myDefendants = new DefendantsData(myEntries);//creates defendants
        myDefendants.readData();//does calculations
        myDefendants.printTable();//shows calculations
      }

}
