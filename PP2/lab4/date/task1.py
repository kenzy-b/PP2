from datetime import datetime, timedelta
currentDate = datetime.now().date()
daysAgo = currentDate - timedelta(days = 5)
print(daysAgo)