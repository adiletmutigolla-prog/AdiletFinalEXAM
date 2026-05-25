from datetime import datetime

class SleepLog:
    def __init__(self, date_str, hours, quality):
        self.date = self.validate_date(date_str)
        self.hours = self.validate_hours(hours)
        self.quality = self.validate_quality(quality)

    def validate_date(self, date_str):
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Дата форматы қате: {date_str}. Үлгі: YYYY-MM-DD")

    def validate_hours(self, hours):
        if 0 < hours <= 24:
            return float(hours)
        raise ValueError(f"Ұйқы сағаты қате ({hours}). 0 мен 24 аралығында болуы тиіс.")

    def validate_quality(self, quality):
        allowed = ["Төмен", "Орташа", "Жақсы"]
        if quality in allowed:
            return quality
        raise ValueError(f"Сапа қате: {quality}. Рұқсат етілгендер: {allowed}")