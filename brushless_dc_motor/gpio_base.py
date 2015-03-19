#   GPIO Base
#
# Abstract class that should be inheritted from by any class that needs to be
# used as an input/output for the GPIO pins of the Raspberry Pi.
#
# Creator:  Scott Mielcarski
# Created:  March 17, 2015
# Modified: March 18, 2015


#   Logger
# Pretty print to console
from logger import Logger

#   ABC
# Abstract class support
from abc import ABCMeta, abstractmethod



class GPIOBase(metaclass=ABCMeta):
    #   Coil State: (bool, bool)
    # Representation of which sets of coils are currently active; one boolean
    # value per coil set.
    #
    # Coil 0 (coil_state[0]): True -> active; False -> inactive
    # Coil 1 (coil_state[1]): True -> active; False -> inactive
    @property
    @abstractmethod
    def coil_state(self):
        pass

    @coil_state.setter
    @abstractmethod
    def coil_state(self, val):
        pass



    #   Start: () -> None
    # Perform setup for monitoring inputs and setting outputs.
    @abstractmethod
    def start(self):
        pass



    #   Toggle Coil State: () -> None
    # Toggles the values of all coils stored in coil_state.
    def toggle_coil_state(self):
        val = None

        if (
                self.coil_state == (False, False) or
                self.coil_state == (True, True)
            ):
            val = (True, False)
        else:
            val = tuple(not x for x in self.coil_state)

        self.coil_state = val