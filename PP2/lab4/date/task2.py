from datetime import datetime, timedelta
currentDate = datetime.now().date()
yesterday = currentDate - timedelta(days = 1)
tomorrow = currentDate + timedelta(days = 1)
print(yesterday, currentDate, tomorrow)