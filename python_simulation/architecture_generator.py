import matplotlib.pyplot as plt
import os

class ArchitectureGenerator:

    @staticmethod
    def generate_architecture():

        os.makedirs("images", exist_ok=True)

        fig, ax = plt.subplots(figsize=(8, 8))

        ax.axis("off")

        text = """
Bin Simulation
      ↓
Fill Level Calculation
      ↓
Status Classification
      ↓
Alert Generation
      ↓
CSV Logging
      ↓
Report Generation
      ↓
Dashboard Charts
"""

        ax.text(
            0.5,
            0.5,
            text,
            ha="center",
            va="center",
            fontsize=14
        )

        plt.savefig(
            "images/system_architecture.png",
            bbox_inches="tight"
        )

        plt.close()