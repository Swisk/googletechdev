#helper function to test if word is a subsequence
def check_subsequence(word, string):
    
    #set the original starting position of the search to the start of the string
    pos = 0

    for letter in word:
        #find the position of the first occurence of each letter, increasing the starting point to ensure letters are arranged in the correct oredr 
        pos = string.find(letter, pos)    

        #if at some point the sequence of letters breaks, it is not possible to create the word given that string
        if pos == -1:
            return False

    #return true if there are these letters arranged in the correct order
    return True

    
    
def main(word_list, string):
    
    #sort strings assuming the input is unordered
    word_list = list(word_list)
    word_list.sort(key=len, reverse=True)

    #test the words in order, and return the first match (which should be the longest)
    for word in word_list:
        if check_subsequence(word, string):
            return word



#testing
S = "abppplee"
D = {"able", "ale", "apple", "bale", "kangaroo"}

assert check_subsequence("finger", "finrst") == False
assert check_subsequence("finger", "frtrstriftrstngernrst") == True
assert main(D, S) == "apple"
