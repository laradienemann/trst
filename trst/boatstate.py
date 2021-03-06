"""
boatstate.py

Written by Alex Tong September 2015

This class holds the servo states of a boat

"""
class BoatState(object):
    """ Holds a boatstate """
    """ Constants need to be finetuned """
    R_SERVO_LOW = 1100
    R_SERVO_CENTER = 1470
    R_SERVO_HIGH = 1800
    R_SERVO_START = R_SERVO_CENTER
    S_SERVO_LOW = 1100
    S_SERVO_HIGH = 1800
    S_SERVO_START = (S_SERVO_HIGH + S_SERVO_LOW) / 2
    
    INCREMENT = 100
    def __init__(self):
        """ inits boatstate, boats should start rudder centered sails eased """
        self.rudder_pos = self.R_SERVO_START
        self.sails_pos = self.S_SERVO_START

    def turn_right(self, n = INCREMENT):
        self.set_rudder_pos(self.rudder_pos + n)

    def turn_left(self, n = INCREMENT):
        self.set_rudder_pos(self.rudder_pos - n)

    def adjust_sails(self, n):
        self.set_sails_pos(self.sails_pos + n)

    def set_rudder_pos(self, new_pos):
        if new_pos >= self.R_SERVO_LOW and new_pos < self.R_SERVO_HIGH:
            self.rudder_pos = new_pos

    def set_rudder_scaled_pos(self, new_pos):
        """ new_pos is a float between -1 and 1 representing the rudder position """
        assert new_pos >= -1
        assert new_pos <= 1
        if new_pos < 0:
            scale = self.R_SERVO_CENTER - self.R_SERVO_LOW #positive
            pos = new_pos * scale + self.R_SERVO_CENTER
        else:
            scale = self.R_SERVO_HIGH - self.R_SERVO_CENTER
            pos = new_pos * scale + self.R_SERVO_CENTER
        self.set_rudder_pos(int(pos))

    def set_sails_pos(self, new_pos):
        if new_pos >= self.S_SERVO_LOW and new_pos < self.S_SERVO_HIGH:
            self.sails_pos = new_pos

    def set_pos(self, new_pos):
        """ convinience method to set both rudders and sails at once """
        assert type(new_pos) == tuple
        assert len(new_pos) == 2
        self.set_rudder_pos(new_pos[0])
        self.set_sails_pos(new_pos[1])

    def get_pos(self):
        return self.rudder_pos, self.sails_pos

    def __repr__(self):
        return "<BoatState Obj: " + str(id(self)) + " rudder: " + str(self.rudder_pos) + " sails: " + str(self.sails_pos) + ">"
