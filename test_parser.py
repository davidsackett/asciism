from unittest import TestCase

from parser import *

class TestParser(TestCase):
    def test_diag(self):
        a = ''
        with self.assertRaises(ValueError):
            d = Diagram(a) 

        a = 'a'
        d = Diagram(a) 
        assert(d.canvas == ['a'])

        a = '''\
a
b'''
        d = Diagram(a) 
        assert(d.canvas == ['a', 'b'])
     
        a = '''ab
cd'''
        d = Diagram(a) 
        assert(d.canvas == ['ab', 'cd'])

    def test_diag_iter(self):
        d1 = Diagram('''ab
cd''')
        assert(list(d1) == [Point(0, 0, 'a'), Point(1, 0, 'b'), 
                            Point(0, 1, 'c'), Point(1, 1, 'd')]) 

        # test that indexing matches iter
        for p in d1:
            assert(p == d1[p.x, p.y])

    def test_diag_slice(self):
        d = Diagram('''abc
def
ghi''')
        assert(list(d[:,0]) == [Point(0, 0, 'a'), Point(1, 0, 'b'), 
                                Point(2, 0, 'c')])
        assert(list(d[1:2,0]) == [Point(1, 0, 'b')])
        assert(list(d[0,:]) == [Point(0, 0, 'a'), Point(0, 1, 'd'), 
                                Point(0, 2, 'g')])
        assert(list(d[0,1:2]) == [Point(0, 1, 'd')])

def test_points_eq():
    assert(Point(1, 1, 'a') == Point(1, 1, 'a'))
    assert(Point(1, 1, 'a') != Point(1, 2, 'a'))

def test_boxes_eq():
    assert(Box(Point(1,1, 'a'), Point(2,2, 'a'))
           == Box(Point(1,1, 'a'), Point(2,2, 'a')))
    assert(Box(Point(1,1, 'a'), Point(2,3, 'a')) 
           != Box(Point(1,1, 'a'), Point(2,2, 'a')))

def test_parse_boxes():
    # complete box
    box = '''
    +---+
    |   |
    |   |
    +---+

'''
    diag = Diagram(box)
    boxes = Box.parse(diag)
    assert(boxes == [Box(Point(4,1, '+'), Point(8, 4, '+'))])

    # broken box
    box = '''
    +- -+
    |   |
    |   |
    +---+

'''
    diag = Diagram(box)
    assert([] == Box.parse(diag))

    box = '''
    +---+
    |    
    |   |
    +---+

'''
    diag = Diagram(box)
    assert([] == Box.parse(diag))

def xtest_parses_diagram_with_uneven_rows():
    # TODO parse diagram with uneven rows see below. The second row of box is
    # one character shorter than the other rows
    # broken box
    box = '''
    +---+
    |   
    |   |
    +---+

'''
    diag = Diagram(box)
    assert([] == Box.parse(diag))

