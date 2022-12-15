from dataclasses import dataclass
import math

INPUT_FILE = 'input.txt'

#imports data from the file, returns it as a 2D with each item containing a row of the forest
#each sublist contains each individual tree in the row represented as an integer
def input_data():
    with open(INPUT_FILE,'r') as f:
        data=f.read().splitlines()
    return [[int(x) for x in row] for row in data]

#Point dataclass, works in conjunction with the grid class; stores the X and Y coordinates of a tree in the forest
@dataclass
class Point:
    x: int
    y: int

#Grid class, represents the entire forest; accepts one argument, which is the rows of the forest, represented as a 2D list
class Grid:
    def __init__(self,grid_rows):
        self.rows = grid_rows
        #This takes the self-evident self.rows variable and creates the subsequent columns
        self.columns = list(zip(*self.rows))
        self.width = len(self.columns)
        self.height = len(self.rows)
        self.size = self.width * self.height
    
    #This is a helper function that captures the value at a specific point
    def height_at_point(self,point):
        return self.rows[point.y][point.x]
    
    #This function returns whether the tree at a specific point should be visible, based on the rules of the problem
    def is_visible(self,point):
        #these 2 if statments determine if the tree is on the edge of the forest (every tree on the edge is visible)
        if point.x==0 or point.x==self.width-1:
            return True
        if point.y==0 or point.y==self.height-1:
            return True
        
        #if the tree is not on the edge, we need to compare it to other trees around it to determine visibility
        #it must be taller than every tree between it and one edge of the forest either horizontally or vertically
        value = self.height_at_point(point)
        #these 2 if statments test horizontally
        if value > max(self.rows[point.y][0:point.x]):
            return True
        if value > max(self.rows[point.y][point.x+1:]):
            return True

        #these 2 if statments test vertically
        if value > max(self.columns[point.x][0:point.y]):
            return True
        if value > max(self.columns[point.x][point.y+1:]):
            return True
        
        #if none of the if statements are tripped, the tree is not visible, return False
        return False

    #this function calculates the total number of hidden trees; needed for part 1
    def get_hidden_trees(self):
        #list comprehension that finds every x,y point which evaluates to True in the is_visible function
        return [Point(x,y) for x in range(self.height)
                           for y in range(self.width)
                           if not self.is_visible(Point(x,y))]

    #this function accepts one argument, which is a point, and returns the scenic score of the point
    #the scenic score is calculated by taking the # of visible trees in all 4 cardinal directions
    #and multiplying them
    def get_scenic_score_for_point(self,point):
        tree_height = self.height_at_point(point)

        #these generators create a list of all the trees in the respective direction
        #with regards to the tree we are finding the scenic score for
        left = (x for x in reversed(self.rows[point.y][0:point.x]))
        right = (x for x in self.rows[point.y][point.x+1:])
        up =  (y for y in reversed(self.columns[point.x][0:point.y]))
        down = (y for y in self.columns[point.x][point.y+1:])

        #loops over all of the generators created previously, then iterates over each value within
        #increments view distance until a taller tree is encountered, then breaks the loop
        view_distance = []
        for direction in (left,right,up,down):
            distance = 0
            for value in direction:
                if value < tree_height:
                    distance+=1
                else:
                    distance+=1
                    break
            view_distance.append(distance)
        return math.prod(view_distance)

    #this function leverages the get_scenic_score_for_point helper function to find the scenic score
    #of every point in our forest; finding the max of the result yields the answer to part 2
    def get_scenic_scores(self):
        scenic_scores = []
        for y in range(self.width):
            for x in range(self.height):
                point = Point(x,y)
                score = self.get_scenic_score_for_point(point)
                scenic_scores.append(score)
        return scenic_scores



if __name__ == '__main__':
    rows = input_data()
    forest = Grid(rows)
    #hidden_trees = forest.get_hidden_trees()
    scenic_scores = forest.get_scenic_scores()
    print(f'The best treehouse candidate has a scenic score of {max(scenic_scores)}') #268912
