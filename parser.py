'''
Parses the elements of an ascii art state machine diagram
'''

#Point = namedtuple('Point', ['x', 'y'])
#Box = namedtuple('Box', ['x', 'y'])

class Point:
    '''represents a point using x and y coordinates'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x == other.x and 
                self.y == other.y)

    def __repr__(self):
        return 'Point({}, {}'.format(self.x, self.y)

class Box:
    '''represents a box using two points'''
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    @classmethod
    def parse(cls, diagram):
        '''returns all the Boxes in the given diagram'''

        # search for '+' and determine if top left or botton right
        # +- or  |
        # |     -+

        candidates = [(x, y, p) for x, y, p in diagram if p == '+']

        top_right_candidates = [
            (x, y, p) for x, y, p in candidates
                if (diagram[x+1, y] == '-' and 
                    diagram[x, y+1] == '|')]
                    
        bottom_right_candidates = [
            (x, y, p) for x, y, p in candidates
                if (diagram[x-1, y] == '-' and 
                    diagram[x, y-1] == '|')]

        # try all combination of top right and bottom left corners to see if
        # the sides are unbroken
        print(candidates)
        print(top_right_candidates)
        print(bottom_right_candidates)


        #return [cls(Point(1,5), Point(4,9))]

    def __eq__(self, other):
        return (self.top_left == other.top_left and 
                self.bottom_right == other.bottom_right)

class Diagram:
    '''represents a complete ascii art diagram'''
    def __init__(self, ascii_art):
        if not ascii_art:
            raise ValueError('ascii art cannot be empty string')
        self.canvas = [row for row in ascii_art.split('\n')]

        # parse boxes
        #self.boxes = Box.parse(self)

    def __str__(self):
        return '\n'.join(self.canvas)

    def __iter__(self):
        for y, row in enumerate(self.canvas):
            for x, col in enumerate(row):
                yield x, y, col

    def __getitem__(self, val):
        x, y = val
        # lots of tests are done against adjacent points so we return None
        # rather than IndexError to avoid lots of catching the exception
        # TODO how to gracefully handle IndexErrors? Just return None?
        try:
            return self.canvas[x][y]
        except IndexError:
            return None
