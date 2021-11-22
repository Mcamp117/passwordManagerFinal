import java.util.Random;
import java.util.Scanner;

public class javaPasswordManager {
    public static void main(String[] args) {
        
        ArrayList <Boolean> reqCheckList = new ArrayList<Boolean>();
        ArrayList <Integer> specialCharacters = new ArrayList<Integer>();
        ArrayList <String> passwordList = new ArrayList<String>();
        char[] lowerAlphabet = "abcdefghijklmnopqrstuvwxyz".toCharArray();
        char[] upperAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".toCharArray();
        char[] symbols = "!\"#$%'()*".toCharArray();
    }

    private static void randomizer() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Input Number of Capital Letters: ");
        int  capitalLetterInput = sc.nextInt();
        System.out.println("Input Number of Lowercase Letters: ");
        int  lowerLetterInput = sc.nextInt();
        System.out.println("Input Number of Numbers: ");
        int  numberInput = sc.nextInt();
        System.out.println("Input Number of Symbols: ");
        int  symbolInput = sc.nextInt();
        String letterDigit = "";
        //adds random items to the final output
        for ( int count=0; count<capitalLetterInput; count++) {
            letterDigit += 
        }

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

}
