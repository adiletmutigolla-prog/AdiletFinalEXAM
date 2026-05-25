import pandas as pd
import numpy as np


class SleepAnalytics:
    def __init__(self, data_dict):
        self.df = pd.DataFrame(data_dict)

    def get_statistics(self):
        if self.df.empty:
            return 0, pd.DataFrame()

        avg_sleep = np.mean(self.df["hours"])

        weekday_summary = self.df.groupby("weekday")["hours"].mean().reset_index()

        return avg_sleep, weekday_summary