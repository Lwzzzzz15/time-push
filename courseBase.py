class courseBase():
    name = ""
    classRoom = ""
    startWeek = 0
    endWeek = 0
    weekDay = 0
    time = ""

    def __init__(self,  name,
                        classRoom,
                        startWeek,
                        endWeek,
                        weekDay,
                        time):
        self.name = name
        self.classRoom = classRoom
        self.startWeek = startWeek
        self.endWeek = endWeek
        self.weekDay = weekDay
        self.time = time


    def isNowTeching(self, currentWeek):
        if self.startWeek <= currentWeek and self.endWeek >= currentWeek :
            return True
        else :
            return False
