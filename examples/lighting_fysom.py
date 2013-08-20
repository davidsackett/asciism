#!/usr/bin/env python3
'''State machine for lighting
'''
from fysom import Fysom

class Lights:
    '''A state machine to control lighting

    # Ascii art diagram

        +-+
        +++
         | /lights=False
         |
         v     tr(switch)
    +--------+ /lights=True  +--------+
    |        +-------------->|        |
    | Lights |               | Lights |
    | off    |               | on     |
    |        |<--------------+        |
    +--------+ tr(switch)    +--------+
               /lights=False

    # API for interacting with state machine class

    class Lights(AsciiSm):
        switch

    # Desired output from parser

    states = ['Lights off', 'Lights on']
    transitions = [{'default': True, 'dst': 'Lights off', 
                    'action': 'lights=False'},
                   {'src': 'Lights off', 'dst': 'Lights on',
                    'event': 'tr(switch)', 'action': 'lights=True'},
                   {'src': 'Lights on', 'dst': 'Lights off',
                    'event': 'tr(switch)', 'action': 'lights=False'}]



    '''
    def __init__(self):
        self.switch = False
        self.sm = Fysom({
            'initial': 'Lights off',
            'events': [
                {'name': 'toggle', 'src': 'lights_off', 'dst': 'lights_on'},
                {'name': 'toggle', 'src': 'lights_on', 'dst': 'lights_off'}],
            'callbacks': {
                'on_Lights_on': self.lights_on,
                'on_Lights_off': self.lights_off,
            }
        })

    @property 
    def switch(self):
        return self.switch

    @switch.setter
    def switch(self, value):
        '''State machine input'''
        print('Lights set to %d' % value)
        if not self.switch and value:
            self.sm.toggle()
        elif self.switch and not value:
            self.sm.toggle()

        self.switch = value

    def lights_on(self):
        self.lights(True)

    def lights_off(self):
        self.lights(False)

    def lights(self, value):
        '''State machine output'''
        print('Lights set to %d' % value)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    living_room = Lights()

    print(living_room.sm.current)

    # lights on
    living_room.switch = True
    living_room.switch = False

    # lights off
    living_room.switch = True
    living_room.switch = False

