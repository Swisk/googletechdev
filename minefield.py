import random
import unittest
from tile import Tile

class Minefield:

    def __init__(self, n, m):

        #create minefield
        self.mine_array = [[Tile() for x in range(n)] for y in range(n)]
        self.size = n
        self.unopened = n * n - m
        self.end = False

        #generate random coordinates for each mine
        seen = set()

        #add mines
        while len(seen) < m:
            x, y = random.randint(0, n-1), random.randint(0, n-1)
            if (x, y) not in seen:
                seen.add((x, y))
                self.mine_array[x][y].mine()

        #calculate the number of neighbour mines each tile has
        for x in range(n):
            for y in range(n):
                
                mines = 0

                for x1, y1 in self.get_neighbours(x, y):
                    if self.mine_array[x1][y1].is_mined():
                        mines += 1

                self.mine_array[x][y].set_neighbours(mines)

    #get neighbours
    def get_neighbours(self, x, y):

        for i in [-1, 0 ,1]:
            for j in [-1, 0 ,1]:
                
                #filter out of bounds
                if x+i < self.size and x+i>=0 and y+j < self.size and y+j>=0:
                    
                    # filter out the case where on the same spot
                    if x+i != x or y+j != y:

                        #give the coordinates  back
                        yield x+i, y+j


    #need to open recursively
    def open(self, x, y):
        if self.end == True:
            return "game over"
        elif self.mine_array[x][y].is_open():
            return "already opened"
        elif self.mine_array[x][y].is_mined():
            self.end = True
            return "mined"
        else:
            self.mine_array[x][y].open()

            self.unopened -= 1

            if self.mine_array[x][y].num_neighbours() == 0:
                for x1, y1 in self.get_neighbours(x, y):
                    self.open(x1, y1)

            if self.unopened <= 0:
                self.end = True
                return "win"
        

    def render(self):
        output = []
        for x in range(self.size):
            col = []
            for y in range(self.size):
                if self.mine_array[x][y].is_open():
                    if self.mine_array[x][y].num_neighbours() > 0:
                        col.append( self.mine_array[x][y].num_neighbours())
                    else:
                        col.append(" ")
                else:
                    col.append("-")
            output.append(col)

        return output

class TestMinefield(unittest.TestCase):

    def setUp(self):
        random.seed(1234)
        self.Minefield = Minefield(5, 5)

    def testRender(self):
        self.assertEqual(self.Minefield.render(), [['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-']])

    def testOpen(self):
        self.assertEqual(self.Minefield.open(0, 4), None)
        self.assertEqual(self.Minefield.render(), [['-', '-', '-', 1, ' '], ['-', '-', 2, 1, ' '], ['-', '-', 1, ' ', ' '], ['-', 3, 1, ' ', ' '], ['-', 2, ' ', ' ', ' ']])
        self.assertEqual(self.Minefield.open(0, 3), "already opened")

    def testLose(self):
        self.assertEqual(self.Minefield.open(0, 0), "mined")
        self.assertEqual(self.Minefield.open(0, 0), "game over")
        self.assertEqual(self.Minefield.open(0, 4), "game over")
        self.assertEqual(self.Minefield.render(), [['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-']])

    def testWin(self):
        self.Minefield.open(0, 4)
        self.Minefield.open(0, 1)
        self.Minefield.open(1, 0)
        self.Minefield.open(1, 1)
        self.assertEqual(self.Minefield.open(2, 0), "win")
        self.assertEqual(self.Minefield.open(2, 0), "game over")

        self.assertEqual(self.Minefield.render(), [['-', 2, '-', 1, ' '], [2, 3, 2, 1, ' '], [2, '-', 1, ' ', ' '], ['-', 3, 1, ' ', ' '], ['-', 2, ' ', ' ', ' ']])

        
        


if __name__ == '__main__':
    unittest.main()