import unittest

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



class TestTile(unittest.TestCase):

    def setUp(self):
        self.Tile = Tile()
    
    def default(self):
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




if __name__ == '__main__':
    unittest.main()