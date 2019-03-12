//finding transpose of a matrix
class Solution {
    public int[][] transpose(int[][] A) {
        int rows = A[0].length;
		int columns = A.length;
		int [][] result = new int[columns][rows];
		
		for(int i = 0; i < rows; i++){
			for(int j = 0; j < columns; j++){
				
				result[j][i] = A[i][j];
				
			}
		}
		return result;
	}
    }
