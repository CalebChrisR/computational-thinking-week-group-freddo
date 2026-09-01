from datetime import datetime

def day_week(date_string, date_format="%Y-%m-%d"):
    japanese_days = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]
    dates = datetime.strptime(date_string, date_format)
    weekday_index = dates.weekday()
    
    return japanese_days[weekday_index]

print(day_week("2024-09-02”))