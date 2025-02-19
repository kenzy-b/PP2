from datetime import datetime
currentDate = datetime.now()
dateInSeconds = currentDate.replace(microsecond = 0)
print(dateInSeconds)