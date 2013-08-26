'''
Parses the elements of an ascii art state machine diagram
'''

#Point = namedtuple('Point', ['x', 'y'])
#Box = namedtuple('Box', ['x', 'y'])

class Point:
    '''represents a point using x and y coordinates'''
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def __eq__(self, other):
        return (self.x == other.x and 
                self.y == other.y and
                self.value == other.value)

    def __repr__(self):
        return 'Point({}, {}, {})'.format(self.x, self.y, self.value)

class Box:
    '''represents a box using two points'''
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    @classmethod
    def parse(cls, diagram):
        '''returns all the Boxes in the given diagram'''
        # TODO parse more efficiently. Could follow edge from first '+'

        # search for '+' and determine if top left or botton right
        candidates = [p for p in diagram if p.value == '+']

        # check if '+' is part of a top left corner:
        # +-
        # | 
        top_left_candidates = [
            p for p in candidates
                if (diagram[p.x+1, p.y].value == '-' and 
                    diagram[p.x, p.y+1].value == '|')]
                    

        # check if '+' is part of a bottom right corner:
        #  |
        # -+ 
        bottom_right_candidates = [
            p for p in candidates
                if (diagram[p.x-1, p.y].value == '-' and 
                    diagram[p.x, p.y-1].value == '|')]

        #print(candidates)
        #print(top_left_candidates)
        #print(bottom_right_candidates)

        # try all combination of top right and bottom left corners to see if
        # the sides are unbroken
        boxes = []
        for top_left_candidate in top_left_candidates:
            for bottom_right_candidate in bottom_right_candidates:
                if cls.closed_box(top_left_candidate, 
                                  bottom_right_candidate, diagram):
                    boxes.append(Box(top_left_candidate, 
                                     bottom_right_candidate))

        return boxes

    @classmethod
    def closed_box(cls, top_left, bottom_right, diagram):
        '''returns true if the two points form the corners of a closed box'''
        # check top edge
        for p in diagram[top_left.x+1:bottom_right.x, top_left.y]:
            if p.value != '-':
                return False

        # check bottom edge
        for p in diagram[top_left.x+1:bottom_right.x, bottom_right.y]:
            if p.value != '-':
                return False

        # check left edge
        for p in diagram[top_left.x, top_left.y+1:bottom_right.y]:
            if p.value != '|':
                return False

        # check right edge
        for p in diagram[bottom_right.x, top_left.y+1:bottom_right.y]:
            if p.value != '|':
                return False

        return True

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
        # TODO __iter__ should use __getitem__
        for y, row in enumerate(self.canvas):
            for x, col in enumerate(row):
                yield self[x, y]

    def __getitem__(self, val):
        x_slice, y_slice = val
        try:
            # return a single point if indexed with ints
            if (type(x_slice) == int and
                type(y_slice) == int):
                return Point(x_slice, y_slice, self.canvas[y_slice][x_slice])

            ps = []
            if type(x_slice) == int:
                x_slice = slice(x_slice, x_slice+1)
            if type(y_slice) == int:
                y_slice = slice(y_slice, y_slice+1)

            for y in range(len(self.canvas))[y_slice]:
                for x in range(len(self.canvas[y]))[x_slice]:
                    #print('x:{}, y:{}, canvas:{}'.format(x, y, self.canvas[y][x]))
                    ps.append(Point(x, y, self.canvas[y][x]))
            return ps
        except IndexError:
            # lots of tests are done against adjacent points so we return None
            # rather than IndexError to avoid lots of catching the exception
            # TODO how to gracefully handle IndexErrors? Just return None?
            return Point(None, None, None)

