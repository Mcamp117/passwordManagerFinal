

public class ChangeText {
    public static String ToTitle() {
            if (text == null || text.isEmpty()) {       //if there is nothing in the parenthesis ()
                return text;                            //return nothing 
            }
        
            StringBuilder converted = new StringBuilder();  //like a list but it creates a string without all the brackets and commas
        
            boolean convertNext = true;
            for (char ch : text.toCharArray()) {
                if (Character.isSpaceChar(ch)) {        //if there is a space before the first actuall character
                    convertNext = true;
                } else if (convertNext) {               //once it gets to the first letter character
                    ch = Character.toTitleCase(ch);     //convert it to a Capital letter
                    convertNext = false;
                } else {                                //the rest of the text
                    ch = Character.toLowerCase(ch);     //make everything after the first letter Lowercase even if it is Uppercase
                }
                converted.append(ch);                   //creates the modified string
            }
        
            return converted.toString();                //function returns converted string
    }
}