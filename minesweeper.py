import random
import unittest

#TODO need to create exception handling if the n and m are not valid

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
            row = []
            for y in range(self.size):
                if self.mine_array[x][y].is_open():
                    if self.mine_array[x][y].num_neighbours() > 0:
                        row.append( self.mine_array[x][y].num_neighbours())
                    else:
                        row.append(" ")
                else:
                    row.append("-")
            output.append(row)

        return output

class Tile:

    def __init__(self):
        
        #variables required as a mine
        self._is_mine = False
        self._neighbour_mines = 0
        self._is_open = False

    def set_neighbours(self, n):
        self._neighbour_mines = n

    def open(self):
        self._is_open = True

    def mine(self):
        self._is_mine = True

    def is_mined(self):
        return self._is_mine

    def is_open(self):
        return self._is_open

    def num_neighbours(self):
        return self._neighbour_mines

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

class TestTile(unittest.TestCase):

    def setUp(self):
        self.Tile = Tile()
    
    def testDefault(self):
        self.assertEqual(self.Tile.is_mined(), False)
        self.assertEqual(self.Tile.is_open(), False)
        self.assertEqual(self.Tile.num_neighbours(), 0)


    def testSetMethods(self):
        self.Tile.open()
        self.Tile.mine()
        self.Tile.set_neighbours(2)

        self.assertEqual(self.Tile.is_mined(), True)
        self.assertEqual(self.Tile.is_open(), True)
        self.assertEqual(self.Tile.num_neighbours(), 2)



class TestMinesweeper(unittest.TestCase):

    def setUp(self):
        self.Minesweeper = minesweeper()
    
    def testDefault(self):
        pass

    def testRender(self):
        self.Minesweeper.render()


class minesweeper:

    def __init__(self):

        while True:
            try:
                n = input("Size of board? ")
                m = input("Number of mines? ")
                n = int(n)
                m = int(m)
                self.minefield = Minefield(n, m)
                break
            except:
                print("ha ha. Answer the question properly.")
                pass

        

    def play(self, n, m):
        pass


    def render(self):
        
        to_print = self.minefield.render()
        print("")
        for rows in to_print:
            print("|", end = "")
            for cell in rows:
                print(cell, end = '|')
            print("")


if __name__ == '__main__':
    unittest.main()