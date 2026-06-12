from datetime import datetime
import os
import shutil
import pandas as pd
import matplotlib.pyplot as plt

from python_simulation.bin_simulator import BinSimulator
from python_simulation.fill_level_calculator import FillLevelCalculator
from python_simulation.alert_system import AlertSystem
from python_simulation.data_logger import DataLogger
from python_simulation.dashboard_generator import DashboardGenerator


# =====================================
# CREATE REQUIRED FOLDERS
# =====================================

os.makedirs("outputs/alerts", exist_ok=True)
os.makedirs("outputs/reports", exist_ok=True)
os.makedirs("outputs/charts", exist_ok=True)
os.makedirs("images", exist_ok=True)


# =====================================
# ALERT LOG PREVIEW IMAGE
# =====================================

def generate_alert_preview():

    alert_file = "outputs/alerts/alert_log.txt"

    if not os.path.exists(alert_file):
        return

    with open(alert_file, "r") as file:
        content = file.read()

    if not content.strip():
        content = "No alerts generated."

    plt.figure(figsize=(10, 6))

    plt.axis("off")

    plt.text(
        0.01,
        0.99,
        content,
        fontsize=10,
        va="top"
    )

    plt.savefig(
        "images/alert_log_preview.png",
        bbox_inches="tight"
    )

    plt.close()

    print("Alert log preview generated.")


# =====================================
# COPY CHARTS TO IMAGES
# =====================================

def copy_chart_images():

    chart_files = [
        "outputs/charts/fill_level_trend.png",
        "outputs/charts/temperature_trend.png",
        "outputs/charts/humidity_trend.png"
    ]

    for chart in chart_files:

        if os.path.exists(chart):

            shutil.copy(
                chart,
                "images"
            )

    print("Chart images copied.")


# =====================================
# INITIALIZE CSV
# =====================================

DataLogger.initialize_file()

print("\nSMART WASTE MANAGEMENT SYSTEM")
print("=" * 50)

# =====================================
# GENERATE SIMULATED READINGS
# =====================================

for _ in range(50):

    distance = BinSimulator.generate_distance()

    temperature = (
        BinSimulator.generate_temperature()
    )

    humidity = (
        BinSimulator.generate_humidity()
    )

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
                f"{status} | "
                f"{alert_message}\n"
            )

    print(
        f"Distance: {distance} cm | "
        f"Fill: {fill_percentage}% | "
        f"Status: {status}"
    )

# =====================================
# REPORT GENERATION
# =====================================

df = pd.read_csv(
    "data/bin_data_log.csv"
)

latest = df.iloc[-1]

report = f"""
========================================
SMART WASTE MANAGEMENT REPORT
========================================

Timestamp: {latest['Timestamp']}

Distance: {latest['Distance(cm)']} cm

Fill Percentage: {latest['Fill Percentage']} %

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

print("\nReport Generated")

# =====================================
# GENERATE DASHBOARD CHARTS
# =====================================

DashboardGenerator.generate_charts()

# =====================================
# GENERATE ALERT IMAGE
# =====================================

generate_alert_preview()

# =====================================
# COPY CHARTS TO IMAGES
# =====================================

copy_chart_images()

# =====================================
# COMPLETION
# =====================================

print("\nFiles Generated Successfully")

print("\nGenerated Outputs:")
print("- data/bin_data_log.csv")
print("- outputs/alerts/alert_log.txt")
print("- outputs/reports/daily_report.txt")
print("- outputs/charts/fill_level_trend.png")
print("- outputs/charts/temperature_trend.png")
print("- outputs/charts/humidity_trend.png")
print("- images/alert_log_preview.png")

print("\nProject Completed Successfully")