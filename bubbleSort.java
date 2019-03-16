
public class algorithm {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int arr[][] = {{10,1}, {7,2}, {8,2},{9,1}, {1,10},{2,5},{1,7}}; 
        bubbleSort(arr); 
        System.out.println("sorted array"); 
        printArray(arr);  
		
	} 
	
	 static void bubbleSort(int arr[][]) 
	    { 
	        int n = arr.length; 
	        for (int i = 0; i < n-1; i++) 
	            for (int j = 0; j < n-i-1; j++) 
	                if (arr[j][0] <= arr[j+1][0]) 
	                { 
	                	if (arr[j][0] == arr[j+1][0]) {
	                		if (arr[j][1] >= arr[j+1][1]) {
	                			// swap arr[j+1] and arr[i] 
	    	                    int[] temp = arr[j]; 
	    	                    arr[j] = arr[j+1]; 
	    	                    arr[j+1] = temp;
	                		}
	                	}else {
	                		// swap arr[j+1] and arr[i] 
		                    int[] temp = arr[j]; 
		                    arr[j] = arr[j+1]; 
		                    arr[j+1] = temp; 
	                	}
	                } 
	    } 
    
    static void printArray(int[][] arr) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) {
        	for(int j = 0; j < 2; j++) {
        		System.out.print(arr[i][j]+" ");
        	}
        System.out.print("|");
        }
            
        System.out.println(); 
    } 
	

}
