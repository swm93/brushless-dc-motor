#   GPIO Simulation
#
# This class simulates a sensor being activated and output GPIO pins being
# set.
#
# Creator:  Scott Mielcarski
# Created:  March 9, 2015
# Modified: March 18, 2015


#   GPIO Base
# Abstract class that GPIO Simulation inherits from
from gpio_base import GPIOBase
#   Logger
# Pretty print to console
from logger import Logger

#   Threading
# Multithreading support
from threading import Thread
#   Math
# 3.141592653589793, 2.718281828459045
from math import pi, e
#   Time
# Used to get the current time
from time import time



class GPIOSimulation(GPIOBase):
    #   Initialize: (motor:Motor) -> GPIOSimulation
    # Sets motor model and default properties.
    def __init__(self, motor):
        #   Motor: Motor
        # Motor model containing information about the design of the motor.
        self.motor = motor

        #   Max Acceleration Time: float
        # Time (s) at which the motor is accelerating the fastest.
        self.max_acceleration_time = 3

        #   Max Velocity: float
        # Maximum velocity (rad/s) the motor will reach.
        self.max_velocity = 3*pi

        #   Duration: float
        # Amount of time (s) to simulate the motor.
        self.duration = 10



    #   Coil State: (bool, bool)
    # Representation of which sets of coils are currently active; one boolean
    # value per coil set.
    #
    # Coil 0 (coil_state[0]): True -> active; False -> inactive
    # Coil 1 (coil_state[1]): True -> active; False -> inactive
    @property
    def coil_state(self):
        return self.motor.coil_state

    @coil_state.setter
    def coil_state(self, value):
        self.motor.coil_state = value



    #   Start: () -> None
    # Begin simulation of sensor input in a separate thread.
    def start(self):
        thread = Thread(target=self.run)
        thread.start()


    #   Run: () -> None
    # Simulation of sensor input. This function simulates a motor accelerating
    # and triggering an sensor every time the motor rotates a distance equal
    # to the angle between two consecutive coils.
    def run(self):
        # current time
        start = time()
        current_time = start
        prev_time = start

        # time elapsed since motor started running
        time_elapsed = 0
        angle_since_tick = 0
        last_tick_time = start

        while (time_elapsed < self.duration):
            current_time = time()
            time_elapsed = current_time - start
            d_t = current_time - prev_time
            prev_time = current_time

            velocity = self.max_velocity/(1+pow(e, -time_elapsed+self.max_acceleration_time))
            d_angle = velocity * d_t
            angle_since_tick += d_angle

            if (angle_since_tick > self.motor.coil_spacing_angle):
                if (self.input_callback):
                    self.input_callback()

                angle_since_tick = angle_since_tick % self.motor.coil_spacing_angle

                print(current_time - last_tick_time)
                last_tick_time = current_time
