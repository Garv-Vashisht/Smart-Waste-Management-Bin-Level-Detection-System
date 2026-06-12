"""
Fill Level Calculator
Converts ultrasonic sensor distance
into bin fill percentage and status.
"""

class FillLevelCalculator:

    BIN_HEIGHT_CM = 100

    @classmethod
    def calculate_fill_percentage(cls, distance):

        fill_percentage = (
            (cls.BIN_HEIGHT_CM - distance)
            / cls.BIN_HEIGHT_CM
        ) * 100

        fill_percentage = max(
            0,
            min(100, fill_percentage)
        )

        return round(fill_percentage, 2)

    @staticmethod
    def classify_bin(fill_percentage):

        if fill_percentage <= 20:
            return "Empty"

        elif fill_percentage <= 40:
            return "Low"

        elif fill_percentage <= 70:
            return "Medium"

        elif fill_percentage <= 90:
            return "High"

        return "Full"