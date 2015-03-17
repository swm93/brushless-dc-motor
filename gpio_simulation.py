import threading
import math
import time
from logger import Logger


class GPIOSimulation():
    def __init__(self, coil_spacing_angle):
        self.coil_spacing_angle = coil_spacing_angle

        # time (s) at which the motor is accelerating the fastest
        self.max_acceleration_time = 3
        self.max_acceleration_time_scale = 1
        # time (s) between velocity measurements
        self.measurement_interval = 0.01
        # maximum velocity (rad/s) the motor will reach
        self.max_velocity = 3*math.pi

        self.coil_state = (False, False)


    def start(self, callback):
        self.tick_callback = callback

        thread = threading.Thread(target=self.run)
        thread.start()


    def run(self):
        # current time
        start = time.time()
        current_time = start
        prev_time = start
        duration = 10

        # time elapsed since motor started running
        time_elapsed = 0
        angle_since_tick = 0
        # time_since_tick = 0
        last_tick_time = start

        while (time_elapsed < duration):
            current_time = time.time()
            time_elapsed = current_time - start
            d_t = current_time - prev_time
            prev_time = current_time

            velocity = self.max_velocity/(1+pow(math.e, -self.max_acceleration_time_scale*time_elapsed+self.max_acceleration_time))
            d_angle = velocity * d_t
            angle_since_tick += d_angle

            if (angle_since_tick > self.coil_spacing_angle):
                self.tick_callback()

                angle_since_tick = angle_since_tick % self.coil_spacing_angle
                # time_since_tick = 0

                print(current_time - last_tick_time)
                last_tick_time = current_time


    def toggle_coil_state(self):
        if (self.coil_state == (False, False)):
            self.coil_state = (True, False)
            Logger.success("Motor is starting up")
        elif (self.coil_state == (True, True)):
            Logger.error("Both sets of coils are active")
        else:
            self.coil_state = tuple(not x for x in self.coil_state)
            Logger.info("Coil 0 is %s\nCoil 1 is %s" % self.coil_state)
