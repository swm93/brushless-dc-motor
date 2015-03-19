#   Motor
#
# By providing accurate dimensions of a brushless DC motor, this class will
# calculate the angular velocity of the motor based on the time interval
# between consecutive 'ticks', as well as determine when the polarity of the
# coils should be inverted. A tick is expected to occur each time the rotor
# rotates a distance equal to the angle between consecutive coils.
#
# Expects:
#   Number of coils to be twice the number of magnets.
#   Number of sensors to be one less than the number of magnets.
#   Sensors to be connected to consecutive coils.
#
# Creator:  Scott Mielcarski
# Created:  January 29, 2015
# Modified: March 17, 2015


#   Logger
# Pretty print to console
from logger import Logger

#   Math
# 3.141592653589793
from math import pi
#   Time
# Used to get the current time
from time import time



class Motor:
    #   Initialize: (radius:float, num_magnets:int) -> Motor
    # Sets geometric properties of the motor itself.
    def __init__(self, radius, num_magnets):
        #   Radius: float
        # Radius of the rotor
        self.radius = radius

        #   Num Magnets: int
        # Number of magnets attached to the rotor
        self.num_magnets = num_magnets

        #   Velocity: int
        # Angular velocity of the rotor
        self.velocity = 0

        #   Last Tick Time: int
        # Time (s) since the sensor was last activated
        self.last_tick_time = 0

        self._coil_state = (False, False)



    #   Coil State: (bool, bool)
    # Representation of which sets of coils are currently active; one boolean
    # value per coil set.
    #
    # Coil 0 (coil_state[0]): True -> active; False -> inactive
    # Coil 1 (coil_state[1]): True -> active; False -> inactive
    @property
    def coil_state(self):
        return self._coil_state

    @coil_state.setter
    def coil_state(self, value):
        if (value == (True, True)):
            Logger.error("Both sets of coils are active")
        elif (
                self._coil_state == (False, False) and
                value != (False, False)
            ):
            Logger.success("Motor is starting up")
        elif (
                self._coil_state != (False, False) and
                value == (False, False)
            ):
            Logger.success("Motor is shutting down")
        else:
            status_msg = tuple("active" if x else "inactive" for x in value)
            Logger.info("Coil 0 is %s\nCoil 1 is %s" % status_msg)

        self._coil_state = value


    #   Perimeter: float
    # The perimeter of the rotor. This value is calculated from the radius of
    # the rotor.
    @property
    def perimeter(self):
        return 2 * pi * self.radius


    #   Magnet Spacing Angle: float
    # Angle (rad) between the center points of two consecutive magnets on the
    # rotor. This value is calculated from the number of magnets fixed on the
    # rotor.
    @property
    def magnet_spacing_angle(self):
        return (2 * pi) / self.num_magnets


    #   Coil Spacing Angle: float
    # Angle (rad) between the center points of two consecutive coils on the
    # stator. This value is calculated from the number of magnets fixed on the
    # rotor; the number of coils is always twice the number of magnets.
    @property
    def coil_spacing_angle(self):
        return pi / self.num_magnets

    #   Time Until Switch: int
    # Time remaining until the polarity of the coils should be reversed. This
    # property is calculated from the coil_spacing angle and the current
    # angular velocity.
    @property
    def time_until_switch(self):
        return self.coil_spacing_angle / self.velocity



    #   Run: () -> None
    # Sets up time based variables that will be needed in order to calculate
    # the angular velocity.
    #
    # Must be called when the motor is turned on.
    def run(self):
        self.last_tick_time = time()


    #   Tick Occurred: () -> None
    # Updates any variables that must be changed once a new state of the motor
    # becomes known.
    #
    # Must be called when a sensor is activated.
    def tick_occurred(self):
        self.update_velocity()


    #   Update Velocity: () -> None
    # Calculates and updates the velocity of the motor based on the current
    # time and the time since the previous tick occurred.
    def update_velocity(self):
        current_time = time()
        dt = current_time - self.last_tick_time

        self.last_tick_time = current_time
        self.velocity = self.coil_spacing_angle / dt
