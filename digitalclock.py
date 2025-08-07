print("welcome to the Python digital clock")
import time
import datetime
while True:
    current_date = time.strftime("%Y-%m-%d")
    current_time=time.strftime("%H:%M:%S")
    print(f"current Date:{current_date}\tCurrent Time: {current_time}", end="\r")
    