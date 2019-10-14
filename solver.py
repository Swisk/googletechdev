import sys, random, string


class Solver():

    def __init__(self):
        self.remaining_guesses = 6
        self.unguessed_char = "etaoinsrhdjucmfywgpbvkxqjz"
        self.toguess = 0
        self.prev_input = ""

    def guess(self):
        #algo for making guesses
        guess_char = self.unguessed_char[self.toguess]
        print(guess_char, flush=True)

        #remove guessed char from unguessed
        self.unguessed_char = self.unguessed_char.replace(guess_char, '')
        
        return 0

    def reset(self):
        
        self.__init__()
        
        return 0

    def parse(self, data):
        
        #TODO: change because now reading as input instead of lines

        if data == "END":
            sys.exit() 

        elif data == self.prev_input:
            #implying guessed wrongly
            self.remaining_guesses -= 1

            
            if self.remaining_guesses <= 0:
                #new word le
                self.reset()

                #reset loop also
                return 0  
        else:
            #guessed correctly, life carries on
            pass

        self.guess()

        self.prev_input = data

    def solve(self):

        while True:
            
            #readlines
            data = input()

            #parse input to decide what to do next
            self.parse(data)




            


#run the solver
task = Solver()
task.solve()




