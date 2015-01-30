#   Brushless DC Motor
#
# Creator:  Scott Mielcarski
# Created:  January 26, 2015
# Modified: January 29, 2015


#import RPi.GPIO as GPIO
import math
import time
import numpy

class Motor:
    def __init__(self, radius, numMagnets, numCoils):
        self.dimensions = Circle(radius)
        self.dimensions.numSegments = numMagnets

        self.coils = Coils(radius - 0.01, numCoils)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def segment_length(self):
        return self.perimeter()/self.numMagnets


class Coils:
    def __init__(self, radius, numCoils):
        self.dimensions = Circle(radius)
        self.dimensions.numSegments = numCoils

        self.states = numpy.tile(False, numCoils)


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.numSegments = 1

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_segment_length(self):
        return self.get_perimeter()/self.numSegments



class Simulation:
    # time (s) at which the motor is accelerating the fastest
    maxAccelerationTime = 1
    # time (s) between velocity measurements
    measurementInterval = 0.05
    # maximum velocity (rad/s) the motor will reach
    maxVelocity = 2*math.pi

    def simulate(self):
        # current time
        start = time.time()
        # time elapsed since motor started running
        duration = 0

        while (duration < 2):
            duration = time.time() - start
            velocity = self.maxVelocity/(1+pow(math.e, -10*(duration-self.maxAccelerationTime)))

            print velocity
            time.sleep(self.measurementInterval)

sim = Simulation()
# sim.simulate()

motor = Motor(0.1, 2, 6)
print motor.dimensions.radius
print motor.dimensions.get_segment_length()