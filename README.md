=======
asciism
=======

Python library for implementing state machines using ascii art

# Ascii state machines

This library aims to allow Python classes to implement state machines by 
drawing the state machine as Ascii art in the class's doc string.

The examples directory will shows how the library should be used. The current
examples are incomplete and not representative of how the library aims to work.

## Tests

Run the tests with:

    env PYTHONPATH=. nosetests -d

To run with ability to debug in pdb:

    env PYTHONPATH=. nosetests -d -s
