/*
	 *Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly 
	 *four of the five integers. Then print the respective minimum and maximum values as a single line of two 
	 *space-separated long integers.
	 **/
	public void solution(int arr[]){
		long sum = 0;
		long min = Long.MAX_VALUE;
		long max = 0;
		
		for(int i = 0; i < arr.length; i++ ){
			if(arr[i] > max){
				max = arr[i];
			}
			if(arr[i] < min){
				min = arr[i];
			}
			sum = sum + arr[i];
		}
		
		System.out.println((sum - max) + " " + (sum - min));
	}
