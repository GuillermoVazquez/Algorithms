int[] array = new int[] {3,2,1,6,0,5};
		
		//this algorithm sorts an array on either side of its max
    
    int max = 0;
		int place = 0;
				
		for( int i = 0; i < array.length; i++){
			if(array[i] > max){
				max = array[i];
				place = i;
			}
		}
		
		int sorted = place;
		int j = 0;
		while(sorted >= 0){
			while( (j + 1 < place) && (array[j] > array[j+1]) ){
				int temp = array[j+1];
				array[j+1] = array[j];
				array[j] = temp;
				j++;
			}
			j = 0;
			sorted--;
		}
		
		sorted = array.length - place - 1;
		j = place + 1;
		while(sorted >= 0){
			while( (j + 1 < array.length) && (array[j] > array[j+1]) ){
				int temp = array[j+1];
				array[j+1] = array[j];
				array[j] = temp;
				j++;
			}
			j = place + 1;
			sorted--;
		}
		
		for(int x = 0; x < array.length; x++){
			System.out.println(array[x]);
		}
