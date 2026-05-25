from fastapi import FastAPI
from SleepTracker import SleepTracker
from SleepAnalytics import SleepAnalytics

app = FastAPI(title="💤 Ұйқы Мониторингі API Жүйесі")



def get_populated_tracker():
    tracker = SleepTracker()
    tracker.add_log("2026-05-18", 7.5, "Жақсы")
    tracker.add_log("2026-05-19", 6.0, "Орташа")
    tracker.add_log("2026-05-20", 5.8, "Төмен")
    tracker.add_log("2026-05-21", 8.0, "Жақсы")
    tracker.add_log("2026-05-22", 7.2, "Орташа")
    return tracker


@app.get("/")
def read_root():
    return {"хабарлама": "Ұйқы талдау API жүйесіне қош келдіңіз! Сводка алу үшін /api/summary парақшасына өтіңіз."}


@app.get("/api/summary")
def get_sleep_summary():
    tracker = get_populated_tracker()
    dict_data = tracker.to_dict_data()
    analytics = SleepAnalytics(dict_data)
    avg_hours, weekday_table = analytics.get_statistics()


    weekday_list = weekday_table.to_dict(orient="records")

    return {
        "status": "success",
        "total_records": len(dict_data["date"]),
        "average_hours": round(avg_hours, 1),
        "verdict": "Ұйқы қалыпты" if avg_hours >= 7 else "Ұйқы жеткіліксіз",
        "weekly_analytics": weekday_list
    }
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("FastAPI:app", host="127.0.0.1", port=8000, reload=True)