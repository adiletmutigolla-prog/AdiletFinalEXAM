import json

class SleepGenerator:
    def __init__(self, tracker):
        self.tracker = tracker

    def filter_by_month(self, month_num):
        for log in self.tracker.logs:
            if log.date.month == month_num:
                yield {
                    "date": str(log.date),
                    "hours": log.hours,
                    "quality": log.quality
                }

    def export_to_json(self, filename="sleep_data.json"):
        all_data = [
            {"date": str(log.date), "hours": log.hours, "quality": log.quality}
            for log in self.tracker.logs
        ]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(all_data, f, indent=4, ensure_ascii=False)
        print(f"Деректер '{filename}' файлына сақталды.")