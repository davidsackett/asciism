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
        d = Diagram('''ab
cd''')
        assert(list(d) == [(0, 0, 'a'), (0, 1, 'b'), (1, 0, 'c'), (1, 1, 'd')]) 

def test_points_eq():
    assert(Point(1,1) == Point(1,1))
    assert(Point(1,1) != Point(1,2))

def test_boxes_eq():
    assert(Box(Point(1,1), Point(2,2)) == Box(Point(1,1), Point(2,2)))
    assert(Box(Point(1,1), Point(2,3)) != Box(Point(1,1), Point(2,2)))

def test_parse_boxes():
    box = '''
    +---+
    |   |
    |   |
    +---+

'''
    diag = Diagram(box)
    print(diag)
    #boxes = diag.box
    #import pdb; pdb.set_trace()
    boxes = Box.parse(diag)
    assert(boxes == [Box(Point(1,5), Point(4, 9))])
