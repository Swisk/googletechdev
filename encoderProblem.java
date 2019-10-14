public String[] encoder(String[] raw, String[] code_words) {
  
  Map <String, String> returnMap = new HashMap <String, String>();
  String[] returnString = new String[raw.length];
  int j = 0;
  
  for (int i = 0; i < raw.length; i++){
    
    if (!returnMap.containsKey(raw[i])) {
      returnMap.put(raw[i], code_words[j]);
      returnString[i] = code_words[j];
      j++;
    } else {
      returnString[i] = returnMap.get(raw[i]);
    }
    
  }
  
  return returnString;
  
}
