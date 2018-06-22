//guillermovazquez
//this algorithm parses through an array of strings and displays the strings that do not contain userInput string

public static void main(String[] args) {
		//task #1
		//"Does not contain"
		//example::: 
		//does not contain: "ll"
		//example data set
		String[] data = {"hello","hi","how","are","you"};
		
		String userInput = "ll";
		//get length of user input
		int length = userInput.length();
		
		//parse through the data set
		for(int i = 0; i < data.length; i++){
			//parse through individual strings
			for(int y = 0, to = length; y < data[i].length() && to <= data[i].length(); y++,to++){
				//get the substring of current stirng
				String sub = data[i].substring( y , to );
				if(!(userInput.equals(sub))){
					System.out.println(data[i]);
				}
			}
		}
		
	}
