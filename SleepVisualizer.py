import matplotlib.pyplot as plt
import json


class SleepVisualizer:
    def __init__(self, analytics_df):
        self.df = analytics_df

    def draw_sleep_line(self):
        sorted_df = self.df.sort_values(by="date")

        plt.figure(figsize=(10, 5))
        plt.plot(sorted_df["date"], sorted_df["hours"], marker='o', color='purple', linestyle='-', linewidth=2)

        plt.title("Күндер бойынша ұйқы ұзақтығы")
        plt.xlabel("Күн")
        plt.ylabel("Ұйқы сағаты")
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.savefig("sleep_trend.png")
        print("📈 График 'sleep_trend.png' болып сақталды.")
        plt.show()
