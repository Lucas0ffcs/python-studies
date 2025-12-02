class WeekDayError(Exception):
    print("Dia inválido")

class Weeker:

    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    def __init__(self, day):
        if day not in self.weekdays:
            raise WeekDayError


