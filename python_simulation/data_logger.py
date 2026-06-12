"""
CSV Data Logger
"""

import csv
import os


class DataLogger:

    FILE_PATH = "data/bin_data_log.csv"

    @classmethod
    def initialize_file(cls):

        if not os.path.exists(cls.FILE_PATH):

            with open(
                cls.FILE_PATH,
                "w",
                newline=""
            ) as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Timestamp",
                    "Distance(cm)",
                    "Fill Percentage",
                    "Status",
                    "Temperature",
                    "Humidity",
                    "Alert"
                ])

    @classmethod
    def save_record(cls, row):

        with open(
            cls.FILE_PATH,
            "a",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow(row)