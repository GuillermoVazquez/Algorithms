/*
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
Example 1:
Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:
Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
*/

//guillermovazquez
//solution
class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        //rows
        int rows = A.length;
        //columns
        int columns = A[0].length;
        
        //flip the image
        //reverse elements of array
        for(int row = 0; row < rows; row++){
        	for(int column = 0, last = columns -1; column < columns/2; column++, last--){
        		//switch the elements
        		int temp = A[row][column];
        		A[row][column] = A[row][last];
        		A[row][last] = temp;
        	}
        }
        
        //invert elements of array
        for(int row = 0; row < rows; row++){
        	for(int column = 0; column < columns; column++){
        		//invert elements
        		if(A[row][column] == 0){
        			A[row][column] = 1;
        		}
        		else{
        			A[row][column] = 0;
        		}
        	}
        }
        return A;
    }
}
