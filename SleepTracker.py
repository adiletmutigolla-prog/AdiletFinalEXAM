from SleepLog import SleepLog

class SleepTracker:
    def __init__(self):
        self.logs = []

    def add_log(self, date_str, hours, quality):
        try:
            log = SleepLog(date_str, hours, quality)
            self.logs.append(log)
        except ValueError as e:
            print(f" Жазба қосылмады: {e}")

    def to_dict_data(self):
        return {
            "date": [log.date for log in self.logs],
            "hours": [log.hours for log in self.logs],
            "quality": [log.quality for log in self.logs],
            "weekday": [log.date.strftime("%A") for log in self.logs]
        }