import datetime
import schedule

def job():
    hours = datetime.datetime.now().hour
    if hours > 12:
        hours -= 12
    elif hours == 0:
        hours = 12
    print("Ку" * hours)

schedule.every().hour.at(":00").do(job)

while True:
    schedule.run_pending()
