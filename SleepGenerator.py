import json

class SleepExporter:
    def __init__(self, tracker):
        self.tracker = tracker

    def filter_by_month(self, month_num):
        filtered_list = []
        for log in self.tracker.logs:
            if log.date.month == month_num:
                log_dict = {
                    "date": str(log.date),
                    "hours": log.hours,
                    "quality": log.quality
                }
                filtered_list.append(log_dict)
        return filtered_list

    def export_to_json(self, filename="sleep_data.json"):
        all_data = [
            {"date": str(log.date), "hours": log.hours, "quality": log.quality}
            for log in self.tracker.logs
        ]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(all_data, f, indent=4, ensure_ascii=False)
        print(f"Деректер '{filename}' файлына сақталды.")