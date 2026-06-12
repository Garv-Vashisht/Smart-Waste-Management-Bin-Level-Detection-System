"""
Dashboard Generator
"""

import pandas as pd
import matplotlib.pyplot as plt
import os


class DashboardGenerator:

    @staticmethod
    def generate_charts():

        csv_file = "data/bin_data_log.csv"

        if not os.path.exists(csv_file):
            return

        df = pd.read_csv(csv_file)

        os.makedirs(
            "outputs/charts",
            exist_ok=True
        )

        plt.figure(figsize=(10, 5))
        plt.plot(df["Fill Percentage"])
        plt.title("Bin Fill Level Trend")
        plt.xlabel("Reading")
        plt.ylabel("Fill Percentage (%)")
        plt.grid()

        plt.savefig(
            "outputs/charts/fill_level_trend.png"
        )

        plt.close()

        plt.figure(figsize=(10, 5))
        plt.plot(df["Temperature"])
        plt.title("Temperature Trend")
        plt.xlabel("Reading")
        plt.ylabel("Temperature")
        plt.grid()

        plt.savefig(
            "outputs/charts/temperature_trend.png"
        )

        plt.close()

        plt.figure(figsize=(10, 5))
        plt.plot(df["Humidity"])
        plt.title("Humidity Trend")
        plt.xlabel("Reading")
        plt.ylabel("Humidity")
        plt.grid()

        plt.savefig(
            "outputs/charts/humidity_trend.png"
        )

        plt.close()

        print("Charts Generated Successfully")