
public class algorithm {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//print ascending pyramid
		//last level should have five symbols
		for(int i = 0; i < 6; i++) {
			printX(i);
		}
		
	}
	
	public static void printX(int amount) {
		for(int i = 0; i < amount; i++) {
			System.out.print("5");
		}
		System.out.println();
	}
}
