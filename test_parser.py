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
        assert(list(d1) == [(0, 0, 'a'), (1, 0, 'b'), (0, 1, 'c'), (1, 1, 'd')]) 

        # test that indexing matches iter
        for x, y, p in d1:
            print(x, y, p, d1[x, y])
            assert(p == d1[x, y])
        

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
    boxes = Box.parse(diag)
    assert(boxes == [Box(Point(1,5), Point(4, 9))])
