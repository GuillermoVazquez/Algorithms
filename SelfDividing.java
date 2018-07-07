/*A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.*/

//guillermovazquez
class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
            
        //first create a list of integers
       List<Integer> list = new ArrayList<Integer>();
       
       //parse through given ints
       for(int i = left; i <= right; i++){
           //split number by digits
           int number = i;
           int alertFlag = 0;
           while(number > 0){
               int result = number % 10;
               if((result == 0) || (i % result != 0 ) ){
                   alertFlag = 1;
               }
               number = number / 10;
           }
           if(alertFlag != 1){
               list.add(i);
           }
       }
        return list;
        
    }
}
