import RPi.GPIO as GPIO



class GPIOManager:
    def __init__(self, output_pins, input_pin=None):
        self.output_pins = output_pins
        self.input_pin = input_pin



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
            raise(ValueError(msg))


    @property
    def input_callback(self):
        return self._input_callback or self.__default_input_callback__

    @input_callback.setter
    def input_callback(self, value):
        self._input_callback = value


    @property
    def _input_enabled(self):
        return hasattr(self, 'input_pin')



    def start(self):
        GPIO.setmode(GPIO.BOARD)

        [GPIO.setup(p, GPIO.OUT) for p in self.output_pins]

        if (self._input_enabled):
            GPIO.setup(self.input_pin, GPIO.IN)
            GPIO.add_event_detect(
                self.input_pin,
                GPIO.RISING,
                callback=self.input_callback
            )


    def toggle_coil_state(self):


    def __default_input_callback__(self):
        print("Input triggered")