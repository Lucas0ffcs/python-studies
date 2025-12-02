class Timer:
    def __init__(self, hour = 0, min = 0, sec = 0):
        self.hour = hour
        self.min = min
        self.sec = sec

    def __str__(self):
        if self.hour < 10:
            self.strhour = "0"+str(self.hour)
        if self.min < 10:
            self.strmin = "0"+str(self.min)
        if self.sec < 10:
            self.strsec = "0"+str(self.sec)
        return strhour, strmin, strsec
