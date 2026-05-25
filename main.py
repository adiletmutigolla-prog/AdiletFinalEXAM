from SleepTracker import SleepTracker
from SleepGenerator import SleepExporter
from SleepAnalytics import SleepAnalytics
from SleepVisualizer import SleepVisualizer

if __name__ == "__main__":
    print("--- 💤 ҰЙҚЫ МОНИТОРИНГІ ЖҮЙЕСІ ІСКЕ ҚОСЫЛДЫ ---")

    # 1. Деректерді жинақтау (1-6 Апта)
    tracker = SleepTracker()
    tracker.add_log("2026-05-18", 7.5, "Жақсы")
    tracker.add_log("2026-05-19", 6.0, "Орташа")
    tracker.add_log("2026-05-20", 5.8, "Төмен")
    tracker.add_log("2026-05-21", 8.0, "Жақсы")
    tracker.add_log("2026-05-22", 7.2, "Орташа")

    # 2. Генератор және Экспорт (7-8 Апта)
    exporter = SleepExporter(tracker)
    exporter.export_to_json()

    print("\n[7-Апта] Генератор арқылы Мамыр (05) айын сүзу:")
    for log in exporter.filter_by_month(5):
        print(log)

    # 3. Математикалық Аналитика (9-12 Апта)
    dict_data = tracker.to_dict_data()
    analytics = SleepAnalytics(dict_data)
    avg_hours, weekday_table = analytics.get_statistics()

    print(f"\n[9-11 Апта] Жалпы орташа ұйқы: {round(avg_hours, 2)} сағат")
    print("\n[12-Апта] Күндер бойынша топтау (Groupby):")
    print(weekday_table)

    # 4. Визуализация және API Жауабы (13-14 Апта)
    visualizer = SleepVisualizer(analytics.df)
    print("\n[14-Апта] API-дан келетін Сводка:")
    print(visualizer.get_api_summary())

    print("\n[13-Апта] График терезесі ашылуда...")
    visualizer.draw_sleep_line()