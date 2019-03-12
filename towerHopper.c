#include <stdio.h>
int towerHopper(int[],int,int);
//this algorithm will solve the tower hopper problem

//problem:
//given an array of integer values determine if it is possible to exit the array on the basis that
//the number of index slots you can "hopp" is determined by the value your current index holds

//input: integer array
//output: 1 if possible 0 if not possible
int main(int argc, char const *argv[]) {
  //example positive array
  int array[] = {2,0,1,3,0,0};
  int array1[] = {2,0,0,0,0,0};
  int length = sizeof(array)/sizeof(array[0]);
  int posReturnValue = towerHopper(array,length,length - 1);
  int negReturnVaule = towerHopper(array1,length,length - 1);
  printf("positive = %d\n", posReturnValue );
  printf("negative = %d\n", negReturnVaule );


  return 0;
}


//the algorithm will return an integer
//hopping is possible 1
//hopping is not possible 0
//array will hold the array being analyzed
//base is the point in the array ( or out of it if in the inital step ) that we are looking to jump
//to.base should be length when calling towerHopper()
//compare is the moving point in the array that will be compare to steps
int towerHopper(int array[], int base, int compare){
  int steps = 1;
  if(base == 0){
    return 1;
  }
  while( compare >= 0 ){
    if(array[compare] >= steps){
      return towerHopper(array,compare,compare - 1);
    }else{
      if(compare == 0){
        return 0;
      }
      else{
        steps++;
        compare--;
      }
    }
  }

}
