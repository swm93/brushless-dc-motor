#   GPIO Manager
#
# This class is used to activate or deactivate the electromagnetic coils. If
# an input pin is provided, it will be treated as a sensor and will call a
# callback function if one is provided. It also handles toggling/setting the
# state of the output pins.
#
# Creator:  Scott Mielcarski
# Created:  March 9, 2015
# Modified: March 18, 2015


#   GPIO Base
# Abstract class that GPIO Manager inherits from
from gpio_base import GPIOBase
#   Logger
# Pretty print to console
from logger import Logger

#   RPi.GPIO
# Handles setup and handling of GPIO pins
import RPi.GPIO as GPIO



class GPIOManager(GPIOBase):
    #   Initialize: (motor:Motor, output_pins:[int, int], input_pin:int) ->
    #       GPIOManager
    # Sets GPIO pin numbers and motor model.
    def __init__(self, motor, output_pins, input_pin=None):
        #   Motor: Motor
        # Motor model containing information about the design of the motor.
        self.motor = motor

        self._output_pins = None
        self.output_pins = output_pins

        self._input_pin = None
        self.input_pin = input_pin



    #   Coil State: (bool, bool)
    # Representation of which sets of coils are currently active; one boolean
    # value per coil set. When this property is set, the associated GPIO pins
    # are activated/deactivated.
    #
    # Coil 0 (coil_state[0]): True -> active; False -> inactive
    # Coil 1 (coil_state[1]): True -> active; False -> inactive
    @property
    def coil_state(self):
        return self.motor.coil_state

    @coil_state.setter
    def coil_state(self, value):
        try:
            [GPIO.output(self.output_pins[i], x) for i, x in enumerate(value)]
            self.motor.coil_state = value
        except Exception as e:
            Logger.error(e)


    #   Output Pins: [int, int]
    # List of all pin numbers that act as output pins.
    @property
    def output_pins(self):
        return self._output_pins

    @output_pins.setter
    def output_pins(self, value):
        if (isinstance(value, list) and len(value) == 2):
            self._output_pins = value
        else:
            msg = ("output_pins is expected to be a list of length 2, but a "
                   "%s of length %s was provided." % (type(value).__name__,
                   len(value)))
            Logger.error(msg, ValueError)


    #   Input Pin: int
    # Pin number that should be used as an output pin.
    @property
    def input_pin(self):
        return self._input_pin

    @input_pin.setter
    def input_pin(self, value):
        if (isinstance(value, int)):
            self._input_pin = value
        else:
            msg = ("input_pin is expected to be an int but a %s was provided."
                   % type(value).__name__)
            Logger.error(msg, ValueError)


    #   Input Enabled: bool
    # Infers whether the user intends to use an input pin or not.
    @property
    def _input_enabled(self):
        return self.input_pin != None



    #   Start: () -> None
    # Setup GPIO in preparation for setting output pins and reading input
    # pins.
    def start(self):
        GPIO.setmode(GPIO.BOARD)

        [GPIO.setup(p, GPIO.OUT) for p in self.output_pins]

        if (self._input_enabled):
            GPIO.setup(self.input_pin, GPIO.IN)
            GPIO.add_event_detect(
                self.input_pin,
                GPIO.RISING,
                callback=self.input_callback or (lambda: None)
            )