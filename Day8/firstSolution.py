from dataclasses import dataclass

INPUT_FILE = 'input.txt'

def input_data():
    with open(INPUT_FILE,'r') as f:
        data=f.read().splitlines()
    return [[int(x) for x in row] for row in data]

@dataclass
class Point:
    x: int
    y: int

class Grid:
    def __init__(self,grid_rows):
        self.rows = grid_rows
        self.columns = list(zip(*self.rows))
        self.width = len(self.columns)
        self.height = len(self.rows)
        self.size = self.width * self.height

    def height_at_point(self,point):
        return self.rows[point.y][point.x]

    def is_visible(self,point):
        if point.x==0 or point.x==self.width-1:
            return True
        if point.y==0 or point.y==self.height-1:
            return True

        value = self.height_at_point(point)
        if value > max(self.rows[point.y][0:point.x]):
            return True
        if value > max(self.rows[point.y][point.x+1:]):
            return True

        if value > max(self.columns[point.x][0:point.y]):
            return True
        if value > max(self.columns[point.x][point.y+1:]):
            return True

        return False

    def get_hidden_trees(self):
        return [Point(x,y) for x in range(self.height)
                           for y in range(self.width)
                           if not self.is_visible(Point(x,y))]

if __name__ == '__main__':
    rows = input_data()
    forest = Grid(rows)
    hidden_trees = forest.get_hidden_trees()
    print(f'Number of visible trees: {forest.size - len(hidden_trees)}') #1803

