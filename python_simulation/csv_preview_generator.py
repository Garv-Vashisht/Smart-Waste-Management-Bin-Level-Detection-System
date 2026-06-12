import pandas as pd
import matplotlib.pyplot as plt
import os

class CSVPreviewGenerator:

    @staticmethod
    def generate_csv_preview():

        os.makedirs("images", exist_ok=True)

        df = pd.read_csv("data/bin_data_log.csv")

        df = df.tail(10)

        fig, ax = plt.subplots(figsize=(12, 4))

        ax.axis('off')

        table = ax.table(
            cellText=df.values,
            colLabels=df.columns,
            loc='center'
        )

        table.auto_set_font_size(False)
        table.set_fontsize(8)

        plt.savefig(
            "images/csv_log_preview.png",
            bbox_inches='tight'
        )

        plt.close()