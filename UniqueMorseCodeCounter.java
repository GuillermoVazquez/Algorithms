/*International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is given below:
[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.
Return the number of different transformations among all words we have.
Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.". */

class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        String[] morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];
        String[] morseTotal;
        int count = 0;
        //parse the words array
        for(int i = 0; i < words.length; i++){
            //get a single word
            String word = words[i];
            //build the morse code word
            String build = "";
            for(int length = 0; length < words[i].length(); length++){
                //lets map the character to morse code 
                char c = word.charAt(length); 
                int numericValue = ((int) c) - 97;
                //get the morse code for that letter
                String m = morse[numericValue];
                build = build + m; 
            }
            //the morse code for the current word has now been built and is in build
            //store the morse code in an array
            morseTotal.append(build); 
        }
        
        //now we have to count the unique morse code words
        for(int x = 0; x < morseTotal.length; x++){
            for(int y = 1; y < morseTotal.length; y++){
            if(morse[x] == morse[y]){
                count++;
            }
        }
        }
        
        return count;
    }
}
