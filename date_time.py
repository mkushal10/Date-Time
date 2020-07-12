import time
import datetime

class Date(object):
    def __init__(self):
        self.date = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

    def __repr__(self):
        return self.date

if __name__ == "__main__":
    now = Date()
    print(now)
