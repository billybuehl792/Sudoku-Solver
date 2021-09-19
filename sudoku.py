#!python3
# sudoku.py - solve sudoku puzzles

from math import sqrt

class Sudoku:
    
    def __init__(self, puzz):
        self.puzz = puzz
    
    @property
    def dim(self):
        dim = sqrt(len(self.puzz))
        if dim % 1 > 0:
            raise Exception('Puzzle board must be square!')
        
        return int(dim)

    @property
    def difficulty(self):
        given = 0
        for i in self.puzz:
            if i != 0:
                given += 1

        area = self.dim ** 2
        if given > .75 * area:
            return 'easy'
        elif given > .5 * area:
            return 'medium'
        elif given > .25 * area:
            return 'hard'
        else:
            return 'very hard'

    @property
    def given(self):
        given = []
        for i in range(len(self.puzz)):
            if self.puzz[i] != 0:
                given.append(i)
        
        return given

    def puzzle(self, solved=False):
        # return pretty string of puzzle
        # print solved puzzle
        if solved:
            puzz = self.solve()
        
        # no solutions
        if not puzz:
            return "Puzzle has no possible solutions!"

        string = ''
        x = 0
        for i in puzz:
            if x != 0 and x % self.dim == 0:
                string = string + '\n'
                x = 0
            
            string = string + f' {str(i)} '
            x += 1

        return string

    def row(self, pos):
        # return position row given index
        return pos // self.dim

    def column(self, pos):
        # return position column given index
        return pos % self.dim
    
    def row_items(self, pos, exclude=True):
        # return idexes of row items
        items = []
        for i in range(self.dim):
            items.append((self.row(pos) * self.dim) + i)
        
        # remove position
        if exclude:
            items.remove(pos)

        return items

    def column_items(self, pos, exclude=True):
        # return indexes of column items
        items = []
        for i in range(self.dim):
            items.append(self.column(pos) + (self.dim * i))
        
        # remove position
        if exclude:
            items.remove(pos)

        return items
    
    def square_items(self, pos, exclude=True):

        # check square of square
        sqr_dim = sqrt(self.dim)
        if sqr_dim % 1 > 0:
            raise Exception('Square root of puzzle must have square root!')
        else:
            sqr_dim = int(sqr_dim)
        
        items = []
        sqr_row = self.row(pos) // sqr_dim
        sqr_col = self.column(pos) // sqr_dim
        for i in range(sqr_dim):
            sqr_row = sqr_dim * (self.row(pos) // sqr_dim) + i
            for n in range(sqr_dim):
                sqr_col = sqr_dim * (self.column(pos) // sqr_dim) + n
                items.append(sqr_col + (self.dim * sqr_row))
        
        # remove position
        if exclude:
            items.remove(pos)

        return items

    def neighbors(self, pos, exclude=True):
        # items in same row, column, or square
        neighbors = []

        # add row items to neighbors
        for i in self.row_items(pos, exclude):
            if i not in neighbors:
                neighbors.append(i)

        # add column items to neighbors
        for i in self.column_items(pos, exclude):
            if i not in neighbors:
                neighbors.append(i)
        
        # add square items to neighbors
        for i in self.square_items(pos, exclude):
            if i not in neighbors:
                neighbors.append(i)
        
        return neighbors

    def solve(self, puzz=None, pos=0):
        # set puzzle
        if not puzz:
            puzz = self.puzz

        # base case > reached final position
        if pos == len(puzz):
            return puzz

        # position in given > next position
        if pos in self.given:
            return self.solve(puzz, pos+1)
        
        for _ in range(self.dim):
            puzz[pos] += 1

            items = []
            for p in self.neighbors(pos):
                items.append(puzz[p])
            
            if puzz[pos] not in items:
                solved = self.solve(puzz, pos+1)
                if solved:
                    return solved
                else:
                    continue

        puzz[pos] = 0
        return False

    def __repr__(self):
        return f'Puzzle({self.dim**2})'


if __name__ == '__main__':
    puzz = [
        0,0,0,0,0,7,0,3,4,
        0,3,0,0,0,0,0,0,6,
        0,0,4,6,0,8,0,0,0,
        0,9,0,0,1,0,5,0,0,
        0,0,5,2,0,6,3,0,0,
        0,0,2,0,4,0,0,7,0,
        0,0,0,8,0,9,1,0,2,
        9,0,0,0,0,0,0,5,0,
        6,8,0,3,0,0,0,0,0,
    ]
    #puzz = [7,0,0,0,4,0,0,2,1,0,4,2,0,0,3,0,5,0,6,0,5,0,9,0,0,0,3,8,2,0,0,0,1,0,7,4,0,0,6,0,0,0,8,0,0,4,7,0,9,0,0,0,6,5,1,0,0,0,6,0,5,0,2,0,3,0,4,0,0,6,9,0,5,6,0,0,2,0,0,0,8]

    puzz = Sudoku(puzz)
    print(puzz.puzzle(solved=True))
