class Timer:
    def __init__(self, hour = 0, min = 0, sec = 0):
        self.__hour = hour
        self.__min = min
        self.__sec = sec

    def __str__(self):
        if self.__hour < 10:
            self.__strhour = "0"+str(self.__hour)
        if self.__min < 10:
            self.__strmin = "0"+str(self.__min)
        if self.__sec < 10:
            self.__strsec = "0"+str(self.__sec)
        return self.__strhour, self.__strmin, self.__strsec

    def next_second(self):
        self.__sec += 1
        if self.__sec == 60:
            self.__sec = 0
            self.__min += 1

        if self.__min == 60:
            self.__min = 0
            self.__hour += 1

        if self.__hour == 24:
            self.__hour = 0




def stringer(hour, min, sec):
    print(hour + ":" + min + ":" +  sec)

time  = Timer(15, 12, 30)
stringer(time.__hour)