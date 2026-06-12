from datetime import datetime
import os
import pandas as pd

from python_simulation.bin_simulator import BinSimulator
from python_simulation.fill_level_calculator import FillLevelCalculator
from python_simulation.alert_system import AlertSystem
from python_simulation.data_logger import DataLogger
from python_simulation.dashboard_generator import DashboardGenerator

os.makedirs("outputs/alerts", exist_ok=True)
os.makedirs("outputs/reports", exist_ok=True)

DataLogger.initialize_file()

print("\nSMART WASTE MANAGEMENT SYSTEM")
print("-" * 40)

for _ in range(50):

    distance = BinSimulator.generate_distance()

    temperature = BinSimulator.generate_temperature()

    humidity = BinSimulator.generate_humidity()

    fill_percentage = (
        FillLevelCalculator.calculate_fill_percentage(
            distance
        )
    )

    status = (
        FillLevelCalculator.classify_bin(
            fill_percentage
        )
    )

    alert_flag, alert_message = (
        AlertSystem.generate_alert(
            status
        )
    )

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    DataLogger.save_record([
        timestamp,
        distance,
        fill_percentage,
        status,
        temperature,
        humidity,
        alert_message
    ])

    if alert_flag:

        with open(
            "outputs/alerts/alert_log.txt",
            "a"
        ) as file:

            file.write(
                f"{timestamp} | "
                f"{alert_message}\n"
            )

    print(
        f"{status} | "
        f"{fill_percentage}% Full"
    )

df = pd.read_csv(
    "data/bin_data_log.csv"
)

latest = df.iloc[-1]

report = f"""
SMART WASTE MANAGEMENT REPORT

Timestamp: {latest['Timestamp']}
Fill Percentage: {latest['Fill Percentage']}%
Status: {latest['Status']}
Temperature: {latest['Temperature']}
Humidity: {latest['Humidity']}
Alert: {latest['Alert']}
"""

with open(
    "outputs/reports/daily_report.txt",
    "w"
) as file:

    file.write(report)

DashboardGenerator.generate_charts()

print("\nReport Generated")
print("Charts Generated")
print("Project Completed Successfully")