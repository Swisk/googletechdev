public String collapseDuplicates(String a) { 
  
  
  String result = ""; 
  char ch = a.charAt(0);
  result += Character.toString(ch); 
  
  for (int i = 1; i < a.length(); i++){
    
    
    if (a.charAt(i) == ch) { 
      i++; 
      
    } else {
      ch = a.charAt(i); 
      result += Character.toString(ch); 
    }
    
    
  }

  return result; 
  
}
