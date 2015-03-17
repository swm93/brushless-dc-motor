#   Motor
#
# Creator:  Scott Mielcarski
# Created:  January 29, 2015
# Modified: January 31, 2015


import math
import time



# Expects:
#   Number of coils to be twice the number of magnets.
#   Number of hall effect sensors to be one less than the number of magnets.
#   Hall effect sensors to be connected to consecutive coils.
class Motor:
    def __init__(self, radius, num_magnets):
        # rotor
        self.radius = radius
        self.perimeter = 2 * math.pi * self.radius
        self.num_magnets = num_magnets
        self.magnet_spacing_angle = (2*math.pi) / self.num_magnets

        # stator
        self.coil_spacing_angle = (2*math.pi) / (2 * num_magnets)

        # list of the currently active coils
        self.active_coils = (False, False)
        # anglular velocity based on last two ticks
        self.velocity = 0
        # the last time when a hall effect sensor was activated
        self.last_tick_time = 0


    def run(self):
        self.last_tick_time = time.time()


    def tick_occurred(self):
        self.update_velocity()


    def update_velocity(self):
        current_time = time.time()
        dt = current_time - self.last_tick_time

        self.last_tick_time = current_time
        self.velocity = self.coil_spacing_angle / dt


    @property
    def time_until_switch(self):
        return self.coil_spacing_angle / self.velocity
