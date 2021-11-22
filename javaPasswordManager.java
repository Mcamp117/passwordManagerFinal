import java.util.Random;
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class javaPasswordManager {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random rand = new Random();
        
        ArrayList <Boolean> reqCheckList = new ArrayList<Boolean>();
        ArrayList <Integer> specialCharacters = new ArrayList<Integer>();
        ArrayList <String> passwordList = new ArrayList<String>();

        int loginTries = 5;

        ArrayList <String> category = new ArrayList<String>();
        category.add("home");
        category.add("work");
        category.add("entertainment");
        category.add("bills");

        randomizer();

    }

    private static void randomizer() {
        Scanner sc = new Scanner(System.in);
        Random rand = new Random();
        ArrayList <String> ui = new ArrayList<String>();
        
        //User says how many Cap & Low Letters, Nums, and Syms
        System.out.println("Input Number of Capital Letters: ");
        int  capitalLetterInput = sc.nextInt();
        System.out.println("Input Number of Lowercase Letters: ");
        int  lowerLetterInput = sc.nextInt();
        System.out.println("Input Number of Numbers: ");
        int  numberInput = sc.nextInt();
        System.out.println("Input Number of Symbols: ");
        int  symbolInput = sc.nextInt();
        String password = "";

        //adds random items to the final output
        for ( int count=0; count<capitalLetterInput; count++) {
            password += (char)getRandInt(65,91);
        }

        for ( int count=0; count<lowerLetterInput; count++) {
            password += (char)getRandInt(97,122);
        }

        for ( int count=0; count<numberInput; count++) {
            password += (char)getRandInt(48, 57);
        }

        int special = 0;
        String symbolsDigit = "";
        while (!(symbolInput == 0)) {
            special = getRandInt(33,64);
            if ((special == 33) || (special == 35) || (special == 36) || (special == 37) || (special == 38) || (special == 40) || (special == 41) || (special == 42) || (special == 64)) {
                password += (char) special;
                symbolInput -= 1;
            }
        }
        System.out.println(password);
        // ui.addAll(1, password);
    }



    private static void printArray(int[] listy){
        for (int i=0; i<listy.length;i++){
            System.out.println(listy[i]);
        }
    }
    
    private static void printArray(double[] listy){
        for (int i=0; i<listy.length;i++){
            System.out.print(listy[i]);
        }
    }
    
    private static void printArray(String[] listy){
        for (int i=0; i<listy.length;i++){
            System.out.print(listy[i]);
        }
    }
    
    private static void printArray(boolean[] listy){
        for (int i=0; i<listy.length;i++){
            System.out.print(listy[i]);
        }
    }

    private static int getRandInt(int minimum, int maximum){
        return ((int) (Math.random()*(maximum - minimum))) + minimum;
    }
}
