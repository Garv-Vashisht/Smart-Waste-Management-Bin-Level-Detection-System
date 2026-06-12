"""
Alert System
"""


class AlertSystem:

    @staticmethod
    def generate_alert(status):

        if status == "Full":

            return (
                True,
                "URGENT: Bin is Full. Collection Required."
            )

        elif status == "High":

            return (
                True,
                "WARNING: Bin nearing capacity."
            )

        return (
            False,
            "Bin operating normally."
        )