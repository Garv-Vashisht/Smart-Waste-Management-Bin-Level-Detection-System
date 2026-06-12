"""
Bin Sensor Simulator
Simulates ultrasonic sensor readings.
"""

import random


class BinSimulator:

    @staticmethod
    def generate_distance():

        return round(
            random.uniform(0, 100),
            2
        )

    @staticmethod
    def generate_temperature():

        return round(
            random.uniform(20, 45),
            2
        )

    @staticmethod
    def generate_humidity():

        return round(
            random.uniform(25, 90),
            2
        )