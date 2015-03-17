from motor import Motor
try:
    from gpio_manager import GPIOManager as GPIOManager
    DEBUG = 0
except:
    from gpio_simulation import GPIOSimulation as GPIOManager
    DEBUG = 1



sensor_radius = 0.1
num_magnets = 6
motor = Motor(sensor_radius, num_magnets)

gpio_manager = None


def main():
    global gpio_manager
    gpio_manager = debug_mode_function[DEBUG]()

    motor.run()
    gpio_manager.start(__tick_occurred__)


def run():
    input_pin = 11
    output_pins = []

    return GPIOManager(input_pin, output_pins)


def simulate():
    return GPIOManager(motor.coil_spacing_angle)



def __tick_occurred__():
    motor.tick_occurred()
    gpio_manager.toggle_coil_state()




debug_mode_function = {
    0: run,
    1: simulate
}

if (__name__ == '__main__'):
    main()