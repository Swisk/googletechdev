int[] sort(int[] a) {
  
  //floor division
  int half = (int) a.length/2;
  
  //create arrays, right will be longer if odd length
  int[] left = new int[half];
  int[] right = new int[a.length - half];
  
  //get slice of the arrays
  for (int i = 0; i < half; i++){
    left[i] = a[i];
  }
  
  for (int j = half; j < a.length; j++){
    right[j - half] = a[j];
  }
  
    //recursively sort
    if (left.length > 1){
      left = sort(left);
    }
    
    if (right.length > 1){
      right = sort(right);
    }
    
      //array to hold sorted values
    int[] returnArray = new int[left.length + right.length];
  
    //length of new array to create without duplicates
    int dedupLength = left.length + right.length;

    //combine the arrays
    int i = 0, j = 0, k = 0;
    
    while (i < left.length && j < right.length ){
      
      if (left[i] < right[j]){
        returnArray[k] = left[i];
        i++;
        k++;
      } else if (left[i] > right[j]) {
        returnArray[k] = right[j];
        j++;
        k++;
      } else {
        returnArray[k] = left[i];
        dedupLength--;
        i++;
        j++;
        k++;
      }
      
    }

    // add on the rest of the remaining mismatched array
    for (; i < left.length; i++, k++){
      returnArray[k] = left[i];
    }
    for (; j < right.length; j++, k++){
      returnArray[k] = right[j];
    }
    
    //transfer values into dedup array
    int[] dedupArray = new int[dedupLength];

    for (k = 0 ; k < dedupLength; k++){
      dedupArray[k] = returnArray[k];
    }

    

  
  return dedupArray;
}
