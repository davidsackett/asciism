#!/usr/bin/env python3
'''State machine for lighting
'''

class Lights:
    '''A state machine to control lighting

        +-+
        +++
         | /lights=0
         |
         v     tr(switch)
    +--------+ /lights=True  +--------+
    |        +-------------->|        |
    | Lights |               | Lights |
    | off    |               | on     |
    |        |<--------------+        |
    +--------+ tr(switch)    +--------+
               /lights=False

    '''
    # inputs
    switch = 0
    switch_tr = False
    switch_fs = False

    # outputs
    lights = 0

    # states
    state = 'Lights off'
    states = ['Lights off', 'Lights on']

    def switch(self, value):
        '''State machine input'''
        print('Lights set to %d' % value)
        if not self.switch and value:
            self.switch_tr = True
        elif self.switch and not value:
            self.switch_fs = True

    def lights(self, value):
        '''State machine output'''
        print('Lights set to %d' % value)

    def step(self):
        '''step the state machine'''
        print('Start of step: state={}'.format(self.state))

        if (self.state == 'Lights off' and self.switch_tr):
            self.lights(True)
            self.state == 'Lights on'
            
        elif (self.state == 'Lights on' and self.switch_tr):
            self.lights(True)
            self.state == 'Lights off'

        print('State is: %s' % self.state)

        # reset input edge detection
        self.switch_tr = False
        self.switch_fs = False

if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    living_room = Lights()
    living_room.step()

    # lights on
    living_room.switch(1)
    living_room.step()
    living_room.switch(0)
    living_room.step()

    # lights off
    living_room.switch(1)
    living_room.step()
    living_room.switch(0)
    living_room.step()

